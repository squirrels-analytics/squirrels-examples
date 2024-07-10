{%- import 'macros/common.j2' as c -%}
{%- import 'macros/transaction_features.j2' as tf -%}

SELECT {{ tf.full_name() }} as first_last_name, {{ c.cc_num_with_comma(ctx) }}
    {{ ctx.group_by_cols_select }},
    SUM(is_fraud) as num_frauds
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
    AND category in ({{ ctx.transaction_category }})
{% if is_placeholder("name_pattern") -%} AND {{ tf.full_name() }} LIKE :name_pattern {%- endif %}
GROUP BY {{ tf.full_name() }}, {{ c.cc_num_with_comma(ctx) }} {{ ctx.group_by_cols }}
