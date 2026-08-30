# Shawn Lin — Personal Website

The first production version of [shawnlin.me](https://shawnlin.me): a warm editorial personal site for professional work, photography, journal entries, travel notes, and future ideas.

## Stack

- Astro and TypeScript
- Tailwind CSS 4 through the Vite plugin
- Markdown / MDX content collections
- Local Newsreader and Inter font files
- Static GitHub Pages deployment

Node 24 is recommended and recorded in `.nvmrc`.

## Local development

```sh
npm install
npm run dev
```

Astro prints the local preview URL, normally `http://localhost:4321`.

## Validate and build

```sh
npm run check
npm run build
npm run preview
```

The static output is written to `dist/`.

## Deployment

Push `main` to GitHub. `.github/workflows/deploy.yml` builds the Astro site and deploys it to GitHub Pages. In the repository's Pages settings, choose **GitHub Actions** as the publishing source.

The project already includes `public/CNAME` for `shawnlin.me` and Astro's production `site` value is `https://shawnlin.me`. The domain's DNS still needs to point to GitHub Pages in the domain provider.

## Editing work history

Work chapters live in `src/content/work/`. Each Markdown or MDX file uses:

```yaml
company: Company name
role: Role title
period: 2025 — Present
order: 1
summary: One concise public description.
location: Optional location
```

The homepage and `/work` both read from this collection.

## Adding photography

1. Export an optimized web copy of the photograph. Keep the full-resolution original outside the public repository.
2. Place the web copy in `public/images/` using a descriptive filename. JPEG is supported now; adding AVIF/WebP sources later is straightforward through a shared picture component.
3. Add a Markdown or MDX file in `src/content/photography/`:

```yaml
title: Collection title
description: Short description
date: 2026-08-30
cover: /images/example.jpg
coverAlt: Meaningful description of the photograph
orientation: landscape
featured: true
placeholder: false
```

The three first-release photographs are generated image studies and are labeled as such in their records and on the site. Replace them with Shawn's own optimized images before treating the photography collection as final.

The About portrait is intentionally not fabricated. Replace the portrait placeholder in `src/pages/index.astro` and `src/pages/about.astro` with a real optimized photograph of Shawn and his dog.

## Adding journal entries

Create a Markdown or MDX file in `src/content/journal/`:

```yaml
title: Article title
description: Search and social description
date: 2026-08-30
category: Travel # Travel, Food, Stay, Fly, Cards, or Notes
cover: /images/optional-cover.jpg
draft: false
```

With no published entries, the Journal displays the intentional “Growing soon” state. Draft entries are excluded from public routes.

## Adding garden entries

Create a Markdown or MDX file in `src/content/garden/`:

```yaml
title: Idea title
description: A short explanation
date: 2026-08-30
status: Seed # Seed, Growing, Bloomed, or Archived
draft: false
```

## Personal links

Update `src/data/site.ts` with Shawn's public LinkedIn URL and preferred public email link. They are deliberately left unset rather than guessed from private local information. Until supplied, their labels remain visible but inactive. The Resume label currently links to the full Work page and can be replaced with a PDF URL later.

## SEO and accessibility

The shared layout provides titles, descriptions, canonical URLs, Open Graph and X metadata, and the generated social card. Astro generates a sitemap; `robots.txt` points to it. Pages use semantic landmarks, visible keyboard focus, meaningful alt text, and reduced-motion behavior.
