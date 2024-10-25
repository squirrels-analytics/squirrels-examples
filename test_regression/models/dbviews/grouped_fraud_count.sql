WITH
transactions_with_month AS (
    {{ transactions_with_month() | indent(4) }}
)
SELECT {{ full_name() }} as first_last_name, {{ cc_num_with_comma(ctx) }}
    {{ ctx.group_by_cols }},
    SUM(is_fraud) as num_frauds
FROM transactions_with_month
WHERE true
{%- if ctx.has_job_subcategory %}
    AND job IN ({{ ctx.job_subcategory }})
{%- endif %}
    AND date(trans_date_trans_time) >= date(:start_date)
    AND date(trans_date_trans_time) <= date(:end_date)
    AND cast(amt as numeric) >= {{ ctx.min_amount }}
    AND cast(amt as numeric) <= {{ ctx.max_amount }}
{%- if ctx.has_gender %}
    AND gender in ({{ ctx.gender }})
{%- endif %}
    AND date(dob) >= date({{ ctx.dob_start_date }})
    AND date(dob) <= date({{ ctx.dob_end_date }})
    AND category in ({{ ctx.transaction_category }})
{% if is_placeholder("name_pattern") -%} AND {{ full_name() }} LIKE :name_pattern {%- endif %}
GROUP BY {{ full_name() }}, {{ cc_num_with_comma(ctx) }} {{ ctx.group_by_cols }}
