-- Task 13, 13.3.1
UPDATE "Order Details"
SET Discount = 0.20
WHERE Discount < 0.20 AND Quantity > 50;


-- Task 13, 13.3.2
UPDATE Contacts
SET City = 'Piter', Country = 'Russia'
WHERE City = 'Berlin' AND Country = 'Germany';


-- Task 13, 13.3.3
INSERT INTO Shippers (CompanyName, Phone)
VALUES ('New company 1', '123'), ('New company 2', '123');

DELETE FROM Shippers
WHERE ShipperID > 3;
/* В качестве критерия для удаления выбрал ShipperID */
