-- Task 9, ex. 9.4.1
SELECT t1.CustomerID, t2.CustomerID
FROM Customers t1, Customers t2
WHERE t1.CustomerID <> t2.CustomerID
    AND t1.Region IS NULL
    AND t2.Region IS NULL;


-- Task 9, ex. 9.4.2
SELECT * FROM Orders
WHERE EXISTS
    (SELECT CustomerID, Region FROM Customers
    WHERE Orders.CustomerID = Customers.CustomerID
    AND Customers.Region IS NOT NULL);


-- Task 9, ex. 9.4.3
SELECT * FROM Orders
WHERE Orders.Freight > ALL
    (SELECT UnitPrice FROM Products);
