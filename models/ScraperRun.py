from datetime import date
from typing import List
from models.Product import Product
from models.Store import Store

class ScraperRun:
    def __init__(self, run_id: int, store: Store, products: List[Product], filters: List[str], arguments: List[str]):
        """
        Class that represents a scraper run.

        :param run_id: Unique identifier for the run (int)
        :param date: Date when the run was executed (date)
        :param store: Name of the target store (Store)
        :param products: List of products obtained in the run (List[Product])
        :param filters: List of filters applied during the run (List[str])
        :param arguments: List of additional arguments used in the run (List[str])
        """
        self.run_id = run_id
        self.date = date.today().strftime("%d/%m/%Y")
        self.time = date.today().strftime("%H:%M:%S")
        self.store = store
        self.products = products
        self.filters = filters
        self.arguments = arguments
