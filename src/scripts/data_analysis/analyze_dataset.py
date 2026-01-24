"""
Dataset Analysis Script
=======================

Comprehensive analysis of the AI News dataset stored in PostgreSQL.
Combines structural, categorical, temporal, and textual analysis.

Usage:
    uv run python src/scripts/data_analysis/analyze_dataset.py
"""

import sys
import os
import numpy as np
import pandas as pd
from scipy import stats
from tabulate import tabulate

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.modules.database import get_datascience_db

# Configuration
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", 100)
pd.set_option("display.width", 1000)

def print_header(title):
    print(f"\n{'='*80}")
    print(f" {title.upper()}")
    print(f"{'='*80}")

def analyze_structure(df):
    print_header("1. Structural Overview")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]}")
    print("\nColumn Types & Nulls:")
    
    info_data = []
    for col in df.columns:
        non_null = df[col].count()
        nulls = df[col].isnull().sum()
        pct_null = (nulls / len(df)) * 100
        dtype = str(df[col].dtype)
        info_data.append([col, dtype, non_null, nulls, f"{pct_null:.1f}%"])
        
    print(tabulate(info_data, headers=["Column", "Type", "Non-Null", "Nulls", "% Null"], tablefmt="simple"))

def analyze_categorical(df, cols):
    print_header("2. Categorical Analysis")
    for col in cols:
        if col not in df.columns: continue
        
        print(f"\n📌 {col.upper()}")
        print("-" * 40)
        print(f"Unique Values: {df[col].nunique()}")
        
        # Entropy & Diversity
        counts = df[col].value_counts()
        probs = counts / len(df)
        entropy = -np.sum(probs * np.log2(probs + 1e-10))
        max_entropy = np.log2(df[col].nunique()) if df[col].nunique() > 1 else 1
        metric_normalized = entropy / max_entropy
        
        print(f"Normalized Entropy: {metric_normalized:.4f} (1.0 = Max Diversity)")
        
        print("\nTop 10 Values:")
        top10 = counts.head(10).reset_index()
        top10.columns = [col, "Count"]
        top10["%"] = (top10["Count"] / len(df) * 100).round(1)
        print(tabulate(top10, headers="keys", tablefmt="simple"))

def analyze_temporal(df, date_col='pubdate'):
    print_header("3. Temporal Analysis")
    if date_col not in df.columns:
        print(f"Date column '{date_col}' not found.")
        return

    # Ensure datetime
    if not np.issubdtype(df[date_col].dtype, np.datetime64):
         df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

    valid_dates = df[date_col].dropna()
    print(f"Date Range: {valid_dates.min()} to {valid_dates.max()}")
    print(f"Total Days: {(valid_dates.max() - valid_dates.min()).days}")
    
    df['year'] = valid_dates.dt.year
    print("\nDistribution by Year:")
    print(df['year'].value_counts().sort_index())

def analyze_text(df, text_cols):
    print_header("4. Text Analysis")
    for col in text_cols:
        if col not in df.columns: continue
        
        lengths = df[col].dropna().astype(str).str.len()
        print(f"\n📝 {col.upper()} Length Stats:")
        print(lengths.describe().to_frame().T)

def main():
    print("🚀 Connecting to Database...")
    try:
        with get_datascience_db() as db:
            print("📦 Fetching 'ai_news' table...")
            df = db.read_sql("SELECT * FROM ai_news")
    except Exception as e:
        print(f"❌ Database Connection Failed: {e}")
        print("💡 Hint: Run 'src/services/postgres/postgres-status.sh' to check connectivity/tunnel.")
        return

    # Run Sub-Analyses
    analyze_structure(df)
    
    # Categorical
    cat_cols = ['topic', 'tag', 'ambito', 'source', 'category']
    # Normalize col names to lower case for check if needed, but db columns usually lower in postgres unless quoted
    analyze_categorical(df, cat_cols)
    
    # Temporal
    # Check for likely date columns
    date_cols = [c for c in df.columns if 'date' in c.lower()]
    if date_cols:
        analyze_temporal(df, date_cols[0])
    elif 'pubdate' in df.columns:
         analyze_temporal(df, 'pubdate')

    # Text
    analyze_text(df, ['title', 'description'])
    
    print_header("✅ Analysis Complete")

if __name__ == "__main__":
    main()
