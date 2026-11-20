#!/usr/bin/env bash
# Checks the render: VO is sample-aligned with the original, and loudness of the mix.
# usage: tools/verify_audio.sh out/stokin-sukan-grip.mp4 assets/vo.wav
set -euo pipefail
OUT=$1; VO=$2
python3 - "$OUT" "$VO" <<'PY'
import subprocess, sys, numpy as np
def pcm(f, t=None):
    cmd=["ffmpeg","-nostdin","-v","error","-i",f]+(["-t",str(t)] if t else [])+["-ac","1","-ar","48000","-f","f32le","-"]
    return np.frombuffer(subprocess.run(cmd,capture_output=True).stdout,np.float32)
out, vo = pcm(sys.argv[1]), pcm(sys.argv[2])
n = min(len(out), len(vo)); a, b = out[:n], vo[:n]
# cross-correlate a 20 s window to find the lag
w = 48000*20; A=np.fft.rfft(a[:w], 2*w); B=np.fft.rfft(b[:w], 2*w)
xc = np.fft.irfft(A*np.conj(B)); lag = int(np.argmax(np.concatenate([xc[-4800:], xc[:4800]]))) - 4800
g = np.dot(a[:n], b[:n]) / np.dot(b[:n], b[:n])
print(f"VO lag vs original: {lag} samples ({lag/48:.2f} ms); best-fit VO gain in mix: {20*np.log10(abs(g)):+.2f} dB")
PY
ffmpeg -nostdin -hide_banner -i "$OUT" -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I|Peak):"
