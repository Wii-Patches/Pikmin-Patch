# Pikmin Patch

Play **New Play Control! Pikmin** (Wii) with a **GameCube controller** — using
the controls of the original GameCube game — or with a **Classic Controller**
instead of the Wii Remote and Nunchuk. Works with the USA (`R9IE01`), European
(`R9IP01`) and Japanese (`R9IJ01`) releases, and each patch is optional.

The patches are applied to your own copy of the game: drop a clean `.wbfs` or
`.iso` onto the patcher and play the result on a Wii (USB loader) or in
Dolphin. Nothing from the game is included in this repository.

![Pikmin](assets/logo.png)

## How it works, in one paragraph

The game was written for a Wii Remote with a Nunchuk. The patches rewrite
whatever you are holding into exactly that — right where the Wii's `KPAD`
library reads its samples — so the game just runs its ordinary Nunchuk code. The
pointer, which the game aims its cursor with, is synthesised from a stick.
See [docs/TECHNICAL.md](docs/TECHNICAL.md) for the details.

## Controls

### GameCube controller (port 1)

The layout is the original GameCube game's. Where the Wii version moved an
action to another button, the patch presses that button for you.

| Input | Action |
| --- | --- |
| Control stick | Move · the cursor sits where the stick points |
| C stick | Swarm (direction and distance by where it points) |
| A | Hold and throw a Pikmin · pluck · punch · Onion menu |
| B | Whistle |
| X | Dismiss (tap) · lie down (hold) |
| Y | Radar / Map |
| L | Face the camera forward (tap) · rotate it with the stick (hold) |
| R | Change camera distance / zoom (tap) |
| Z | Change camera vertical angle |
| D-pad | Camera controls · (while holding a Pikmin) left/right swap type, up/down swap maturity |
| Start | Pause |

### Classic Controller

| Input | Action |
| --- | --- |
| Left stick | Move |
| Right stick | Aim the cursor |
| A | Hold and throw a Pikmin · pluck · punch · Onion menu |
| B | Whistle · (while holding a Pikmin) swap type |
| X | Dismiss (tap) · lie down (hold) |
| Y or − | Radar / Map |
| ZL | Face the camera forward (tap) · rotate it (hold) |
| L / R | Camera zoom (in / out) |
| ZR | Swarm · (while holding a Pikmin) swap maturity |
| D-pad | Camera distance and angle · swarm (down) |
| + | Pause |
| HOME | HOME Menu |

With a Classic Controller on a Wii U (vWii) injection, enable *Force Classic
Controller Connected*.

## Installing

### Patch your disc image

You need a clean `.wbfs` or `.iso` of the game. Download the patcher for your
system from the releases page (or the artifacts of the latest CI run), or run
it from source (needs Python 3 with tkinter and
[Wiimms ISO Tool](https://wit.wiimm.de/) (`wit`) on your `PATH`):

```bash
python3 tools/gui.py
```

Tick the patches you want, then drop the image onto the window (or click to
choose it). The patcher checks the disc id, patches `sys/main.dol`, rebuilds the
image in the same format and replaces your file, keeping the original next to
it as `<name>.bak`. Other releases, and images already modified by something
else, are refused rather than corrupted. You can run it again later to add the
other patch.

There is a command-line twin:

```bash
python3 tools/patch_disc.py "Pikmin (USA) (En,Fr,Es).wbfs" --cc --gc
```

### Gecko codes (Dolphin)

Copy `codes/<disc id>.ini` (`R9IE01`, `R9IP01` or `R9IJ01`) into Dolphin's
`GameSettings` folder and enable the codes under **Properties → Gecko Codes**.
The two codes are independent. Set GameCube Port 1 to a Standard Controller
(for the GameCube patch). A Wii Remote is optional for the GameCube patch.

The same codes are in `codes/<disc id>.txt` in the plain layout loaders read.

### Riivolution

`riivolution/<disc id>.xml` is a Riivolution patch with one switch per feature.
Put it in your Riivolution folder (or Dolphin's `Load/Riivolution`) and enable
the options you want. It matches on the disc id and version, so it cannot be
applied to the wrong release.

### Which release do I have?

The disc id is the first six characters of the disc (`R9IE01` USA, `R9IP01`
Europe, `R9IJ01` Japan). `python3 tools/patch_disc.py` and the GUI read
it for you.

## Limits

- The GameCube controller works with **no Wii Remote connected at all**; with one
  connected, the remote's own buttons still work alongside the pad. GameCube
  port 1 drives player 1.
- Without a Wii Remote there is no HOME button (the HOME Menu belongs to the
  remote) and no rumble.
- Plug the GameCube controller in **before** starting the game; hot-plugging is
  not handled.
- While a patched controller is in use, the Wii Remote's own pointer is ignored:
  the cursor follows the stick.
- The Classic Controller still plugs into a Wii Remote, so that patch needs one.

## Repository layout

| Path | What |
| --- | --- |
| `src/` | the PowerPC routines (devkitPPC assembly) and the per-release builders |
| `tools/` | the patcher, GUI, Gecko / Riivolution generators and the checks |
| `tools/prebuilt/` | the patch data the patcher ships (generated from `src/`) |
| `codes/`, `riivolution/` | generated Gecko code lists and Riivolution patches |
| `docs/TECHNICAL.md` | how the patches work |

Rebuilding the patch data from source needs devkitPPC and your own `main.dol`
dumps; end users need neither:

```bash
P1_DOLS=/path/with/R9IE01.dol,R9IP01.dol,R9IJ01.dol python3 tools/gen_prebuilt.py
python3 tools/build.py
python3 tools/check.py
```

## License

MIT, see [LICENSE](LICENSE).
