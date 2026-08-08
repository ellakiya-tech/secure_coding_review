# Secure Coding Review of a Python Login System

## Project Objective

This project demonstrates the security vulnerabilities present in a simple Python login system and shows how secure coding practices can be applied to improve password security.

## Project Description

The project contains two Python login programs:

1. vulnerable_login.py - Demonstrates an insecure login system where the password is stored in plain text.
2. secure_login.py - Demonstrates an improved login system where the password is hashed before comparison.

The project helps to understand the importance of secure password handling in software development.

## Technologies Used

- Python
- Visual Studio Code
- Git
- GitHub
- hashlib

## Files

### 1. vulnerable_login.py

This program stores the username and password directly as plain text.

Example:

- Username: admin
- Password: admin123

The program checks the entered username and password against the stored values.

### 2. secure_login.py

This program uses SHA-256 hashing to transform the password before comparing it with the stored hash.

This prevents the password from being stored directly as plain text.

## Security Vulnerability

The vulnerable version stores the password in plain text.

If an attacker gains access to the source code or stored credentials, the original password can be easily exposed.

## Security Improvement

The secure version hashes the password using SHA-256 before comparison.

This demonstrates the basic concept of protecting passwords using hashing.

> Note: In a real production application, password-specific hashing algorithms such as Argon2, bcrypt, or scrypt should be preferred over plain SHA-256.

## Testing

### Vulnerable Login - Successful Login

Input:

```text
Username: admin
Password: admin123