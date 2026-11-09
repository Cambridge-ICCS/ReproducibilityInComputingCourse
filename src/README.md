# Building the slides

The slide deck (`slides.qmd`) is generated with [quarto](https://quarto.org) and outputs `index.html` in this directory.

## Requirements

- The [quarto CLI](https://quarto.org/docs/get-started/)
- A Python installation with the packages from [requirements.txt](../requirements.txt) (Quarto executes the Python code cells with `python3`).
- The `Summer-school-Intro-Git` submodule checked out (some slides are included from it).

## Setup

Fetch the summer school submodule:
```bash
git submodule update --init --recursive
```
(or clone with `git clone --recurse-submodules <url>`).

Set up the a Python environment from the repository root.
With a Python venv this would be:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you use [nix](https://nixos.org/), the root [flake.nix](../flake.nix) provides a shell with quarto and all Python dependencies:

```bash
nix develop
```

## Render

From this directory (`src/`):

```bash
quarto render slides.qmd
```

If you used a virtual environment, make sure its `bin` directory is on your `PATH` so that `python3` resolves to it:

```bash
PATH="$PWD/../.venv/bin:$PATH" quarto render slides.qmd
```

The rendered deck is written to `index.html` in this directory.
