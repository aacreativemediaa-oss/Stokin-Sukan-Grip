#!/usr/bin/env bash
# Rebuilds assets/clips/ (gitignored) from the source footage in Google Drive
# (main folder + the 'B Rolls' folder for c01 and c04).
# Each clip is one shot at 1x speed, conformed to 1080x1920 @ 60 fps.
# usage: tools/cut_clips.sh <dir-with-downloaded-sources>
set -euo pipefail
SRC=${1:-sources}; OUT=assets/clips; mkdir -p "$OUT"
# id  film_in film_out source_file              source_in  pad(s)
while read -r id a b src ms pad; do
  d=$(python3 -c "print(round($b-$a+$pad,3))")
  pre=""; [ "$id" = c01 ] && pre="crop=1600:2844:320:0,"   # B-roll toe: frame the bruised nail
  ffmpeg -nostdin -v error -y -ss "$ms" -i "$SRC/$src.mp4" -t "$d" \
    -vf "${pre}scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=60,format=yuv420p" \
    -c:v libx264 -preset slow -crf 15 -g 30 -c:a aac -b:a 192k -ar 48000 -ac 2 "$OUT/$id.mp4"
  echo "$id <- $src @ $ms"
done <<'CUTS'
c01 0.00 3.55 video_20250529_093604 7.55 0.04
c02 3.55 6.20 video_20260906_194651 6.00 0.1
c03 6.20 9.45 video_20260906_194608 9.00 0.1
c04 9.45 12.70 video_20251226_091215 1.00 0.1
c05 12.70 15.90 lv_0_20260801220651 5.75 0.08
c06 15.90 20.10 lv_0_20260808145834 7.15 0.1
c07 20.10 22.62 lv_0_20260801221135 17.00 0.1
c08 22.62 25.85 lv_0_20260808150503 4.94 0.02
c09 25.85 28.14 lv_0_20260801220651 41.92 0.1
c10 28.14 31.40 lv_0_20260801220651 0.30 0.1
CUTS
