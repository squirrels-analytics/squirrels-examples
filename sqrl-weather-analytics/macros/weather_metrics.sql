{%- macro get_metrics() -%}
    CAST(SUM(precipitation) AS DECIMAL(6, 1)) AS precipitation,
    CAST(MAX(temperature_max) AS DECIMAL(4, 1)) AS temperature_max,
    CAST(MIN(temperature_min) AS DECIMAL(4, 1)) AS temperature_min,
    CAST(AVG(wind) AS DECIMAL(6, 4)) AS wind
{%- endmacro -%}
