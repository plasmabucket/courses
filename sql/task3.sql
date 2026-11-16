-- 3.9.1
SELECT ProductName, UnitsInStock FROM Products;


-- 3.9.2
SELECT ProductName, UnitPrice FROM Products
WHERE UnitPrice < 20;


-- 3.9.3
SELECT OrderID, Freight FROM Orders
WHERE Freight > 11.7 AND Freight < 98.1;


-- 3.9.4
SELECT EmployeeID, FirstName, LastName FROM Employees
WHERE TitleOfCourtesy = 'Mr.' OR EmployeeID = 2;
-- Employee №2 is a man, but he has a "Dr." title instead of "Mr."


-- 3.9.5
SELECT CompanyName, Country FROM Suppliers
WHERE Country = 'Japan';


-- 3.9.6
SELECT OrderID, EmployeeID FROM Orders
WHERE EmployeeID = '2' OR EmployeeID = '4' OR EmployeeID = '8';


-- 3.9.7
SELECT OrderID FROM "Order Details"
WHERE UnitPrice > 40 AND Quantity < 10;
