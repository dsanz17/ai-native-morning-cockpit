from src.data_generator import generate_bank_history
from src.metrics import calculate_metrics
from src.scenarios import run_scenario


history = generate_bank_history(months=48, seed=20260826)
metrics = calculate_metrics(history)

print("\n--- BASELINE: LATEST MONTH ---")
print(metrics.iloc[-1][
        [
            "cet1_ratio_pct",
            "tier1_ratio_pct",
            "total_capital_ratio_pct",
            "lcr_pct",
            "nim_pct",
            "cost_to_income_pct",
            "loan_growth_yoy_pct",
            "deposit_growth_yoy_pct",
            "stage_3_ratio_pct",
            "rwa_density_pct",
        ]
    ].round(2)
)

scenario = run_scenario(
    history=history,
    rate_shock_bps=-50,
    deposit_outflow_pct=8,
    stage_2_increase_pct_points=2.0,
    stage_3_increase_pct_points=0.5,
)

print("\n--- STRESS TEST: -50 BPS, 8% DEPOSIT OUTFLOW ---")
print(
    scenario[
        [
            "cet1_ratio_pct",
            "lcr_pct",
            "nim_pct",
            "stage_3_ratio_pct",
            "provisions",
            "rwa",
        ]
    ].round(2)
)