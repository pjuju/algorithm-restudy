SELECT animal_id, name
FROM animal_outs as outs
WHERE animal_id not in (
                    SELECT animal_id
                    FROM animal_ins)
order by animal_id
