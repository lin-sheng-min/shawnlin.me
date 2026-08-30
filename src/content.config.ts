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
    featured: z.boolean().default(false),
    placeholder: z.boolean().default(false),
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
