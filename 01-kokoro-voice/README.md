# 01 · Kokoro: a free AI voice that sounds human 🎧

> Keyword: **VOICE** · Original project: [hexgrad/kokoro](https://github.com/hexgrad/kokoro) (Apache-2.0)

Kokoro is an open-weight text-to-speech model with **82 million parameters**. It's small enough to run **offline on a normal laptop**.
I use it for every voiceover on my page.

- **54 voices** across **9 languages** (English US/UK, Spanish, French, Hindi, Italian, Japanese, Portuguese, Chinese)
- Runs on CPU, no GPU and no account needed
- Free for commercial use (Apache-2.0)

## Setup in 3 steps

I use the ONNX build ([thewh1teagle/kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx)) because it's the lightest to run.

**1. Install**
```bash
pip install kokoro-onnx soundfile
```

**2. Download the two model files** from the [kokoro-onnx releases](https://github.com/thewh1teagle/kokoro-onnx/releases) and put them next to your script:
- `kokoro-v1.0.onnx`
- `voices-v1.0.bin`

**3. Run [`speak.py`](speak.py)**
```bash
python speak.py "Your script here"
```
It writes `voice.wav`.

## My exact settings

| Setting | Value | Why |
|---|---|---|
| Voice | `am_michael` | Calm, clear male narrator |
| Speed | `1.05` | Slightly brisk, without sounding rushed |
| Language | `en-us` | |

Other voices worth trying: `bm_george` (British), `am_fenrir`, `am_puck`, `bm_fable`.

## Pro tips

- **Generate one sentence at a time** and join them. You get cleaner pauses and can redo a single line.
- Leave **0.3 to 0.4 s of silence** between sentences so it breathes.
- Finish with a loudness pass so it's even on phones: `ffmpeg -i voice.wav -af loudnorm=I=-15:TP=-1.5 out.wav`

---

Follow [@ai.with.saad](https://www.instagram.com/ai.with.saad/) for one practical AI tip every day ✨
