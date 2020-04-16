import pymysql.cursors
from datetime import datetime

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Tulipanes5',
                             db='inventory',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

ITEMS = {}

# Add items taken from User input to MySQL inventory
def addInventorySQL(items):
    itemsList = list(items.values())
    connection.cursor().executemany("""
    INSERT INTO Apple(iname, timestamp)
    VALUES (%(iname)s, %(timestamp)s)""", itemsList)
    connection.commit()
    print ("MYSQL DB UPDATED!!")

# Check items in MySQL inventory and create the list of items from our data
def CheckInventory():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Apple")
        results = cursor.fetchall()

    return  str(results)

    ##return [ITEMS[key] for key in sorted(ITEMS.keys())]

# Update ITEMS dictionary with items to be added
def populateItems(dictionary):
    ITEMS.update(dictionary)
    return addInventorySQL(ITEMS)

# Match user input to item and initiate sending to MySQL inventory
def sendValue(value):
    dictionary = {}
    if value == "MACBOOKAIR7,2":
        dictionary["MacbookAir2017"] = {'iname': "MacbookAir7,2", 'timestamp': get_timestamp()}
        populateItems(dictionary)

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
