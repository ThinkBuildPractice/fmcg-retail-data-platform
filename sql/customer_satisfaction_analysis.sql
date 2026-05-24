SELECT
    review_score,
    COUNT(*) AS total_orders,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage_distribution
FROM retail_orders
GROUP BY review_score
ORDER BY review_score;
