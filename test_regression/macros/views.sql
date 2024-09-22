{%- macro transactions_with_month() -%}

SELECT *,
    STRFTIME('%Y-%m', date(trans_date_trans_time)) AS month

FROM transactions

{%- endmacro -%}


{%- macro add_fraud_stats_to_cte(ref, ctx, most_fraud_cte) -%}

SELECT a.*, 
{%- if ctx.percent_toggle == "count" %}
    b.num_frauds as group_total_num_frauds
{%- else %}
    b.percent_frauds as group_avg_percent_frauds
{%- endif %}
FROM {{ most_fraud_cte }} a
    LEFT JOIN {{ ref("fraud_stats") }} b
    ON {{ ctx.join_cols }}
ORDER BY {{ ctx.group_by_cols }}

{%- endmacro -%}
