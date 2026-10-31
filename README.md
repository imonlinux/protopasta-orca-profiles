# Protopasta OrcaSlicer Filament Profiles

Community-built [OrcaSlicer](https://orcaslicer.com) filament profiles for the
entire [Proto-Pasta](https://proto-pasta.com) (Protoplant) filament catalog —
28 material lines covering every current product family, built exclusively
from Proto-Pasta's own published data (Material Data Table, TDS/SDS sheets,
per-material FAQ pages, and product pages).

OrcaSlicer ships no Proto-Pasta profiles and Proto-Pasta publishes no
downloadable slicer profiles; this bundle fills that gap so it can be hosted
by Proto-Pasta and/or upstreamed into OrcaSlicer's Orca Filament Library
(alongside Polymaker, eSUN, Overture, SUNLU, and friends).

## Coverage

| Profile | Products covered | Data basis |
|---|---|---|
| Protopasta PLA | Back to Basics PLA, Recycled PLA | Material Data Table + TDS/SDS |
| Protopasta HTPLA | Premium HTPLA v3, HTPLA v2, all color/glitter/fluorescent/Quantum Dot/glow lines | Data Table + TDS + FAQ |
| Protopasta High Flow PLA | HFPLA | Data Table |
| Protopasta c-Matte PLA | c-Matte colors | Data Table + SDS |
| Protopasta Matte Fiber HTPLA | Matte Fiber incl. wood tones | Data Table + TDS |
| Protopasta Calcium Carbonate PLA | CaCO3 composite | SDS (PLA-family defaults) |
| Protopasta Carbon Fiber PLA | CF PLA, High Temp CF PLA, Recycled CF PLA | Data Table + TDS + FAQ |
| Protopasta Stainless Steel PLA | Stainless Steel (all colors) | Data Table + TDS + FAQ |
| Protopasta Magnetic Iron PLA | Magnetic Iron | Data Table + TDS + FAQ |
| Protopasta High Density Iron/Steel HTPLA | HD Iron, HD Steel | Metal-composite row (no TDS published) |
| Protopasta Brass/Bronze/Copper HTPLA | Metal composites | Data Table + TDS |
| Protopasta Conductive PLA | Conductive PLA | Data Table + TDS + FAQ |
| Protopasta Static Dissipative PLA / CF PLA / PETG | ESD lines | Data Table + TDS |
| Protopasta PETG | Simply PETG, Translucent, Recycled | Data Table + SDS |
| Protopasta Carbon Fiber PETG | CF PETG, Recycled CF PETG | Data Table |
| Protopasta Carbon Fiber HTPETG | High Strength + High Impact CF HTPETG | Product page (up to 300C) |
| Protopasta Glass Fiber HTPETG / PCTG | GF lines | PETG/PCTG-family defaults* |
| Protopasta PCTG / CF PCTG | Clear PCTG, High Impact/High Strength CF PCTG | PCTG-family defaults* |
| Protopasta Metal Composite PETG | Copper/Steel/Iron PETG | Product page + PETG row |
| Protopasta Rigid / Flexible TPU | TPU lines (Rigid discontinued) | Orca Generic TPU defaults* |

\* Proto-Pasta publishes no numbers for these lines; the profile says so in
its notes and inherits Orca's Generic family defaults rather than inventing
values. See [docs/SOURCES.md](docs/SOURCES.md) for value-level provenance.

## How the "Temp @ Max Vol" data was encoded

Proto-Pasta's Material Data Table publishes temperature-at-flow pairs (e.g.
*220C@6, 240C@12 mm³/s*). A static profile can't vary temperature with flow,
so profiles default to the **low** temperature (Proto-Pasta's stated
preference: lowest temperature that works), keep the **high** flow as
`filament_max_volumetric_speed`, widen `nozzle_temperature_range_low/high` to
bracket everything published, and spell out the pairing in `filament_notes`
("raise toward 240C at 12 mm³/s").

## Profile granularity rule

One profile per **filament type** (PLA, HTPLA, PETG, PCTG, TPU …), plus one
extra profile for any **notable variation** within that type — meaning
Proto-Pasta's published settings differ materially: a different
temperature-at-flow pair, bed temperature, density, filament type tag
(e.g. PLA-CF), a hardware requirement (hardened nozzle), or distinct
post-processing. Examples: Matte Fiber and c-Matte split from HTPLA/PLA
(different temps, beds, densities); Carbon Fiber HTPETG split from CF PETG
(300C/100C guidance); each metal composite keeps its own profile.

Colorways, glitter/fluorescent/Quantum Dot/glow variants, and recycled
versions of the same formula **never** get separate profiles — they are
listed in the parent profile's `filament_notes`. If only the color differs,
it's notes; if the settings differ, it's a new profile. (Per-color profiles
with preset spool colors could be generated later if ever wanted — the
sitemap in `data/` carries the full product list.)

## Install

The profiles are printer-agnostic (no `compatible_printers` scoping — every
instantiated profile carries `"compatible_printers": []` +
`"compatible_printers_condition": ""`, the explicit universal-compatibility
form Orca's own bundled profiles use). Two delivery formats:

**Option A — flat user presets (most reliable, OrcaSlicer 2.4+):**

Import the JSONs from `user_presets/` (or `dist/Protopasta_user_presets.zip`)
via `File → Import → Import configs`, or copy them directly into Orca's user
preset folder (`<config>/OrcaSlicer/user/<your-id>/filament/`) and restart
OrcaSlicer. They then appear in the filament dropdown under your user
presets, usable with any printer. Each file inherits the matching
instantiated Orca system profile (`Generic PLA @System`, `Generic PETG
@System`, `Generic PLA-CF @System`, `Generic PCTG @System`, `Generic TPU
@System`) for family defaults — note that user presets **cannot** inherit
the library's internal base names (`fdm_filament_pla` etc.): Orca logs
"can not find parent" and silently skips such files. The `@System` naming
requires Orca 2.4+; on older versions use Option B or C.

**Option B — vendor bundle:**

Import `dist/Protopasta.zip` via `File → Import → Import Config Bundle`.
Profiles appear under vendor **Protopasta**.

**If Orca refuses the bundle with "printer is not installed":** that error
comes from Orca's bundle importer evaluating printer compatibility — earlier
revisions of this bundle without the explicit empty `compatible_printers`
markers could trip it. The current files carry the markers. If imported
profiles still don't show in the dropdown, check Orca's
`show_unsupported_presets` setting (`false` hides presets Orca considers
incompatible with the selected printer) — the markers above mark these
profiles as compatible with everything.

**Option C — for OrcaSlicer distributors / custom builds:**

Copy `Protopasta.json` + the `Protopasta/` folder into OrcaSlicer's
`resources/profiles/` directory (that is exactly how the Elegoo/Polymaker
vendor folders ship), or vendor it into the Orca Filament Library — see
[docs/GIFT_NOTE.md](docs/GIFT_NOTE.md).

## Repo layout

```
profiles/                 the OrcaSlicer vendor bundle (Option B)
  Protopasta.json         vendor index (filament_list)
  Protopasta/filament/    28 × (@base + instantiated) profile pairs
user_presets/             flat user-preset JSONs (Option A - most reliable)
dist/                     importable zips of both formats
scripts/generate_profiles.py   single source of truth - edit + rerun
scripts/validate_profiles.py   bundle consistency checks
data/                     gathered source material (see data/README.md)
docs/SOURCES.md           value-level provenance per material line
docs/GIFT_NOTE.md         hosting proposal for Proto-Pasta
```

To change a value: edit the material table in
`scripts/generate_profiles.py`, run it, then run the validator:

```bash
python3 scripts/generate_profiles.py
python3 scripts/validate_profiles.py
```

## Status / caveats

- Format modeled on OrcaSlicer 2.4.2's shipped vendor bundles (Elegoo,
  OrcaFilamentLibrary/Polymaker structure: `@base` inherits Orca's
  `fdm_filament_*` bases, instantiated profiles are thin wrappers).
  Not yet import-tested inside the OrcaSlicer GUI — do a test import before
  publishing.
- Volumetric-speed caps follow Proto-Pasta's table (12 standard, 18 high-flow
  lines, 24 metal composites). These are caps, not targets; their FAQ notes
  most hardware performs best around 3–4 mm³/s.
- Estimated values (clearly flagged in profile notes and SOURCES.md):
  densities for the High Density Iron/Steel HTPLA and Metal Composite PETG
  lines, where no TDS is published.

## License

[CC0-1.0](LICENSE) — public-domain dedication so Proto-Pasta, OrcaSlicer, or
anyone else can host, modify, and redistribute these profiles with no
obligations. Filament settings are facts; the more places they live, the
better they print.
