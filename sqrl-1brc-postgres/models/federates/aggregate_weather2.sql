SELECT city, 
    MIN(min_temperature)::DECIMAL(4, 1) AS min_temperature, 
    MAX(max_temperature)::DECIMAL(4, 1) AS max_temperature, 
    (SUM(total_temperature) / SUM(total_records))::DECIMAL(4, 1) AS avg_temperature

FROM {{ ref("pre_aggr_weather") }} wd

WHERE recorded_date BETWEEN '2000-01-01' AND '2020-12-31'

GROUP BY city 

ORDER BY city
