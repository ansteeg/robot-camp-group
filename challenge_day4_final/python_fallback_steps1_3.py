import json
import csv
from pathlib import Path
from statistics import median

PROJECT_ROOT = Path(__file__).parent


def read_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def step1_fill_missing_means(data1_path: Path, data2_path: Path) -> None:
    data = read_json(data1_path)
    people = list(data.get("people", []))

    skill_keys = [
        "Technical Skills",
        "Soft Skills",
        "Business Skills",
        "Creative Skills",
        "Academic Skills",
    ]

    # Compute column means ignoring None
    means = {}
    for key in skill_keys:
        vals = [p.get(key) for p in people if isinstance(p.get(key), (int, float))]
        means[key] = (sum(vals) / len(vals)) if vals else 0.0

    # Replace missing with mean
    for p in people:
        for key in skill_keys:
            v = p.get(key)
            if not isinstance(v, (int, float)):
                p[key] = means[key]

    data["people"] = people
    write_json(data2_path, data)


def step2_json_to_csv(data2_path: Path, data3_path: Path) -> None:
    data = read_json(data2_path)
    people = list(data.get("people", []))

    headers = [
        "Name",
        "Technical Skills",
        "Soft Skills",
        "Business Skills",
        "Creative Skills",
        "Academic Skills",
    ]

    with data3_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for p in people:
            writer.writerow([
                p.get("name", ""),
                p.get("Technical Skills", 0),
                p.get("Soft Skills", 0),
                p.get("Business Skills", 0),
                p.get("Creative Skills", 0),
                p.get("Academic Skills", 0),
            ])


def quartiles(values):
    if not values:
        return (0.0, 0.0, 0.0)
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    q2 = median(sorted_vals)
    mid = n // 2
    lower = sorted_vals[:mid]
    upper = sorted_vals[-mid:] if n % 2 == 0 else sorted_vals[mid+1:]
    q1 = median(lower) if lower else sorted_vals[0]
    q3 = median(upper) if upper else sorted_vals[-1]
    return (q1, q2, q3)


def classify(value: float, q1: float, q2: float, q3: float) -> str:
    if value <= q1:
        return "low"
    elif value <= q2:
        return "middle"
    elif value <= q3:
        return "good"
    else:
        return "super"


def step3_csv_to_categories(data3_path: Path, data4_path: Path) -> None:
    # Read CSV rows
    with data3_path.open("r", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    header = rows[0]
    data_rows = rows[1:]

    # Transpose numeric columns 1..5 to compute quartiles
    numeric_cols = list(zip(*data_rows))[1:6] if data_rows else [[]] * 5
    numeric_cols_float = []
    for col in numeric_cols:
        col_vals = []
        for v in col:
            try:
                col_vals.append(float(v))
            except Exception:
                pass
        numeric_cols_float.append(col_vals)

    q = [quartiles(col) for col in numeric_cols_float]

    # Map each numeric to category
    out_rows = [header]
    for row in data_rows:
        out = row[:]
        for i in range(1, 6):
            try:
                val = float(row[i])
            except Exception:
                # default category if non-numeric
                out[i] = "low"
                continue
            q1, q2, q3 = q[i - 1]
            out[i] = classify(val, q1, q2, q3)
        out_rows.append(out)

    # Write to TXT with comma-separated values
    with data4_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(out_rows)


def main():
    # Resolve paths
    data1 = PROJECT_ROOT / "fulldata" / "data1.json"
    # Copy into working name expected by subsequent steps
    working_data1 = PROJECT_ROOT / "data1.json"
    if data1.exists():
        working_data1.write_text(data1.read_text(encoding="utf-8"), encoding="utf-8")

    data2 = PROJECT_ROOT / "data2.json"
    data3 = PROJECT_ROOT / "data3.csv"
    data4 = PROJECT_ROOT / "data4.txt"

    step1_fill_missing_means(working_data1, data2)
    step2_json_to_csv(data2, data3)
    step3_csv_to_categories(data3, data4)


if __name__ == "__main__":
    main()


