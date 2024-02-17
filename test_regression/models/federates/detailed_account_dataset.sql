{%- import 'macros/views.j2' as v -%}

WITH
most_fraudulent AS (
    SELECT
        {{ ctx["order_by_cols"] }},
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
    {{ v.add_fraud_stats_to_cte(ref, ctx, "most_fraudulent") }}
)
SELECT * FROM result
