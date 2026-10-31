#!/usr/bin/env python3
"""Generate OrcaSlicer filament profiles for the Proto-Pasta catalog.

Where each value comes from is documented in docs/SOURCES.md and in each
profile's filament_notes. Sources are Proto-Pasta's Material Data Table
(proto-pasta.com/pages/material-data-table), their TDS/SDS documents, their
FAQ pages, product pages and launch articles. Where Proto-Pasta publishes no
number for a setting, the profile either inherits Orca's Generic value or
borrows Proto-Pasta's number for the closest related material, and the notes
say which.

Granularity rule (see README): one profile per filament type, plus one per
notable variation within the type (different temperatures, flow, bed,
density, type tag or hardware needs). Colorways and recycled versions are
listed in the parent profile's notes, never given their own profile.

Usage (from the repo root):  python3 scripts/generate_profiles.py
Writes: profiles/Protopasta.json, profiles/Protopasta/filament/*.json and
user_presets/*.json. It does NOT rebuild the zips in dist/.
"""

import json
import random
import string
from pathlib import Path

VENDOR = "Protopasta"
VENDOR_VERSION = "02.04.00.00"
VENDOR_DESCRIPTION = "Proto-Pasta (Protoplant) filament profiles - community-built from published Proto-Pasta data"

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "profiles" / VENDOR / "filament"

# ---------------------------------------------------------------------------
# Material table.
#
# Proto-Pasta's "Temp @ Max Vol" data pairs a nozzle temperature with a
# volumetric flow (e.g. 220C up to 6 mm3/s, 240C up to 12 mm3/s). A static
# profile holds one temperature, so profiles use the LOW temperature as the
# default, use the HIGH flow as filament_max_volumetric_speed (the cap), and
# the notes tell the user to raise the temperature when printing near the
# cap. range_low/range_high span every temperature Proto-Pasta publishes.
#
# density: g/cm3, from the TDS/SDS where published (see docs/SOURCES.md).
# bed: written to the hot-plate and textured-plate fields only; other plate
#      types keep Orca's inherited values.
# ---------------------------------------------------------------------------
M = []

def mat(**kw):
    kw.setdefault("nozzle", None)
    kw.setdefault("initial", kw["nozzle"])
    kw.setdefault("range_low", None)
    kw.setdefault("range_high", None)
    kw.setdefault("mvs", None)
    kw.setdefault("bed", None)
    kw.setdefault("density", None)
    kw.setdefault("filament_type", None)
    kw.setdefault("flow_ratio", None)
    kw.setdefault("notes", "")
    M.append(kw)

# ----- PLA family -------------------------------------------------------------

mat(
    id="PPF001", name="Protopasta PLA", inherits="fdm_filament_pla",
    nozzle=220, range_low=195, range_high=240, mvs=12, bed=55, density=1.24,
    notes=(
        "Covers Back to Basics PLA and Recycled PLA.\n"
        "Material Data Table: 220C up to 6 mm3/s, 240C up to 12 mm3/s, 55C plate. "
        "This profile uses 220C with a 12 mm3/s cap - raise toward 240C when printing "
        "near the cap. Getting-started page: 195-225C nozzle, 50-60C bed.\n"
        "Proto-Pasta finds PLA normally prints fine without drying; if you do dry it, "
        "stay below 50C."
    ),
)

mat(
    id="PPF002", name="Protopasta HTPLA", inherits="fdm_filament_pla",
    nozzle=220, range_low=195, range_high=240, mvs=12, bed=55, density=1.24,
    notes=(
        "Covers Premium HTPLA v3, High Temp PLA v2 and the color lines (opaque, "
        "translucent, metallic, glitter, fluorescent, multicolor, glow) plus Quantum "
        "Dot HTPLA.\n"
        "Material Data Table: 220C up to 6 mm3/s, 240C up to 12 mm3/s, 55C plate. "
        "This profile uses 220C with a 12 mm3/s cap - raise toward 240C when printing "
        "near the cap. Quantum Dot TDS: 220-240C nozzle, 55-65C bed.\n"
        "Heat treating (after printing): TDS says 95-110C for 10+ minutes; the HTPLA "
        "FAQ says 95-120C, usually about 10 minutes, on a flat wood or silicone "
        "surface. Parts shrink, so scale them up in the slicer first. Heat-treated "
        "HTPLA holds its shape to roughly 140-155C.\n"
        "Prusa MK2/MK3 with the stock heatbreak: Proto-Pasta says 235-240C can help "
        "avoid jams at the heatbreak ledge, but recommends a different hotend as the "
        "better fix."
    ),
)

mat(
    id="PPF003", name="Protopasta High Flow PLA", inherits="fdm_filament_pla",
    nozzle=200, range_low=190, range_high=220, mvs=18, bed=45, density=1.24,
    notes=(
        "High Flow PLA (HFPLA). Material Data Table: 200C up to 12 mm3/s, 220C up to "
        "18 mm3/s, 45C plate. This profile uses 200C with an 18 mm3/s cap - raise "
        "toward 220C when printing near the cap.\n"
        "Let the plate cool below 40C before removing prints."
    ),
)

mat(
    id="PPF004", name="Protopasta c-Matte PLA", inherits="fdm_filament_pla",
    nozzle=200, range_low=190, range_high=220, mvs=18, bed=45, density=1.3,
    notes=(
        "c-Matte PLA (matte finish). Material Data Table: 200C up to 12 mm3/s, 220C up "
        "to 18 mm3/s, 45C plate. This profile uses 200C with an 18 mm3/s cap - raise "
        "toward 220C when printing near the cap. Density 1.3 g/cm3 per SDS.\n"
        "Let the plate cool below 40C before removing prints."
    ),
)

mat(
    id="PPF005", name="Protopasta Matte Fiber HTPLA", inherits="fdm_filament_pla",
    nozzle=200, range_low=190, range_high=220, mvs=18, bed=55, density=1.14,
    notes=(
        "Matte Fiber HTPLA, including the wood-tone colors. Material Data Table: 200C "
        "up to 12 mm3/s, 220C up to 18 mm3/s, 55C plate; avoid printing below "
        "3 mm3/s. TDS: 195C nozzle, 60C bed. This profile uses 200C with an 18 mm3/s "
        "cap.\n"
        "Rough on PTFE tubing - replace it more often. The TDS says this fiber does "
        "not need a wear-resistant nozzle. Heat treat like HTPLA (TDS: 95-110C, 10+ "
        "minutes)."
    ),
)

mat(
    id="PPF006", name="Protopasta Calcium Carbonate PLA", inherits="fdm_filament_pla",
    nozzle=220, range_low=195, range_high=240, mvs=12, bed=55, density=1.5,
    notes=(
        "Calcium-carbonate-filled PLA. The Material Data Table lists this line but "
        "gives no temperatures, so this profile borrows Proto-Pasta's standard PLA "
        "numbers (220C up to 6 mm3/s, 240C up to 12 mm3/s, 55C plate). Density "
        "1.5 g/cm3 per SDS."
    ),
)

mat(
    id="PPF007", name="Protopasta Carbon Fiber PLA", inherits="fdm_filament_pla",
    filament_type="PLA-CF", flow_ratio=0.95,
    nozzle=210, range_low=195, range_high=240, mvs=12, bed=55, density=1.3,
    notes=(
        "15% (by weight) chopped carbon fiber in PLA or HTPLA; covers Carbon Fiber "
        "PLA, Carbon Fiber HTPLA and Recycled Carbon Fiber PLA.\n"
        "FAQ: 195-220C. TDS: 205C, 60C bed. Material Data Table: 220C up to 6 mm3/s, "
        "240C up to 12 mm3/s, 55C plate. This profile uses 210C with a 12 mm3/s cap "
        "- raise the temperature when printing near the cap.\n"
        "Abrasive: Proto-Pasta recommends a hard steel nozzle and gears, and "
        "replacing PTFE tubing more often. They report good results with a 0.5 mm "
        "nozzle and a spring-loaded direct-drive extruder. Brittle as filament - "
        "avoid sharp bends. Density: TDS and FAQ say 1.3 g/cm3 (used here); the SDS "
        "says 1.15."
    ),
)

mat(
    id="PPF008", name="Protopasta Stainless Steel PLA", inherits="fdm_filament_pla",
    nozzle=200, range_low=190, range_high=220, mvs=24, bed=55, density=2.3,
    notes=(
        "Steel-filled PLA. Material Data Table: 200C up to 24 mm3/s, 55C plate; avoid "
        "printing below 3 mm3/s; hard steel nozzle and gears recommended. FAQ: "
        "195-220C (215C with a 0.5 mm nozzle). TDS: 198C, 60C bed.\n"
        "Dense (about 2.3 g/cm3; about 90 m per 500 g) and more brittle than PLA as "
        "filament. Finish by wire brushing, tumbling, or wheel polishing with "
        "compound."
    ),
)

mat(
    id="PPF009", name="Protopasta Magnetic Iron PLA", inherits="fdm_filament_pla",
    nozzle=190, range_low=185, range_high=220, mvs=24, bed=55, density=1.85,
    notes=(
        "Iron-filled PLA (45% iron by weight). FAQ: 185-195C, about 10C cooler than "
        "standard PLA. Material Data Table: 200C up to 24 mm3/s, 55C plate; avoid "
        "printing below 3 mm3/s; hard steel nozzle and gears recommended. TDS: 192C, "
        "60C bed. This profile uses 190C with a 24 mm3/s cap - move toward 200C when "
        "printing near the cap.\n"
        "If parts warp, Proto-Pasta suggests turning the fan off and printing slower. "
        "Ferromagnetic (sticks to magnets, but isn't a magnet). Can be rusted for an "
        "aged finish. More brittle than PLA as filament; about 100 m per 500 g."
    ),
)

mat(
    id="PPF010", name="Protopasta High Density Iron HTPLA", inherits="fdm_filament_pla",
    nozzle=200, range_low=190, range_high=220, mvs=24, bed=55, density=2.4,
    notes=(
        "High Density Iron HTPLA: 60% iron by weight. No TDS is published. "
        "Proto-Pasta's launch article (Endless Exploration EX10) printed it at 200C "
        "at up to 24 mm3/s with a 0.4 mm steel nozzle. The 55C plate and the 'avoid "
        "below 3 mm3/s' advice are borrowed from their other metal-composite rows. "
        "Density 2.4 g/cm3 is an estimate - verify by weighing a known length.\n"
        "Hardened nozzle recommended. Heat treat at 100C for 10+ minutes for heat "
        "resistance up to about 150C; expect some shrinkage."
    ),
)

mat(
    id="PPF011", name="Protopasta High Density Steel HTPLA", inherits="fdm_filament_pla",
    nozzle=200, range_low=190, range_high=220, mvs=24, bed=55, density=2.4,
    notes=(
        "High Density Steel HTPLA: 70% 400-series stainless steel by weight. No TDS "
        "is published. Proto-Pasta's launch article (Endless Exploration EX10) "
        "printed it at 200C at up to 24 mm3/s with a 0.4 mm steel nozzle. The 55C "
        "plate and the 'avoid below 3 mm3/s' advice are borrowed from their other "
        "metal-composite rows. Density 2.4 g/cm3 is a rough estimate and probably "
        "low for 70% steel - verify by weighing a known length.\n"
        "Hardened nozzle recommended. Heat treat at 100C for 10+ minutes for heat "
        "resistance up to about 150C; expect some shrinkage."
    ),
)

for idx, metal in enumerate(("Brass", "Bronze", "Copper")):
    mat(
        id=f"PPF01{2 + idx}",  # PPF012, PPF013, PPF014
        name=f"Protopasta {metal} HTPLA", inherits="fdm_filament_pla",
        nozzle=200, range_low=190, range_high=220, mvs=24, bed=55, density=2.3,
        notes=(
            f"{metal}-filled HTPLA. Material Data Table: 200C up to 24 mm3/s, 55C "
            "plate; avoid printing below 3 mm3/s; hard steel nozzle and gears "
            "recommended. TDS: 195C nozzle, 60C bed, density about 2.3 g/cm3 (the SDS "
            "says 2.5), about 97 m per 500 g.\n"
            "Heat treat like HTPLA (TDS: 95-110C, 10+ minutes) to firm up parts."
        ),
    )

mat(
    id="PPF015", name="Protopasta Conductive PLA", inherits="fdm_filament_pla",
    nozzle=220, range_low=210, range_high=240, mvs=12, bed=55, density=1.24,
    notes=(
        "Carbon-black-filled conductive PLA. FAQ: 215-230C, run on the hotter side "
        "for layer adhesion. TDS: 210-230C, 60C plate, up to 8 mm3/s, 0.4 mm or "
        "larger nozzle. Material Data Table: 220C up to 6 mm3/s, 240C up to "
        "12 mm3/s, 55C plate. This profile uses the table's 12 mm3/s cap; the TDS "
        "only goes up to 8 mm3/s.\n"
        "Use Magigoo or glue stick - prints can fuse to the plate. Purge extra on "
        "filament changes. The filament is fairly flexible but breaks if bent "
        "repeatedly; printed parts are weaker along layer lines. Suited to "
        "low-voltage circuits, touch sensors and ESD uses."
    ),
)

mat(
    id="PPF016", name="Protopasta Static Dissipative PLA", inherits="fdm_filament_pla",
    nozzle=220, range_low=210, range_high=240, mvs=12, bed=55, density=1.24,
    notes=(
        "Static Dissipative PLA. TDS: 210-230C, 60C plate, up to 12 mm3/s, 0.4 mm or "
        "larger nozzle. Material Data Table: 220C up to 6 mm3/s, 240C up to "
        "12 mm3/s, 55C plate.\n"
        "Use Magigoo or glue stick so prints don't fuse to the plate; purge extra on "
        "filament changes."
    ),
)

mat(
    id="PPF017", name="Protopasta Static Dissipative Carbon Fiber PLA",
    inherits="fdm_filament_pla", filament_type="PLA-CF", flow_ratio=0.95,
    nozzle=220, range_low=210, range_high=240, mvs=12, bed=55, density=1.14,
    notes=(
        "Static Dissipative Carbon Fiber PLA. TDS: 210-230C, 60C plate, up to "
        "12 mm3/s, 0.4 mm or larger nozzle. Material Data Table: 220C up to 6 mm3/s, "
        "240C up to 12 mm3/s, 55C plate.\n"
        "Abrasive: hard steel nozzle and gears recommended; replace PTFE tubing more "
        "often. Use Magigoo or glue stick and purge extra on filament changes."
    ),
)

# ----- PETG family ------------------------------------------------------------

mat(
    id="PPF018", name="Protopasta PETG", inherits="fdm_filament_pet",
    nozzle=250, range_low=230, range_high=270, mvs=12, bed=80, density=1.2,
    notes=(
        "Covers Simply PETG colors, translucent PETG and Recycled PETG.\n"
        "Material Data Table: 250C up to 12 mm3/s, 80C plate. Use Magigoo or glue "
        "stick so prints don't fuse to the plate. If you dry it, stay below 65C."
    ),
)

mat(
    id="PPF019", name="Protopasta Carbon Fiber PETG", inherits="fdm_filament_pet",
    filament_type="PETG-CF", flow_ratio=0.95,
    nozzle=250, range_low=230, range_high=270, mvs=12, bed=80, density=1.2,
    notes=(
        "Covers Carbon Fiber PETG (PETG-CF7) and Recycled Carbon Fiber PETG.\n"
        "Material Data Table: 250C up to 12 mm3/s, 80C plate. Product page: 235C and "
        "up (they print up to 275C; 255C is a good compromise), 70C+ bed; reduce flow "
        "below 100% if material builds up on the nozzle.\n"
        "Abrasive: hard steel nozzle and gears recommended; replace PTFE tubing more "
        "often. Use Magigoo or glue stick. For the HTPETG lines, use the Protopasta "
        "Carbon Fiber HTPETG profile instead."
    ),
)

mat(
    id="PPF020", name="Protopasta Carbon Fiber HTPETG", inherits="fdm_filament_pet",
    filament_type="PETG-CF", flow_ratio=0.95,
    nozzle=260, range_low=240, range_high=300, mvs=12, bed=100,
    notes=(
        "High Strength (black, more carbon fiber) and High Impact (Galaxy Black, less "
        "carbon fiber) HTPETG, with ABS/ASA-level heat resistance.\n"
        "Product pages: nozzle up to 300C (hotter improves layer adhesion but risks "
        "overheating when printing slowly), bed 100C+, flow below 100% and a nozzle "
        "wipe at layer change to limit buildup. Proto-Pasta's launch article (EX14) "
        "printed at 300C and chose 6 mm3/s for a full melt. This profile's 260C with "
        "a 12 mm3/s cap is our own middle-ground choice, not a Proto-Pasta number.\n"
        "Dry before printing (wet filament causes nozzle buildup). Hard steel nozzle "
        "required (abrasive). EX14 also turned auxiliary and chamber fans off and "
        "used glue stick."
    ),
)

mat(
    id="PPF021", name="Protopasta Glass Fiber HTPETG", inherits="fdm_filament_pet",
    nozzle=250, range_low=230, range_high=270, mvs=12, bed=80,
    notes=(
        "Glass Fiber HTPETG (White, Highfive Blue). Product page: same guidance as "
        "the carbon-fiber HTPETG - nozzle up to 300C, bed 100C+, flow below 100% and "
        "a nozzle wipe at layer change to limit buildup. Higher heat resistance than "
        "Glass Fiber PCTG.\n"
        "This profile still uses Proto-Pasta's standard PETG numbers (250C, 80C "
        "plate, 12 mm3/s cap), which are below the product page's guidance - expect "
        "to raise the nozzle and bed temperatures.\n"
        "Dry before printing. Hard steel nozzle required (abrasive). Use glue stick."
    ),
)

mat(
    id="PPF022", name="Protopasta PCTG", inherits="fdm_filament_pctg",
    nozzle=250, range_low=230, range_high=270, mvs=12, bed=80,
    notes=(
        "Clear PCTG.\n"
        "Product page: start from a Generic PETG or PCTG profile; 255C and up (they "
        "print up to 275C; 255C is a good compromise), 80C+ bed, about 2 mm3/s; reduce "
        "flow below 100% if material builds up on the nozzle.\n"
        "This profile currently uses 250C, 80C plate and a 12 mm3/s cap - raise the "
        "nozzle toward 255C. Use Magigoo or glue stick."
    ),
)

mat(
    id="PPF023", name="Protopasta Carbon Fiber PCTG", inherits="fdm_filament_pctg",
    filament_type="PETG-CF", flow_ratio=0.95,
    nozzle=250, range_low=230, range_high=270, mvs=12, bed=80,
    notes=(
        "High Impact (gray, ~20% stronger and 115% stiffer than unfilled PCTG) and "
        "High Strength (black, ~45% stronger and 250% stiffer) carbon-fiber PCTG.\n"
        "Product pages: 255C and up (they print up to 275C; 255C is a good "
        "compromise), 70-80C+ bed, about 2 mm3/s; reduce flow below 100% and add a "
        "nozzle wipe at layer change if material builds up on the nozzle.\n"
        "This profile currently uses 250C, 80C plate and a 12 mm3/s cap - raise the "
        "nozzle toward 255C. Carbon fiber is abrasive - use a hardened nozzle. Use "
        "Magigoo or glue stick."
    ),
)

mat(
    id="PPF024", name="Protopasta Glass Fiber PCTG", inherits="fdm_filament_pctg",
    nozzle=250, range_low=230, range_high=270, mvs=12, bed=80,
    notes=(
        "White Glass Fiber PCTG - stiff like PLA, durable like PCTG (~75% stiffer "
        "than unfilled PCTG).\n"
        "Product page: 255C and up (they print up to 275C; 255C is a good "
        "compromise), 70-80C+ bed, about 2 mm3/s; reduce flow below 100% and add a "
        "nozzle wipe at layer change if material builds up on the nozzle.\n"
        "This profile currently uses 250C, 80C plate and a 12 mm3/s cap - raise the "
        "nozzle toward 255C. Glass fiber is abrasive - use a hardened nozzle. Use "
        "Magigoo or glue stick."
    ),
)

mat(
    id="PPF025", name="Protopasta Metal Composite PETG", inherits="fdm_filament_pet",
    nozzle=245, range_low=230, range_high=270, mvs=12, bed=80, density=2.4,
    notes=(
        "Copper, Steel (400-series stainless) and Iron composite PETG, each 60% metal "
        "by weight. Proto-Pasta: density about 2x PETG, so a spool gives about half "
        "the length. This profile uses 2.4 g/cm3 for all three - an estimate.\n"
        "Prints like PETG (Proto-Pasta used Generic PETG temperatures); a slightly "
        "lower nozzle temperature reduces stringing, so this profile defaults to "
        "245C. Avoid very low volume rates (below 2 mm3/s), and lower the temperature "
        "if you must print slowly. Use glue stick. A hardened nozzle is a good idea "
        "for metal-filled filament."
    ),
)

mat(
    id="PPF026", name="Protopasta Static Dissipative PETG", inherits="fdm_filament_pet",
    nozzle=250, range_low=250, range_high=290, mvs=12, bed=80, density=1.2,
    notes=(
        "Static Dissipative PETG. TDS: 250-290C, 70-80C plate, up to 8 mm3/s, 0.4 mm "
        "or larger nozzle; drying highly recommended (65C for 6 hours). Material Data "
        "Table: 250C up to 12 mm3/s, 80C plate. This profile uses the table's "
        "12 mm3/s cap; the TDS only goes up to 8 mm3/s.\n"
        "Use Magigoo or glue stick so prints don't fuse to the plate."
    ),
)

# ----- Flexible ---------------------------------------------------------------

mat(
    id="PPF027", name="Protopasta Rigid TPU", inherits="fdm_filament_tpu",
    notes=(
        "Clear Rigid TPU, about 70D (replaced the earlier White Rigid TPU). "
        "Discontinued; kept for existing stock.\n"
        "Product page: start printing at 240C, no bed heat needed; prep the bed with "
        "Magigoo to avoid a permanent bond; drying overnight recommended. This "
        "profile sets no values of its own and inherits Orca's Generic TPU values "
        "(240C nozzle, 35C bed, 3.2 mm3/s cap)."
    ),
)

mat(
    id="PPF028", name="Protopasta Flexible TPU", inherits="fdm_filament_tpu",
    notes=(
        "Clear Flexible TPU, about 98A; also covers Recycled Black Flexible TPU.\n"
        "Product page: start printing at 240C, no bed heat needed; prep the bed with "
        "Magigoo to avoid a permanent bond; drying overnight recommended. This "
        "profile sets no values of its own and inherits Orca's Generic TPU values "
        "(240C nozzle, 35C bed, 3.2 mm3/s cap). Direct-drive extruders, slow speeds "
        "and short retraction work best for flexible TPU."
    ),
)

# ---------------------------------------------------------------------------
# Emission
# ---------------------------------------------------------------------------

def setting_id(rng):
    return "".join(rng.choice(string.ascii_letters + string.digits) for _ in range(16))

def plate_fields(bed):
    if bed is None:
        return {}
    return {
        "hot_plate_temp": [str(bed)],
        "hot_plate_temp_initial_layer": [str(bed)],
        "textured_plate_temp": [str(bed)],
        "textured_plate_temp_initial_layer": [str(bed)],
    }

def base_profile(m):
    d = {
        "type": "filament",
        "name": f"{m['name']} @base",
        "inherits": m["inherits"],
        "from": "system",
        "filament_id": m["id"],
        "instantiation": "false",
        "filament_vendor": [VENDOR],
    }
    settings = {}
    if m["filament_type"]:
        settings["filament_type"] = [m["filament_type"]]
    if m["density"] is not None:
        settings["filament_density"] = [str(m["density"])]
    if m["nozzle"] is not None:
        settings["nozzle_temperature"] = [str(m["nozzle"])]
        settings["nozzle_temperature_initial_layer"] = [str(m["initial"])]
    if m["range_low"] is not None:
        settings["nozzle_temperature_range_low"] = [str(m["range_low"])]
    if m["range_high"] is not None:
        settings["nozzle_temperature_range_high"] = [str(m["range_high"])]
    if m["mvs"] is not None:
        settings["filament_max_volumetric_speed"] = [str(m["mvs"])]
    settings.update(plate_fields(m["bed"]))
    if m["notes"]:
        settings["filament_notes"] = [m["notes"]]
    d.update(dict(sorted(settings.items())))
    return d

def system_profile(m, sid):
    d = {
        "type": "filament",
        "name": m["name"],
        "inherits": f"{m['name']} @base",
        "from": "system",
        "setting_id": sid,
        "instantiation": "true",
        # Explicit "compatible with every printer": an empty list, the form
        # OrcaFilamentLibrary's own @System profiles use (e.g. Generic PLA
        # @System). The empty condition string makes it doubly explicit.
        "compatible_printers": [],
        "compatible_printers_condition": "",
    }
    if m["flow_ratio"] is not None:
        d["filament_flow_ratio"] = [str(m["flow_ratio"])]
    return d

# User presets cannot inherit the library's internal base names (Orca logs
# "can not find parent fdm_filament_pla" and skips the file). They must
# inherit the selectable Generic profiles, whose names end in "@System"
# (tested on Orca 2.4.2; these names exist in OrcaFilamentLibrary from
# Orca 2.3.0 onward). Note: Orca has no "Generic PCTG-CF", so Carbon Fiber
# PCTG's user preset inherits Generic PETG-CF @System, while its vendor-bundle
# @base inherits fdm_filament_pctg.
GENERIC_SYSTEM = {
    "pla": "Generic PLA @System",
    "pla_cf": "Generic PLA-CF @System",
    "pet": "Generic PETG @System",
    "pet_cf": "Generic PETG-CF @System",
    "pctg": "Generic PCTG @System",
    "tpu": "Generic TPU @System",
}

def user_inherits(m):
    cf = (m.get("filament_type") or "").endswith("-CF")
    if m["inherits"] == "fdm_filament_pla":
        return GENERIC_SYSTEM["pla_cf" if cf else "pla"]
    if m["inherits"] == "fdm_filament_pet":
        return GENERIC_SYSTEM["pet_cf" if cf else "pet"]
    if m["inherits"] == "fdm_filament_pctg":
        return GENERIC_SYSTEM["pet_cf" if cf else "pctg"]
    if m["inherits"] == "fdm_filament_tpu":
        return GENERIC_SYSTEM["tpu"]
    raise ValueError(f"unknown family {m['inherits']!r} for {m['name']}")

def user_preset(m):
    """Flat user-preset variant of a profile.

    Same values as the @base file plus the flow ratio, but in the format
    OrcaSlicer stores user presets in (from: "User"), inheriting the matching
    Generic @System profile. Any setting this file doesn't set comes from that
    Generic profile, so it can differ slightly from the vendor bundle (e.g.
    Generic PETG-CF @System sets its own fan speeds). These import via
    File -> Import -> Import Configs, or can be copied into Orca's user
    preset folder.
    """
    d = {
        "filament_settings_id": [m["name"]],
        "from": "User",
        "inherits": user_inherits(m),
        "is_custom_defined": "0",
        "name": m["name"],
        "version": "2.4.2.0",
    }
    settings = {}
    if m["filament_type"]:
        settings["filament_type"] = [m["filament_type"]]
    settings["filament_vendor"] = [VENDOR]
    if m["density"] is not None:
        settings["filament_density"] = [str(m["density"])]
    if m["flow_ratio"] is not None:
        settings["filament_flow_ratio"] = [str(m["flow_ratio"])]
    if m["nozzle"] is not None:
        settings["nozzle_temperature"] = [str(m["nozzle"])]
        settings["nozzle_temperature_initial_layer"] = [str(m["initial"])]
    if m["range_low"] is not None:
        settings["nozzle_temperature_range_low"] = [str(m["range_low"])]
    if m["range_high"] is not None:
        settings["nozzle_temperature_range_high"] = [str(m["range_high"])]
    if m["mvs"] is not None:
        settings["filament_max_volumetric_speed"] = [str(m["mvs"])]
    settings.update(plate_fields(m["bed"]))
    if m["notes"]:
        settings["filament_notes"] = [m["notes"]]
    d.update(dict(sorted(settings.items())))
    return d

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rng = random.Random(0x5EED)  # deterministic setting_ids
    filament_list = []
    used_sids = set()
    for m in M:
        while True:
            sid = setting_id(rng)
            if sid not in used_sids:
                used_sids.add(sid)
                break
        base_name = f"{m['name']} @base.json"
        sys_name = f"{m['name']}.json"
        (OUT_DIR / base_name).write_text(
            json.dumps(base_profile(m), indent="\t", ensure_ascii=False) + "\n"
        )
        (OUT_DIR / sys_name).write_text(
            json.dumps(system_profile(m, sid), indent="\t", ensure_ascii=False) + "\n"
        )
        filament_list.append({"name": f"{m['name']} @base", "sub_path": f"filament/{base_name}"})
        filament_list.append({"name": m["name"], "sub_path": f"filament/{sys_name}"})

    vendor = {
        "name": VENDOR,
        "version": VENDOR_VERSION,
        "force_update": "0",
        "description": VENDOR_DESCRIPTION,
        "filament_list": filament_list,
    }
    (REPO / "profiles" / f"{VENDOR}.json").write_text(
        json.dumps(vendor, indent="\t", ensure_ascii=False) + "\n"
    )

    user_dir = REPO / "user_presets"
    user_dir.mkdir(exist_ok=True)
    for stale in user_dir.glob("*.json"):
        stale.unlink()
    for m in M:
        (user_dir / f"{m['name']}.json").write_text(
            json.dumps(user_preset(m), indent="\t", ensure_ascii=False) + "\n"
        )
    print(f"Wrote {len(M)} profiles ({len(M)*2} files) + {VENDOR}.json to profiles/")
    print(f"Wrote {len(M)} user presets to user_presets/")

if __name__ == "__main__":
    main()
