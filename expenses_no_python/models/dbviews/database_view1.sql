{%- macro zip_with_as_and_join(array1, array2) -%}
    {%- for x in array1 %}
    {{ x }} as {{ array2[loop.index0] }},
    {%- endfor -%}
{%- endmacro -%}

{%- set columns = prms["group_by"].get_selected("columns") -%}
{%- set aliases = prms["group_by"].get_selected("aliases", default_field="columns") -%}
{%- set select_dim_cols = zip_with_as_and_join(columns, aliases) -%}
{%- set group_by_cols = ", ".join(columns) -%}

{%- if param_exists("description_filter") -%}
    {%- set desc_pattern = prms["description_filter"].get_entered_text().apply_percent_wrap() -%}
    {%- set _ = set_placeholder("desc_pattern", desc_pattern) -%}
{%- endif -%}

WITH
transactions_with_masked_id AS (
    SELECT *,
        '***' as masked_id
    FROM transactions
)
SELECT {{ select_dim_cols }}
    sum(-amount) as total_amount
FROM transactions_with_masked_id
WHERE category <> 'Income'
{% if is_placeholder("desc_pattern") -%} 
    AND description LIKE :desc_pattern 
{% endif -%}
GROUP BY {{ group_by_cols }}
