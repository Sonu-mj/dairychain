# SQL Injection Prevention


## Purpose
This file answers how DairyChain must prevent SQL injection and why parameterised queries are the rule. It is for a developer who writes any query that takes input from outside the code. Its sources are the Master Project Brief and section 4.2 of the user-supplied "Code Review and Security Practices" document, 2026-11-11 (Source 5).

## In this file
- The rule
- Unsafe example
- Safer example using parameterised SQL
- The illustrative example from the brief
- What not to do

## The rule
Use parameterised database queries for every value that comes from outside the code. Never build SQL by string concatenation with untrusted input.

## Unsafe example
Source: "Code Review and Security Practices", section 4.2. SQL injection occurs when untrusted input is inserted directly into a SQL statement. The input is being inserted into the SQL string directly.

```python
customer_id = input("Enter customer ID: ")

query = (
    "SELECT * FROM customers "
    f"WHERE customer_id = '{customer_id}'"
)
```

## Safer example using parameterised SQL
Source: "Code Review and Security Practices", section 4.2, using psycopg. The database driver handles the parameter separately from the SQL statement.

```python
customer_id = input("Enter customer ID: ")

query = """
    SELECT *
    FROM customers
    WHERE customer_id = %s
"""

cursor.execute(query, (customer_id,))
```

The placeholder syntax depends on the database driver being used. Do not assume every driver uses `%s`.

## The illustrative example
From the brief, using psycopg as an illustration. Placeholder style depends on the actual driver.

```python
cursor.execute(
    '''
    SELECT procurement_id, supplier_id, quantity
    FROM procurement
    WHERE procurement_id = %s
    ''',
    (procurement_id,)
)
record = cursor.fetchone()
```

What it does: the value is passed as a parameter, not pasted into the SQL text, so it cannot change the meaning of the query.

## What not to do
Do not build a query by joining input into the SQL string, even if the input looks safe today. A value that is safe once can be unsafe the next time it is used, and a review that allows one unsafe query will allow the next one too.

## Next step / Related files
- [Security review](security_review.md)
- [SQL development](../07_AI_Assisted_Development/sql_development.md)
- [Code review](../07_AI_Assisted_Development/code_review.md)
