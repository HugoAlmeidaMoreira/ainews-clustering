-- View: source_stats
-- Aggregates AAV stats per source

DROP VIEW IF EXISTS source_stats;

CREATE VIEW source_stats AS
SELECT 
    source,
    COUNT(*) as article_count,
    ROUND(AVG(aav)::numeric, 2) as avg_aav,
    ROUND(SUM(aav)::numeric, 2) as total_aav_value,
    MIN(pubdate) as first_seen,
    MAX(pubdate) as last_seen
FROM ai_news
GROUP BY source
ORDER BY avg_aav DESC;
