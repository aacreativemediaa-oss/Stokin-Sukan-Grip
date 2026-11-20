#!/usr/bin/env bash
# Rebuilds assets/clips/ (gitignored) from the source footage in Google Drive
# (main footage folder + the 'B Rolls' folder). One shot per clip, 1x speed, 1080x1920 @ 60 fps.
# usage: tools/cut_clips.sh <dir-with-all-downloaded-sources>
set -euo pipefail
SRC=${1:-sources}; OUT=assets/clips; mkdir -p "$OUT"
# id  film_in film_out source_file  source_in  pad(s)
while read -r id a b src ms pad; do
  d=$(python3 -c "print(round($b-$a+$pad,3))")
  pre=""; [ "$src" = video_20250529_093604 ] && pre="crop=1600:2844:320:0,"   # B-roll toe: frame the bruised nail
  ffmpeg -nostdin -v error -y -ss "$ms" -i "$SRC/$src.mp4" -t "$d" \
    -vf "${pre}scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=60,format=yuv420p" \
    -c:v libx264 -preset slow -crf 15 -g 30 -c:a aac -b:a 192k -ar 48000 -ac 2 "$OUT/$id.mp4"
  echo "$id <- $src @ $ms"
done <<'CUTS'
c01 0.00 2.20 video_20250529_093604 7.70 0.1
c02 2.20 4.25 video_20260802_130614 1.15 0.1
c03 4.25 7.28 video_20251226_091144 2.00 0.1
c04 7.28 9.45 video_20260906_194608 9.00 0.1
c05 9.45 12.00 video_20251226_091215 1.00 0.1
c06 12.00 15.72 lv_0_20260801220651 5.12 0.08
c07 15.72 20.30 lv_0_20260808145834 7.10 0.1
c08 20.30 23.84 lv_0_20260801221135 16.00 0.1
c09 23.84 27.12 lv_0_20260808150503 4.91 0.0
c10 27.12 32.15 lv_0_20260801220651 0.00 0.0
CUTS
