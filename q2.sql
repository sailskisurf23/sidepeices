--schema
--create tables described in problem,

CREATE TABLE Orders
    (`Number` int, `order_date` datetime, `cust_id` int, `salesperson_id` int, `Amount` int)
;

INSERT INTO Orders
    (`Number`, `order_date`, `cust_id`, `salesperson_id`, `Amount`)
VALUES
    (10, '1996-08-02 00:00:00', 4, 2, 540),
    (20, '1999-01-30 00:00:00', 4, 8, 1800),
    (30, '1995-07-14 00:00:00', 9, 1, 460),
    (40, '1998-01-29 00:00:00', 7, 2, 2400),
    (50, '1998-02-03 00:00:00', 6, 7, 600),
    (60, '1998-03-02 00:00:00', 6, 7, 720),
    (70, '1998-05-06 00:00:00', 9, 7, 150)
;


CREATE TABLE Salesperson
    (`ID` int, `Name` varchar(5), `Age` int, `Salary` int)
;

INSERT INTO Salesperson
    (`ID`, `Name`, `Age`, `Salary`)
VALUES
    (1, 'Abe', 61, 140000),
    (2, 'Bob', 34, 44000),
    (5, 'Chris', 34, 40000),
    (7, 'Dan', 41, 52000),
    (8, 'Ken', 57, 115000),
    (11, 'Joe', 38, 38000)
;

-- Create new table by doing innerjoin on salesperson_ID
-- Return 'Name' and 'Amount' columns, GroupBy Name, Sum Amount

CREATE TABLE Order_Totals
   AS(SELECT Salesperson.Name, SUM(Orders.Amount) AS AmountOfOrders FROM Orders
      INNER JOIN Salesperson
      ON Salesperson.ID=Orders.salesperson_ID
      GROUP BY Salesperson.Name)

--Query
--Return Just Names for those who had more than $1300 in total orders

SELECT Name FROM Order_Totals
WHERE AmountOfOrders > 1300
