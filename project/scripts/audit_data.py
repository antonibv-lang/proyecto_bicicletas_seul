"""Reproduce la inspección del CSV original de UCI, sin modificar sus datos."""
from pathlib import Path
from zipfile import ZipFile
import hashlib
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
archive = ROOT / "data/raw/seoul-bike-sharing-demand.zip"
csv_path = ROOT / "data/raw/SeoulBikeData.csv"
if not csv_path.exists():
    with ZipFile(archive) as z:
        member = next(n for n in z.namelist() if n.endswith("SeoulBikeData.csv"))
        csv_path.write_bytes(z.read(member))
raw = csv_path.read_bytes()
df = pd.read_csv(csv_path, encoding="cp1252")
dates = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="raise")
timestamp = dates + pd.to_timedelta(df["Hour"], unit="h")
expected = pd.date_range(timestamp.min(), timestamp.max(), freq="h")
operating = df["Functioning Day"].eq("Yes")
numeric = df.select_dtypes("number")
report = {
    "source": "https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand",
    "download_date": "2026-10-20",
    "sha256_csv": hashlib.sha256(raw).hexdigest(),
    "bytes_csv": len(raw),
    "rows": len(df),
    "columns": len(df.columns),
    "column_names": df.columns.tolist(),
    "start": str(timestamp.min()),
    "end": str(timestamp.max()),
    "months": int(dates.dt.to_period("M").nunique()),
    "null_cells": int(df.isna().sum().sum()),
    "duplicate_rows": int(df.duplicated().sum()),
    "duplicate_timestamps": int(timestamp.duplicated().sum()),
    "missing_hours": len(expected.difference(pd.DatetimeIndex(timestamp))),
    "categories": {
        c: {str(k): int(v) for k, v in df[c].value_counts().items()}
        for c in ["Seasons", "Holiday", "Functioning Day"]
    },
    "non_operating_hours": int((~operating).sum()),
    "non_operating_positive_rentals": int(
        ((~operating) & df["Rented Bike Count"].gt(0)).sum()
    ),
    "operating_zero_rentals": int(
        (operating & df["Rented Bike Count"].eq(0)).sum()
    ),
    "operating_hours": int(operating.sum()),
    "total_rentals": int(df["Rented Bike Count"].sum()),
    "numeric_ranges": {
        c: {"min": float(numeric[c].min()), "max": float(numeric[c].max())}
        for c in numeric.columns
    },
}
out = ROOT / "evidence/data-audit.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
