-- 코드를 입력하세요
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN (SELECT CATEGORY, max(price)
                         FROM FOOD_PRODUCT
                         GROUP BY CATEGORY HAVING CATEGORY IN ('과자', '국', '김치', '식용유')) 
    

order by MAX_PRICE desc

# CATEGORY	MAX_PRICE	PRODUCT_NAME
# 김치	19000	맛있는배추김치
# 식용유	8950	맛있는콩기름
# 국	2900	맛있는미역국
# 과자	1950	맛있는포카칩

# SELECT *
# FROM FOOD_PRODUCT
