# When working with pachages, this imports from __init__.py file
from app import app

# Only true when this script is run directly, as stated above
if __name__ == "__main__":
    # Running in debug mode so that changes take effect without restarting web server
    app.run(debug=True)
    

