# Write your MySQL query statement below
WITH FilteredStadium AS (
    -- Step 1 & 2: Filter for 100+ people and create the "Island ID"
    SELECT 
        id, 
        visit_date, 
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS island_id
    FROM Stadium
    WHERE people >= 100
),
IslandCounts AS (
    -- Step 3: Count how many days are in each island
    SELECT 
        id, 
        visit_date, 
        people,
        COUNT(id) OVER (PARTITION BY island_id) AS consecutive_days
    FROM FilteredStadium
)
-- Step 4: Keep only the islands with 3 or more days
SELECT 
    id, 
    visit_date, 
    people
FROM IslandCounts
WHERE consecutive_days >= 3
ORDER BY visit_date;