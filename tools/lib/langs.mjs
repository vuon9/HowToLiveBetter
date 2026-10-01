// Ngôn ngữ của các bản dựng: EPUB, PDF, trang tra cứu, bản HTML một tệp.
// 中文是主语言，它的路径与产物名保持原样，其他语言都从这个登记表读自己的一份。
export const LANGS = {
  zh: {
    code: 'zh',
    readme: 'README.md',
    bookGlob: 'book/',
    docsGlob: 'docs/',
    page: 'index.html',
    title: '高性价比人生指南',
    // README 里被三套构建解析的三段标题
    marks: { questions: '## 这本书想回答的问题', toc: '## 目录', body: '## 正文' },
    htmlLang: 'zh-CN',
    typstLang: 'zh', typstRegion: 'cn',
    coverImage: '/og.png',
    labels: {
      front: '前言', contents: '各节简介', about: '版本说明',
      toc: '目录',
      aboutLead: '这本电子书由仓库里的 Markdown 正文自动生成，正文一改就重新生成一本。手里这本的版本：',
      builtAt: '生成时间', commit: '对应提交',
      /* epub */
      epubLead: '这本电子书由仓库里的 Markdown 正文自动生成，正文一改就重新生成一本。手里这本的版本：',
      latestDownload: '最新版下载', siteLine: '在线检索页（按关键词、章节、证据等级和成本筛选）', repoLine: '仓库、提意见、看每条来源的核实记录',
      internalLinks: '正文里指向仓库内其他文件的链接已改成书内跳转；指向核实记录、许可证这类没收进书的文件的链接改成了 GitHub 网址。',
      navToc: '目录', navCover: '封面', navBody: '正文',
      offlineFoot: '离线副本，生成于', offlineTz: '（北京时间）', offlineCommit: '，正文提交', offlineLive: '；正文会继续更新，以 <a href="%SITE%">在线版</a> 为准。',
      /* pdf */
      pdfLead: '这本 PDF 由仓库里的 Markdown 正文自动排版，正文一改就重新排一本。手里这本的版本：',
      pdfRepoLine: '最新版下载、在线检索、提意见', pdfSiteLine: '在线检索页（按关键词、章节、证据等级和成本筛选，也能存成单文件离线看）',
      pdfLinks: '正文里指向书内其他节的链接已改成书内跳转；指向核实记录、许可证这类没排进书的文件的链接改成了 GitHub 网址。',
      coverBuilt: '生成于', coverTz: '（北京时间）', coverCommit: '正文提交', coverLive: '正文每天都在改，以在线版为准', coverWhere: '在线检索、EPUB 与本 PDF 的最新版都在',
      license: '正文以 CC BY 4.0 发布（https://creativecommons.org/licenses/by/4.0/）。可以转载、改编、商用，要写明出处「高性价比人生指南」并附仓库链接，改过内容的要注明改过。',
    },
    outputs: { epub: 'HowToLiveBetter.epub', pdf: 'HowToLiveBetter.pdf', offline: 'HowToLiveBetter.html' },
  },
  vi: {
    code: 'vi',
    readme: 'README.vi.md',
    bookGlob: 'book/vi/',
    docsGlob: 'docs/vi/',
    page: 'index.vi.html',
    title: 'Cẩm nang sống tốt với chi phí thấp',
    marks: {
      questions: '## Những câu hỏi cuốn sách này muốn giải đáp',
      toc: '## Mục lục',
      body: '## Nội dung chính',
    },
    htmlLang: 'vi',
    typstLang: 'vi', typstRegion: 'vn',
    coverImage: '/og-vi.png',
    labels: {
      front: 'Lời nói đầu', contents: 'Tóm tắt các phần', about: 'Thông tin bản dựng',
      toc: 'Mục lục',
      aboutLead: 'Bản điện tử này được sinh tự động từ phần Markdown trong kho. Bản trong tay bạn:',
      builtAt: 'Thời điểm dựng', commit: 'Commit tương ứng',
      epubLead: 'Bản điện tử này được sinh tự động từ phần Markdown trong kho. Bản trong tay bạn:',
      latestDownload: 'Tải bản mới nhất', siteLine: 'Trang tra cứu trực tuyến (lọc theo từ khóa, phần, mức bằng chứng và chi phí)', repoLine: 'Kho mã nguồn, góp ý và hồ sơ kiểm chứng nguồn của từng mục',
      internalLinks: 'Liên kết tới các tệp khác trong kho đã đổi thành liên kết trong sách; liên kết tới hồ sơ kiểm chứng, giấy phép và những tệp không đưa vào sách đã đổi thành địa chỉ GitHub.',
      navToc: 'Mục lục', navCover: 'Bìa', navBody: 'Nội dung',
      offlineFoot: 'Bản ngoại tuyến, dựng ngày', offlineTz: ' (giờ Bắc Kinh)', offlineCommit: ', commit nội dung', offlineLive: '; nội dung vẫn được cập nhật, bản <a href="%SITE%">trực tuyến</a> là bản chuẩn.',
      pdfLead: 'Bản PDF này được dàn tự động từ phần Markdown trong kho. Bản trong tay bạn:',
      pdfRepoLine: 'Tải bản mới nhất, tra cứu trực tuyến, góp ý', pdfSiteLine: 'Trang tra cứu trực tuyến (lọc theo từ khóa, phần, mức bằng chứng và chi phí; lưu được thành một tệp để đọc ngoại tuyến)',
      pdfLinks: 'Liên kết tới phần khác trong sách đã đổi thành liên kết trong sách; liên kết tới hồ sơ kiểm chứng, giấy phép và những tệp không đưa vào sách đã đổi thành địa chỉ GitHub.',
      coverBuilt: 'Dựng ngày', coverTz: ' (giờ Bắc Kinh)', coverCommit: 'Commit nội dung', coverLive: 'Phần nội dung được cập nhật hằng ngày, bản trực tuyến là bản chuẩn', coverWhere: 'Bản tra cứu trực tuyến, EPUB và PDF mới nhất đều nằm ở',
      license: 'Phần nội dung phát hành theo CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Được phép đăng lại, chuyển thể, dùng cho mục đích thương mại, miễn là ghi rõ nguồn là 「高性价比人生指南」 kèm liên kết kho; bản đã sửa nội dung phải ghi rõ là đã sửa.',
    },
    outputs: { epub: 'HowToLiveBetter-vi.epub', pdf: 'HowToLiveBetter-vi.pdf', offline: 'HowToLiveBetter-vi.html' },
  },
};

export const DEFAULT_LANG = 'zh';

// 命令行里的语言：--lang vi、--lang=vi、或最后一个不是路径的短参数
export function pickLang(argv = process.argv.slice(2)) {
  for (const a of argv) {
    const m = /^--lang[= ]?(\w+)$/.exec(a);
    if (m) return assertLang(m[1]);
  }
  const bare = argv.find(a => /^(zh|vi)$/.test(a));
  return bare ? assertLang(bare) : DEFAULT_LANG;
}

function assertLang(code) {
  if (!LANGS[code]) throw new Error(`chưa khai báo ngôn ngữ "${code}" trong tools/lib/langs.mjs`);
  return code;
}

// 命令行里除了语言之外的那个参数就是输出路径
export function outputArg(argv = process.argv.slice(2)) {
  const rest = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--lang') { i++; continue; }
    if (a.startsWith('--')) continue;
    rest.push(a);
  }
  return rest[0];
}

export function outputPath(kind, lang, argv = process.argv.slice(2)) {
  return outputArg(argv) ?? `dist/${LANGS[lang].outputs[kind]}`;
}
