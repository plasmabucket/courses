-- Task 8, ex. 8.3.1
SELECT Products.ProductName, Categories.CategoryName
FROM Products, Categories
WHERE Products.CategoryID = Categories.CategoryID;


-- Task 8, ex. 8.3.2
SELECT "Order Details".UnitPrice, Products.ProductName
FROM "Order Details", Products
WHERE ("Order Details".UnitPrice < 20)
    AND ("Order Details".ProductID = Products.ProductID);


-- Task 8, ex. 8.3.3
SELECT "Order Details".UnitPrice, Products.ProductName, Categories.CategoryName
FROM "Order Details", Products, Categories
WHERE ("Order Details".UnitPrice < 20)
    AND ("Order Details".ProductID = Products.ProductID)
    AND (Products.CategoryID = Categories.CategoryID);
