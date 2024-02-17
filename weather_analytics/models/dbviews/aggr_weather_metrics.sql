{%- from 'macros/weather_metrics.sql' import get_metrics -%}

SELECT {{ ctx['dim_col'] }}, {{ ctx['order_col'] }} as ordering
    {{ get_metrics() }}
FROM weather
GROUP BY {{ ctx['dim_col'] }}, {{ ctx['order_col'] }}
