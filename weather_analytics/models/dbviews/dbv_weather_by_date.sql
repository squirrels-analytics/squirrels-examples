{%- from 'macros/weather_metrics.sql' import get_metrics -%}

WITH
aliased AS (

    SELECT *,
        temp_max AS temperature_max,
        temp_min AS temperature_min

    FROM weather
),
aggregated AS (

    SELECT
        CAST(date AS VARCHAR) AS date,
        {{ get_metrics() | indent(4) }},
        CAST(condition AS VARCHAR) AS condition,
        CAST(STRFTIME('%Y', date) AS INT) AS year,
        CAST(STRFTIME('%m', date) AS INT) AS month_order, 
        CAST(STRFTIME('%j', date) AS INT) AS day_of_year
    
    FROM aliased
    
    GROUP BY date
),
weather_by_date_with_quarter AS (

    SELECT *,
        (month_order - 1) / 3 + 1 AS quarter_order
    
    FROM aggregated
)
SELECT *,
    'Q' || quarter_order AS quarter

FROM weather_by_date_with_quarter

{%- if is_placeholder("start_date") %}

WHERE date >= :start_date 
    AND date <= :end_date

{%- endif %}