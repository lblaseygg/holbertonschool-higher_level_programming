-- Lists all tables in the database hbtn_0d_tvshows
-- Each query should have a comment above it
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'hbtn_0d_tvshows'; 