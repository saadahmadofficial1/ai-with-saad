# 02 · Pro sound effects for AI edits, free 🔊

> Keyword: **SOUND** · Tools: [Openverse](https://openverse.org) (free, openly licensed media search) · [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) (MIT)

AI can make your edits look great. Sound is what makes them feel premium. These two free tools fix that.

## 1. Openverse: find free sounds (no account, no key)

Search openly licensed audio and filter to **CC0 / public domain**, so no credit is legally required (crediting is still nice).

- Website: search at openverse.org, choose **Audio**, then filter **License → CC0**.
- API (great for automation):
```bash
curl "https://api.openverse.org/v1/audio/?q=whoosh&license=cc0&page_size=5"
```
Each result gives the title, creator, licence and a download URL.

## 2. Earshot: give your AI agent ears

Open source (MIT). Runs locally on your CPU, with no GPU. Works as a CLI, a Python API and an MCP server.

- Describes what a sound is, finds moments in a recording, and critiques a whole film's sound mix.
- `earshot sfx` / `earshot kit`: sound effects **made in code** (252 in v0.4), placed on your cuts.

**Install** (Python 3.10+, ffmpeg on PATH):
```bash
git clone https://github.com/Leonxlnx/earshot && cd earshot
python -m venv .venv
.venv/bin/python -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.venv/bin/python -m pip install -e ".[mcp,llm,dev]"
.venv/bin/python -m earshot doctor --load
```
The first run downloads two open models (about 1.1 GB). After that it works offline.

## My sound rules for edits

| Rule | Why |
|---|---|
| **No music bed under a voiceover** | The voice is the product; music fights it |
| **No whoosh on every cut** | It gets repetitive fast and sounds cheap |
| **One impact on frame 1** | Stops the scroll |
| **Soft taps only on key reveals**, about 20 dB under the voice | Felt, not heard |
| **Never rapid ticks or dings** | They sound like a slot machine |

---

Part of [AI With Saad](https://github.com/saadahmadofficial1/ai-with-saad) · [all my projects](https://github.com/saadahmadofficial1) · follow [@ai.with.saad](https://www.instagram.com/ai.with.saad/) ✨
