-- Prerequisite
CREATE EXTENSION vector;

-- SHOW the current database
SELECT current_database();

-- SHOW all the tables in the database
SELECT table_name
FROM postgres.information_schema.tables
WHERE table_schema = 'public';

-- SHOW all the collections
SELECT * FROM langchain_pg_collection;

-- SHOW all the embeddings (Before adding the vectors)
SELECT * FROM langchain_pg_embedding;

-- SHOW all the embeddings (After adding the vectors)
SELECT langchain_pg_embedding.collection_id,
       langchain_pg_embedding.embedding,
       langchain_pg_embedding.document
FROM langchain_pg_embedding;


-- [CLEAN UP] Dropping the tables
DROP TABLE langchain_pg_embedding;
DROP TABLE langchain_pg_collection;



