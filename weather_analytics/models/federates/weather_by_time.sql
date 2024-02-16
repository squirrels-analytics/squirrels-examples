SELECT {{ ctx['dim_col'] }}
    , temperature_high_C
    , temperature_low_C
    , precipitation_inches
    , wind_mph
FROM {{ ref("aggr_weather_metrics") }}
ORDER BY ordering
