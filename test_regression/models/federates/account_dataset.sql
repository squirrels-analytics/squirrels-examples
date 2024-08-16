{%- import 'macros/views.j2' as v -%}

WITH
most_fraudulent AS (
    SELECT
        {{ ctx.group_by_cols }},
        first_last_name as most_fraud_individual,
        num_frauds as individual_num_fraud
    FROM
        {{ ref("ranked_fraud") }}
    WHERE
        rn = 1
),
result AS (
    {{ v.add_fraud_stats_to_cte(ref, ctx, "most_fraudulent") | indent(4) }}
)
SELECT * FROM result
