# Vanishka Enterprises Redesign — Homepage

## What's inside
- `index.html` — standalone homepage (Navbar, Hero, Category Strip, Featured Tutorials Grid,
  Newsletter CTA, Footer). Built with Tailwind CSS (via CDN) + Google Fonts, so it works by
  just opening the file in a browser — no build step needed.

## How to use it
1. **Preview instantly:** double-click `index.html`, or drag it into any browser.
2. **Edit content:** open in any code editor and change the text directly inside the HTML —
   card titles, subject codes, links, etc.
3. **Toggle dark mode / mobile menu:** already wired up with the small `<script>` block at the
   bottom of the file.

## Moving this into a real Next.js project
This file is a design reference, not the final app. To turn it into the Next.js + Tailwind
build recommended earlier:

1. `npx create-next-app@latest computerbaba --typescript --tailwind --app`
2. Copy the `tailwind.config` color/font tokens from the `<script>` block in `index.html`
   into `tailwind.config.ts`.
3. Split the HTML into components as per the hierarchy already shared:
   `components/Navbar.tsx`, `components/Hero.tsx`, `components/TutorialCard.tsx`,
   `components/Footer.tsx`, etc.
4. Replace the vanilla dark-mode script with `next-themes`.
5. Wire up real content from your CMS (Sanity/Payload) or MDX files instead of the
   hardcoded card data.

## Notes
- No real images are used — the design leans on typography, color, and the "stamp" /
  "stitched notebook" motifs instead, so there's nothing to swap out before shipping.
- Ask me any time for the article/tutorial page template, or for the components split out
  into individual React files ready to drop into a Next.js app.
