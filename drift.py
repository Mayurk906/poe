import os
import numpy as np
import pandas as pd

np.random.seed(42)

# Reference data (training-time distribution)
reference = pd.DataFrame({
    "age": np.random.normal(35, 5, 500),
    "income": np.random.normal(50000, 8000, 500),
    "score": np.random.uniform(0, 1, 500),
})

# Current data (production) - drift injected in age and income
current = pd.DataFrame({
    "age": np.random.normal(45, 5, 500),
    "income": np.random.normal(60000, 8000, 500),
    "score": np.random.uniform(0, 1, 500),
})

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "drift_report.html")

try:  # Evidently 0.7+ (new API)
    from evidently import Report
    from evidently.presets import DataDriftPreset
    report = Report([DataDriftPreset()])
    result = report.run(reference_data=reference, current_data=current)
    result.save_html(out_path)
except ImportError:  # Evidently 0.4-0.6 (old API)
    from evidently.report import Report
    from evidently.metric_preset import DataDriftPreset
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference, current_data=current)
    report.save_html(out_path)

print("Drift report saved:", out_path)