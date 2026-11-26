# Editing the course

- Slides are the `chapter-N-slides.qmd` files. Each `## Heading` is one slide; `###` is a sub-heading on the same slide.
- After editing run `./render.sh chapter-9-slides.qmd` (needs pandoc and Python 3). It builds the HTML in the same way as chapters 1 and 2 (chapters 3 to 9 follow the same layout).
- Images are in `images/chapter-N/` and are embedded in the HTML when you render.
- Quiz questions are `::: {.practice-question data-correct="B" data-explanation="..."}` blocks.
- The R helper functions (epsilon-squared, Dunn, Kendall's W, Nemenyi) are inside the script at the end of each `.qmd`.
- `index.html` is the landing page (edit it directly).
- Upload the `.html` files, `slides.css` and `.nojekyll` to GitHub (keep them in the same folder).
  Reveal.js, formulas (MathJax) and the R editor (WebR) load from the internet.

## Figure size
Figures in chapters 3-4 are limited by the `<style id="figure-size">` block at the end of `head-extras.html`
(`max-height:34vh`, `max-width:88%`). Change these numbers and re-run `./render.sh chapter-N-slides.qmd`.
## Index
`index.html` links to `chapter-N-slides.html` in the same folder (or in a `course/` subfolder). Open it through
GitHub Pages or a web server; if a lesson is missing, the page says which file is not found.

## Colours used in chapters 3 to 9
The figures and infographics share one palette: blue `#4a7fb5`, green `#2e8b6e`, orange `#d98a3d`, red `#d9534f`, purple `#7a4fb0`, dark text `#14233a`, notes `#355a85`, grey `#6d7f8f`, headings `#0b4fa8`. Figures have no title inside the picture: the caption on the slide describes them.
