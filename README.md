# Moviri Technical Challenge Solution

Developed using Python and SQLite 

## Description

### Part 1 Coding Exercise: 
Solution in file: "main.py"

Procedure combining information from two CSV files using python to calculate the network bandwidth utilization for each line in the “netbitrate.csv” file. 

Results are printed considering float point numbers as follows:

```Timestamp | Server | Network Interface | Network bit rate / Bandwidth```

To run, first insure python3 is installed, then in the terminal run: 
```python3 main.py```

![Screenshot of Coding Results](Screenshots/Python_Screenshot_Moviri.png?raw=true)


### Part 2 SQL Query Exercise: 
Solution in file: "employeeInvoiceTotals.sql"

SQL query that retrieves all employees and the respective sum of invoice totals for the customers they support. Ordered in descending order by the total invoice sum.

to run, first insure sqlite3 is installed, then in the terminal run:
 
```cat employeeInvoiceTotals.sql | sqlite3 moviri.sqlite.db```

![Screenshot of SQL Results](Screenshots/SQL_Screenshot_Moviri.png
)

## Author 
Alexis Santella 

email: <alexis.santella@gmail.com>
