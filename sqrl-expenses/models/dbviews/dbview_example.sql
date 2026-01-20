{#- SQLite dialect (based on connection used) -#}

SELECT 
    date,
    printf('%.2f', amount) as amount,
    CASE 
        WHEN '{{ user.custom_fields.role }}' = 'manager' THEN description
        ELSE '***MASKED***'
    END as description

FROM {{ source("src_transactions") }}

WHERE {{ date_and_amount_filters(use_from_range=false) }}

ORDER BY 1 DESC
