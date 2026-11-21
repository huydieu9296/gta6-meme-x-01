# STATUS — gta6-meme-x-01 (bản nháp, làm 19/11/2026 ~23:30 VN)

Bounty: Post a GTA 6 meme on X — $500, 50 suất (nhất $100, nhì $60, ba $30,
4–10 mỗi $10, 11–50 mỗi $6). Hạn nộp: 23/11/2026 21:00 VN
(2026-11-23T14:00:00Z). Kết quả ~08/12.

## Concept meme
GTA 6 launch night: gamer ngủ gục trên sofa, tay cầm rơi xuống sàn; ma trắng
make.fun (mắt lấp lánh, đồng xu sao magenta) ngồi ghế gaming cầm tay cầm,
vẫn đang cày Vice City lúc bình minh. Caption trong ảnh:
"GTA 6 LAUNCH NIGHT" / "ME: WASTED. MY AGENT: STILL GRINDING."
"WASTED" là màn hình chết đặc trưng của GTA; ma = agent — vừa là joke, vừa
là pitch make.fun (agent kiếm tiền thật trong lúc người ngủ).

## Checklist
- [x] Đọc competition.yaml + starter (main.ts / README / AGENT.md / POST.json)
- [x] Xác minh referral code n4ek0hab (`node cli/makefun.mjs referrals`)
- [x] Tạo ảnh nền bằng image-gen (không chữ), overlay caption bằng PIL
- [x] Tự xem lại meme.png: ma rõ, chữ đọc được, không lỗi chính tả/méo chữ
- [x] Viết tay trong session này: main.ts, README.md (3 badge make.fun),
      AGENT.md, LICENSE MIT, POST.json (placeholder), x-post.txt, STATUS.md
- [x] Chạy thử main.ts với MAKEFUN_OUTPUT_DIR (Node v24.22.1) — xem dưới
- [ ] Lấy play code THẬT dạng makefun-xxx-yyy-zzz (xem Blocker)
- [ ] Đăng X từ @HuyDieu9296 (ảnh meme.png + caption x-post.txt)
- [ ] Điền URL post thật vào POST.json
- [ ] Tạo repo GitHub huydieu9296/gta6-meme-x-01, push, set About
      (website make.fun, topic makefun)
- [ ] Chạy `node cli/makefun.mjs check` + submit từ PHIÊN CHÍNH
      (kèm transcript các session làm meme + repo này)

## Test main.ts (19/11 ~23:35 VN)
`mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts`
→ exit 0, không in gì (chỉ warning MODULE_TYPELESS_PACKAGE_JSON vô hại,
starter cũng vậy — không có package.json), out/POST.json byte-for-byte giống
POST.json gốc (đã cmp). Node trên máy: v24.22.1 (≥ 22.18 yêu cầu).

## Blocker / lưu ý
- ⚠️ PLAY CODE CHƯA CÓ: n4ek0hab là referral code, KHÔNG phải play code.
  Post bắt buộc phải có play code `makefun-<từ>-<từ>-<từ>` (lấy qua
  GET /api/competitions/gta6-meme-x-01/play-code, ?n=0..3), nếu không gate
  từ chối ngay từ intake. x-post.txt đã để placeholder, phiên chính điền
  trước khi đăng.
- POST.json hiện là placeholder — cố tình, gate từ chối cho đến khi có URL thật.
- Không nộp entry từ session này; việc nộp do phiên chính làm.

## Cập nhật 19/11 ~23:35 VN (phiên watch)
- Play code THẬT đã lấy qua API: makefun-swallow-condor-hornet (n=0/4). Đã điền vào x-post.txt. Lưu ý: n4ek0hab chỉ là referral code, không dùng làm play code.
- Meme.png đã kiểm tra trực tiếp: ma rõ, chữ sạch, không lỗi.
