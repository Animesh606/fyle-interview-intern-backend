-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH teacher_grading_count AS (
    SELECT
        teacher_id,
        COUNT(*) AS total_assignments_graded
    FROM
        assignments
    WHERE
        state = 'GRADED'
    GROUP BY
        teacher_id
),
max_grading_teacher AS (
    SELECT
        teacher_id
    FROM
        teacher_grading_count
    ORDER BY
        total_assignments_graded DESC
    LIMIT 1
)
SELECT
    COUNT(*) AS grade_A_count
FROM
    assignments
WHERE
    grade = 'A'
    AND teacher_id IN (SELECT teacher_id FROM max_grading_teacher);
