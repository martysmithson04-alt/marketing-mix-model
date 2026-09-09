import { defineConfig } from "astro/config";

/**
 * Fully static output for Cloudflare Pages.
 * Set `site` to the production origin when the Pages hostname is known
 * so canonical + Open Graph URLs resolve absolutely.
 */
export default defineConfig({
  output: "static",
  compressHTML: true,
});
