SELECT city, 
    MIN(temperature)::DECIMAL(4, 1) AS min_temperature, 
    MAX(temperature)::DECIMAL(4, 1) AS max_temperature, 
    AVG(temperature)::DECIMAL(4, 1) AS avg_temperature,
    (1::int / 2::int) AS translate_test

FROM {{ source("src_weather_data") }} wd 

GROUP BY city 

ORDER BY city