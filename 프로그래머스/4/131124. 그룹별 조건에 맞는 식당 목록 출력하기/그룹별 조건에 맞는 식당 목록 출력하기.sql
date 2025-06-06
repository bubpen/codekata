-- 코드를 입력하세요
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') REVIEW_DATE
FROM MEMBER_PROFILE P JOIN REST_REVIEW R ON P.MEMBER_ID = R.MEMBER_ID
WHERE R.MEMBER_ID IN
(
SELECT MEMBER_ID
FROM REST_REVIEW
GROUP BY MEMBER_ID
HAVING COUNT(MEMBER_ID)>=
(
SELECT MAX(CNT)
FROM 
(
SELECT MEMBER_ID, COUNT(MEMBER_ID) CNT
FROM REST_REVIEW
GROUP BY MEMBER_ID
) m
)
)
ORDER BY REVIEW_DATE
