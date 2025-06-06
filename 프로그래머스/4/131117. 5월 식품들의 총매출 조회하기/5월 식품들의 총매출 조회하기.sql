-- 코드를 입력하세요
SELECT PRODUCT_ID, PRODUCT_NAME, (PRICE*TOTAL_AMOUNT) TOTAL_SALES
FROM
(
SELECT P.PRODUCT_ID, PRODUCT_NAME, PRICE, SUM(AMOUNT) TOTAL_AMOUNT
FROM FOOD_PRODUCT P JOIN FOOD_ORDER O ON P.PRODUCT_ID = O.PRODUCT_ID
WHERE DATE_FORMAT(PRODUCE_DATE, '%Y-%m') = '2022-05'
GROUP BY P.PRODUCT_ID, PRODUCT_NAME, PRICE
) F
ORDER BY TOTAL_SALES DESC, PRODUCT_ID