{{- config(connection_name="duckdb") -}}

SELECT
    CAST(date AS VARCHAR) AS date,
    ROUND(SUM(ice_cream_profits), 2) AS ice_cream_profits

FROM ice_cream_profits

WHERE date >= strptime($start_date , '%Y-%m-%d')
    AND date <= strptime($end_date , '%Y-%m-%d')

GROUP BY date

ORDER BY date
