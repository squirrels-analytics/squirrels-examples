{%- macro get_metrics() -%}
    , avg(temp_max) as temperature_high_C
    , avg(temp_min) as temperature_low_C
    , avg(precipitation) as precipitation_inches
    , avg(wind) as wind_mph
{%- endmacro -%}