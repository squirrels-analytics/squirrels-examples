WITH Grouped_Fraud_Count AS (
    SELECT first || ' ' || last as first_last_name, cc_num,
        {{ctx["group_by_cols_select"]}},
        SUM(is_fraud) as num_frauds
    FROM transactions
    WHERE 1=1
        {%- if ctx["has_job_subcategory"] %}
            AND job IN ({{ ctx["job_subcategory"] }})
        {%- endif %}
        AND date(trans_date_trans_time) >= date({{ ctx["start_date"] }})
        AND date(trans_date_trans_time) <= date({{ ctx["end_date"] }})
        AND cast(amt as numeric) >= {{ctx["min_amount"]}}
        AND cast(amt as numeric) <= {{ctx["max_amount"]}}
        {%- if ctx["has_gender"] %}
            and gender in ({{ctx["gender"]}})
        {%- endif %}
            AND date(dob) >= date({{ ctx["dob_start_date"] }})
            AND date(dob) <= date({{ ctx["dob_end_date"] }})
        AND category in ({{ctx["transaction_category"]}})
    GROUP BY first || ' ' || last, cc_num,{{ctx["group_by_cols"]}}
),
Ranked_Fraud AS (
    SELECT
        first_last_name, cc_num,
        num_frauds,
        {{ctx["order_by_cols"]}},
        ROW_NUMBER() OVER (
            PARTITION BY {{ctx["order_by_cols"]}}
            ORDER BY num_frauds DESC
        ) AS rn
    FROM
        Grouped_Fraud_Count
), 
user_info as (
    select DISTINCT first || ' ' || last as first_last_name, cc_num,
    street, zip, job
    FROM transactions
)
SELECT
    {{ctx["order_by_cols"]}},
    ui.first_last_name as max_fraud_name,
    ui.cc_num,
    ui.job,
    ui.street,
    num_frauds
FROM
    Ranked_Fraud rf
LEFT JOIN user_info ui ON
rf.first_last_name = ui.first_last_name
AND rf.cc_num = ui.cc_num
WHERE
    rn = 1


