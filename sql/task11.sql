-- Task 11, ex. 11.5.1
SELECT Customers.CompanyName, Orders.OrderID
FROM Customers LEFT JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
WHERE Orders.OrderID IS NULL;


-- Task 11, ex. 11.5.2
SELECT ContactName, City, Country, 'Customer' As 'Type'
FROM Customers
UNION ALL
SELECT ContactName, City, Country, 'Suppliers' As 'Type'
FROM Suppliers;
