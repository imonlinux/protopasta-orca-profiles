# Where each value comes from

Source material was gathered from proto-pasta.com on 2026-10-18; the product
pages, FAQ pages and launch articles cited below were re-checked on
2026-10-31.

## Sources

- **MDT** – the Material Data Table,
  https://proto-pasta.com/pages/material-data-table. Each row gives a
  suggested starting profile (Generic PLA or Generic PETG), "Temp @ Max Vol"
  pairs (nozzle temperature up to a volumetric flow), a plate temperature and
  printing notes. It has rows for the PLA, HTPLA, Matte Fiber, carbon fiber,
  metal composite, conductive, ESD and PETG lines. It has no rows for PCTG,
  TPU, HTPETG, Glass Fiber, High Density or metal-composite PETG lines, and
  the Calcium Carbonate PLA row has no numbers.
- **TDS/SDS** – the technical and safety data sheets linked from the MDT.
  The 11 TDS and 15 SDS PDFs are kept locally in `data/tds/` (not in git);
  the values used are summarized in `data/tds/tds_summary.md`.
- **FAQ pages** – getting-started, high-temp-pla (HTPLA), carbon-fiber-pla,
  stainless-steel-pla, magnetic-iron-pla, conductive-pla, general-faq,
  prusa-compatibility and creality-compatibility (all under
  proto-pasta.com/pages/).
- **Product pages** – for lines without an MDT row: CF and GF HTPETG, PCTG
  (clear, CF, GF), metal-composite PETG, High Density HTPLA, TPU.
- **Launch articles** (Proto-Pasta's "Endless Exploration" blog posts) –
  EX10 (High Density Metal HTPLA), EX14 (High Temp PETG) and EX16 (Metal PETG
  Composites).

## Per-profile values

"Inherit" means the profile sets nothing and Orca's base value applies
(values shown are from OrcaSlicer 2.4.2's `fdm_filament_*` bases).

| Profile | Nozzle (°C) | Range (°C) | Max flow (mm³/s) | Plate (°C) | Density (g/cm³) | Sources and reasoning |
|---|---|---|---|---|---|---|
| PLA | 220 | 195–240 | 12 | 55 | 1.24 | MDT 220 @ 6 / 240 @ 12, 55 plate. Getting-started 195–225 / 50–60. Density from the HTPLA TDS (1.24); the PLA SDS says 1.2 |
| HTPLA | 220 | 195–240 | 12 | 55 | 1.24 | MDT as PLA. TDS 206 / 60, density 1.24. Quantum Dot TDS 220–240 / 55–65. Heat treating: TDS 95–110 °C, 10+ min; HTPLA FAQ 95–120 °C, about 10 min. Prusa page: 235–240 °C helps avoid heatbreak-ledge jams |
| High Flow PLA | 200 | 190–220 | 18 | 45 | 1.24 | MDT 200 @ 12 / 220 @ 18, 45 plate. No TDS; 1.24 is the HTPLA TDS figure (the PLA-family SDS that lists HFPLA says 1.2) |
| c-Matte PLA | 200 | 190–220 | 18 | 45 | 1.30 | MDT 200 @ 12 / 220 @ 18, 45 plate. SDS 1.3 |
| Matte Fiber HTPLA | 200 | 190–220 | 18 | 55 | 1.14 | MDT 200 @ 12 / 220 @ 18, 55 plate, avoid below 3 mm³/s. TDS 195 / 60, density 1.14 |
| Calcium Carbonate PLA | 220 | 195–240 | 12 | 55 | 1.50 | MDT row has no numbers, so Proto-Pasta's PLA row is borrowed. SDS 1.5 |
| Carbon Fiber PLA | 210 | 195–240 | 12 | 55 | 1.30 | FAQ 195–220. TDS 205 / 60. MDT 220 @ 6 / 240 @ 12, 55 plate. Density: TDS and FAQ 1.3 (used); SDS 1.15. Flow ratio 0.95, as Orca's Generic PLA-CF uses |
| Stainless Steel PLA | 200 | 190–220 | 24 | 55 | 2.30 | MDT 200 @ 24, 55 plate. FAQ 195–220 (215 with a 0.5 mm nozzle). TDS 198 / 60, density 2.3 (the FAQ says 2.4) |
| Magnetic Iron PLA | 190 | 185–220 | 24 | 55 | 1.85 | FAQ 185–195, "about 10 degrees cooler" than PLA; fan off and slower printing if it warps. MDT 200 @ 24, 55 plate. TDS 192 / 60, density 1.85 (the FAQ says 1.8) |
| High Density Iron HTPLA | 200 | 190–220 | 24 | 55 | 2.40 **est.** | No TDS or MDT row. EX10: printed at 200 °C up to 24 mm³/s; 60 wt% iron. 55 °C plate borrowed from the metal-composite MDT rows. Density is an estimate; none is published |
| High Density Steel HTPLA | 200 | 190–220 | 24 | 55 | 2.40 **est.** | As HD Iron; 70 wt% 400-series stainless steel. A simple mixing calculation (solid steel in PLA, no voids) suggests about 3.0, so 2.4 is probably low |
| Brass / Bronze / Copper HTPLA | 200 | 190–220 | 24 | 55 | 2.30 | MDT 200 @ 24, 55 plate. TDS 195 / 60, density 2.3 (SDS says 2.5) |
| Conductive PLA | 220 | 210–240 | 12 | 55 | 1.24 | FAQ 215–230, "on the hotter side". TDS 210–230 / 60, up to 8 mm³/s. MDT 220 @ 6 / 240 @ 12, 55 plate (its 12 mm³/s cap is used). SDS 1.24 (the FAQ's "1.15 g/cm³ (1500 kg/m³)" contradicts itself, so it isn't used) |
| Static Dissipative PLA | 220 | 210–240 | 12 | 55 | 1.24 | TDS 210–230 / 60, up to 12 mm³/s. MDT 220 @ 6 / 240 @ 12, 55 plate. SDS 1.24 |
| Static Dissipative CF PLA | 220 | 210–240 | 12 | 55 | 1.14 | TDS 210–230 / 60, up to 12 mm³/s. MDT as SD PLA. SDS 1.14. Flow ratio 0.95 |
| PETG | 250 | 230–270 | 12 | 80 | 1.20 | MDT 250 @ 12, 80 plate. SDS 1.2. The getting-started page's older 210–230 °C / 70–80 °C PETG range is not used |
| Carbon Fiber PETG | 250 | 230–270 | 12 | 80 | 1.20 | MDT 250 @ 12, 80 plate. SDS 1.2. Product page: 235 °C and up, up to 275 °C, 255 °C "a good compromise", 70 °C+ bed. Flow ratio 0.95 is our choice |
| Carbon Fiber HTPETG | 260 | 240–300 | 12 | 100 | inherit (1.27) | Product pages: "up to 300 C", bed "100+ C", flow below 100 %, nozzle wipe. EX14: 300 °C, 6 mm³/s chosen for full melt; dry first; fans off. **260 °C and the 12 mm³/s cap are our own middle-ground choices**, not Proto-Pasta numbers |
| Glass Fiber HTPETG | 250 | 230–270 | 12 | 80 | inherit (1.27) | Uses Proto-Pasta's PETG row. **The product page instead says up to 300 °C with a 100 °C+ bed**, the same as CF HTPETG |
| PCTG | 250 | 230–270 | 12 | 80 | inherit (1.27) | Uses Proto-Pasta's PETG row. **The product page instead says 255 °C and up (255 °C "a good compromise", up to 275 °C), 80 °C+ bed, about 2 mm³/s** |
| Carbon Fiber PCTG | 250 | 230–270 | 12 | 80 | inherit (1.27) | As PCTG (product pages give 70+ and 80+ °C for the bed). Strength/stiffness figures from the product pages |
| Glass Fiber PCTG | 250 | 230–270 | 12 | 80 | inherit (1.27) | As PCTG. "~75% stiffer" from the product page |
| Metal Composite PETG | 245 | 230–270 | 12 | 80 | 2.40 **est.** | Product pages: 60 wt% metal for all three, "density ~2x PETG", "a lower nozzle temp can reduce stringing", hence 245. EX16: Generic PETG temperatures, glue stick, avoid below 2 mm³/s |
| Static Dissipative PETG | 250 | 250–290 | 12 | 80 | 1.20 | TDS 250–290 / 70–80, up to 8 mm³/s, drying highly recommended (65 °C, 6 h). MDT 250 @ 12, 80 plate (its 12 mm³/s cap is used). SDS 1.2 |
| Rigid TPU / Flexible TPU | inherit (240) | inherit (200–250) | inherit (3.2) | inherit (35) | inherit (1.24) | Product pages: start at 240 °C, no bed heat needed, Magigoo, dry overnight. Nothing is set, so Orca's Generic TPU values apply |

## Where Proto-Pasta's sources disagree

The profiles follow the MDT where it has a row. Notable differences:

- **Volumetric flow.** The older TDS sheets list 2–3 mm³/s (2–4 for Carbon
  Fiber HTPLA), with print settings based on an Ultimaker S5 profile; the MDT
  allows 12–24. (The Quantum Dot TDS lists 10–12.)
  The newer TDS sheets for Conductive PLA and Static Dissipative PETG stop at
  8 mm³/s, while the MDT allows 12.
- **Nozzle temperature.** The older TDS sheets list single values (192–206 °C)
  that are lower than the MDT pairs.
- **Density.** Carbon Fiber PLA: TDS 1.3, SDS 1.15 (the TDS length of
  360 m/kg also works out to about 1.15). Brass/Bronze/Copper HTPLA: TDS 2.3,
  SDS 2.5. Stainless Steel PLA: TDS/SDS 2.3, FAQ 2.4.
- **Heat treating.** TDS 95–110 °C for 10+ minutes; HTPLA FAQ 95–120 °C for
  about 10 minutes; EX10 100 °C for 10+ minutes.

## Other facts used in profile notes

- Heat resistance after heat treating: TDS "more than 140C" (HDT); general
  FAQ "up to 155C"; EX10 "up to 150 C" for High Density HTPLA.
- Drying (getting-started page): PLA usually prints fine without drying;
  if you dry it, stay below 50 °C for PLA and below 65 °C for PETG.
- Bed adhesion: the MDT recommends Magigoo or glue for the Conductive, ESD
  and PETG lines (prints can fuse to the plate).
- Abrasion: the MDT recommends a hard steel nozzle and gears for the carbon
  fiber PLA and PETG lines and the metal-composite PLA lines, and more frequent PTFE tubing changes
  for rough filaments. EX14 says a hard steel nozzle is required for HTPETG.
  The general FAQ recommends a hardened brass nozzle for the metal PLAs.
  The Matte Fiber TDS says that fiber does not need a wear-resistant nozzle.
- Reference setup: the carbon-fiber and stainless-steel FAQ pages report good
  results with a 0.5 mm nozzle and a spring-loaded direct-drive extruder.
- Prusa MK2/MK3 (prusa-compatibility page): a small ledge in the stock
  heatbreak can snag filament; 235–240 °C helps but can cause other issues,
  so a different hotend is the recommended fix. Out of Darts runs tens of
  stock MK printers reliably.
- Ender 3 (creality-compatibility page): the stock printer prints well up to
  4 mm³/s when set up properly.
- Spool length: the FAQ pages give about 90 m (stainless steel) and about
  100 m (magnetic iron) per 500 g, against "nearly 200" for standard PLA. The
  TDS figure for standard HTPLA is 346 m/kg, about 173 m per 500 g.
