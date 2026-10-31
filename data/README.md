# Gathered source data

Everything here was gathered from proto-pasta.com on 2026-10-18 while
building the profiles. The TDS/SDS PDFs and page snapshots are Proto-Pasta's
documents — kept locally for provenance but excluded from git (see
.gitignore); only the URL lists and extracted facts are committed.

- `product_urls.txt` — all 183 product URLs from the Shopify product sitemap
  (`sitemap_products_1.xml`, also saved). The material-line grouping derived
  from these handles is in the README coverage table.
- `page_urls.txt` — the 41 non-product pages (FAQs, compatibility pages,
  material data table) from the pages sitemap.
- `tds/tds_summary.md` — density + temperature facts extracted from the 10
  TDS and 15 SDS PDFs listed on the Material Data Table page, with the
  source filename for each value.
- `tds/*.pdf`, `sitemap*.xml` — local-only copies (gitignored).

Gathering method: sitemaps via curl with a browser user-agent; rendered page
content via a web-reader service; PDF text via `pdftotext -layout`.
