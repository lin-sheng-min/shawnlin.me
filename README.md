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

1. Keep the full-resolution original outside the public repository. Shawn's originals live in a separate local Pictures folder and are never modified by the site build.
2. Export a metadata-free WebP copy into the relevant folder under `public/images/` using a descriptive filename. Current gallery copies use a maximum long edge of 2400px; hero and About images use up to 2800px.
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
location: Optional location label
images:
  - src: /images/photography/example/second-frame.webp
    alt: Meaningful description of the photograph
    caption: Optional short caption
    width: 2400
    height: 1600
```

The photography section contains Shawn's own photographs, organized into content-driven editorial collections. The original files must remain outside the repository; only optimized copies belong in `public/images/`.

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
