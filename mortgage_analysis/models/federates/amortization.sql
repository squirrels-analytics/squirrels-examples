WITH RECURSIVE
cte AS (

    SELECT
        0 AS month,
        NULL AS current_month,
        NULL AS principal_start,
        NULL AS payment,
        NULL AS interest_payment,
        {{ ctx.loan_amount }} AS principal_remaining
    
    UNION ALL
    
    SELECT 
        month + 1 AS month,
        DATE(:start_date, '+' || month || ' months') AS current_month,
        principal_remaining AS principal_start,
        {{ ctx.monthly_payment }} AS payment,
        principal_remaining * {{ ctx.applied_monthly_rate }} AS interest_payment,
        principal_remaining * (1 + {{ ctx.applied_monthly_rate }}) - {{ ctx.monthly_payment }} AS principal_remaining
    
    FROM cte

    WHERE month < {{ ctx.total_num_months }}

)
SELECT
    month AS month_number,
    current_month,
    PRINTF("%.2f", principal_start) AS principal_start,
    PRINTF("%.2f", payment) AS payment,
    PRINTF("%.2f", interest_payment) AS interest_payment,
    PRINTF("%.2f", payment - interest_payment) AS principal_payment

FROM cte

WHERE month > 0
