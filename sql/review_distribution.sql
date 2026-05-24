SELECT
    review_score,
    COUNT(*) AS total_reviews
FROM retail_orders
GROUP BY review_score
ORDER BY review_score;
