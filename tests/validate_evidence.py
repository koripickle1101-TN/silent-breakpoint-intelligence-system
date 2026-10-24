import csv
from pathlib import Path

root = Path(__file__).resolve().parents[1]
with (root / "templates/breakpoint-log.csv").open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 3, f"Expected three synthetic cases, found {len(rows)}"
ids = [r["Simulated Case ID"] for r in rows]
assert ids == ["SB001", "SB002", "SB003"], ids
required = ["Simulated Workflow Area", "Observed Simulation Signal", "Root-Cause Hypothesis", "Simulated Owner or Queue", "Review Priority", "Status", "Follow-Up Date"]
for row in rows:
    assert all(row[k].strip() for k in required), row["Simulated Case ID"]
    assert row["Status"] in {"Open", "In Progress", "Closed"}
    assert row["Review Priority"] in {"Higher", "Moderate", "Lower"}
readme = (root / "README.md").read_text(encoding="utf-8")
dictionary = (root / "templates/kpi-dictionary.md").read_text(encoding="utf-8")
assert "student" in readme.lower() and "no-phi" in readme.lower()
assert "not industry benchmarks" in dictionary
print("PASS: SBI synthetic records, required fields, statuses, priority labels, and disclosure checks")
