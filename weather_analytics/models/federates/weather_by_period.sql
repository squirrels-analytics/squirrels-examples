{%- from 'macros/weather_metrics.sql' import get_metrics -%}

SELECT 
    '{{ ctx.dim_col }}' AS dimension_type, 
    {{ ctx.dim_col }} AS dimension_value,
    {{ get_metrics() }}

FROM {{ ref("dbv_weather_by_date") }} AS a

{%- if ctx.dim_col == "month_name" %}
    LEFT JOIN {{ ref("seed_month_names") }} AS b USING (month_order)
{%- endif %}

GROUP BY dimension_value

ORDER BY a.{{ ctx.order_col }}
