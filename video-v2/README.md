# Stokin Sukan Grip — iklan menegak v2 (VO baharu, Hyperframes)

1080×1920, 60 fps, 32.15 s, Hyperframes `0.9.72` (`index.html`). Output: `out/stokin-sukan-grip-v2.mp4` (65.5 MB).
VO baharu: Drive `1XGDB-BqypgGGy2HwsylGDth3xBR08HcE`, diukur −29.5 LUFS → footage diselaraskan ke −56.5 LUFS (27 dB di bawah VO, had +12 dB).

## Transkrip VO (asal, tidak dipotong, 100%)

| Masa | Ayat |
| --- | --- |
| 0.00–4.00 | Kalau tak nak jadi korang melecet lebam macam ni, korang kena tukar stokin yang korang pakai tu. |
| 4.14–9.18 | Especially yang aktif bersukan, macam jogging dan running tu, tapak kaki korang akan bergesel dalam kasut tau. |
| 9.36–11.70 | Sebab tu lama-lama, jadi korang boleh jadi melecet teruk. |
| 11.88–15.64 | So lepas ni, korang tukar kepada stokin jenis anti-slip macam ni. |
| 15.78–17.52 | Dekat tapak ni, dia ada grip dot tau. |
| 17.80–20.22 | Memang rasa kesat dan rasa timbul bila korang sentuh. |
| 20.34–23.78 | So lepas ni, tapak kaki korang kurang bergesel bila korang aktif bergerak. |
| 23.86–27.14 | Dan kain dia pun breathable, tak panas berkuap bila korang pakai lama tau. |
| 27.52–30.58 | Sekarang warna dah banyak restock, korang boleh grab sekarang sebelum sold out. |

Masa setiap perkataan: `transcript.words.json` (whisper large-v3; ejaan dibetulkan dalam caption: lebam, bergesel, berkuap, restock, grab).

## Potongan (10 klip, satu shot setiap satu, laju 1×)

| # | Masa | Sumber | Babak | Gain |
| --- | --- | --- | --- | --- |
| c01 | 0.00–2.20 | B Rolls/video_20250529_093604 @7.70 (crop) | Hook: kuku jari lebam | −30.2 dB |
| c02 | 2.20–4.25 | video_20260802_130614 @1.15 | Stokin lama | −19.4 dB |
| c03 | 4.25–7.28 | B Rolls/video_20251226_091144 @2.00 | Jogging | −25.6 dB |
| c04 | 7.28–9.45 | video_20260906_194608 @9.00 | Kaki bergesel dalam kasut | −32.1 dB |
| c05 | 9.45–12.00 | B Rolls/video_20251226_091215 @1.00 | Pegang kaki kesakitan | −18.3 dB |
| c06 | 12.00–15.72 | lv_0_20260801220651 @5.12 | Reveal stokin anti-slip | −18.9 dB |
| c07 | 15.72–20.30 | lv_0_20260808145834 @7.10 | Grip dot + sentuh | −18.5 dB |
| c08 | 20.30–23.84 | lv_0_20260801221135 @16.00 | Lompat dengan kasut | −31.2 dB |
| c09 | 23.84–27.12 | lv_0_20260808150503 @4.91 | Ujian semburan (breathable) | −34.9 dB |
| c10 | 27.12–32.15 | lv_0_20260801220651 @0.00 | CTA | −14.7 dB |

## Bina semula

```bash
tools/cut_clips.sh <folder-footage+broll>
npm run check && npm run render
tools/verify_audio.sh out/stokin-sukan-grip-v2.mp4 assets/vo.wav
```
