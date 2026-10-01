// Dựng trang tra cứu ở dạng đường dẫn theo ngôn ngữ: index.vi.html -> vi/index.html
// (GitHub Pages phục vụ thư mục gốc, nên /vi/ sẽ là trang tiếng Việt.)
//
//   node tools/translate-vi/build-site.mjs
//
// Trang nằm sâu một cấp nên ba chỗ đọc dữ liệu phải thêm '../':
// README.vi.md, các tệp book/vi/*.md và các bài dài docs/vi/*.md. Cùng lúc chèn
// hàng liên kết ngôn ngữ vào cuối trang, cả bản ở gốc lẫn bản trong vi/.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '../..');
const SRC = resolve(ROOT, 'index.vi.html');
const OUT_DIR = resolve(ROOT, 'vi');
const OUT = resolve(OUT_DIR, 'index.html');

const LANG_ROW = (prefix) => [
  '<div class="foot lang-nav">',
  'Ngôn ngữ khác: ',
  `<a href="${prefix}">中文</a> · `,
  `<a href="${prefix === '' ? 'index.vi.html' : prefix + 'vi/'}">Tiếng Việt</a> · `,
  '<a href="https://dlgrv.github.io/HowToLiveBetter/en/">English</a> · ',
  '<a href="https://dlgrv.github.io/HowToLiveBetter/ru/">Русский</a> · ',
  '<a href="https://dlgrv.github.io/HowToLiveBetter/es/">Español</a> · ',
  '<a href="https://dlgrv.github.io/HowToLiveBetter/pt/">Português</a>',
  '</div>',
].join('');

const withRow = (html, prefix) => {
  if (html.includes('class="foot lang-nav"')) return html;
  const marker = '</main>';
  if (!html.includes(marker)) throw new Error('trang không có </main>, không chèn được hàng ngôn ngữ');
  return html.replace(marker, `  ${LANG_ROW(prefix)}\n${marker}`);
};

let root = readFileSync(SRC, 'utf8');
root = withRow(root, '');
writeFileSync(SRC, root);
console.log('index.vi.html: đã chèn hàng liên kết ngôn ngữ');

let page = root;
for (const [from, to] of [
  ["await readText('README.vi.md')", "await readText('../README.vi.md')"],
  ["await readText(f)", "await readText('../' + f)"],
  ["await readText(path)", "await readText('../' + path)"],
  ['<a class="title" href="./"', '<a class="title" href="../"'],
]) {
  if (!page.includes(from)) throw new Error(`không tìm thấy mảnh cần thay: ${from}`);
  page = page.split(from).join(to);
}
page = withRow(page, '../');
mkdirSync(OUT_DIR, { recursive: true });
writeFileSync(OUT, page);
console.log(`vi/index.html: đã ghi (${page.length} ký tự), trang đọc dữ liệu qua '../'`);
if (!existsSync(resolve(OUT_DIR, 'index.html'))) throw new Error('vi/index.html không được ghi');
