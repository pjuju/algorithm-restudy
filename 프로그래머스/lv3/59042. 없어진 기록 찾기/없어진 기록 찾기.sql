-- 코드를 입력하세요
SELECT outs.animal_id, outs.name FROM animal_outs as outs
LEFT JOIN animal_INS as ins
ON ins.animal_id = outs.animal_id
WHERE ins.intake_condition is NULL
ORDER BY animal_id;