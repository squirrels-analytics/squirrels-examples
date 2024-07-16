{%- from 'macros/weather_metrics.sql' import get_metrics -%}

WITH
weather_by_date_with_period_starts AS (
    
    SELECT *,
        DATE(year||'-01-01') AS start_of_year,
        DATE(year||'-01-01', '+'||((quarter_order-1)*3)||' month') AS start_of_quarter,
        DATE(year||'-01-01', '+'||(month_order-1)||' month') AS start_of_month,
        DATE(date, '-6 days', 'weekday 0') AS start_of_week
    
    FROM {{ ref("dbv_weather_by_date") }}
)
SELECT 
    '{{ ctx.period_type }}' AS period_type,
    {{ ctx.dim_col }} AS reference_date,
    {{ get_metrics() }}

FROM weather_by_date_with_period_starts

GROUP BY reference_date

ORDER BY reference_date
