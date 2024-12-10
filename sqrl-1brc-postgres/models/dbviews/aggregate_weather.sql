SELECT city, 
    min(temperature) as min_temperature, 
    max(temperature) as max_temperature, 
    avg(temperature) as avg_temperature 

FROM {{ source("src_weather_data") }} wd 

GROUP BY city 

ORDER BY city