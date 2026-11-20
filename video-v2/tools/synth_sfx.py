"""Synthesise all SFX from scratch (numpy only). Output: 48 kHz stereo 16-bit WAV.
Each sound is normalised to a quiet target so it always sits under the voiceover."""
import numpy as np, wave, sys, os
SR = 48000
rng = np.random.default_rng(7)
out = sys.argv[1] if len(sys.argv) > 1 else "assets/sfx"
os.makedirs(out, exist_ok=True)

def t(d): return np.arange(int(SR * d)) / SR
def env(n, a, r, curve=4.0):
    e = np.ones(n); na = max(1, int(a * SR)); e[:na] = np.linspace(0, 1, na)
    e[na:] = np.exp(-curve * np.linspace(0, 1, n - na) * (n - na) / SR / max(r, 1e-3))
    return e
def lp(x, fc):  # one-pole low-pass, fc may be array
    fc = np.broadcast_to(fc, x.shape); y = np.zeros_like(x); s = 0.0
    a = 1 - np.exp(-2 * np.pi * fc / SR)
    for i in range(len(x)): s += a[i] * (x[i] - s); y[i] = s
    return y
def hp(x, fc): return x - lp(x, fc)
def bp(x, lo, hi): return hp(lp(x, hi), lo)
def sweep(f0, f1, d, shape="exp"):
    k = np.linspace(0, 1, int(SR * d))
    f = f0 * (f1 / f0) ** k if shape == "exp" else f0 + (f1 - f0) * k
    return np.sin(2 * np.pi * np.cumsum(f) / SR)

def whoosh():
    d = 0.55; n = int(SR * d); x = rng.standard_normal(n)
    k = np.linspace(0, 1, n); fc = 300 + 5200 * np.sin(np.pi * k) ** 2
    y = bp(x, 200, 1) if False else lp(x, fc); y = hp(y, 150)
    return y * np.sin(np.pi * k) ** 1.5
def pop():
    d = 0.12; tt = t(d); f = 900 * np.exp(-tt * 28) + 380
    y = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(tt), 0.002, 0.05)
    return y + 0.15 * hp(rng.standard_normal(len(tt)), 3000) * env(len(tt), 0.0005, 0.008)
def ding():
    d = 1.4; tt = t(d); y = np.zeros_like(tt)
    for f, a, r in [(1568, 1, 0.9), (3136, .45, .5), (4704, .25, .3), (2350, .2, .6)]:
        y += a * np.sin(2 * np.pi * f * tt) * env(len(tt), 0.003, r)
    return y
def impact():
    d = 0.9; tt = t(d); f = 120 * np.exp(-tt * 9) + 42
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(tt), 0.002, 0.45)
    crack = lp(rng.standard_normal(len(tt)), 2500) * env(len(tt), 0.001, 0.06)
    return np.tanh(1.6 * (boom + 0.6 * crack))
def cha_ching():
    d = 1.3; tt = t(d); y = np.zeros_like(tt)
    for st in (0.0, 0.07):  # mechanical "cha" clicks
        i = int(st * SR); m = int(0.05 * SR)
        y[i:i + m] += 0.7 * hp(rng.standard_normal(m), 2500) * env(m, 0.0005, 0.02)
    i = int(0.16 * SR); tb = tt[: len(tt) - i]  # "ching" bell
    bell = sum(a * np.sin(2 * np.pi * f * tb) * env(len(tb), 0.002, r)
               for f, a, r in [(2093, 1, .7), (2637, .7, .6), (3136, .5, .5), (4186, .35, .35), (5274, .2, .25)])
    y[i:] += 0.8 * bell
    return y
def riser():
    d = 1.6; n = int(SR * d); k = np.linspace(0, 1, n)
    tone = sweep(180, 1400, d) * 0.5 + sweep(181.5, 1410, d) * 0.5
    noise = lp(rng.standard_normal(n), 400 + 7000 * k ** 2)
    y = (0.6 * tone + 0.7 * noise) * k ** 2.2
    y[-int(0.03 * SR):] *= np.linspace(1, 0, int(0.03 * SR))
    return y
def zap():
    d = 0.32; tt = t(d); f = 2400 * np.exp(-tt * 14) + 120
    car = np.sin(2 * np.pi * np.cumsum(f) / SR + 3 * np.sin(2 * np.pi * 90 * tt))
    return np.tanh(2 * car) * env(len(tt), 0.001, 0.12)

def loudness_rms_db(x):  # simple K-ish proxy: RMS of 400 ms max window
    w = int(0.4 * SR); x2 = np.convolve(x ** 2, np.ones(w) / w, "same")
    return 10 * np.log10(np.max(x2) + 1e-12)
def write(name, y, target_db):
    y = y / (np.max(np.abs(y)) + 1e-9)
    y *= 10 ** ((target_db - loudness_rms_db(y)) / 20)
    pk = np.max(np.abs(y)); y = y / pk * min(pk, 10 ** (-12 / 20))  # peak <= -12 dBFS
    fade = int(0.004 * SR); y[-fade:] *= np.linspace(1, 0, fade)
    st = np.stack([y, y], 1)
    with wave.open(os.path.join(out, name + ".wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype("<i2").tobytes())
    print(name, round(len(y) / SR, 2), "s")

# Targets tuned so each SFX lands near -40 LUFS (~10 dB under the -30 LUFS voiceover).
for name, fn, tgt in [("whoosh", whoosh, -46), ("pop", pop, -45), ("ding", ding, -40),
                      ("impact", impact, -37), ("cha-ching", cha_ching, -43.5),
                      ("riser", riser, -41), ("zap", zap, -44)]:
    write(name, fn(), tgt)
