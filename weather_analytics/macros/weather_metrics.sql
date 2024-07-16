{%- macro round(col_name) -%}
    ROUND({{ col_name }}, 2)
{%- endmacro -%}

{%- macro get_metrics() -%}
    {{ round("SUM(precipitation)") }} AS precipitation,
    {{ round("MAX(temperature_max)") }} AS temperature_max,
    {{ round("MIN(temperature_min)") }} AS temperature_min,
    {{ round("AVG(wind)") }} AS wind
{%- endmacro -%}
