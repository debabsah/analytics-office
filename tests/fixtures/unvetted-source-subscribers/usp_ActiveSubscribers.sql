-- usp_ActiveSubscribers — the platform team's subscriber-report proc.
-- Inherited; the style is theirs.
CREATE PROC usp_ActiveSubscribers @asOf date AS
;WITH sub AS (
  SELECT s.ACCOUNTID, s.PLAN_TYPE, s.MRR_USD, s.STATUS_CODE
  FROM SUBSCRIPTION s
  JOIN ACCOUNT a ON a.ACCOUNTID = s.ACCOUNTID
  WHERE s.PLAN_TYPE IN ('monthly', 'annual')        -- subscription plans
    AND s.STATUS_CODE = 2                            -- active
    AND a.IS_INTERNAL = 0                            -- exclude internal / test accounts
    AND s.EFFECTIVE_DATE <= @asOf
    AND (s.END_DATE IS NULL OR s.END_DATE > @asOf)
)
SELECT COUNT(DISTINCT ACCOUNTID) AS ActiveSubscribers,
       SUM(MRR_USD)              AS MRR
FROM sub;
