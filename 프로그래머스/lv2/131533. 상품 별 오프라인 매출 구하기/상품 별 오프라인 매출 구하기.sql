-- 코드를 입력하세요
SELECT product.PRODUCT_CODE,  sum(sale.SALES_AMOUNT) * product.PRICE as SALES
FROM offline_sale as sale
LEFT JOIN product
ON sale.product_id = product.product_id
GROUP BY product.PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE