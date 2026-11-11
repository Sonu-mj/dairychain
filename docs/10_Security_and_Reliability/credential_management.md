# Credential Management

> Status: PENDING EVIDENCE

## Purpose
This file answers how DairyChain credentials must be handled, and what must never be written into the repository or the documentation. It is for a developer who connects to PostgreSQL or any other service. Its source is section 4.1 of the user-supplied "Code Review and Security Practices" document, 2026-11-11 (Source 5). The examples below are practices to follow, not a claim that they are implemented in DairyChain.

## In this file
- Rules
- Risky approach: hardcoded credentials
- Recommended approach: environment variables
- .env and .gitignore
- What never to include
- Status

## Rules
- Store credentials in environment variables or a secure store, not in code.
- Do not commit a .env file, a password, a key or a token to GitHub.
- Use a separate database user for the application, with only the privileges it needs.
- Rotate a credential if it has been exposed, and record that it was rotated, not the value itself.

## Risky approach: hardcoded credentials
Hardcoding credentials in source files can expose them when code is shared or committed to Git. The password below is an illustrative placeholder from the source document only. It is not a real credential, and it must never be used as one.

```python
DB_USER = "postgres"
DB_PASSWORD = "my_database_password"
DB_HOST = "localhost"
DB_NAME = "dairychain"
```

## Recommended approach: environment variables
The actual credentials should be supplied through environment variables or a properly managed secret store.

```python
import os

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

required_settings = {
    "DB_HOST": DB_HOST,
    "DB_NAME": DB_NAME,
    "DB_USER": DB_USER,
    "DB_PASSWORD": DB_PASSWORD
}

missing_settings = [
    key for key, value in required_settings.items()
    if not value
]

if missing_settings:
    raise RuntimeError(
        f"Missing database configuration: {missing_settings}"
    )
```

## .env and .gitignore
For local development, a `.env` file can be used with an appropriate configuration library, provided it is excluded from version control.

Example `.gitignore` entries:

```gitignore
.env
.env.*
!.env.example

.venv/
__pycache__/
*.py[cod]
```

A safe `.env.example` may contain variable names and non-secret placeholders, but never actual passwords or tokens.

**Note:** Environment variables reduce the risk of exposing secrets in source code, but they do not replace proper secret management or access control.

## What never to include
Never include a password, key, token, connection string with a password, or a personal path in any documentation file in this set. If a value appears in a log or a screenshot, remove it before the log or screenshot is kept.

## Status
No credential setup was supplied. Status: PENDING EVIDENCE. The brief reported an earlier PostgreSQL authentication error. That error is RESOLVED by Source 17, which shows a successful connection as user postgres; no password or credential value is visible in the screenshots and none is recorded here.

## Next step / Related files
- [Security review](security_review.md)
- [Access control](access_control.md)
- [Transaction and data integrity](transaction_and_data_integrity.md)
