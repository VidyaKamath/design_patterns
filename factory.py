from abc import ABC, abstractmethod
from product_release import (
    ProductARelease,
    ProductBRelease, 
    ProductA1Release, 
    ProductA2Release, 
    ProductB1Release, 
    ProductB2Release)

class IProductReleaseFactory(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def get_product_release(self, product_type):
        pass

class ProductReleaseFactory_1(IProductReleaseFactory):
    def __init__(self):
       super().__init__()

    def get_product_release(self, product_type):
        if product_type == "A":
            return ProductARelease(product_type)
        elif product_type == "A1":
            return ProductA1Release(product_type)
        elif product_type == "B":
            return ProductBRelease(product_type)
        elif product_type == "B1":
            return ProductB1Release(product_type)
        else:
            raise Exception(f"{product_type} not found")

class ProductReleaseFactory_2(IProductReleaseFactory):
    def __init__(self):
       super().__init__()

    def get_product_release(self, product_type):
        if product_type == "A":
            return ProductARelease(product_type)
        elif product_type == "A2":
            return ProductA2Release(product_type)
        elif product_type == "B":
            return ProductBRelease(product_type)
        elif product_type == "B2":
            return ProductB2Release(product_type)
        else:
            raise Exception(f"{product_type} not found")
