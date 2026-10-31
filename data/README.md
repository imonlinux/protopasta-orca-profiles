# Gathered source data

Everything here was gathered from proto-pasta.com on 2026-10-18 while
building the profiles.

**In git:**

- `product_urls.txt` – the 183 product URLs from the Shopify product sitemap.
- `product_handles.txt` – the same 183 products as bare handles (the last
  part of each URL). The README's coverage table groups these into material
  lines.
- `page_urls.txt` – the 41 non-product pages (FAQs, compatibility pages,
  Material Data Table and so on) from the pages sitemap.
- `tds/tds_summary.md` – density and temperature values taken from the 11 TDS
  and 15 SDS PDFs linked from the Material Data Table, with the source file
  for each value.

**Local only (excluded by `.gitignore`, because they are Proto-Pasta's
documents):**

- `tds/*.pdf` – the TDS and SDS sheets themselves.
- `sitemap.xml`, `sitemap_pages_1.xml`, `sitemap_products_1.xml` – the
  sitemaps the URL lists came from.

How it was gathered: sitemaps with curl (browser user-agent), page text with
a web-reader service, PDF text with `pdftotext -layout`.

Values taken from product pages, FAQ pages and launch articles are cited in
`docs/SOURCES.md`; those pages were not saved here.
