# What is a data warehouse?

- Data warehouse
- database maintained separately from the organization's operational database(s) for consolidated, historical data analysis and decision making
- Data warehouse composition:
- dimension tables: such as item, supplier, location or time
- fact table: contains measures and keys to each related dimension table
- Why a separate data warehouse?
- databases: tuned for OLTP (access methods, indexing, concurrency, recovery)
- warehouses: tuned for OLAP (complex queries, consolidation)
- missing data: operational DBs do not typically maintain all historical data
- data consolidation: aggregation, summarization of heterogeneous data
- data quality: reconciliation of sources with inconsistent data representations, codes, formats

TÉCNICO+ FORMACÃO AVANÇADA