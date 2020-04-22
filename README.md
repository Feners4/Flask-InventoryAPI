Example of an Inventory API using Flask, REST, and a MYSQL database.

## How to use:

```
git clone git@github.com:Feners4/Flask-InventoryAPI.git
cd Flask-InventoryAPI.git

```
Run virtual enviroment
`source ENV/bin/activate`

Start the Flask server
`python3 flask_server.py`

Now that the Flask server is running, in a browser we can go to `http://0.0.0.0:5000/` or the address you will use as home page for your server. 

In this specific project, there are three predefined routes:
```
http://0.0.0.0:5000/ (Home)
/addinventory
/checkinventory


```
A Swagger UI has been integrated for better use of API data structures. It can be accessed with `http://0.0.0.0:5000/api/ui`.

MySQL database has to be running. Database setup can be found in `mysqldb.py`.
