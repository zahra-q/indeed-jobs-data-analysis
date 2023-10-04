# indeed-jobs-data-analysis
Created a python web scraper to scrape Indeed for job details and stored it in MySQL. Performed data cleaning using SQL and then visualized the data using power BI.

## About the Files:
- jobscraper.py: This program scrapes indeed.com for job related data. The details extracted include:
  1. Job title
  2. Company name
  3. Rating
  4. Salary
 
- indeedjobs.pbix: the dashboard made in Power BI


## Data Cleaning

The data extracted from Indeed was dirty and needed to be cleaned. The tasks were performed in SQL and power BI and included:
1. Removing null values
  - Used power bi to remove rows where column values were Null.
2. Dropping irrelevant columns
  - In this case, the "job details" column only had null values, so we drop it using Power BI.
3. Removing duplicate rows
  - First we check for duplicates:

    ![image](https://github.com/zahra-q/indeed-jobs-data-analysis/assets/58932323/10f8dad2-43a8-49ab-b01e-89ee85960cab)
  - Remove them:

    ![image](https://github.com/zahra-q/indeed-jobs-data-analysis/assets/58932323/28552ebd-dbdb-4d98-b006-9bc73536b378)


5. Formatting the columns values

The "salary" column consisted of values in different forms:
- it had ranges, e.g. $24,000-$30,000
- it had yearly salaries
- monthly, hourly salaries
- salary values were prefixed by text e.g. "$24 an hour"
- salary column type was text

We needed to format this data by bringing it on the same scale e.g. yearly basis, and removing any extra text from it, and if the values were in a range then taking average of the range to get only one value. Here's the sql code:
![image](https://github.com/zahra-q/indeed-jobs-data-analysis/assets/58932323/85c866ce-2c90-4c1b-9776-221f1875d535)

![image](https://github.com/zahra-q/indeed-jobs-data-analysis/assets/58932323/ad61a666-749f-417b-b3d4-b8dbc49a2493)


6. Converting variable data types

As shown above, we converted salary column type from text to float. We also needed to convert the rating column data type to float: 
![image](https://github.com/zahra-q/indeed-jobs-data-analysis/assets/58932323/a035dee2-82c5-4b95-aa6d-3d4dd339f911)



