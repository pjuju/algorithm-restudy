-- 코드를 입력하세요


SELECT ins.ANIMAL_ID, ins.name
FROM ANIMAL_OUTS as outs
LEFT JOIN ANIMAL_INS as ins
ON ins.animal_id = outs.animal_id
WHERE outs.datetime <= ins.datetime
GROUP BY animal_id 
ORDER BY ins.datetime