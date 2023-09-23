# Тест на проверку, что по треку заказа можно получить данные о заказе в Яндекс Самокат  с помощью API Яндекс.Самокат.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest

# Запросы SQL
1. SELECT c.login, COUNT(o.id) AS total_order
   FROM "Orders" AS o
   INNER JOIN "Couriers" AS c ON o."courierId" = c.id
   WHERE o."inDelivery" = true
   GROUP BY c.login;
2. SELECT track,
     CASE
       WHEN finished = true THEN '2'
       WHEN cancelled = true THEN '-1'
       WHEN "inDelivery" = true THEN '1'
       ELSE '0'
     END AS order_status
   FROM "Orders";