from datetime import datetime

class Store:
    def __init__(self, store_id: int, name: str, url: str, country: str, location: str = None):
        """
        Initializes a store with the provided attributes.
        
        :param store_id: Unique identifier for the store (int)
        :param name: Name of the store (str)
        :param url: URL of the store (str)
        :param country: Country of the store (str)
        :param location: Location of the store (optional, str)
        """
        self.store_id = store_id
        self.name = name
        self.url = url
        self.location = location
        self.country = country
        self.date_created = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

