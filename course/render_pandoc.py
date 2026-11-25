#!/usr/bin/env python3
"""Render a chapter .qmd to HTML exactly like chapters 1-2 (pandoc Reveal.js, CDN scripts,
images embedded as data URIs). Usage: python3 render_pandoc.py chapter-3-slides.qmd [transition]"""
import sys, re, base64, mimetypes, subprocess, pathlib
src = pathlib.Path(sys.argv[1]); out = src.with_suffix('.html')
cmd = ['pandoc', str(src), '-f', 'markdown', '-s', '-t', 'revealjs', '--mathjax',
       '-V', 'revealjs-url=https://unpkg.com/reveal.js@^4/', '-V', 'theme=black',
       '-c', 'slides.css', '-H', 'head-extras.html', '-o', str(out)]
if len(sys.argv) > 2: cmd[-2:-2] = ['-V', 'transition=' + sys.argv[2]]
subprocess.run(cmd, check=True, stderr=subprocess.DEVNULL)
h = out.read_text(encoding='utf-8')
# Drop pandoc's own MathJax / Reveal math-plugin tags: head-extras.html already loads MathJax
# with the course configuration (same as chapters 1-2).
h = re.sub(r'\s*<script[^>]*polyfill[^>]*></script>', '', h)
h = re.sub(r'\s*<script[^>]*id="MathJax-script"[^>]*></script>', '', h)
h = re.sub(r'\s*<script[^>]*plugin/math/math\.js"[^>]*></script>', '', h)
h = re.sub(r'\s*RevealMath,', '', h)
def emb(m):
    p = src.parent / m.group(2)
    if not p.exists(): return m.group(0)
    mt = mimetypes.guess_type(p.name)[0] or 'image/png'
    return f'{m.group(1).replace("data-src=","src=")}"data:{mt};base64,{base64.b64encode(p.read_bytes()).decode()}"'
h = re.sub(r'(<img[^>]*?\s(?:data-)?src=)"(images/[^"]+)"', emb, h).replace(' data-src="data:', ' src="data:')
out.write_text(h, encoding='utf-8'); print('wrote', out)
