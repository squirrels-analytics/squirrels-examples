WITH Grouped_Fraud_Count AS (
    SELECT first || ' ' || last as first_last_name,
        {{ctx["group_by_cols_select"]}},
        SUM(is_fraud) as num_frauds
    FROM transactions
    WHERE 1=1
        {%- if ctx["has_job_subcategories"] %}
            AND job IN ({{ ctx["job_subcategories"] }})
        {%- endif %}
        AND date(trans_date_trans_time) >= date({{ ctx["range_start_date"] }})
        AND date(trans_date_trans_time) <= date({{ ctx["range_end_date"] }})
        AND cast(amt as numeric) >= {{ctx["min_amount"]}}
        AND cast(amt as numeric) <= {{ctx["max_amount"]}}
        {%- if ctx["has_gender"] %}
            and gender in ({{ctx["gender"]}})
        {%- endif %}
            AND date(dob) >= date({{ ctx["dob_start_date"] }})
            AND date(dob) <= date({{ ctx["dob_end_date"] }})
        AND category in ({{ctx["transaction_category"]}})
    GROUP BY first || ' ' || last, {{ctx["group_by_cols"]}}
),
Ranked_Fraud AS (
    SELECT
        first_last_name,
            num_frauds,
        {{ctx["order_by_cols"]}},
        ROW_NUMBER() OVER (
            PARTITION BY {{ctx["order_by_cols"]}}
            ORDER BY num_frauds DESC
        ) AS rn
    FROM
        Grouped_Fraud_Count
)
SELECT
    {{ctx["order_by_cols"]}},
    first_last_name as most_fraud_individual,
    num_frauds as individual_num_fraud
FROM
    Ranked_Fraud
WHERE
    rn = 1


