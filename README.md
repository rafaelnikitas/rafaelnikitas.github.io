# Nikitas Rafael Nikitas — portfolio

An editable Quarto website for three public case studies: Beyond FIFA Potential, Agora Match, and Football Forecasting Lab.

**Website:** https://rafaelnikitas.github.io

## Edit the story

Edit the ordinary Markdown in `index.qmd`, `about.qmd`, or a study's `index.qmd`. The site builds from saved charts and computed tables. It does not train models or require API keys.

| File | Purpose |
|---|---|
| `index.qmd` | Homepage and featured work |
| `projects/index.qmd` | Searchable project catalogue |
| `writing/index.qmd` | Analysis and article catalogue |
| `about.qmd` | Professional background and contact profiles |
| `studies/*/index.qmd` | Editable case-study narratives |
| `assets/` | Recorded plots and application screenshots |
| `demos/scouting.html` | Browser-only scouting replay |
| `styles.css` | Visual design and responsive layouts |

## Preview and publish

Install Quarto 1.11.9 or a compatible newer version, then run:

```bash
quarto preview
```

Pushes to `main` run the Pages workflow: render, check local links, upload the static site and deploy. In GitHub repository **Settings → Pages**, select **GitHub Actions** as the source. `quarto render` creates `_site/`; it is a build artifact and is not committed.

## Evidence boundaries

- FIFA results are retrospective game-rating outcomes, not measured real-world scouting impact. The latest explained shortlist uses 21 September 2025 data.
- Agora Match uses fictional synthetic data. Its static demo has deterministic answers; the separately hosted Azure application is documented in its own repository.
- Forecasting Lab's published benchmark is synthetic. Real EPL and La Liga benchmark evidence remains pending.

Source data, project code and screenshots retain their original notices. Site text and design © Nikitas Rafael Nikitas. No additional blanket code license is declared.
