# Gifting these profiles to Proto-Pasta — proposal & hosting options

The goal of this project: hand Proto-Pasta (Protoplant) a ready-to-host,
community-built OrcaSlicer profile set covering their whole catalog, at zero
obligation to them (CC0). This note is the outreach pitch and the practical
hosting menu, so whoever has the conversation doesn't have to re-derive it.

## The pitch (short version)

> OrcaSlicer is one of the most popular open-source slicers and ships bundled
> filament profiles for brands like Polymaker, eSUN, Overture and SUNLU — but
> nothing for Proto-Pasta, and Proto-Pasta's excellent published settings
> (Material Data Table, TDS sheets, FAQ pages) aren't in a form a slicer can
> import. We turned every number Proto-Pasta already publishes into 28
> OrcaSlicer filament profiles covering the entire catalog, with per-value
> provenance documented, estimates clearly flagged, and a CC0 license so you
> can host or modify them however you like. Want them? They're yours.

## Hosting options (pick any, they stack)

1. **Downloadable zip on proto-pasta.com** — cheapest to ship. A release zip
   (`Protopasta.zip` containing `Protopasta.json` + `Protopasta/`) that
   customers import via OrcaSlicer's *File → Import → Import Config Bundle*.
   Polymaker does exactly this at presets.polymaker.com; there is no Orca
   equivalent for Proto-Pasta today.

2. **Upstream into OrcaSlicer proper** — the higher-reach option. The same
   files drop into OrcaSlicer's `resources/profiles/` as a new vendor, or the
   profiles can be added to the Orca Filament Library next to Polymaker/
   Overture/SUNLU. PR against https://github.com/OrcaSlicer/OrcaSlicer
   following their wiki's "How to create profiles" guide. Every OrcaSlicer
   user then gets Proto-Pasta profiles in the filament dropdown with zero
   steps. Proto-Pasta endorsement (they check the numbers) makes the PR much
   more likely to merge quickly.

3. **FilamentHub listing** — the profiles can also be uploaded to
   filamenthub.ru (the community preset catalog behind the FilamentHub
   OrcaSlicer plugin), which currently has zero Proto-Pasta content.

## What Proto-Pasta should verify before hosting

- The flagged estimates: densities for High Density Iron/Steel HTPLA and
  Metal Composite PETG (no TDS published — we estimated from their "60% iron,
  ~2× density" language).
- Default nozzle temperature choices for the two-point "Temp @ Max Vol" data
  (we default to the low temp; high-flow guidance lives in profile notes).
- The Carbon Fiber HTPETG defaults (260C nozzle / 100C bed derived from "up
  to 300C" and "100+ C" on the product page).
- Discontinued/renamed lines: Rigid TPU kept for existing stock; the old
  PC-ABS and HTPLA-F lines are not in the current catalog and were not
  profiled.

## Maintenance path

The repo's `scripts/generate_profiles.py` holds the whole catalog as one
data table with per-line notes. New colorway or material launch = add one
`mat(...)` entry, run the generator + validator, re-zip. If Proto-Pasta takes
ownership, the table doubles as an internal checklist for publishing numbers
for lines that currently have none (TPU, PCTG, GF lines).
