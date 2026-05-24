SELECT
    customer_unique_id,
    COUNT(order_id) AS repeat_orders
FROM retail_orders
GROUP BY customer_unique_id
HAVING COUNT(order_id) > 1;
