# Design And Implementation Of Smart Doorbell

## My database models, and their relations are showing in the below picture

![ERD DIAGRAM](erd.png)

i use jwt token for login and this token has two main tokens access token and refresh tokens and the url for testing is
in below:

` http post http://127.0.0.1:8000/api/token/ username=mahdi  password=Ma13761376@ `

chromium-browser --disable-web-security --user-data-dir="/home/mahdi"

http GET 127.0.0.1:8000/hello/ 'Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0MTIxMjU3LCJqdGkiOiI2MzczYWNkODY0NzE0ZDUzYTgxZjcwYzk2ZWI3MTIwNSIsInVzZXJfaWQiOjF9.W1flCrkz3HovBz7Q_H3hmeX0-Dhj0ZrgNhoZLimY2PE'
