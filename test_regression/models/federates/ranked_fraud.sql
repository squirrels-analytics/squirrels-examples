{%- import 'macros/common.j2' as c -%}

SELECT
    first_last_name, {{ c.cc_num_with_comma(ctx) }}
    num_frauds,
    {{ ctx["order_by_cols"] }},
    ROW_NUMBER() OVER (
        PARTITION BY {{ ctx["order_by_cols"] }}
        ORDER BY num_frauds DESC
    ) AS rn
FROM {{ ref("grouped_fraud_count") }}
