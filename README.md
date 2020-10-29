
# User Authentication
This repo includes user registration and login, logout , search users data etc. with the authentication token .

Steps :

- Cretaed Schema
- Created Table
- Model and API written , URLs added
- Testing
- Lastly added pagination

- For Registion Use : localhost:9000/restapis/registration/ 
Request : { 
  "username":"artikhot", 
  "password":"Password@1997!", 
  "first_name":"arti", 
  "last_name":"khot", 
  "empolyee_id":"123", 
  "organiztion_name":"ABC" 
}

- For Login User : localhost:9001/restapi/login_user/ with Token
Response { 
  "message": "Login Successful", 
  "token": "b04fb99e21325783afd8a6b4d30bb9b0ff7089d1" 
}

- Get List of All User : localhost:9001/restapi/get_list/

- Pagination Details: localhost:9001/restapi/pagination_list/?page=1

- Search Data: localhost:9001/restapi/search_data_by_condition/?last_name=khot

Install Some Packages :
djangorestframework==3.6.3
pip install mysql-connector
pip install mysqlclient==1.3.7
MySQL-python==1.2.5

Install Mysql Reference Link :
https://dev.mysql.com/downloads/mysql/

Install and connect with Root and Password 
Please Remeber password


