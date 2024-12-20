SELECT city, recorded_date,
    MIN(temperature) AS min_temperature, 
    MAX(temperature) AS max_temperature, 
    SUM(temperature) AS total_temperature,
    COUNT(*) AS total_records

FROM {{ ref("src_weather_data") }} wd 

GROUP BY city, recorded_date 

ORDER BY recorded_date
