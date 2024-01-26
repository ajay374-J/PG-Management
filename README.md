# PG-Management
PG Management App

## Usage
### 1. Installation
Navigate to the bench directory and run the following command:
> bench get-app frepple https://github.com/ajay374-J/PG-Management --branch master

Install the app onto your site.
> bench --site [your.site.name] install-app pg_management

Bench start
> bench start

Pg Management Workspace
<img width="866" alt="PG Management main page" src="https://github.com/ajay374-J/PG-Management/blob/master/pg_management/images/Screenshot%202024-01-26%20at%206.59.36%E2%80%AFPM.png">

### 2. Room Booking Page
Guest Will See AVailable Room & Book Room from This WebPage
<img width="866" alt="PG Management main page" src="https://github.com/ajay374-J/PG-Management/blob/master/pg_management/images/Screenshot%202024-01-26%20at%206.24.37%E2%80%AFPM.png">
<img width="866" alt="PG Management main page" src="https://github.com/ajay374-J/PG-Management/blob/master/pg_management/images/Screenshot%202024-01-26%20at%206.24.37%E2%80%AFPM.png">
<img width="866" alt="PG Management main page" src="https://github.com/ajay374-J/PG-Management/blob/master/pg_management/images/Screenshot%202024-01-26%20at%206.24.45%E2%80%AFPM.png">
When Submit Of Webpage Customer Doctype & Room Booking Details Doctype Entry Will Create


###3.Working Details
    DOctypes:
    1) Room ---PG Manager Will Create Room & Update Room Details: Wrriten Background Job To update Room Status
    
    2)Customer---Entry Automatically Created when Guest Submit web form.
    
    3)Room Booking details--This Will also Automatically Create,In this DOctype Have 2 Date Fields 1st field is checkin date & 2nd Field is checkout Date,When Pg Manager Enters
      checkout date Amount will Calculate Automatically.
      
    4)Pg Work--This doctype Is master of Work in Pg .in This Master We Need to Define Job Schedule in days

    5)Pg employee-This Doctype Is master Of Employee Worked in Pg 

    6)Work Log--Background Job written For Create Work Log automatically.The Job Equally Distribute work in Employee As per Schdule days.




