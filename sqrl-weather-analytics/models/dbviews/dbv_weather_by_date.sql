WITH
aliased AS (

    SELECT *,
        temp_max AS temperature_max,
        temp_min AS temperature_min

    FROM {{ source('src_weather') }}

),
aggregated AS (

    SELECT
        date,
        {{ get_metrics() | indent(4) }},
        CAST(condition AS VARCHAR) AS condition,
        CAST(STRFTIME('%Y', date) AS INT) AS year,
        CAST(STRFTIME('%m', date) AS INT) AS month_order, 
        CAST(STRFTIME('%j', date) AS INT) AS day_of_year
    
    FROM aliased
    
    GROUP BY date, condition

)

SELECT *,
    'Q' || CAST(FLOOR((month_order - 1) / 3 + 1) AS INT) AS quarter

FROM aggregated

{%- if is_placeholder("start_date") %}

WHERE date >= :start_date 
    AND date <= :end_date

{%- endif %}