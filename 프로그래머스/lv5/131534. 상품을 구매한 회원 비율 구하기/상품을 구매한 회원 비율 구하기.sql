    SELECT YEAR, MONTH, COUNT(*), ROUND(COUNT(*)/(SELECT COUNT(*)
                                                 FROM USER_INFO
                                                 WHERE YEAR(JOINED) = '2021'),1)
    
    FROM (
        SELECT DISTINCT YEAR(S.SALES_DATE) AS YEAR, MONTH(S.SALES_DATE) AS MONTH, U.USER_ID
        FROM ONLINE_SALE S
        JOIN USER_INFO U ON S.USER_ID = U.USER_ID AND YEAR(U.JOINED) = '2021'
        ) AS A
    
    GROUP BY YEAR, MONTH
    ORDER BY YEAR, MONTH