# Proto-Pasta TDS Data Summary

Source: https://proto-pasta.com/pages/material-data-table. PDFs hosted on
`cdn.shopify.com/s/files/1/0717/9095/files/`. Downloaded 2026-10-18.

Legend:
- **TDS nozzle/bed** = values printed in the Technical Data Sheet PDF.
- **Table temp** = "Temp @ Max Vol" column of the material-data-table web page
  (nozzle temp @ volumetric flow, bed/plate temp).
- **SDS density** = "Relative density" from Section 9 of the Safety Data Sheet
  (used when the TDS does not state a density).

## PLA family

| Material line | Density (g/cc) | Temps | Source PDFs |
|---|---|---|---|
| Quantum Dot PLA (QPLA) | TDS: ~1.24; SDS: 1.24 | TDS: nozzle 220-240 C, bed 55-65 C. Table: 220 C @ 6 mm3/s, 240 C @ 12 mm3/s, 55 C plate. Tg ~60 C, Tm onset ~155 C | `tds_quantum_dot_pla.pdf` (TDS_QD_HTPLA.pdf), `sds_quantum_dot_pla.pdf` (QD_PLA.pdf) |
| PLA (PLA1) | SDS: 1.2 (SDS trade name: "PLA, Recycled PLA, & HTPLA Colors (w/o fibers)") | Table: 220 C @ 6 mm3/s, 240 C @ 12 mm3/s, 55 C plate. No PLA-specific TDS exists; HTPLA TDS lists nozzle 206 C, bed 60 C | `sds_pla_colors.pdf` (PLA_Colors.pdf), `tds_pla_htpla_colors.pdf` |
| Recycled PLA (RPLA) | SDS: 1.2 (covered by same "PLA, Recycled PLA, & HTPLA Colors" SDS) | Same table row as PLA: 220 C @ 6, 240 C @ 12, 55 C plate | `sds_pla_colors.pdf` |
| High Temp PLA v2/v3 (HTP2, HTP3) | TDS: ~1.24 (Translucent/Sparkly HTPLA TDS); SDS: 1.2 | TDS: nozzle 206 C, bed 60 C. Table: 220 C @ 6, 240 C @ 12, 55 C plate. Heat treat 95-110 C for 10+ min | `tds_pla_htpla_colors.pdf` (TDS__Translucent_Sparkly_HTPLA_1.0.0.pdf), `sds_pla_colors.pdf` |
| High Flow PLA (HFPL) | SDS: 1.2 (product code HFPLxxxx listed in PLA Colors SDS) | Table: 200 C @ 12 mm3/s, 220 C @ 18 mm3/s, 45 C plate; cool below 40 C before removal. No dedicated TDS | `sds_pla_colors.pdf` |
| c-Matte PLA (MPLA) | SDS: 1.3 (trade name "cMatte PLA") | Table: 200 C @ 12 mm3/s, 220 C @ 18 mm3/s, 45 C plate. No dedicated TDS | `sds_c_matte_pla.pdf` (PLA_CaCO3.pdf) |
| Calcium Carbonate PLA (PLAC) | SDS: 1.5 (trade name "PLA w/ Calcium Carbonate", PLACxxxx-C60) | Table lists no temps for this row. No dedicated TDS | `sds_calcium_carbonate_pla.pdf` (PLA_CaCO3_60_SDS.pdf) |
| Matte Fiber HTPLA (HTMF) | TDS: ~1.14; SDS: 1.14 | TDS: nozzle 195 C, bed 60 C, extrusion width 0.45 mm. Table: 200 C @ 12, 220 C @ 18, 55 C plate; avoid below 3 mm3/s. Heat treat 95-110 C | `tds_matte_fiber_htpla.pdf` (TDS__Matte_Fiber_HTPLA_1.0.0.pdf), `sds_matte_fiber_htpla.pdf` (HTPLA_MF.pdf) |
| Carbon Fiber PLA / Carbon Fiber HTPLA (CFP1, HTP2-CF, HTP2-CFX) | TDS: ~1.3 (Carbon Fiber Composite HTPLA TDS); SDS: 1.15 (SDS covers Composite CF PLA, CF HTPLA, Recycled CF PLA) | TDS: nozzle 205 C, bed 60 C, extrusion width 0.65 mm. Table: 220 C @ 6, 240 C @ 12, 55 C plate. Heat treat 95-110 C. Hard steel nozzle + gears recommended | `tds_carbon_fiber_htpla.pdf` (TDS__CarbonFiber_HTPLA_1.0.1.pdf), `sds_carbon_fiber_pla.pdf` (PLA_HTPLA_CF.pdf) |
| Stainless Steel PLA (SSP1) | TDS: ~2.3; SDS: 2.3 | TDS: nozzle 198 C, bed 60 C, extrusion width 0.65 mm. Table: 200 C @ 24 mm3/s, 55 C plate; avoid below 3 mm3/s. Hard steel nozzle recommended | `tds_stainless_steel_pla.pdf` (TDS__Stainless_Steel_PLA_1.0.1.pdf), `sds_stainless_steel_pla.pdf` (PLA_Steel.pdf) |
| Magnetic Iron PLA (FEP1) | TDS: ~1.85; SDS: 1.85 | TDS: nozzle 192 C, bed 60 C, extrusion width 0.65 mm. Table: 200 C @ 24 mm3/s, 55 C plate. Tm onset ~155 C | `tds_magnetic_iron_pla.pdf` (TDS__Iron_PLA_1.0.1.pdf), `sds_magnetic_iron_pla.pdf` (FEP1xxxx_SDS.pdf) |
| Brass / Bronze / Copper HTPLA (HTPC-BRA, BRO, CU) | TDS: ~2.3; SDS: 2.5 (HTPLA Copper Alloy SDS) | TDS: nozzle 195 C, bed 60 C, extrusion width 0.65 mm. Table: 200 C @ 24 mm3/s, 55 C plate. Heat treat 95-110 C. Hard steel nozzle recommended | `tds_brass_bronze_copper_htpla.pdf` (TDS__BrassBronzeCopper_HTPLA_1.0.0.pdf), `sds_brass_bronze_copper_htpla.pdf` (HTPLA_Copper_Alloy.pdf) |
| Conductive PLA (CDP1) | SDS: 1.24 (TDS does not state density) | TDS: print 210-230 C, build plate 60 C, up to 8 mm3/s, 0.4 mm+ nozzle. Table: 220 C @ 6, 240 C @ 12, 55 C plate. Magigoo/glue; extra purge | `tds_conductive_pla.pdf` (CDP1xxxx_TDS.pdf), `sds_conductive_pla.pdf` (CDP1xxxx_SDS.pdf) |
| Static Dissipative PLA (PLA1-ESD) | SDS: 1.24 (TDS does not state density) | TDS: print 210-230 C, build plate 60 C. Table: 220 C @ 6, 240 C @ 12, 55 C plate. Magigoo/glue; extra purge | `tds_static_dissipative_pla.pdf` (PLA1xxxx-ESD_TDS.pdf), `sds_static_dissipative_pla.pdf` (PLA_ESD.pdf) |
| Static Dissipative CF PLA (CFP1-ESD) | SDS: 1.14 (TDS does not state density) | TDS: print 210-230 C, build plate 60 C. Table: 220 C @ 6, 240 C @ 12, 55 C plate. Abrasive: hard nozzle recommended | `tds_static_dissipative_cf_pla.pdf` (CFP1xxxx-ESD_TDS.pdf), `sds_static_dissipative_cf_pla.pdf` (CF_ESD.pdf) |

## PETG family

| Material line | Density (g/cc) | Temps | Source PDFs |
|---|---|---|---|
| PETG (PETGxxxx) | SDS: 1.2 (trade name "Protopasta PETG") | Table: 250 C @ 12 mm3/s, 80 C plate. No dedicated TDS published. Magigoo/glue recommended | `sds_petg_colors.pdf` (PETG_Colors.pdf) |
| Carbon Fiber PETG (PETG-CF7) | SDS: 1.2 | Table: 250 C @ 12 mm3/s, 80 C plate. No dedicated TDS published. Hard steel nozzle + gears recommended | `sds_carbon_fiber_petg.pdf` (PETG_CF7.pdf) |
| Static Dissipative PETG (PETG-ESD) | SDS: 1.2 (TDS does not state density) | TDS: print 250-290 C, build plate 70-80 C, drying 65 C for 6 h. Table: 250 C @ 12 mm3/s, 80 C plate | `tds_static_dissipative_petg.pdf` (PETGxxxx-ESD_TDS.pdf), `sds_static_dissipative_petg.pdf` (PETG_ESD.pdf) |

## Lines with NO TDS/SDS found (not on the material-data-table page)

Checked the material-data-table, the relevant product pages (which contain no PDF
links at all), and probed plausible Shopify CDN filenames (all 404). No published
documents found for:

- PCTG (Clear PCTG, CF PCTG, GF PCTG products)
- Rigid TPU
- Flexible TPU
- Glass Fiber PETG (sold as "Glass Fiber HTPETG")
- Recycled PETG (Black Recycled PETG; note the PETG Colors SDS product code is
  PETGxxxx only and does not list recycled PETG)
- High Density Steel HTPLA
- High Density Iron HTPLA

Carbon Fiber HTPETG and Glass Fiber HTPLA have no Material Data Table row either and
were not probed.

Product pages and launch articles for these lines do give print temperatures (see
`docs/SOURCES.md`). No densities are published for them, except "about 2x PETG" for
the metal-composite PETGs.

## Notes

- The newer 2-page TDS format (Conductive PLA, all Static Dissipative lines) omits
  density; densities for those lines come from the paired SDS Section 9.
- PLA family TDS/SDS cover multiple SKUs in one document: the "Translucent/Sparkly
  HTPLA" TDS and the "PLA, Recycled PLA, & HTPLA Colors (w/o fibers)" SDS are the
  documents the table links for the whole unfilled PLA family (PLA1, HTGL, HTPM,
  HTP2, HTP3, RPLA, SUBX, WSXX).
- Brass/Bronze/Copper: TDS says ~2.3 g/cc while its SDS says 2.5 g/cc; both reported.
- Heat treat guidance (HTPLA lines): typical 95-110 C for 10+ minutes.
