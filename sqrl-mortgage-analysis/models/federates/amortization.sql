WITH RECURSIVE
cte AS (

    SELECT
        0 AS month,
        ($start_date::DATE - INTERVAL 1 MONTH) AS current_month,
        NULL AS principal_start,
        NULL AS payment,
        NULL AS interest_payment,
        {{ ctx.loan_amount }} AS principal_remaining
    
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
    month AS month_number,
    current_month::DATE AS current_month,
    ROUND(principal_start, 2) AS principal_start,
    ROUND(payment, 2) AS payment,
    ROUND(interest_payment, 2) AS interest_payment,
    ROUND(payment - interest_payment, 2) AS principal_payment

FROM cte

WHERE month > 0
