{%- macro date_and_amount_filters(use2) -%}
    
    {%- if use2 -%}
        date >= {{ ctx.start_date2 }}
        AND date <= {{ ctx.end_date2 }}
        AND amount >= {{ ctx.min_amount2 }}
        AND amount <= {{ ctx.max_amount2 }}
    {%- else -%}
        date >= {{ ctx.start_date }}
        AND date <= {{ ctx.end_date }}
        AND amount >= {{ ctx.min_amount }}
        AND amount <= {{ ctx.max_amount }}
    {%- endif -%}

{%- endmacro -%}
