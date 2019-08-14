from datetime import datetime
from mysqldb import CheckInventory

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
ITEMS = {
    "MacbookAir2017": {
        "iname": "MacbookAir7,2",
        "timestamp": get_timestamp()
    },
    "MacbookPro2015": {
        "iname": "MacbookPro11,5",
        "timestamp": get_timestamp()
    },
    "iMac2015": {
        "iname": "iMac17,1",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/item
    with the complete lists of items

    :return:        sorted list of items
    """
    # Create the list of items from our data
    return [ITEMS[key] for key in sorted(ITEMS.keys())]

def readSQL():
    return CheckInventory()
