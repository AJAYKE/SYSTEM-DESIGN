## Lets Test ATOMICITY IN SQL

Let's create the Account table with a check constraint that ensures the balance cannot be negative, and then define the test cases.

```sql
CREATE TABLE Account (
    AccountID INT PRIMARY KEY,
    Balance DECIMAL(10, 2) CHECK (Balance >= 0)
);
```

Inset some initial data

```sql
INSERT into Account (AccountID, Balance) VALUES(1,1000)
INSERT INTO Account (AccountID, Balance) VALUES(2, 1000)
```

Check the update

```sql
SELECT * FROM Account
```

## ATOMICITY (All or Nothing)

In an atomic transaction, either all operations succeed or none succeed. If any part fails, the entire transaction is rolled back to its original state, and the database remains consistent. This prevents partial updates that could lead to data corruption or inconsistencies.

Let's Test the Atomicity.

The default behaviour in MYSQl is that if an error occurs within a transaction, the specific statement that caused the error is terminated. Still, the transaction itself is not automatically rolled back. This means subsequent statements within the same transaction can still be executed unless you explicitly handle the rollback.

We can use the XACT_ABORT method

When SET XACT_ABORT is ON, the transaction is terminated and rolled back if a Transact-SQL statement raises a run-time error.

We can achieve this atomicity behaviour in other ways aswell, by using TRY and CATCH

```sql
SET XACT_ABORT ON;

BEGIN TRANSACTION

    -- THIS WILL BE SUCCESSFUL AS THE BALANCE WILL STILL BE GREATER THAN 0
    UPDATE ACCOUNT SET BALANCE = BALANCE - 500 WHERE ACCOUNTID = 1

    -- LETS UPDATE THE ACCOUNTID 1 AGAIN AND TRY TO BREACH NON NEGATIVE BALANCE CONSTRAINT
    UPDATE ACCOUNT SET BALANCE = BALANCE - 700 WHERE ACCOUNTID = 1
    -- THIS SHOULD THROW THE ERROR

    --NOW LETS UPDATE ACCOUNTID 2 AGAIN
    UPDATE Account SET Balance = Balance + 500.00 WHERE AccountID = 2;

COMMIT TRANSACTION
```

Check the update

```sql
SELECT * FROM ACCOUNT
```

Lets try the same change again with XACT_ABORT OFF

```sql
SET XACT_ABORT OFF;

BEGIN TRANSACTION

    -- THIS WILL BE SUCCESSFUL AS THE BALANCE WILL STILL BE GREATER THAN 0
    UPDATE ACCOUNT SET BALANCE = BALANCE - 500 WHERE ACCOUNTID = 1

    -- LETS UPDATE THE ACCOUNTID 1 AGAIN AND TRY TO BREACH NON NEGATIVE BALANCE CONSTRAINT
    UPDATE ACCOUNT SET BALANCE = BALANCE - 700 WHERE ACCOUNTID = 1
    -- THIS SHOULD THROW THE ERROR

    --NOW LETS UPDATE ACCOUNTID 2 AGAIN
    UPDATE Account SET Balance = Balance + 500.00 WHERE AccountID = 2;

COMMIT TRANSACTION
```

Check the update

```sql
SELECT * FROM ACCOUNT
```
