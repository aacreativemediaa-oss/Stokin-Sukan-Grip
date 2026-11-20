# Stokin Sukan Grip — iklan menegak (Hyperframes)

1080×1920, 60 fps, 31.4 s. Dibina dengan [Hyperframes](https://hyperframes.heygen.com) `0.9.72` (`index.html`).
Output: `out/stokin-sukan-grip.mp4`.

## Transkrip VO (asal, tidak dipotong, 100%)

| Masa | Ayat |
| --- | --- |
| 0.00–3.46 | Tak nak jadi melecit lebam macam ni, korang tukar stokin yang korang pakai tu. |
| 3.60–6.10 | Especially yang aktif bersukan, yang banyak bergerak. |
| 6.30–9.30 | Tapak kaki akan banyak bergesel dalam kasut setiap kali korang bergerak tau. |
| 9.54–11.50 | Lama-lama, jadi korang boleh melecit teruk. |
| 11.62–12.62 | Memang pedih gila kan? |
| 12.76–15.74 | So lepas ni, korang tukar kepada stokin anti-slip macam ni. |
| 16.04–17.62 | Dekat tapak ni ada grip dot tau. |
| 17.80–20.04 | Bila korang sentuh, akan rasa kesat dan timbul. |
| 20.16–22.60 | So geselan pun berkurang bila korang aktif bergerak. |
| 22.62–23.84 | Dan kain pun breathable sangat. |
| 24.10–26.70 | Korang pakai lama pun tak rasa panas, tak rasa berkuap tau. |
| 27.00–29.54 | Warna dah banyak restock, korang grab cepat sebelum sold out. |

Masa setiap perkataan: `transcript.words.json` (whisper large-v3).

## Senarai potongan (10 klip, setiap satu satu shot, laju 1×)

| # | Masa | Sumber | Babak | Gain → −57 LUFS |
| --- | --- | --- | --- | --- |
| c01 | 0.00–3.55 | video_20260802_130614 @1.15 | Hook: stokin lama | −31.3 dB |
| c02 | 3.55–6.20 | video_20260906_194651 @6.00 | Main pickleball | −32.2 dB |
| c03 | 6.20–9.45 | video_20260906_194608 @9.00 | Kaki bergerak atas court | −31.2 dB |
| c04 | 9.45–12.70 | lv_0_20260826195949 @0.20 | Stokin biasa + titik sakit | −10.8 dB |
| c05 | 12.70–15.90 | lv_0_20260801220651 @5.75 | Reveal stokin anti-slip | +7.0 dB |
| c06 | 15.90–20.10 | lv_0_20260808145834 @7.15 | Grip dot + sentuh | −18.9 dB |
| c07 | 20.10–22.62 | lv_0_20260801221135 @17.00 | Lompat dengan kasut | −31.9 dB |
| c08 | 22.62–25.85 | lv_0_20260808150503 @4.94 | Ujian semburan (breathable) | −35.2 dB |
| c09 | 25.85–28.14 | lv_0_20260801220651 @41.92 | 3 warna | +0.1 dB |
| c10 | 28.14–31.40 | lv_0_20260801220651 @0.30 | CTA | −3.6 dB |

VO diukur −30.0 LUFS, jadi sasaran footage −57 LUFS (27 dB di bawah VO). Gain dihadkan +12 dB.

## Bina semula

```bash
tools/cut_clips.sh <folder-footage>          # assets/clips/ (tidak dicommit)
python3 tools/synth_sfx.py assets/sfx         # SFX disintesis sendiri
npx hyperframes@0.9.72 check .
npx hyperframes@0.9.72 render . -f 60 -q delivery --video-bitrate 17M --max-bitrate 20M -o out/stokin-sukan-grip.mp4
tools/verify_audio.sh out/stokin-sukan-grip.mp4 assets/vo.wav
```
