from api import fetch_resources
from ui import ui

def main():
    fetch_resources()
    user_interface = ui()
    user_interface.run()
    
if __name__ == "__main__":
    main()