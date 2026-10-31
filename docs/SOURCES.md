# Value-level provenance

All data gathered 2026-10-18 from proto-pasta.com. Primary sources:

- **MDT** — Material Data Table, https://proto-pasta.com/pages/material-data-table
  (also served at /pages/documentation). Rows give "Suggested profile",
  "Temp @ Max Vol" pairs and plate temperature. Raw HTML snapshot and the
  parsed table live in `data/` (see data/README.md).
- **TDS/SDS** — technical/safety data sheets linked from the same page.
  Downloaded PDFs are in `data/tds/` (not redistributed in git); extracted
  values are summarized in `data/tds/tds_summary.md`.
- **FAQ pages** — per-material pages: getting-started, high-temp-pla,
  conductive-pla, carbon-fiber-pla, magnetic-iron-pla, stainless-steel-pla,
  prusa-compatibility, creality-compatibility.
- **Product pages** — for the HTPETG carbon-fiber lines and metal-composite
  PETG (settings appear in marketing copy there rather than the table).

## Per-profile decisions

| Profile | Nozzle | Range | MVS | Bed | Density | Reasoning |
|---|---|---|---|---|---|---|
| PLA | 220 | 195–240 | 12 | 55 | 1.24 | MDT 220@6/240@12, 55C plate; getting-started 195–225/50–60; TDS 206/60; TDS density ~1.24 |
| HTPLA | 220 | 195–240 | 12 | 55 | 1.24 | Same sources as PLA; QPLA TDS 220–240/55–65; Prusa MK FAQ 235–240 anti-jam; annealing 85–115C, 5–60 min from HTPLA FAQ |
| High Flow PLA | 200 | 190–220 | 18 | 45 | 1.24 | MDT 200@12/220@18, 45C plate; density from PLA-family SDS |
| c-Matte PLA | 200 | 190–220 | 18 | 45 | 1.30 | MDT 200@12/220@18, 45C plate; SDS density 1.3 |
| Matte Fiber HTPLA | 200 | 190–220 | 18 | 55 | 1.14 | MDT 200@12/220@18, 55C; TDS 195/60, density ~1.14; "avoid below 3 mm³/s" from MDT |
| Calcium Carbonate PLA | 220 | 195–240 | 12 | 55 | 1.50 | MDT row blank → PLA-family defaults; SDS density 1.5 |
| Carbon Fiber PLA | 210 | 195–240 | 12 | 55 | 1.30 | FAQ 195–220 (success 195–210, some at 220); TDS 205/60; MDT 220@6/240@12; TDS density ~1.3; flow ratio 0.95 per Orca PLA-CF convention |
| Stainless Steel PLA | 200 | 190–220 | 24 | 55 | 2.30 | MDT 200@24, 55C; FAQ 195–220 (215 with 0.5 mm nozzle); TDS density ~2.3 (FAQ page prints 2400 kg/m³) |
| Magnetic Iron PLA | 190 | 185–220 | 24 | 55 | 1.85 | FAQ 185–195 ("~10C cooler than PLA"); MDT 200@24, 55C; TDS density ~1.85; fan-off/slow-down anti-warp advice from FAQ |
| HD Iron / HD Steel HTPLA | 200 | 190–220 | 24 | 55 | 2.40 **est.** | No TDS published; metal-composite row values; density estimated from Proto-Pasta's "60% iron by weight / ~2× base polymer" description of the HD iron line |
| Brass / Bronze / Copper HTPLA | 200 | 190–220 | 24 | 55 | 2.30 | MDT 200@24, 55C; TDS 195/60, density ~2.3 (SDS 2.5) |
| Conductive PLA | 220 | 210–240 | 12 | 55 | 1.24 | FAQ 215–230 "hotter side"; TDS 210–230/60; MDT 220@6/240@12; SDS density 1.24 (FAQ's "1500 kg/m³" is internally inconsistent, not used) |
| Static Dissipative PLA | 220 | 210–240 | 12 | 55 | 1.24 | TDS 210–230/60; MDT 220@6/240@12 |
| Static Dissipative CF PLA | 220 | 210–240 | 12 | 55 | 1.14 | TDS 210–230/60; SDS density 1.14; + CF handling |
| PETG | 250 | 230–270 | 12 | 80 | 1.20 | MDT 250@12, 80C plate; SDS density 1.2. Getting-started's "210–230C" PETG range appears legacy; MDT (newer, flow-based) preferred |
| Carbon Fiber PETG | 250 | 230–270 | 12 | 80 | 1.20 | MDT 250@12, 80C |
| Carbon Fiber HTPETG | 260 | 240–300 | 12 | 100 | (inherit 1.27) | Product page: "up to 300C", bed "100+ C", flow <100% + nozzle-wipe advice; 260 default is mid-range since overheating risk when slow; no TDS density published |
| Glass Fiber HTPETG | 250 | 230–270 | 12 | 80 | (inherit) | No published numbers → PETG-family defaults, flagged in notes |
| PCTG | 250 | 230–270 | 12 | 80 | (inherit 1.27) | No published numbers → Orca fdm_filament_pctg defaults |
| Carbon Fiber PCTG | 250 | 230–270 | 12 | 80 | (inherit) | No published numbers → PCTG-family defaults + CF handling |
| Glass Fiber PCTG | 250 | 230–270 | 12 | 80 | (inherit) | No published numbers → PCTG-family defaults |
| Metal Composite PETG | 245 | 230–270 | 12 | 80 | 2.40 (iron) | Product page: "prints like PETG, lower nozzle temp reduces stringing" → 245; iron 60% by weight, density ~2× PETG; Cu/Steel densities unpublished (2.4 default reflects iron) |
| Static Dissipative PETG | 250 | 250–290 | 12 | 80 | 1.20 | TDS 250–290/70–80; MDT 250@12, 80C |
| Rigid / Flexible TPU | (inherit 240) | (inherit 200–250) | (inherit 3.2) | (inherit 35) | (inherit 1.24) | Proto-Pasta publishes no TPU settings (MDT lists none; product pages defer); Orca Generic TPU defaults, flagged in notes |

## Cross-cutting source facts folded into notes

- Annealing (HTPLA family): 85–115C, 5–60 min, sand or gel method, treat with
  supports on; heat resistance ~140–155C after vs ~55–60C as printed.
- Drying: PLA family below 50C, PETG below 65C; particle-filled filaments
  become more brittle when dried hot.
- Adhesion: Magigoo/glue recommended for Conductive, ESD and PETG families
  (prints can fuse to smooth plates when hot).
- Hardware: hardened nozzle + gears for all CF/GF lines; metal composites
  wear nozzles too ("hardened brass nozzle" per general FAQ); 0.5 mm nozzle +
  spring-loaded direct drive is Proto-Pasta's reference setup for composites;
  rough fiber lines warrant more frequent PTFE tubing replacement.
- Prusa MK2/MK3: stock heatbreak ledge snags filament; 235–240C keeps it hot
  enough to avoid jams (Out of Darts runs stock fleets fine).
- Ender 3: good to ~4 mm³/s on a stock hotend.
- Spool lengths (weight→length intuition): SS ~90 m/500 g, iron ~100 m/500 g
  vs ~200 m for standard PLA.
