// gta6-meme-x-01 entry: "Post a GTA 6 meme on X".
//
// The entry is the X post itself. This program (Node 22, standard library
// only) does the one thing the bounty asks of it: it copies POST.json from
// the repository root to /output/POST.json, where the house reads the post's
// address and then reads the post from X (its first picture and its text)
// to hand to the judge. Nothing this program writes is judged.
//
// POST.json currently holds the placeholder address
// "https://x.com/<handle>/status/<id>" — it is NOT a real post yet. Replace
// it with the real post's address after the meme is posted on X, before
// submitting. With the placeholder in place the gate refuses the entry,
// by design: a starter that passed would need no post at all.
//
// Local test (mirrors the grader's /bot and /output):
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
// Afterwards out/POST.json is byte for byte this directory's POST.json.

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });

try {
  copyFileSync(join(BOT_DIR, 'POST.json'), join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`could not copy POST.json from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
