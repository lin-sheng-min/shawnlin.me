import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const work = defineCollection({
  loader: glob({ base: './src/content/work', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    company: z.string(),
    role: z.string(),
    period: z.string(),
    order: z.number(),
    summary: z.string(),
    location: z.string().optional(),
    highlights: z.array(z.string()).default([]),
    featured: z.boolean().default(true),
  }),
});

const photography = defineCollection({
  loader: glob({ base: './src/content/photography', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    cover: z.string(),
    coverAlt: z.string(),
    orientation: z.enum(['landscape', 'portrait']).default('landscape'),
    layout: z.enum(['editorial', 'compact']).default('editorial'),
    featured: z.boolean().default(false),
    placeholder: z.boolean().default(false),
    location: z.string().optional(),
    images: z.array(z.object({
      src: z.string(),
      alt: z.string(),
      caption: z.string().optional(),
      width: z.number(),
      height: z.number(),
    })).default([]),
  }),
});

const journal = defineCollection({
  loader: glob({ base: './src/content/journal', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    category: z.enum(['Travel', 'Food', 'Stay', 'Fly', 'Cards', 'Notes']),
    cover: z.string().optional(),
    coverAlt: z.string().optional(),
    coverWidth: z.number().optional(),
    coverHeight: z.number().optional(),
    draft: z.boolean().default(false),
  }),
});

const garden = defineCollection({
  loader: glob({ base: './src/content/garden', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    status: z.enum(['Seed', 'Growing', 'Bloomed', 'Archived']),
    draft: z.boolean().default(false),
  }),
});

export const collections = { work, photography, journal, garden };
