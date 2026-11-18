-- Task 5, ex. 6.3.1
SELECT ContactType,
	COUNT(ContactType) AS NUM_CONTACTS
FROM Contacts
GROUP BY ContactType;


-- Task 5, ex. 6.3.2
SELECT CategoryID,
    AVG(UnitPrice) AS AVG_PRICE
FROM Products
GROUP BY CategoryID
ORDER BY AVG(UnitPrice);
