SELECT date, description,
    sum(-amount) as total_amount
FROM transactions
WHERE category <> 'Income'
    AND description LIKE :desc_pattern
GROUP BY date, description
