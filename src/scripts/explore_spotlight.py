"""
Explore AI News dataset with Renumics Spotlight.

Usage:
    uv run python src/scripts/explore_spotlight.py
"""

import pandas as pd
from renumics import spotlight

# Load the dataset
df = pd.read_parquet("data/bronze/ai_news.parquet")

print(f"Dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# Launch Spotlight viewer
# This will open a browser window with the interactive visualization
spotlight.show(df)
