-- Task 4, ex. 4.3.1
SELECT CustomerID, ContactName FROM Customers
WHERE ContactName LIKE '% C%'


-- Task 4, ex. 4.3.2
SELECT OrderID, Freight, ShipCountry FROM Orders
WHERE Freight BETWEEN 100 AND 200
AND ShipCountry IN ('USA', 'France')


-- Task 4, ex. 4.3.3
SELECT EmployeeID, TerritoryID FROM EmployeeTerritories
WHERE TerritoryID BETWEEN 6897 AND 31000
