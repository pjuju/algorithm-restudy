-- 코드를 입력하세요
SELECT ins.animal_id, ins.animal_type, ins.name 
FROM ANIMAL_INS as ins
JOIN ANIMAL_OUTS as outs
ON ins.animal_id = outs.animal_id
WHERE ins.SEX_UPON_INTAKE != outs.SEX_UPON_OUTCOME;