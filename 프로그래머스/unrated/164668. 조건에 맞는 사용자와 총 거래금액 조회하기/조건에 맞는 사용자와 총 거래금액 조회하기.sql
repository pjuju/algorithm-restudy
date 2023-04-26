-- 코드를 입력하세요

SELECT board.WRITER_ID AS USER_ID, users.NICKNAME, sum(board.PRICE) AS TOTAL_SALES  
FROM USED_GOODS_BOARD as board
LEFT JOIN USED_GOODS_USER as users
ON users.USER_ID = board.WRITER_ID
WHERE board.STATUS = 'DONE'
GROUP BY USER_ID HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES