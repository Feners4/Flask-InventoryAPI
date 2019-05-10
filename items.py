from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
ITEMS = {
    "MacbookAir2017": {
        "iname": "MacbookAir7,2",
        "timestamp": get_timestamp()
    },
    "MacbookPro2015": {
        "iname": "",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "iname": "Bunny",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
