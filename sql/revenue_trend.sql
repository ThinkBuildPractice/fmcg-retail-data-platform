SELECT
    order_purchase_timestamp,
    COUNT(*) AS total_orders
FROM retail_orders
GROUP BY order_purchase_timestamp
ORDER BY order_purchase_timestamp;
