/*
On the basis of merit, a company decides to promote some of its employee in its HR division at the end of the quarter because of their high performance.
Write a query to find the employee IDs along with the names of all its employees who work in the HR department who earned a bonus of 5000 dollars or more in the last quarter.
*/

SELECT employee_information.employee_ID, employee_information.name
FROM employee_information INNER JOIN last_quarter_bonus
ON employee_information.employee_ID = last_quarter_bonus.employee_ID
WHERE employee_information.division = 'HR' AND last_quarter_bonus.bonus >= 5000;