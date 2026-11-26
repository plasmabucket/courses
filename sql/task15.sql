-- Task 15, ex. 15.7
CREATE DATABASE MyDatabase;

USE MyDatabase;

CREATE TABLE Territories (
    TerritoryID nvarchar(20) NOT NULL,
    TerritoryDescription nchar(50) NOT NULL,
    RegionID int NOT NULL
);

CREATE TABLE Region (
    RegionID int NOT NULL,
    RegionDescription nchar(50) NOT NULL
);

INSERT INTO Region (RegionID, RegionDescription)
VALUES (1, 'Eastern'), (2, 'Western'), (3, 'Northern'), (4, 'Southern');

INSERT INTO Territories (TerritoryID, TerritoryDescription, RegionID)
VALUES ('01581', 'Westboro', 1), ('01730', 'Bedford', 1), ('03049', 'Hollis', 3);
