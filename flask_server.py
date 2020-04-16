from flask import render_template, request
from mysqldb import CheckInventory, sendValue

import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# URL route for displaying items in MySQL inventory
@app.route('/checkinventory/')
def inve():
	return CheckInventory()

# URL route for adding items to MySQL inventory through user input in rendered page
@app.route('/addinventory/')
def addInv():
    return render_template('inputdata.html')

@app.route('/getValue',methods=['POST','GET'])
def getValueform():
    value = request.form['itembox']
    processed_value = value.upper()
    sendValue(processed_value)
    return render_template('inputdata.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
