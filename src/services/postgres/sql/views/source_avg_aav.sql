-- View: source_avg_aav
-- Description: Média da coluna 'aav' por 'source' na tabela ai_news
-- Author: Antigravity (Requested by Hugo)

CREATE OR REPLACE VIEW source_avg_aav AS
SELECT 
    source, 
    AVG(aav) as avg_aav
FROM 
    ai_news
WHERE 
    aav IS NOT NULL
GROUP BY 
    source
ORDER BY 
    avg_aav DESC;
