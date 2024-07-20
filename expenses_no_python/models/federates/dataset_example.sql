{%- set aliases = prms["group_by"].get_selected("aliases", default_field="columns") -%}
{%- set order_by_cols -%}
    {%- for x in aliases -%}
    {{ x }} DESC {%- if not loop.last %}, {% endif -%}
    {%- endfor -%}
{%- endset -%}

SELECT *
FROM {{ ref("database_view1") }}
ORDER BY {{ order_by_cols }}
