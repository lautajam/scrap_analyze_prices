from datetime import datetime

class Product:
    def __init__(self, name, price, rating, 
                       description, has_installments, has_interest_on_installments, 
                       installments_count, installments_price, sales_position, 
                       in_stock, stock_quantity):
        """
        Initializes a Product object with the following attributes:
        
        :param name: Name of the product (str)
        :param price: Price of the product (float)
        :param rating: Rating of the product (float)
        :param description: Description of the product (str)
        :param has_installments: Indicates if the product has installment options (bool)
        :param has_interest_on_installments: Indicates if the product has interest on installments (bool)
        :param installments_count: Number of installments available for the product (int)
        :param installments_price: Price per installment of the product (float)
        :param sales_position: Sales position of the product (str)
        :param in_stock: Indicates if the product is in stock (bool)
        :param stock_quantity: Quantity of the product available in stock (int)
        """
        
        self.name = name
        self.price = price
        self.rating = rating
        self.description = description
        self.has_installments = has_installments
        self.has_interest_on_installments = has_interest_on_installments
        self.installments_count = installments_count
        self.installments_price = installments_price
        self.sales_position = sales_position
        self.in_stock = in_stock
        self.stock_quantity = stock_quantity
