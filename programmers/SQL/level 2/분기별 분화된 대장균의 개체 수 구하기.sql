SELECT B.QUARTER AS QUARTER, COUNT(*) AS ECOLI_COUNT
FROM ECOLI_DATA AS A LEFT JOIN (SELECT ID, 
                                CASE
                                    WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 1 AND 3 THEN "1Q"
                                    WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 4 AND 6 THEN "2Q"
                                    WHEN MONTH(DIFFERENTIATION_DATE) BETWEEN 7 AND 9 THEN "3Q"
                                    ELSE "4Q"
                                    END AS QUARTER
                                FROM ECOLI_DATA) AS B
     ON A.ID = B.ID
GROUP BY B.QUARTER
ORDER BY QUARTER ASC

-- CASE WHEN 조건문에서는 양쪽 부등호가 아닌 BETWEEN을 써야 함.
-- 혹은 각각의 조건문에서 한 개의 부등호만 써야 함.