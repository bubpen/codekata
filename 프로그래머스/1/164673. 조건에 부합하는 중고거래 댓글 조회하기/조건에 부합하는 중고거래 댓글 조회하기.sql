-- 코드를 입력하세요
SELECT TITLE, B.BOARD_ID, REPLY_ID, R.WRITER_ID, R.CONTENTS, LEFT(R.CREATED_DATE,10) CREATED_DATE
FROM USED_GOODS_BOARD B JOIN USED_GOODS_REPLY R ON B.BOARD_ID = R.BOARD_ID
WHERE LEFT(B.CREATED_DATE, 7) = '2022-10'
ORDER BY CREATED_DATE, TITLE