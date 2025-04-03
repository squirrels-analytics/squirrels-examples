WITH
weather_by_date_with_period_starts AS (
    
    SELECT *,
        DATE_TRUNC('year', "date"::DATE) AS start_of_year,
        DATE_TRUNC('quarter', "date"::DATE) AS start_of_quarter,
        DATE_TRUNC('month', "date"::DATE) AS start_of_month,
        DATE_TRUNC('week', "date"::DATE) AS start_of_week
    
    FROM {{ ref("dbv_weather_by_date") }}
)
SELECT 
    '{{ ctx.trend_period_type }}' AS period_type,
    {{ ctx.trend_dim_col }} AS reference_date,
    {{ get_metrics() }}

FROM weather_by_date_with_period_starts

GROUP BY {{ ctx.trend_dim_col }}

ORDER BY {{ ctx.trend_dim_col }}
