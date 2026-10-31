#!/usr/bin/env python3
"""Generate OrcaSlicer filament profiles for the Proto-Pasta catalog.

Data sources are documented per-material in docs/SOURCES.md and in each
profile's filament_notes. Values come from Proto-Pasta's published Material
Data Table (proto-pasta.com/pages/material-data-table), TDS/SDS documents,
per-material FAQ pages, and product pages. Where Proto-Pasta publishes no
numbers for a line, the profile inherits Orca's Generic family defaults and
says so in its notes - nothing is invented.

Granularity rule (see README): one profile per filament type, plus one per
notable variation within the type (differing temps/flow/bed/density/type tag/
hardware requirements). Colorways and recycled variants fold into the parent
profile's notes, never separate profiles.

Usage: python3 scripts/generate_profiles.py   (from repo root)
Writes: profiles/Protopasta.json + profiles/Protopasta/filament/*.json
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
# nozzle encoding of Proto-Pasta's "Temp @ Max Vol" guidance: their data pairs
# a temperature with a volumetric flow (e.g. 220C@6, 240C@12 mm3/s). Profiles
# default to the LOW temperature (best surface quality, their stated
# preference for "lowest possible temperature"), keep the high-flow cap as
# filament_max_volumetric_speed, and the notes tell the user which temperature
# to move to at high flow. range_low/range_high bracket everything published.
#
# density: g/cm3 from TDS/SDS where published (see docs/SOURCES.md).
# bed: Proto-Pasta plate temperature -> hot + textured plate fields.
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
        "Covers Back to Basics PLA (Ingeo 4043D) and Recycled PLA.\n"
        "Proto-Pasta data: 220C suits ~6 mm3/s; raise toward 240C when printing at the "
        "full 12 mm3/s cap. Getting-started range: 195-225C nozzle, 50-60C bed.\n"
        "Dry below 50C if needed; printing without drying is normally fine."
    ),
)

mat(
    id="PPF002", name="Protopasta HTPLA", inherits="fdm_filament_pla",
    nozzle=220, range_low=195, range_high=240, mvs=12, bed=55, density=1.24,
    notes=(
        "Covers Premium HTPLA v3, High Temp PLA v2 and all color lines "
        "(opaque, translucent, metallic, glitter, fluorescent, Quantum Dot, glow).\n"
        "220C suits ~6 mm3/s; raise toward 240C at 12 mm3/s (240C also improves layer "
        "fusion). Quantum Dot TDS: 220-240C nozzle, 55-65C bed.\n"
        "Anneal for heat resistance up to ~140-155C (vs ~55-60C as printed): oven at "
        "85-115C for 5-60 min, ideally buried in silica sand or submerged in gel; treat "
        "with supports on.\n"
        "Prusa MK2/MK3 stock heatbreak: 235-240C helps avoid heat-creep jams."
    ),
)

mat(
    id="PPF003", name="Protopasta High Flow PLA", inherits="fdm_filament_pla",
    nozzle=200, range_low=190, range_high=220, mvs=18, bed=45, density=1.24,
    notes=(
        "HFPLA. Proto-Pasta data: 200C@12, 220C@18 mm3/s, 45C plate.\n"
        "Let the plate cool below 40C before removing prints."
    ),
)

mat(
    id="PPF004", name="Protopasta c-Matte PLA", inherits="fdm_filament_pla",
    nozzle=200, range_low=190, range_high=220, mvs=18, bed=45, density=1.3,
    notes=(
        "c-Matte PLA (calcium-carbonate matte finish). Proto-Pasta data: "
        "200C@12, 220C@18 mm3/s, 45C plate.\n"
        "Let the plate cool below 40C before removing prints."
    ),
)

mat(
    id="PPF005", name="Protopasta Matte Fiber HTPLA", inherits="fdm_filament_pla",
    nozzle=200, range_low=190, range_high=220, mvs=18, bed=55, density=1.14,
    notes=(
        "Matte Fiber HTPLA including wood-tone colors. Proto-Pasta data: "
        "200C@12, 220C@18 mm3/s, 55C plate. TDS: 195C nozzle, 60C bed.\n"
        "Avoid printing below 3 mm3/s. Fiber filling is rough on PTFE tubing - "
        "replace tubing more often."
    ),
)

mat(
    id="PPF006", name="Protopasta Calcium Carbonate PLA", inherits="fdm_filament_pla",
    nozzle=220, range_low=195, range_high=240, mvs=12, bed=55, density=1.5,
    notes=(
        "CaCO3 composite PLA. Proto-Pasta's table lists no dedicated temps for this "
        "line - use PLA-family defaults (220C@6, 240C@12 mm3/s, 55C plate). "
        "Density 1.5 g/cm3 per SDS."
    ),
)

mat(
    id="PPF007", name="Protopasta Carbon Fiber PLA", inherits="fdm_filament_pla",
    filament_type="PLA-CF", flow_ratio=0.95,
    nozzle=210, range_low=195, range_high=240, mvs=12, bed=55, density=1.3,
    notes=(
        "15% chopped-carbon-fiber PLA/HTPLA; covers Carbon Fiber PLA, High Temp CF PLA "
        "and Recycled CF PLA.\n"
        "FAQ range 195-220C (TDS 205C); Material Data Table: 220C@6, 240C@12 mm3/s, 55C "
        "plate. Hardened nozzle and drive gears recommended - fiber is abrasive. "
        "Proto-Pasta cites good results with 0.5 mm nozzles and spring-loaded "
        "direct-drive extruders. Filament is brittle in spool form - avoid sharp bends.\n"
        "Recycled variant prints the same."
    ),
)

mat(
    id="PPF008", name="Protopasta Stainless Steel PLA", inherits="fdm_filament_pla",
    nozzle=200, range_low=190, range_high=220, mvs=24, bed=55, density=2.3,
    notes=(
        "Proto-Pasta data: 200C@24 mm3/s, 55C plate; FAQ range 195-220C "
        "(215C cited with a 0.5 mm nozzle). Avoid printing below 3 mm3/s.\n"
        "Dense (2.3 g/cm3, ~90 m per 500 g) and brittle in spool form. Hardened brass "
        "or steel nozzle recommended for wear. Finish by wire brushing, tumbling, or "
        "buffing with compound."
    ),
)

mat(
    id="PPF009", name="Protopasta Magnetic Iron PLA", inherits="fdm_filament_pla",
    nozzle=190, range_low=185, range_high=220, mvs=24, bed=55, density=1.85,
    notes=(
        "Proto-Pasta data: 200C@24 mm3/s, 55C plate; FAQ: prints ~10C cooler than "
        "standard PLA (185-195C). Avoid printing below 3 mm3/s.\n"
        "If warping occurs, reduce fan speed or print slower (table cap 24 mm3/s is a "
        "maximum, not a target). Ferromagnetic but not a magnet itself; rustable for "
        "aged finishes. Brittle in spool form; ~100 m per 500 g."
    ),
)

mat(
    id="PPF010", name="Protopasta High Density Iron HTPLA", inherits="fdm_filament_pla",
    nozzle=200, range_low=190, range_high=220, mvs=24, bed=55, density=2.4,
    notes=(
        "60% iron by weight. Proto-Pasta publishes no TDS for this line; settings "
        "follow their metal-composite row (200C@24 mm3/s, 55C plate) and density is "
        "estimated at ~2x base polymer from their published description - verify by "
        "weighing a known length.\n"
        "Avoid printing below 3 mm3/s. Hardened nozzle recommended. Brittle in spool "
        "form. Anneal like HTPLA for heat resistance."
    ),
)

mat(
    id="PPF011", name="Protopasta High Density Steel HTPLA", inherits="fdm_filament_pla",
    nozzle=200, range_low=190, range_high=220, mvs=24, bed=55, density=2.4,
    notes=(
        "High-density steel-filled HTPLA. Proto-Pasta publishes no TDS for this line; "
        "settings follow their metal-composite row (200C@24 mm3/s, 55C plate) and "
        "density is estimated - verify by weighing a known length.\n"
        "Avoid printing below 3 mm3/s. Hardened nozzle recommended. Brittle in spool "
        "form. Anneal like HTPLA for heat resistance."
    ),
)

for idx, metal in enumerate(("Brass", "Bronze", "Copper")):
    mat(
        id=f"PPF01{2 + idx}",  # PPF012, PPF013, PPF014
        name=f"Protopasta {metal} HTPLA", inherits="fdm_filament_pla",
        nozzle=200, range_low=190, range_high=220, mvs=24, bed=55, density=2.3,
        notes=(
            f"{metal}-filled metal-composite HTPLA. Proto-Pasta data: "
            "200C@24 mm3/s, 55C plate; TDS 195C nozzle, 60C bed, density ~2.3 g/cm3 "
            "(~90-100 m per 500 g).\n"
            "Avoid printing below 3 mm3/s. Hardened nozzle recommended. Brittle in "
            "spool form. Polish by sanding/burnishing for real-metal luster; anneal "
            "like HTPLA for heat resistance."
        ),
    )

mat(
    id="PPF015", name="Protopasta Conductive PLA", inherits="fdm_filament_pla",
    nozzle=220, range_low=210, range_high=240, mvs=12, bed=55, density=1.24,
    notes=(
        "Carbon-black conductive PLA (4043D base). FAQ: 215-230C, run on the hotter "
        "side for layer adhesion; TDS 210-230C, 60C plate; table 220C@6/240C@12, 55C "
        "plate.\n"
        "Use Magigoo or glue stick - prints can fuse to smooth plate surfaces when "
        "hot. Purge thoroughly on filament changes. Filament is quite flexible; "
        "printed parts are weaker along layer lines. Low-voltage circuits, touch "
        "sensors, ESD applications."
    ),
)

mat(
    id="PPF016", name="Protopasta Static Dissipative PLA", inherits="fdm_filament_pla",
    nozzle=220, range_low=210, range_high=240, mvs=12, bed=55, density=1.24,
    notes=(
        "SD PLA. TDS: 210-230C nozzle, 60C plate; table 220C@6/240C@12, 55C plate.\n"
        "Use Magigoo or glue stick and purge thoroughly on changes."
    ),
)

mat(
    id="PPF017", name="Protopasta Static Dissipative Carbon Fiber PLA",
    inherits="fdm_filament_pla", filament_type="PLA-CF", flow_ratio=0.95,
    nozzle=220, range_low=210, range_high=240, mvs=12, bed=55, density=1.14,
    notes=(
        "SD CF PLA. TDS: 210-230C nozzle, 60C plate; table 220C@6/240C@12, 55C "
        "plate.\n"
        "Hardened nozzle and gears recommended (abrasive). Use Magigoo or glue stick "
        "and purge thoroughly on changes."
    ),
)

# ----- PETG family ------------------------------------------------------------

mat(
    id="PPF018", name="Protopasta PETG", inherits="fdm_filament_pet",
    nozzle=250, range_low=230, range_high=270, mvs=12, bed=80, density=1.2,
    notes=(
        "Covers Simply PETG colors, translucent PETG and Recycled PETG.\n"
        "Proto-Pasta data: 250C@12 mm3/s, 80C plate. Use Magigoo or glue stick to "
        "avoid fusing to smooth build surfaces. Dry below 65C if needed.\n"
        "Lower nozzle temperature reduces stringing on the metal-composite PETGs."
    ),
)

mat(
    id="PPF019", name="Protopasta Carbon Fiber PETG", inherits="fdm_filament_pet",
    filament_type="PETG-CF", flow_ratio=0.95,
    nozzle=250, range_low=230, range_high=270, mvs=12, bed=80, density=1.2,
    notes=(
        "Covers Carbon Fiber PETG and Recycled Carbon Fiber PETG.\n"
        "Proto-Pasta data: 250C@12 mm3/s, 80C plate. Hardened nozzle and gears "
        "required (abrasive). Use Magigoo or glue stick; purge thoroughly.\n"
        "For the high-temperature HTPETG carbon-fiber lines see the dedicated "
        "Protopasta Carbon Fiber HTPETG profile."
    ),
)

mat(
    id="PPF020", name="Protopasta Carbon Fiber HTPETG", inherits="fdm_filament_pet",
    filament_type="PETG-CF", flow_ratio=0.95,
    nozzle=260, range_low=240, range_high=300, mvs=12, bed=100,
    notes=(
        "High Strength (black, higher CF) and High Impact (galaxy black, lower CF) "
        "carbon-fiber HTPETG. ABS/ASA-level heat resistance without fumes.\n"
        "Product page: nozzle up to 300C - higher temps improve layer adhesion but "
        "risk overheating when printing slow. Bed from 100C up prints flat. Consider "
        "flow below 100% and a nozzle-wipe-at-layer-change gcode to limit buildup; "
        "drying may not fully resolve nozzle stick.\n"
        "Hardened nozzle and gears required (abrasive). Use Magigoo or glue stick."
    ),
)

mat(
    id="PPF021", name="Protopasta Glass Fiber HTPETG", inherits="fdm_filament_pet",
    nozzle=250, range_low=230, range_high=270, mvs=12, bed=80,
    notes=(
        "Glass Fiber HTPETG (Highfive Blue, White).\n"
        "Proto-Pasta publishes no numeric settings for this line; PETG-family "
        "defaults applied (250C@12 mm3/s, 80C plate). Stiff like PLA, durable like "
        "PETG, higher temperature resistance than GF PCTG.\n"
        "Glass fiber is abrasive - hardened nozzle recommended. Use Magigoo or glue "
        "stick."
    ),
)

mat(
    id="PPF022", name="Protopasta PCTG", inherits="fdm_filament_pctg",
    nozzle=250, range_low=230, range_high=270, mvs=12, bed=80,
    notes=(
        "Clear PCTG.\n"
        "Proto-Pasta publishes no numeric settings for this line; PCTG-family "
        "defaults applied. Use Magigoo or glue stick."
    ),
)

mat(
    id="PPF023", name="Protopasta Carbon Fiber PCTG", inherits="fdm_filament_pctg",
    filament_type="PETG-CF", flow_ratio=0.95,
    nozzle=250, range_low=230, range_high=270, mvs=12, bed=80,
    notes=(
        "High Impact (gray, ~20% stronger / 115% stiffer than unfilled PCTG) and High "
        "Strength (black, ~45% stronger / 250% stiffer) carbon-fiber PCTG.\n"
        "Proto-Pasta publishes no numeric settings for this line; PCTG-family "
        "defaults applied. Hardened nozzle and gears required (abrasive). Use Magigoo "
        "or glue stick."
    ),
)

mat(
    id="PPF024", name="Protopasta Glass Fiber PCTG", inherits="fdm_filament_pctg",
    nozzle=250, range_low=230, range_high=270, mvs=12, bed=80,
    notes=(
        "White Glass Fiber PCTG - stiff like PLA, durable like PCTG (~75% stiffer "
        "than unfilled), layer-hiding texture.\n"
        "Proto-Pasta publishes no numeric settings for this line; PCTG-family "
        "defaults applied. Glass fiber is abrasive - hardened nozzle recommended. "
        "Use Magigoo or glue stick."
    ),
)

mat(
    id="PPF025", name="Protopasta Metal Composite PETG", inherits="fdm_filament_pet",
    nozzle=245, range_low=230, range_high=270, mvs=12, bed=80, density=2.4,
    notes=(
        "Copper, Steel and Iron composite PETG. PETG properties with real metal "
        "powder; iron version is 60% iron by weight (density ~2x PETG, so a given "
        "weight prints ~half the length). Copper/steel densities not published - the "
        "2.4 g/cm3 default reflects the iron version.\n"
        "Prints like PETG; a slightly lower nozzle temperature reduces stringing "
        "(default set to 245C). Hardened nozzle recommended. Brittle in spool form; "
        "ferrous versions rustable for aged finishes."
    ),
)

mat(
    id="PPF026", name="Protopasta Static Dissipative PETG", inherits="fdm_filament_pet",
    nozzle=250, range_low=250, range_high=290, mvs=12, bed=80, density=1.2,
    notes=(
        "SD PETG. TDS: 250-290C nozzle, 70-80C plate; Material Data Table: "
        "250C@12 mm3/s, 80C plate.\n"
        "Use Magigoo or glue stick to avoid fusing to smooth build surfaces; purge "
        "thoroughly on changes."
    ),
)

# ----- Flexible ---------------------------------------------------------------

mat(
    id="PPF027", name="Protopasta Rigid TPU", inherits="fdm_filament_tpu",
    notes=(
        "Approx. 70D rigid TPU (clear; replaces earlier White Rigid TPU). Line now "
        "discontinued but profiles are kept for existing stock.\n"
        "Proto-Pasta publishes no numeric settings for TPU; Orca Generic TPU "
        "defaults applied. Reduce retraction and speed for best results on Bowden "
        "setups."
    ),
)

mat(
    id="PPF028", name="Protopasta Flexible TPU", inherits="fdm_filament_tpu",
    notes=(
        "Approx. 98A flexible TPU (clear; Recycled Black Flexible TPU prints the "
        "same).\n"
        "Proto-Pasta publishes no numeric settings for TPU; Orca Generic TPU "
        "defaults applied. Prefer direct-drive extruders, slow down and minimize "
        "retraction for clean surfaces."
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
        # Explicit "compatible with every printer". Orca's bundle importer
        # filters profiles against installed printers; an absent key can be
        # treated as printer-scoped and rejected with "printer not
        # installed". Empty list + empty condition is the universal form
        # Orca's own bundled profiles use (e.g. Generic PLA-CF @System).
        "compatible_printers": [],
        "compatible_printers_condition": "",
    }
    if m["flow_ratio"] is not None:
        d["filament_flow_ratio"] = [str(m["flow_ratio"])]
    return d

# User presets cannot inherit the library's internal base names (Orca logs
# "can not find parent fdm_filament_pla" and skips the file). They must
# inherit the INSTANTIATED system profiles, whose names carry the @System
# suffix (verified against a working user preset on Orca 2.4.2:
# "inherits": "Generic TPU @System"). Requires Orca 2.4+ naming; on older
# versions use the vendor bundle instead.
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

    Same authored values as the @base file, but in the format OrcaSlicer
    stores/loads user presets in (from: "User"), inheriting the matching
    instantiated Generic system profile. These import via File ->
    Import -> Import configs, or can be dropped into Orca's user preset
    folder.
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
