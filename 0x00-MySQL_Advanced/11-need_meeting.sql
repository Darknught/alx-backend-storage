-- This view lists all students that have a score under 80 (strict)
-- and no last_meeting date or more than 1 month since their last meeting.
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
  AND (last_meeting IS NULL OR DATE_ADD(last_meeting, INTERVAL 1 MONTH) < CURRENT_DATE());
