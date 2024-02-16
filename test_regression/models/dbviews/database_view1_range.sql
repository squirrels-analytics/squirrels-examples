SELECT {{ctx["group_by_cols_select"] }}
    , 
    {%- if ctx["percent_toggle"] == "Count" %}
        SUM(is_fraud) as num_frauds
    {%- else %}
        AVG(is_fraud)*100 as percent_frauds
    {%- endif %}
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
GROUP BY {{ctx["group_by_cols"]}}
