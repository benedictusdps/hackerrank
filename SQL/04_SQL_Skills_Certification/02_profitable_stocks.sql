/*
A stock is considered profitable if the predicted price is strictly greater than the current price.
Write a query to find the stock_codes of all the stocks which are profitable based on this definition.
Sort the output in ascending order.
*/

SELECT price_today.stock_code
FROM price_today INNER JOIN price_tomorrow
ON price_today.stock_code = price_tomorrow.stock_code
WHERE price_tomorrow.price > price_today.price;

