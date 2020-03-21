'''● * Write a query to display the names (first_name, last_name) of employee using alias
name “First Name", "Last Name"'''
SELECT FIRST_NAME AS 'First Name', LAST_NAME as 'Last Name' FROM employees;

'''● * Write a query to get unique department ID from employee table'''
SELECT DEPARTMENT_ID FROM employees;
 

'''● * Write a query to get all employee details from the employee table order by first name,
descending'''

SELECT * FROM employees
ORDER BY FIRST_NAME DESC;

'''
● * Write a query to get the employee ID, names (first_name, last_name), salary in
ascending order of salary'''

SELECT EMPLOYEE_ID, FIRST_NAME,LAST_NAME,SALARY FROM employees
ORDER BY SALARY;

'''● * Write a query to get the number of employees working with the company'''
SELECT COUNT(FIRST_NAME) AS EMPLOYEE_COUNT  FROM employees;

'''● * Write a query to display the name (first_name, last_name) and salary for all employees
whose salary is not in the range $10,000 through $15,000  '''
SELECT  FIRST_NAME,LAST_NAME,SALARY FROM employees              
WHERE SALARY NOT BETWEEN 10000 AND 15000;

''' ● * Write a query to display the name (first_name, last_name) and department ID of all
employees in departments 30 or 100 in ascending order'''
SELECT  FIRST_NAME,LAST_NAME, DEPARTMENT_ID FROM employees
WHERE DEPARTMENT_ID BETWEEN 30 AND 100
ORDER BY DEPARTMENT_ID;


'''● * Write a query to display the name (first_name, last_name) and hire date for all
employees who were hired in 1987'''
SELECT  FIRST_NAME,LAST_NAME, HIRE_DATE FROM employees WHERE HIRE_DATE LIKE '1987%';

'''● * Write a query to display the last name, job, and salary for all employees whose job is
that of a Programmer or a Shipping Clerk, and whose salary is not equal to $4,500,
$10,000, or $15,000'''
SELECT LAST_NAME,JOB_ID, SALARY  FROM employees WHERE JOB_ID IN  ('SH_CLERK', 'IT_PROG') AND SALARY <> 4500 AND SALARY <> 10000 AND SALARY <> 15000;


'''
● Write a query to select all record from employees where last name in 'BLAKE', 'SCOTT',
'KING' and 'FORD'
'''
SELECT * FROM employees WHERE LAST_NAME REGEXP 'KING|FORD|BLAKE|SCOTT';


'''● * Write a query to get the total salaries payable to employees'''

SELECT SUM(SALARY) FROM employees;


'''● * Write a query to get the minimum salary from employees table'''
SELECT min(SALARY) FROM employees;


'''● * Write a query to get the average salary and number of employees working the
department 90'''

SELECT COUNT(FIRST_NAME) AS EMPLOYEE_COUNT, AVG(SALARY), DEPARTMENT_ID  FROM employees
WHERE DEPARTMENT_ID = 90;

'''● * Write a query to get the number of employees with the same job'''
SELECT DEPARTMENT_ID, COUNT(EMPLOYEE_ID)  FROM employees  GROUP BY DEPARTMENT_ID;


'''● * Write a query to get the average salary for each job ID excluding programmer'''
SELECT DEPARTMENT_ID, AVG(SALARY)  FROM employees WHERE DEPARTMENT_ID <>60 GROUP BY DEPARTMENT_ID;



'''● * Write a query to find addresses (location_id, street_address, city, state_province,
country_name) of all the departments. Hint : Use NATURAL JOIN.'''

SELECT LOCATION_ID, STREET_ADDRESS, CITY, STATE_PROVINCE, DEPARTMENT_NAME FROM locations NATURAL JOIN departments;


'''● * Write a query to find the name (first_name, last name), department ID and name of all
the employees.'''
SELECT FIRST_NAME, LAST_NAME, DEPARTMENT_ID, DEPARTMENT_NAME FROM employees NATURAL JOIN departments;


'''● * Write a query to find the employee id, name (last_name) along with their manager_id
and name (last_name).'''

SELECT FIRST_NAME, LAST_NAME, DEPARTMENT_ID, DEPARTMENT_NAME, MANAGER_ID FROM employees NATURAL JOIN departments;

'''● * Write a query to find the employee ID, job title, number of days between ending date
and starting date for all jobs in department 90.'''

SELECT EMPLOYEE_ID, JOB_TITLE, DATEDIFF(END_DATE,START_DATE) FROM job_history  NATURAL JOIN jobs  where DEPARTMENT_ID = 90;

'''● * Write a query to display the department name, manager name, and city.'''

SELECT departments.DEPARTMENT_NAME, employees.FIRST_NAME, locations.CITY  FROM departments  JOIN employees  ON (departments.MANAGER_ID = employees.EMPLOYEE_ID)  JOIN locations  USING (LOCATION_ID);

'''● * Write a query to display department name, name (first_name, last_name), hire date,
salary of the manager for all managers whose experience is more than 15 years
'''
SELECT departments.DEPARTMENT_NAME, employees.FIRST_NAME, employees.LAST_NAME, employees.HIRE_DATE, employees.SALARY, 
DATEDIFF(NOW(),HIRE_DATE)DAYS_ON_JOB 
FROM departments  
JOIN employees  ON (departments.MANAGER_ID = employees.EMPLOYEE_ID)
WHERE DATEDIFF(NOW(),HIRE_DATE)>5480;


'''● * Write a query to display the first day of the month (in datetime format) three months
before the current month. Sample current date : 2014-09-03 Expected result :
2014-06-01'''

SELECT date(((PERIOD_ADD(EXTRACT(YEAR_MONTH FROM CURDATE()),-3)*100)+1));