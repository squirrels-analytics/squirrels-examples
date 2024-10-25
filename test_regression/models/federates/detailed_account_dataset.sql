WITH
most_fraudulent AS (
    SELECT
        {{ ctx.group_by_cols }},
        ui.first_last_name as max_fraud_name,
        ui.cc_num,
        ui.job,
        ui.street,
        num_frauds
    FROM {{ ref("ranked_fraud") }} rf
        LEFT JOIN {{ ref("customer_info") }} ui 
        ON rf.first_last_name = ui.first_last_name AND rf.cc_num = ui.cc_num
    WHERE
        rn = 1
),
result AS (
    {{ add_fraud_stats_to_cte(ref, ctx, "most_fraudulent") | indent(4) }}
)
SELECT * FROM result
