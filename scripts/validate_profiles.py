#!/usr/bin/env python3
"""Validate the Protopasta OrcaSlicer profile bundle.

Checks:
  1. Every file is valid JSON.
  2. Structure: type/name/inherits/from present, name matches the file
     name, instantiation is "true"/"false", and every instantiated profile
     has a matching "<name> @base" file.
  3. All settings values are arrays (Orca requirement).
  4. Every 'inherits' target resolves (own @base, or an fdm_filament_* base
     shipped in OrcaSlicer 2.4.2's OrcaFilamentLibrary).
  5. filament_id and setting_id uniqueness.
  6. Vendor filament_list <-> files on disk parity.
  7. User presets: valid JSON, from "User", name/filament_settings_id match,
     inherit a known Generic @System profile, filament_vendor set.

It does not check that the zips in dist/ are up to date, and it does not
sanity-check the numbers themselves.
"""

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROFILES = REPO / "profiles"
FILAMENT_DIR = PROFILES / "Protopasta" / "filament"

# Base profiles in OrcaSlicer 2.4.2's OrcaFilamentLibrary/filament/base/
# (the same 22 files ship in 2.5.0-beta).
ORCA_BASES = {
    "fdm_filament_abs", "fdm_filament_asa", "fdm_filament_bvoh",
    "fdm_filament_common", "fdm_filament_cope", "fdm_filament_eva",
    "fdm_filament_hips", "fdm_filament_pa", "fdm_filament_paht",
    "fdm_filament_pc", "fdm_filament_pctg", "fdm_filament_pe",
    "fdm_filament_pet", "fdm_filament_pha", "fdm_filament_pla",
    "fdm_filament_pla_silk", "fdm_filament_pp", "fdm_filament_ppa",
    "fdm_filament_pps", "fdm_filament_pva", "fdm_filament_sbs",
    "fdm_filament_tpu",
}

HEADER_KEYS = ("type", "name", "inherits", "from")
errors, warnings = [], []

def err(msg):
    errors.append(msg)

def warn(msg):
    warnings.append(msg)

def check_arrays(fname, data):
    for k, v in data.items():
        if k in ("type", "name", "inherits", "from", "setting_id",
                 "filament_id", "instantiation", "renamed_from",
                 "compatible_printers_condition", "is_custom_defined",
                 "version"):
            continue
        if not isinstance(v, list):
            err(f"{fname}: setting '{k}' is not an array: {v!r}")

# 1-3: file-level checks
names = set()
filament_ids = {}
setting_ids = {}
files = sorted(FILAMENT_DIR.glob("*.json"))
for f in files:
    try:
        data = json.loads(f.read_text())
    except json.JSONDecodeError as e:
        err(f"{f.name}: invalid JSON: {e}")
        continue
    check_arrays(f.name, data)
    for k in HEADER_KEYS:
        if k not in data:
            err(f"{f.name}: missing header key '{k}'")
    if data.get("type") != "filament":
        err(f"{f.name}: type is {data.get('type')!r}, expected 'filament'")
    name = data.get("name", "")
    if name != f.stem:
        err(f"{f.name}: name {name!r} != filename stem {f.stem!r}")
    names.add(name)
    if "filament_id" in data:
        fid = data["filament_id"]
        if fid in filament_ids:
            err(f"{f.name}: duplicate filament_id {fid} (also {filament_ids[fid]})")
        filament_ids[fid] = f.name
    if "setting_id" in data:
        sid = data["setting_id"]
        if sid in setting_ids:
            err(f"{f.name}: duplicate setting_id {sid} (also {setting_ids[sid]})")
        setting_ids[sid] = f.name
    inst = data.get("instantiation")
    if inst not in ("true", "false"):
        err(f"{f.name}: instantiation is {inst!r}, expected 'true'/'false'")

# 4: inheritance resolution
our_bases = {n for n in names if n.endswith("@base")}
for f in files:
    data = json.loads(f.read_text())
    inh = data.get("inherits", "")
    if inh and inh not in our_bases and inh not in ORCA_BASES:
        err(f"{f.name}: inherits unknown target {inh!r}")
    if inh in our_bases and inh != f"{data.get('name')} @base" and data.get("instantiation") == "true":
        # fine: @System -> its own @base; name check
        expected = f"{data.get('name')} @base"
        if data.get("name", "").endswith("@base") is False and not data.get("name", "").endswith("@System"):
            pass  # our System files are named without @System suffix; see README
    if data.get("instantiation") == "true":
        base_partner = f"{data.get('name')} @base"
        if base_partner not in names:
            err(f"{f.name}: instantiated profile has no @base partner {base_partner!r}")

# Naming note: inside OrcaFilamentLibrary, selectable profiles end in
# "@System" (e.g. "Generic PLA @System"). This bundle's selectable profiles
# use plain names instead; rename them to "... @System" if upstreaming.

# 5: id formats
for fid, fname in filament_ids.items():
    if not fid.startswith("PPF"):
        warn(f"{fname}: filament_id {fid} does not start with PPF")

# 6: vendor json parity
vendor_path = PROFILES / "Protopasta.json"
vendor = json.loads(vendor_path.read_text())
if vendor.get("name") != "Protopasta":
    err("Protopasta.json: vendor name mismatch")
listed = {e["name"] for e in vendor.get("filament_list", [])}
on_disk = {f.stem for f in files}
missing_files = listed - on_disk
unlisted = on_disk - listed
for n in missing_files:
    err(f"Protopasta.json lists {n!r} but no such file exists")
for n in unlisted:
    err(f"{n}.json exists but is not listed in Protopasta.json")
for e in vendor.get("filament_list", []):
    p = PROFILES / "Protopasta" / e["sub_path"]
    if not p.exists():
        err(f"filament_list sub_path does not exist: {e['sub_path']}")

print(f"Checked {len(files)} profile files + vendor index")

# 7: user presets
user_dir = REPO / "user_presets"
ufiles = sorted(user_dir.glob("*.json")) if user_dir.exists() else []
for f in ufiles:
    try:
        data = json.loads(f.read_text())
    except json.JSONDecodeError as e:
        err(f"{f.name}: invalid JSON: {e}")
        continue
    check_arrays(f.name, data)
    if data.get("from") != "User":
        err(f"{f.name}: user preset 'from' is {data.get('from')!r}, expected 'User'")
    if data.get("name") != f.stem:
        err(f"{f.name}: name {data.get('name')!r} != filename stem {f.stem!r}")
    if data.get("filament_settings_id") != [data.get("name")]:
        err(f"{f.name}: filament_settings_id mismatch")
    inh = data.get("inherits", "")
    GENERIC_SYSTEM = {
        "Generic PLA @System", "Generic PLA-CF @System",
        "Generic PETG @System", "Generic PETG-CF @System",
        "Generic PCTG @System", "Generic TPU @System",
    }
    if inh and inh not in GENERIC_SYSTEM:
        err(f"{f.name}: user preset inherits {inh!r}, expected one of {sorted(GENERIC_SYSTEM)}")
    if not data.get("filament_vendor"):
        err(f"{f.name}: missing filament_vendor")
print(f"Checked {len(ufiles)} user preset files")
for w in warnings:
    print(f"  WARN: {w}")
for e in errors:
    print(f"  ERROR: {e}")
if errors:
    sys.exit(f"\n{len(errors)} error(s)")
print("All checks passed.")
