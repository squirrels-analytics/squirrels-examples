{# SQLite dialect (based on connection used) #}

SELECT 
    date,
    printf('%.2f', amount) as amount,
    CASE 
        WHEN '{{ user.role }}' = 'manager' THEN description
        ELSE '***MASKED***'
    END as description

FROM {{ source("src_transactions") }}

WHERE {{ date_and_amount_filters(ctx) }}

ORDER BY date
