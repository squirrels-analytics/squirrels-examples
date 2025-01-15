SELECT
    date::STRING AS date,
    SUM(ice_cream_profits)::DECIMAL(10, 2) AS ice_cream_profits

FROM {{ source('src_ice_cream_profits') }}

WHERE date >= strptime(:start_date, '%Y-%m-%d')
    AND date <= strptime(:end_date, '%Y-%m-%d')

GROUP BY date

ORDER BY date
