-- Drop useless columns identified in data analysis
-- enclosure: 100% NULL
-- category: 100% 'Web'

ALTER TABLE ai_news DROP COLUMN IF EXISTS enclosure;
ALTER TABLE ai_news DROP COLUMN IF EXISTS category;
