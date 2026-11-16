
import os
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# ==========================================
# QUANTUM RANDOM NUMBER GENERATOR
# Stage 7: Comparative Analysis Dashboard
# ==========================================

# Step 1: Load datasets
raw_df = pd.read_csv("data/quantum_random_bits.csv")
deb_df = pd.read_csv("data/debiased_random_bits.csv")
nist_df = pd.read_csv("results/nist_test_results.csv")

raw_bits = raw_df["Random_Bit"].tolist()
deb_bits = deb_df["Debiased_Bit"].tolist()

# Step 2: Calculate statistics
raw_total = len(raw_bits)
deb_total = len(deb_bits)

raw_zeros = raw_bits.count(0)
raw_ones = raw_bits.count(1)

deb_zeros = deb_bits.count(0)
deb_ones = deb_bits.count(1)

raw_zero_pct = raw_zeros / raw_total * 100
raw_one_pct = raw_ones / raw_total * 100

deb_zero_pct = deb_zeros / deb_total * 100 if deb_total else 0
deb_one_pct = deb_ones / deb_total * 100 if deb_total else 0

retained_pairs = len(deb_bits)
total_pairs = raw_total // 2

efficiency = (
    retained_pairs / total_pairs * 100
    if total_pairs else 0
)

# Step 3: NIST summary
passed = (nist_df["Status"] == "PASS").sum()
failed = (nist_df["Status"] == "FAIL").sum()
not_applicable = (nist_df["Status"] == "NOT APPLICABLE").sum()

# Step 4: Create output directory
os.makedirs("results", exist_ok=True)

# ==========================================
# GRAPH 1: RAW VS DEBIASED DISTRIBUTION
# ==========================================

fig1 = go.Figure()

fig1.add_trace(go.Bar(
    name="Zeros",
    x=["Raw Data", "Debiased Data"],
    y=[raw_zeros, deb_zeros]
))

fig1.add_trace(go.Bar(
    name="Ones",
    x=["Raw Data", "Debiased Data"],
    y=[raw_ones, deb_ones]
))

fig1.update_layout(
    title="Raw vs Debiased Bit Distribution",
    xaxis_title="Dataset",
    yaxis_title="Number of Bits",
    barmode="group",
    template="plotly_dark"
)

# ==========================================
# GRAPH 2: NIST P-VALUE COMPARISON
# ==========================================

fig2 = go.Figure()

for dataset in nist_df["Dataset"].unique():

    subset = nist_df[nist_df["Dataset"] == dataset]

    fig2.add_trace(go.Bar(
        name=dataset,
        x=subset["Test"],
        y=subset["P_Value"],
        text=subset["Status"],
        textposition="outside"
    ))

fig2.add_hline(
    y=0.01,
    line_dash="dash",
    annotation_text="Significance threshold = 0.01"
)

fig2.update_layout(
    title="NIST Statistical Test P-Value Comparison",
    xaxis_title="Statistical Test",
    yaxis_title="P-Value",
    barmode="group",
    template="plotly_dark",
    yaxis_range=[0, 1]
)

# ==========================================
# GRAPH 3: CUMULATIVE PROBABILITY
# ==========================================

raw_series = pd.Series(raw_bits).expanding().mean()
deb_series = pd.Series(deb_bits).expanding().mean()

fig3 = go.Figure()

fig3.add_trace(go.Scatter(
    y=raw_series,
    mode="lines",
    name="Raw Data"
))

fig3.add_trace(go.Scatter(
    y=deb_series,
    mode="lines",
    name="Debiased Data"
))

fig3.add_hline(
    y=0.5,
    line_dash="dash",
    annotation_text="Expected probability = 0.5"
)

fig3.update_layout(
    title="Cumulative Probability of Bit 1",
    xaxis_title="Measurement Index",
    yaxis_title="Cumulative Probability",
    template="plotly_dark",
    yaxis_range=[0, 1]
)

# ==========================================
# GRAPH 4: NIST PASS / FAIL SUMMARY
# ==========================================

fig4 = go.Figure(data=[go.Pie(
    labels=["Pass", "Fail", "Not Applicable"],
    values=[passed, failed, not_applicable],
    hole=0.55
)])

fig4.update_layout(
    title="Statistical Test Summary",
    template="plotly_dark"
)

# ==========================================
# CREATE HTML DASHBOARD
# ==========================================

charts = [fig1, fig2, fig3, fig4]

chart_html = ""

for index, figure in enumerate(charts):

    chart_html += figure.to_html(
        full_html=False,
        include_plotlyjs="cdn" if index == 0 else False
    )

# Dashboard HTML
html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Quantum Random Number Generator Dashboard</title>

    <style>
        body {{
            background: #101827;
            color: white;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 25px;
        }}

        h1 {{
            text-align: center;
            color: #60a5fa;
        }}

        .subtitle {{
            text-align: center;
            color: #aab5c5;
        }}

        .cards {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 18px;
            margin: 30px 0;
        }}

        .card {{
            background: #1e293b;
            padding: 22px;
            border-radius: 12px;
            text-align: center;
        }}

        .value {{
            font-size: 30px;
            color: #60a5fa;
            font-weight: bold;
        }}

        .chart {{
            background: #1e293b;
            border-radius: 12px;
            padding: 10px;
            margin-bottom: 25px;
        }}

        .downloads {{
            text-align: center;
            margin: 30px;
        }}

        a {{
            color: #60a5fa;
            margin: 10px;
        }}

        footer {{
            text-align: center;
            color: #94a3b8;
            margin-top: 35px;
        }}
    </style>
</head>

<body>

<h1>Quantum Random Number Generator</h1>

<p class="subtitle">
Quantum Randomness Analysis and Statistical Evaluation
</p>

<div class="cards">

    <div class="card">
        <h3>Total Raw Bits</h3>
        <div class="value">{raw_total:,}</div>
    </div>

    <div class="card">
        <h3>Debiased Bits</h3>
        <div class="value">{deb_total:,}</div>
    </div>

    <div class="card">
        <h3>Debiasing Efficiency</h3>
        <div class="value">{efficiency:.2f}%</div>
    </div>

    <div class="card">
        <h3>NIST Tests Passed</h3>
        <div class="value">{passed}/{len(nist_df)}</div>
    </div>

</div>

<div class="chart">{chart_html}</div>

<div class="downloads">
    <h2>Download Project Datasets</h2>

    <a href="../data/quantum_random_bits.csv" download>
        Download Raw Bits
    </a>

    <a href="../data/debiased_random_bits.csv" download>
        Download Debiased Bits
    </a>

    <a href="nist_test_results.csv" download>
        Download NIST Results
    </a>
</div>

<footer>
Quantum Random Number Generator | Academic Project
<br>
Statistical evaluation at significance level 0.01
</footer>

</body>
</html>
"""

# Step 5: Save dashboard
output_path = "results/dashboard.html"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(html)

print("\n====================================")
print("DASHBOARD GENERATED SUCCESSFULLY")
print("====================================")

print("Raw bits:", raw_total)
print("Debiased bits:", deb_total)
print("Debiasing efficiency:", round(efficiency, 2), "%")
print("NIST tests passed:", passed)

print("\nDashboard location:", output_path)
