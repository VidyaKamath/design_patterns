from abc import ABC, abstractmethod

class IProductARelease(ABC):
    """
    _summary_
    Interface for creating Product A Release
    """
    def __init__(self, product_type):
        self.product_type = product_type
        super().__init__()

    @abstractmethod
    def get_release_date(self):
        pass

    @abstractmethod
    def get_sw_release_version(self):
        pass

    @abstractmethod
    def get_release_type(self):
        pass

    def publish_release_info(self):
       pass

class IProductBRelease(ABC):
    """
    _summary_
    Interface for creating Product B Release
    """
    def __init__(self, product_type):
        self.product_type = product_type
        super().__init__()

    @abstractmethod
    def get_release_date(self):
        pass

    @abstractmethod
    def get_sw_release_version(self):
        pass

    @abstractmethod
    def get_release_type(self):
        pass

    @abstractmethod
    def get_build_number(self):
        pass

    @abstractmethod
    def publish_release_info(self):
        pass
   
class ProductARelease(IProductARelease):
    def __init__(self, product_type):
        super().__init__(product_type)

    def get_release_date(self):
        return "Product A release date"
    
    def get_sw_release_version(self):
        return "Product A software release version"
    
    def get_release_type(self):
        return "Product A release type"

    def publish_release_info(self):
        release_date = self.get_release_date()
        sw_release_version = self.get_sw_release_version()
        release_type = self.get_release_type()
        print(f"***** Product {self.product_type} *******")
        print(f"Release date: {release_date}")
        print(f"Release Version: {sw_release_version}")
        print(f"Release Type: {release_type}\n")

class ProductA1Release(ProductARelease):
    def get_release_date(self):
        return "Product A1 release date"
    
    def get_sw_release_version(self):
        return "Product A1 software release version"
    
    def get_release_type(self):
        return "Product A1 release type"
       
class ProductA2Release(ProductARelease):  
    def get_release_date(self):
        return "Product A2 release date"
    
    def get_sw_release_version(self):
        return "Product A2 software release version"
    
    def get_release_type(self):
        return "Product A2 release type"

class ProductBRelease(IProductBRelease):
    def get_release_date(self):
        return "Product B release date"
    
    def get_sw_release_version(self):
        return "Product B sw release version"
    
    def get_release_type(self):
        return "Product B release type"

    def get_build_number(self):
        return "Product B build number"
    
    def publish_release_info(self):
        release_date = self.get_release_date()
        sw_release_version = self.get_sw_release_version()
        release_type = self.get_release_type()
        build_number = self.get_build_number()
        print(f"***** Product {self.product_type} *******")
        print(f"Release date: {release_date}")
        print(f"Release Version: {sw_release_version}")
        print(f"Release Type: {release_type}")
        print(f"Build Number: {build_number}\n")

class ProductB1Release(ProductBRelease):
    def get_release_date(self):
        return "Product B1 release date"
    
    def get_sw_release_version(self):
        return "Product B1 sw release version"
    
    def get_release_type(self):
        return "Product B1 release type"

    def get_build_number(self):
        return "Product B1 build number"

class ProductB2Release(ProductBRelease):
    def get_release_date(self):
        return "Product B2 release date"
    
    def get_sw_release_version(self):
        return "Product B2 sw release version"
    
    def get_release_type(self):
        return "Product B2 release type"

    def get_build_number(self):
        return "Product B2 build number"
