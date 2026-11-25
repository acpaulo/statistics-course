# Editing the course

- Slides are the `chapter-N-slides.qmd` files. Each `## Heading` is one slide; `###` is a sub-heading on the same slide.
- After editing run `./render.sh chapter-3-slides.qmd` (needs pandoc and Python 3). It builds the HTML in the same way as chapters 1 and 2.
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
