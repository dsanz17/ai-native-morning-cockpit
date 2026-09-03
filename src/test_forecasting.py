from src.data_generator import generate_bank_history
from src.metrics import calculate_metrics
from src.forecasting import forecast_metric


history = calculate_metrics(
    generate_bank_history(months=48, seed=20260826)
)

forecast = forecast_metric(
    history=history,
    metric="cet1_ratio_pct",
    horizon_months=12,
    lookback_months=24,
    confidence_level=0.95,
)

print("Columns created:")
print(forecast.columns.tolist())

print("\nLast 5 forecast rows:")
print(forecast.tail(5).round(3))