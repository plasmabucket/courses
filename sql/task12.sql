-- Task 12, ex.12.3.1
INSERT INTO Employees (LastName, FirstName, TitleOfCourtesy, Address, City, Country)
VALUES ('Petya', 'Ivanov', 'Mr.', 'Main 33/7 21', 'Piter', 'Russia');
-- Новый сотрудник получил EmployeeID №12


-- Task 12, ex. 12.3.2
INSERT INTO EmployeeTerritories (EmployeeID, TerritoryID)
VALUES (12, 78759);


-- Task 12, ex. 12.3.3
INSERT INTO Orders (CustomerID, EmployeeID, ShipVia, Freight)
VALUES ('PARIS', 12, 1, 400);
/*
Вставка прошла успешно. Конфликтов не возникло.
Перед её запуском прошёлся по таблице Orders и посмотрел какие FK поля
есть у этой таблицы:

Указал корректный CustomerID -- клиент с таким ID существует в таблице Clients
Указал корректный EmployeeID
Указал корректный ShipperID для ShipVia
Добавил значение поля Freight просто так -- это не FK поле
OrderID сформировался автоматически.
*/
