{%- import 'macros/transaction_features.j2' as tf -%}

SELECT {{ ctx.group_by_cols_select }},
{%- if ctx.percent_toggle == "Count" %}
    SUM(is_fraud) as num_frauds
{%- else %}
    AVG(is_fraud)*100 as percent_frauds
{%- endif %}
FROM transactions
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
{% if is_placeholder("name_pattern") -%} AND {{ tf.full_name() }} LIKE :name_pattern {%- endif %}
GROUP BY {{ ctx.group_by_cols }}
