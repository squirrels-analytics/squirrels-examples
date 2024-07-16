{{- config(connection_name="duckdb") -}}

SELECT
    CAST(date AS VARCHAR) AS date,
    ROUND(SUM(ice_cream_profits), 2) AS ice_cream_profits

FROM ice_cream_profits

WHERE date >= $start_date 
    AND date <= $end_date

GROUP BY date

ORDER BY date
