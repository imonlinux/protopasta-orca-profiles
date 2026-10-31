# Offering these profiles to Proto-Pasta – proposal and hosting options

The goal: give Proto-Pasta (Protoplant) a ready-to-host, community-built set
of OrcaSlicer profiles for their catalog, with no obligations (CC0). This
note is the outreach pitch plus the practical options, so whoever has the
conversation doesn't have to work them out again.

## The pitch (short version)

> OrcaSlicer is a popular open-source slicer. Its built-in filament library
> includes brands like Polymaker, eSUN, Overture and SUNLU, but nothing from
> Proto-Pasta, and your Material Data Table tells customers to start from a
> Generic PLA or PETG profile. We turned the numbers you already publish
> (Material Data Table, TDS sheets, FAQ and product pages) into 28 OrcaSlicer
> filament profiles, with the source of every value documented, estimates
> flagged, and a CC0 license so you can host or change them however you
> like. Want them? They're yours.

## Before sending: fix or flag these

- **PCTG and Glass Fiber HTPETG profiles** still use your PETG row
  (250 °C / 80 °C). Your product pages say 255 °C and up for PCTG, and up to
  300 °C with a 100 °C+ bed for GF HTPETG. Update the profiles first, or ask
  Proto-Pasta which numbers they want.
- **Glass Fiber HTPLA** has no profile yet.

## Hosting options (any combination)

1. **A download on proto-pasta.com** – the cheapest option. Host
   `Protopasta_user_presets.zip`; customers install it with OrcaSlicer's
   **File → Import → Import Configs…** (requires OrcaSlicer 2.3.0 or newer).
   Do **not** host `Protopasta.zip`: OrcaSlicer's import menu doesn't accept
   that format (see the README). Polymaker runs a similar preset-download
   site at presets.polymaker.com.

2. **Add them to OrcaSlicer itself** – the widest reach: every OrcaSlicer
   user could pick Proto-Pasta filaments from the built-in list. Brand
   filaments go in the **Orca Filament Library**, as a pull request to
   https://github.com/OrcaSlicer/OrcaSlicer following the wiki's
   [How to create profiles](https://www.orcaslicer.com/wiki/developer_reference/how_to_create_profiles)
   guide. The current `profiles/` folder is close, but must be reshaped
   first:
   - move the files into `resources/profiles/OrcaFilamentLibrary/filament/Protopasta/`
     and list them in `OrcaFilamentLibrary.json`, instead of shipping a
     separate `Protopasta.json` vendor;
   - rename the selectable profiles to end in ` @System`
     (e.g. `Protopasta PLA @System`);
   - replace the hand-written `filament_id` (`PPF001`…) and `setting_id`
     values with ones from Orca's ID-generation script;
   - run Orca's profile checker before opening the PR.

   Proto-Pasta checking the numbers would make the pull request much more
   likely to be accepted quickly.

## What Proto-Pasta should check before hosting

- The estimated densities: High Density Iron HTPLA, High Density Steel HTPLA
  and Metal Composite PETG (2.4 g/cm³ each; none published).
- The default nozzle temperature for the two-point "Temp @ Max Vol" data: we
  use the lower temperature with the higher flow cap and tell users in the
  notes to raise the temperature near the cap. They may prefer the higher
  temperature, or a lower cap.
- Carbon Fiber HTPETG: we chose 260 °C nozzle, 100 °C bed and a 12 mm³/s cap
  from "up to 300C" and "100+ C"; their launch article printed at 300 °C and
  6 mm³/s.
- Where their own sources disagree (listed in `docs/SOURCES.md`), e.g. the
  Conductive PLA and Static Dissipative PETG TDS sheets stop at 8 mm³/s while
  the Material Data Table allows 12.
- TPU: their product pages say 240 °C with no bed heat; the profiles inherit
  Orca's Generic TPU values (240 °C, 35 °C bed).
- Rigid TPU is discontinued but kept for existing stock.

## Keeping it up to date

`scripts/generate_profiles.py` holds the whole catalog as one table with
per-line notes. A new colorway usually needs only a note; a new material
needs one new `mat(...)` entry. Then run the generator and the validator, and
re-zip `dist/` (commands in the README). If Proto-Pasta takes this over, the
table also works as a checklist of lines that have no TDS yet (PCTG, TPU,
HTPETG, glass fiber and High Density lines).
