#!/bin/sh
# Usage: ./render.sh chapter-3-slides.qmd
# Builds the HTML the same way as chapters 1-2 (pandoc + Reveal.js from CDN, images embedded).
# Needs pandoc and Python 3. Transition: none.
python3 render_pandoc.py "$1" none
