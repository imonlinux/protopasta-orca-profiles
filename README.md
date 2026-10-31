# Protopasta OrcaSlicer Filament Profiles

Community-built [OrcaSlicer](https://orcaslicer.com) filament profiles for the
[Proto-Pasta](https://proto-pasta.com) (Protoplant) filament catalog: 28
profiles covering the product families listed below, built from the numbers
Proto-Pasta publishes (Material Data Table, TDS/SDS sheets, FAQ pages, product
pages and launch articles). Where Proto-Pasta publishes no number, each
profile's notes say what it uses instead (an Orca default, a related
Proto-Pasta material, or an estimate).

OrcaSlicer ships no Proto-Pasta profiles, and Proto-Pasta's Material Data
Table simply tells you to start from a Generic PLA or PETG profile. These
profiles put Proto-Pasta's published numbers and handling advice into
importable files. They are not affiliated with or endorsed by Proto-Pasta.

> **Status:** the user-preset format was checked against a working user
> preset in OrcaSlicer 2.4.2. Not every profile has been import-tested or
> test-printed; the profiles have not been reviewed by Proto-Pasta.

## Install

**Requirements:** OrcaSlicer 2.3.0 or newer. Each preset builds on one of
Orca's Generic filament profiles (for example `Generic PLA @System`), and
those first shipped in 2.3.0.

**Option 1 – import (easiest)**

1. In OrcaSlicer, choose **File → Import → Import Configs…**
2. Select `dist/Protopasta_user_presets.zip`, or any of the `.json` files in
   `user_presets/`.
3. The profiles appear in the filament list under your user presets. They
   work with any printer.

**Option 2 – copy the files**

1. In OrcaSlicer, choose **Help → Show Configuration Folder**.
2. Open `user/default/filament/` (if you are signed in to an Orca account,
   use `user/<your account id>/filament/` instead).
3. Copy the `.json` files from `user_presets/` into that folder and restart
   OrcaSlicer.

**If a profile doesn't appear:** OrcaSlicer silently skips a user preset when
it can't find the profile it builds on. Check that you are on 2.3.0 or newer.

## What's covered

Each profile covers one filament type, or a variation of it that Proto-Pasta
prints differently (see *How profiles are split* below). Colors and recycled
versions of a material share their parent's profile and are listed in its
notes.

| Profile | Products covered | Where the numbers come from |
|---|---|---|
| Protopasta PLA | Back to Basics PLA, Recycled PLA | Material Data Table (MDT), SDS, getting-started page |
| Protopasta HTPLA | Premium HTPLA v3, HTPLA v2, all color, glitter, fluorescent, multicolor, glow and Quantum Dot lines | MDT, TDS, HTPLA FAQ |
| Protopasta High Flow PLA | HFPLA | MDT |
| Protopasta c-Matte PLA | c-Matte colors | MDT, SDS |
| Protopasta Matte Fiber HTPLA | Matte Fiber, including wood tones | MDT, TDS |
| Protopasta Calcium Carbonate PLA | Calcium Carbonate PLA | SDS for density; temperatures borrowed from Proto-Pasta's PLA row (its MDT row is blank) |
| Protopasta Carbon Fiber PLA | Carbon Fiber PLA, Carbon Fiber HTPLA, Recycled CF PLA | MDT, TDS, FAQ |
| Protopasta Stainless Steel PLA | Stainless Steel PLA (all colors) | MDT, TDS, FAQ |
| Protopasta Magnetic Iron PLA | Magnetic Iron PLA | MDT, TDS, FAQ |
| Protopasta High Density Iron HTPLA | High Density Iron HTPLA | Launch article; density **estimated** (no TDS) |
| Protopasta High Density Steel HTPLA | High Density Steel HTPLA | Launch article; density **estimated** (no TDS) |
| Protopasta Brass / Bronze / Copper HTPLA (3 profiles) | Brass, Bronze, Copper HTPLA | MDT, TDS |
| Protopasta Conductive PLA | Conductive PLA | MDT, TDS, FAQ |
| Protopasta Static Dissipative PLA / Carbon Fiber PLA / PETG (3 profiles) | ESD lines | MDT, TDS, SDS |
| Protopasta PETG | Simply PETG, translucent PETG, Recycled PETG | MDT, SDS |
| Protopasta Carbon Fiber PETG | CF PETG, Recycled CF PETG | MDT, SDS, product page |
| Protopasta Carbon Fiber HTPETG | High Strength and High Impact CF HTPETG | Product pages, launch article |
| Protopasta Glass Fiber HTPETG | White and Highfive Blue GF HTPETG | Proto-Pasta's PETG row ⚠ |
| Protopasta PCTG | Clear PCTG | Proto-Pasta's PETG row ⚠ |
| Protopasta Carbon Fiber PCTG | High Impact and High Strength CF PCTG | Proto-Pasta's PETG row ⚠ |
| Protopasta Glass Fiber PCTG | White GF PCTG | Proto-Pasta's PETG row ⚠ |
| Protopasta Metal Composite PETG | Copper, Steel, Iron PETG | Product pages, launch article; density **estimated** |
| Protopasta Rigid TPU / Flexible TPU (2 profiles) | Clear Rigid TPU (discontinued), Clear Flexible TPU, Recycled Black Flexible TPU | Orca's Generic TPU values (nothing set) |

⚠ These profiles use Proto-Pasta's standard PETG numbers (250 °C nozzle,
80 °C plate, 12 mm³/s cap), but the product pages give different guidance:
**255 °C and up for PCTG, up to 300 °C with a 100 °C+ bed for GF HTPETG.**
Each profile's notes say so; adjust before printing.

**Not covered yet:** Glass Fiber HTPLA (red, white, blue and laser gray). Its
product page gives 240 °C at up to 24 mm³/s.

Value-by-value sources are in [docs/SOURCES.md](docs/SOURCES.md).

## How Proto-Pasta's numbers become a profile

**Temperature and flow.** Proto-Pasta's Material Data Table pairs a nozzle
temperature with a maximum flow, for example *220 °C up to 6 mm³/s, 240 °C up
to 12 mm³/s*. A profile can hold only one temperature, so each profile:

- uses the **lower** temperature as its default,
- uses the **higher** flow as its maximum volumetric speed (the cap Orca
  won't exceed),
- sets the allowed temperature range wide enough to include every published
  value, and
- says in its notes which temperature to move to when printing near the cap.

This means a profile can print at the cap while still at the lower
temperature. If your printer runs near the cap (most fast printers do on
infill), raise the temperature as the notes say, or lower the cap.

The caps follow the Material Data Table: 12 mm³/s for standard lines,
18 mm³/s for the high-flow lines, 24 mm³/s for metal composites. They are
limits, not targets. Proto-Pasta's getting-started page notes that most
machines perform well at 3–4 mm³/s.

**Plate temperature.** Proto-Pasta's plate temperature is written to Orca's
*hot plate* and *textured plate* settings. Other plate types (such as cool,
engineering and super-tack plates) keep Orca's inherited values.

**Everything else** (fan speeds, cooling, pressure advance and so on) is
inherited from the Orca profile each preset builds on: Generic PLA, PLA-CF,
PETG, PETG-CF, PCTG or TPU.

## How profiles are split

One profile per **filament type** (PLA, HTPLA, PETG, PCTG, TPU…), plus one
for any **variation Proto-Pasta prints differently**: a different
temperature/flow pair, plate temperature, density, filament type (such as
PLA-CF), hardware need (such as a hardened nozzle) or post-processing.
Examples: Matte Fiber and c-Matte have their own profiles because their
temperatures, plates and densities differ from HTPLA/PLA; Carbon Fiber HTPETG
is separate from Carbon Fiber PETG because it prints at up to 300 °C on a
100 °C+ bed; each metal composite keeps its own profile.

Colors, glitter, fluorescent, Quantum Dot and glow versions, and recycled
versions of the same formula **never** get their own profile; they are
listed in the parent profile's notes. If only the color differs, it goes in
the notes; if the settings differ, it gets a new profile.

## The two formats in this repo

| Folder | Format | Use it for |
|---|---|---|
| `user_presets/` (zipped in `dist/Protopasta_user_presets.zip`) | OrcaSlicer user presets | **Installing.** This is what the install steps above use. |
| `profiles/` (zipped in `dist/Protopasta.zip`) | OrcaSlicer system-profile ("vendor bundle") format | A starting point for adding the profiles to OrcaSlicer itself. **It can't be installed from OrcaSlicer's menus.** |

Both are generated from the same table and carry the same values. The only
differences come from what each builds on: the user presets build on Orca's
Generic `@System` profiles, while the vendor bundle builds directly on Orca's
internal `fdm_filament_*` bases. For example, Carbon Fiber PCTG's user preset
builds on Generic PETG-CF (Orca has no Generic PCTG-CF), so it picks up that
profile's fan settings.

Why the vendor bundle can't be imported: **File → Import → Import Configs…**
only imports preset files that carry `version` and `filament_settings_id`
fields (plus Orca's own exported bundles). System-format files have neither,
so Orca skips them without an error. Getting the profiles into OrcaSlicer itself means a pull
request to OrcaSlicer, and that needs the files reshaped first; see
[docs/GIFT_NOTE.md](docs/GIFT_NOTE.md).

## Repo layout

```
user_presets/                  the installable profiles (one .json each)
profiles/                      the same profiles in Orca's system format
  Protopasta.json              vendor index (lists every profile file)
  Protopasta/filament/         28 pairs: "<name> @base.json" + "<name>.json"
dist/                          zips of both folders
scripts/generate_profiles.py   the material table - the single source of truth
scripts/validate_profiles.py   structural checks for both formats
data/                          gathered source material (see data/README.md)
docs/SOURCES.md                where each value comes from
docs/GIFT_NOTE.md              proposal for Proto-Pasta / OrcaSlicer
```

## Changing a value

Edit the material table in `scripts/generate_profiles.py`, then from the
repo root:

```bash
python3 scripts/generate_profiles.py    # rewrites profiles/ and user_presets/
python3 scripts/validate_profiles.py    # checks structure
```

The generator does **not** rebuild the zips in `dist/`; re-zip them yourself
so they match:

```bash
(cd profiles && rm -f ../dist/Protopasta.zip && zip -r ../dist/Protopasta.zip Protopasta.json Protopasta)
(cd user_presets && rm -f ../dist/Protopasta_user_presets.zip && zip ../dist/Protopasta_user_presets.zip *.json)
```

## Known limitations

- **Estimated densities** (they only affect Orca's weight and cost
  estimates): High Density Iron HTPLA, High Density Steel HTPLA (probably
  low) and Metal Composite PETG. Weigh a measured length to check.
- **PCTG and Glass Fiber HTPETG profiles** use Proto-Pasta's PETG numbers,
  which are below what their product pages recommend (see ⚠ above).
- **Glass Fiber HTPLA** has no profile yet.
- **TPU profiles** set no values of their own; they use Orca's Generic TPU
  values (240 °C, 35 °C bed, 3.2 mm³/s).
- **Where Proto-Pasta's sources disagree**, the profile follows the Material
  Data Table and the notes mention the other value. Examples: Conductive PLA
  and Static Dissipative PETG use the table's 12 mm³/s cap, while their TDS
  sheets only go to 8 mm³/s; Carbon Fiber PLA uses the TDS density of
  1.3 g/cm³, while the SDS says 1.15.

## License

[CC0-1.0](LICENSE): a public-domain dedication, so Proto-Pasta, OrcaSlicer or
anyone else can host, modify and redistribute these profiles with no
obligations. Proto-Pasta's own documents (the PDFs and page copies in
`data/`) are not covered; they are kept locally and are not in git.
