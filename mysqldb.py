import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Tulipanes5',
                             db='inventoryList',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def CheckInventory():
	try:
		cursorObject = connection.cursor()
		inventorylist = cursorObject.execute('show databases')
		print(inventorylist)
		for (inventorylist) in cursor:
			print(inventorylist[1])
	finally:
		return "TEST"