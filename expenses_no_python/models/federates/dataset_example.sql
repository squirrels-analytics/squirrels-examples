SELECT *
FROM {{ ref("database_view1") }}
ORDER BY date
