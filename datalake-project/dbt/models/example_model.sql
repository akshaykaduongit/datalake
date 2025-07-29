-- SQL model for DBT that transforms data from a source table into a target table

{{ config(
    materialized='table',
    schema='your_schema_name',  -- replace with your schema name
    alias='example_model'
) }}

WITH source_data AS (
    SELECT
        id,
        name,
        created_at,
        updated_at
    FROM {{ ref('source_table') }}  -- replace with your source table name
)

SELECT
    id,
    name,
    created_at,
    updated_at,
    CURRENT_TIMESTAMP() AS processed_at
FROM source_data
WHERE created_at >= '2023-01-01'  -- example filter condition
ORDER BY created_at;