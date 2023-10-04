import requests
from bs4 import BeautifulSoup
import mysql.connector

# Create a MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="WxLd45h81!#y"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Define a function to sanitize and clean data
def clean_data(data):
    if data is not None:
        return data.strip()
    return None

#create a new database if it doesn't exist already
create_database_query = "CREATE DATABASE IF NOT EXISTS indeedjobs"

try:
    # Execute the database creation query
    cursor.execute(create_database_query)
    print("Database 'your_database' created or already exists.")
except Exception as e:
    print("Error creating database:", str(e))

# Switch to the newly created database
db.database = "indeedjobs"

# Create the 'jobs' table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS indeedjobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name_of_the_job VARCHAR(255),
    name_of_the_company VARCHAR(255),
    rating VARCHAR(255),
    salary VARCHAR(255),
    job_details TEXT
)
"""

try:
    # Execute the table creation query
    cursor.execute(create_table_query)
    print("Table 'jobs' created or already exists.")
except Exception as e:
    print("Error creating table:", str(e))


for page_number in range(0,300):

# URL to scrape
    target_url = "https://api.scrapingdog.com/scrape?api_key=651241613682284a59b3a004&url=https://www.indeed.com/jobs?q=&l=New+York%2C+NY&radius=35&start={page_number * 10}&pp=gQAAAAAAAAAAAAAAAAACEoNWmwADAAABAAA&vjk=d88143ba664bc255&dynamic=false"
    resp = requests.get(target_url)
    print(resp.status_code)
    soup = BeautifulSoup(resp.text, 'html.parser')
    allData = soup.find("ul", {"class": "css-zu9cdh eu4oa1w0"})
    alllitags = allData.find_all("div", {"class": "cardOutline"})
    print(len(alllitags))

    # Define a function to sanitize and clean data
    def clean_data(data):
        if data is not None:
            return data.strip()
        return None

    # Iterate through job listings and store data
    for i in range(0, len(alllitags)):
        try:
            name_of_the_job = clean_data(alllitags[i].find("a", {"class": "jcs-JobTitle css-jspxzf eu4oa1w0"}).text)
        except:
            name_of_the_job = None
        try:
            name_of_the_company = clean_data(alllitags[i].find("div", {"class": "companyInfo"}).find("span", {"class": "companyName"}).text)
        except:
            name_of_the_company = None
        try:
            rating = clean_data(alllitags[i].find("div", {"class": "companyInfo"}).find("span", {"class": "ratingsDisplay"}).text)
        except:
            rating = None
        try:
            salary = clean_data(alllitags[i].find("div", {"class": "salary-snippet-container"}).text)
        except:
            salary = None
        try:
            job_details = clean_data(alllitags[i].find("div", {"class": "metadata taxoAttributes-container"}).find("ul").text)
        except:
            job_details = None

        # SQL statement to insert data into the 'jobs' table
        insert_query = "INSERT INTO indeedjobs (name_of_the_job, name_of_the_company, rating, salary, job_details) VALUES (%s, %s, %s, %s, %s)"

        # Data to be inserted
        data = (name_of_the_job, name_of_the_company, rating, salary, job_details)

        try:
            # Execute the SQL query
            cursor.execute(insert_query, data)
            # Commit changes to the database
            db.commit()
            print("Data inserted successfully.")
        except Exception as e:
            # Rollback in case of an error
            db.rollback()
            print("Error inserting data:", str(e))

# Close the cursor and database connection
cursor.close()
db.close()