# Your job, in one page

Enter make.fun's GTA 6 meme bounty: one meme about GTA 6, posted on X from a
public account, handed in as this repository. The post itself is the entry —
the judge sees its first picture, then its text.

## The meme (done)

`meme.png`: GTA 6 launch night. The gamer is asleep on the couch; make.fun's
white ghost mascot (sparkle eyes, magenta star coin) sits in the gaming chair
playing Vice City at sunrise. Captions: "GTA 6 LAUNCH NIGHT" / "ME: WASTED.
MY AGENT: STILL GRINDING." The ghost is large, in-scene, and recognisable —
it is the make.fun brand in the picture, which the judge weighs first.

## Still to do (main session)

1. **Get the real play code.** The bounty gate needs a play code of the form
   `makefun-<word>-<word>-<word>`. `n4ek0hab` is the account's *referral*
   code, NOT a play code — a post carrying only that code is refused.
   Fetch one from `GET /api/competitions/gta6-meme-x-01/play-code`
   (`?n=0` to `?n=3` give the four codes; any one passes).
2. **Post on X** from public `@HuyDieu9296`, before the deadline
   23/11/2026 21:00 VN, with `meme.png` as the first picture and the text in
   `x-post.txt` (bounty link + `@makefunai` + play code + the earn-money
   line). Keep the post up and the account public until the results are out
   (~08/12).
3. **Fill in `POST.json`** with the post's address
   (`https://x.com/HuyDieu9296/status/<id>`). The placeholder there now is
   refused by the gate on purpose.
4. **Create the GitHub repo** `huydieu9296/gta6-meme-x-01` (public, MIT),
   push this directory, set its About: website on make.fun, topic `makefun`.
5. **Test** `mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts`
   (Node 22+; this machine has Node v24.22.1) and check `out/POST.json`.
6. **Submit from the main session** with the kit CLI
   (`node cli/makefun.mjs check` then `submit`), uploading the transcripts
   of the sessions that made the meme and this repository.

## Hard rules

- Post and repo must be created at or after the bounty opening
  (2026-11-19T14:00:00Z); a session that began before it cannot be entered.
- At most 5 submissions a day, 10 in all; the last submission before the
  deadline is the final entry.
- No network, no wall clock, no files outside the repository in `main.ts`.
- The post's text cannot be edited after posting — get the link, tag and
  play code right the first time.
