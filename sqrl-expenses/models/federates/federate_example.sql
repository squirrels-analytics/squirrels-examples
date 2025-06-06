{#- DuckDB dialect -#}

SELECT {{ ctx.select_dim_cols | join }}
    , CAST(SUM(amount) AS DECIMAL(15, 2)) as total_amount

{# ref() can be used on a sources, seeds, builds, dbviews, or other federate models -#}
FROM {{ ref("build_example") }} AS a

WHERE {{ date_and_amount_filters(use_from_range=true) }}
{%- if ctx.has_categories %} 
    AND category_id IN ({{ ctx.categories | quote_and_join }}) 
{%- endif %}
{%- if ctx.has_subcategories %} 
    AND subcategory_id IN ({{ ctx.subcategories | quote_and_join }}) 
{%- endif %}

GROUP BY {{ ctx.group_by_cols | join }}

ORDER BY {{ ctx.order_by_cols_desc | join }}
