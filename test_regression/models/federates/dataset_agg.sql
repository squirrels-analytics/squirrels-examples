SELECT *
FROM {{ ref("fraud_stats") }}
ORDER BY {{ ctx.group_by_cols }}
