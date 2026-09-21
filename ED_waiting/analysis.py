"""Recompute every figure in README.md from ed_visits.csv."""
import pandas as pd

TARGETS = {1: 1, 2: 10, 3: 30, 4: 60, 5: 120}  # ESI -> minutes

df = (pd.read_csv("ed_visits.csv")
        .rename(columns={"Emergency severity index (ESI)": "ESI",
                         "Waiting_Time_Minutes": "wait"}))
df["date"] = pd.to_datetime(df.Visit_Date, format="%d/%m/%Y")
df["ok"] = df.wait <= df.ESI.map(TARGETS)   # derived here, not trusted from file

# sanity: the file's own derived columns must agree with ours
assert (df.ok == df.within_target.astype(str).str.upper().eq("TRUE")).all()

print(f"n={len(df)}  compliance={df.ok.mean():.1%}  avg wait={df.wait.mean():.1f} min")

print("\nBy ESI:")
print(df.groupby("ESI").agg(n=("ok", "size"), compliance=("ok", "mean"),
                            avg=("wait", "mean"), median=("wait", "median")).round(3))

print("\nBy shift:")
print(df.groupby("Shift").agg(n=("ok", "size"), compliance=("ok", "mean")).round(3))

print("\nBreach rate, ESI x shift:")
print((1 - df.pivot_table(index="ESI", columns="Shift", values="ok"))
      .mul(100).round(1)[["Morning", "Afternoon", "Night"]])

print("\nBy weekday:")
print(df.groupby(df.date.dt.day_name()).ok.mean().mul(100).round(1))
