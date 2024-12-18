SELECT city, 
    MIN(temperature) AS min_temperature, 
    MAX(temperature) AS max_temperature, 
    AVG(temperature) AS avg_temperature,
    (1::int / 2::int) AS translate_test

FROM {{ source("src_weather_data") }}

GROUP BY city 

ORDER BY city