-- 1. Top 10 Selling Products by Revenue
SELECT item_name, SUM(total) AS revenue
FROM supermarket_sales
GROUP BY item_name
ORDER BY revenue DESC
LIMIT 10;

-- 2. Daily Average Revenue
SELECT date, AVG(total) AS avg_revenue
FROM supermarket_sales
GROUP BY date
ORDER BY date;

-- 3. Revenue by Category
SELECT category_name, SUM(total) AS revenue
FROM supermarket_sales
GROUP BY category_name
ORDER BY revenue DESC;

-- 4. Discount Impact on Revenue
SELECT discount_yes_no, SUM(total) AS revenue, AVG(quantity_sold_kilo) AS avg_quantity
FROM supermarket_sales
GROUP BY discount_yes_no;

-- 5. Top 10 Items by Quantity Sold
SELECT item_name, SUM(quantity_sold_kilo) AS total_quantity
FROM supermarket_sales
GROUP BY item_name
ORDER BY total_quantity DESC
LIMIT 10;
