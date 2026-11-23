-- Task 10, ex. 10.4.1
SELECT Products.ProductName, "Order Details".UnitPrice
FROM Products JOIN "Order Details"
ON Products.ProductID = "Order Details".ProductID
WHERE "Order Details".UnitPrice < 20;


-- Task 10, ex. 10.4.2
/*
Вариант с FULL JOIN дополнительно выдаёт записи из второй таблицы,
не соответствующие ни одной записи из первой таблицы.
Недостающие данные для таких записей FULL JOIN заполняет значениями NULL.

В данном запросе значения NULL встречаются только в одном выведенном поле -- Freight.
Это две записи, соответствующие компаниям у которых нет заказов.
Предполагаю, что если бы в таблице Orders были бы заказы без указанного CustomerID,
то в выдаче были бы NULL значения в обоих полях -- и в Freight, и в CompanyName.
*/


-- Task 10, ex. 10.4.3
/*
Чтобы превратить CROSS JOIN в INNER JOIN
необходимо в WHERE указать условие эквисоединения.

INNER JOIN x ON [condition A]
эквивалентно
CROSS JOIN x WHERE [condition A]
*/


-- Task 10, ex. 10.4.4
SELECT Products.ProductName, "Order Details".UnitPrice
FROM Products INNER JOIN "Order Details"
ON Products.ProductID = "Order Details".ProductID
