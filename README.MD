#Елена Ржеутская, 12-я когорта — Финальный проект. Инженер по тестированию плюс
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest

Задания к БД:
Задание №1
SELECT c.login, COUNT(o."inDelivery") AS "COUNT inDelivery" 
FROM "Couriers" AS c 
INNER JOIN "Orders" AS o ON c.id=o."courierId" 
GROUP BY login;


Задание №2
SELECT track,
CASE 
WHEN finished=true THEN 'Status 2' 
WHEN cancelled=true THEN 'Status -1' 
WHEN "inDelivery"=true THEN 'Status 1'
ELSE 'Status 0' 
END 
FROM "Orders";
