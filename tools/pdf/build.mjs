// 把 README + book/*.md + docs/*.md 排成一本 PDF：pandoc 把 Markdown 转成 typst，typst 排版。
// 用法：node tools/pdf/build.mjs [输出路径]   默认输出 dist/HowToLiveBetter.pdf
// 需要 pandoc（≥3.1，要有 typst 输出）和 typst（≥0.13）在 PATH 上，或用环境变量 PANDOC、TYPST 指路径。
// 版面在 tools/pdf/template.typ 里；正文一个字都不改，只做三件事：
// 去掉「← 回总目录」、给每节的标题挂上锚点、把仓库内的链接改成书内跳转或 GitHub 网址。
import { writeFileSync, mkdirSync, statSync } from 'node:fs';
import { resolve, dirname, posix, basename } from 'node:path';
import { execFileSync } from 'node:child_process';
import { ROOT, REPO, SITE, read, readBook, gitCommit, buildStamp, stripBackLink, langOf } from '../lib/book.mjs';
import { pickLang, outputArg } from '../lib/langs.mjs';

const lang = pickLang();
const info = langOf(lang);
const outArg = outputArg();
const OUT = resolve(ROOT, outArg ?? `dist/${info.outputs.pdf}`);
const WORK = resolve(ROOT, 'dist/pdf-build.md');
const PANDOC = process.env.PANDOC ?? 'pandoc';
const TYPST = process.env.TYPST ?? 'typst';
const STAMP = buildStamp();          // 「（北京时间）」写在模板和版本说明里，传给 pandoc 的值保持纯 ASCII
const COMMIT = gitCommit();

const { description, frontMd, contentsMd, bookFiles, docFiles } = readBook(lang);
const L = info.labels;
const tocRe = new RegExp('^' + info.marks.toc.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));

// ---------- 页（每页一个一级标题，一级标题在 typst 里另起一页） ----------
const anchorOf = new Map();
bookFiles.forEach(f => anchorOf.set(f, 'sec-' + (basename(f).match(/^\d+/)?.[0] ?? anchorOf.size + 1)));
docFiles.forEach((f, i) => anchorOf.set(f, `doc-${i + 1}`));

const pages = [
  { src: info.readme, md: `# ${L.front}\n\n${description}\n\n${frontMd}`, anchor: 'front' },
  { src: info.readme, md: contentsMd.replace(tocRe, `# ${L.contents}`), anchor: 'contents' },
  ...[...bookFiles, ...docFiles].map(src => ({ src, md: stripBackLink(read(src)), anchor: anchorOf.get(src) })),
  { src: info.readme, md: aboutMd(), anchor: 'about' },
];

function aboutMd() {
  const commitLine = COMMIT ? `- ${L.commit}：${COMMIT.slice(0, 7)}\n` : '';
  return `# ${L.about}

${L.pdfLead}

- ${L.builtAt}：${STAMP}
${commitLine}- ${L.pdfRepoLine}：${REPO}
- ${L.pdfSiteLine}：${SITE}

${L.pdfLinks}

${L.license}`;
}

// ---------- 链接：书内的改成锚点，书外的改成绝对网址 ----------
function rewriteLinks(md, src) {
  return md.replace(/\]\(([^)\s]+)(\s+"[^"]*")?\)/g, (all, href, title) => {
    if (/^(https?:|mailto:)/.test(href)) return all;
    // README 里指向自身小节的锚点（#目录 这种）在书里不一定有，指回 GitHub 上的 README
    if (href.startsWith('#')) return `](${REPO}/blob/main/${info.readme}${href}${title ?? ''})`;
    const [path] = href.split('#');
    const target = posix.normalize(posix.join(posix.dirname(src), path));
    const anchor = anchorOf.get(target);
    if (anchor) return `](#${anchor}${title ?? ''})`;
    const kind = target.endsWith('/') ? 'tree' : 'blob';
    return `](${REPO}/${kind}/main/${target}${title ?? ''})`;
  });
}

const body = pages.map(p => {
  const md = rewriteLinks(p.md, p.src)
    .replace(/<!--[\s\S]*?-->/g, '')                       // 成本标签这类 HTML 注释不进 PDF
    .replace(/^(# .+?)\s*$/m, `$1 {#${p.anchor}}`);        // 给这一页的一级标题挂锚点
  if (!md.includes(`{#${p.anchor}}`)) throw new Error(`${p.src} 里没找到一级标题，挂不上锚点`);
  return md.trim();
}).join('\n\n');

mkdirSync(dirname(OUT), { recursive: true });
writeFileSync(WORK, body);

// ---------- pandoc → typst → pdf ----------
const run = (cmd, args) => {
  try {
    return execFileSync(cmd, args, { cwd: ROOT, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
  } catch (err) {
    if (err.code === 'ENOENT') throw new Error(`找不到 ${cmd}，装上它或用环境变量 ${cmd === PANDOC ? 'PANDOC' : 'TYPST'} 指到可执行文件`);
    throw new Error(`${cmd} 失败：\n${err.stderr || err.stdout || err.message}`);
  }
};

const typFile = resolve(ROOT, 'dist/pdf-build.typ');
run(PANDOC, [
  '--from=gfm+attributes', '--to=typst', '--wrap=none',
  `--template=${resolve(ROOT, 'tools/pdf/template.typ')}`,
  '-V', `booktitle=${info.title}`, '-V', `subtitle=${description}`,
  '-V', `builddate=${STAMP}`, '-V', `commit=${COMMIT.slice(0, 7) || ''}`,
  '-V', `site=${SITE}`, '-V', `repo=${REPO}`,
  '-V', `textlang=${info.typstLang}`, '-V', `region=${info.typstRegion}`,
  '-V', `toctitle=${L.toc}`,
  '-V', `coverbuilt=${L.coverBuilt}`, '-V', `coverlive=${L.coverLive}`, '-V', `coverwhere=${L.coverWhere}`,
  '-V', `commitlabel=${L.coverCommit}`, '-V', `covertz=${L.coverTz}`,
  '-V', `coverimage=${info.coverImage}`,
  '-o', typFile, WORK,
]);
const log = run(TYPST, ['compile', typFile, OUT, '--root', ROOT]);
if (log.trim()) console.log(log.trim());

const entries = pages.filter(p => bookFiles.includes(p.src))
  .reduce((n, p) => n + p.md.split('\n').filter(l => l.startsWith('### ')).length, 0);
console.log(`已生成 ${OUT}：${bookFiles.length} 节 ${entries} 条，附录 ${docFiles.length} 篇，${(statSync(OUT).size / 1048576).toFixed(1)} MB`);
