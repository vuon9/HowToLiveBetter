// Dựng og-vi.png (banner mạng xã hội tiếng Việt) từ tools/og-vi.html.
// Số trong og-vi.html do tools/sync-stats.mjs ghi lại cùng og.html; ở đây chỉ chụp ảnh.
//
//   node tools/translate-vi/build-og.mjs
//
// Chrome tìm theo các đường dẫn quen thuộc, hoặc đặt biến môi trường CHROME.
import { spawnSync } from 'node:child_process';
import { existsSync, mkdtempSync, rmSync, statSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '../..');
const CHROME_PATHS = [
  process.env.CHROME,
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/usr/bin/google-chrome',
  '/usr/bin/google-chrome-stable',
  '/usr/bin/chromium',
  '/usr/bin/chromium-browser',
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
];
const chrome = CHROME_PATHS.find(p => p && existsSync(p));
if (!chrome) throw new Error('không tìm thấy Chrome, đặt biến môi trường CHROME trỏ tới nó');

const profile = mkdtempSync(join(tmpdir(), 'og-vi-shot-'));
const target = join(ROOT, 'og-vi.png');
const startedAt = Date.now();
spawnSync(chrome, [
  '--headless', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
  '--window-size=1200,630', `--user-data-dir=${profile}`, `--screenshot=${target}`,
  pathToFileURL(join(ROOT, 'tools', 'og-vi.html')).href,
], { stdio: 'ignore', timeout: 60000, killSignal: 'SIGKILL' });
rmSync(profile, { recursive: true, force: true });

const png = statSync(target);
if (png.mtimeMs < startedAt - 1000) throw new Error('og-vi.png không được ghi trong lần chạy này, chụp ảnh thất bại');
if (png.size < 120 * 1024 || png.size > 400 * 1024) throw new Error(`og-vi.png có kích thước bất thường (${png.size} byte), mở ra xem thử`);
console.log(`og-vi.png đã dựng lại: ${png.size} byte, tự kiểm tra đạt.`);
