# Spotlight Service

**Renumics Spotlight** service for interactive data exploration and visualization of the AI News dataset.

## Features

- 📊 **Interactive Dataframe**: Filter, sort, and inspect gathered news.
- 📉 **Embeddings Visualization**: (Planned) Visualize semantic clusters using UMAP/t-SNE.
- 🎨 **Data Inspection**: View raw text, tags, and metadata.

## Usage

### Start Service

```bash
./src/services/spotlight/start.sh
```

Or manually:

```bash
uv run python src/services/spotlight/viewer.py
```

Access the dashboard at **http://localhost:7000**.

## Configuration

The service loads data from `data/bronze/ai_news.parquet` by default.

Environment Variables:
- `SPOTLIGHT_PORT`: Port to run the service on (default: 7000)

## Integration

Use this service to:
1. Validate data ingestion quality.
2. Explore potential clusters before creating automated pipelines.
3. Debug embedding semantic relationships.
