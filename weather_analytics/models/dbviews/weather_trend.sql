{%- from 'macros/weather_metrics.sql' import get_metrics -%}

SELECT {{ ctx['dim_col'] }} as {{ ctx['alias'] }}
    {{ get_metrics() }}
FROM weather
{%- if ctx['has_time_periods'] %}
WHERE {{ ctx['filter_by_col'] }} IN ({{ ctx['selected_time_periods'] }})
{%- endif %}
GROUP BY {{ ctx['dim_col'] }}
ORDER BY {{ ctx['dim_col'] }}
