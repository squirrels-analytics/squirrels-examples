WITH RECURSIVE
cte AS (

    SELECT
        0 AS month,
        ($start_date::DATE - INTERVAL 1 MONTH) AS current_month,
        NULL::DOUBLE AS principal_start,
        NULL::DOUBLE AS payment,
        NULL::DOUBLE AS interest_payment,
        {{ ctx.loan_amount }}::DOUBLE AS principal_remaining
    
    UNION ALL
    
    SELECT 
        month + 1 AS month,
        (current_month + INTERVAL 1 MONTH) AS current_month,
        principal_remaining AS principal_start,
        {{ ctx.monthly_payment }} AS payment,
        principal_remaining * {{ ctx.applied_monthly_rate }} AS interest_payment,
        principal_remaining * (1 + {{ ctx.applied_monthly_rate }}) - {{ ctx.monthly_payment }} AS principal_remaining
    
    FROM cte

    WHERE month < {{ ctx.total_num_months }}

)
SELECT
    current_month::DATE AS current_month,
    principal_start::DECIMAL(10, 2) AS principal_start,
    payment::DECIMAL(10, 2) AS payment,
    interest_payment::DECIMAL(10, 2) AS interest_payment,
    (payment - interest_payment)::DECIMAL(10, 2) AS principal_payment,
    principal_remaining::DECIMAL(10, 2) AS principal_remaining

FROM cte

WHERE month > 0
