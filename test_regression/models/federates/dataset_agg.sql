SELECT *
FROM {{ ref("fraud_stats") }}
ORDER BY {{ ctx.order_by_cols }}
