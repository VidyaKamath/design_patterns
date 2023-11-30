from abc import ABC, abstractmethod

# Interface 
class IProductRelease(ABC):
	def __init__(self, product_type):
		self.product_type = product_type
		super().__init__()
	@abstractmethod
	def get_release_date():
		pass

	@abstractmethod
	def get_sw_release_version():
		pass

	@abstractmethod
	def get_release_type():
		pass

# Concrete classes implementing the interface
class ProductARelease(IProductRelease):
	
	def get_release_date(self):
		return "Product A release date"
	
	def get_sw_release_version(self):
		return "Product A sw release version"
	
	def get_release_type(self):
		return "Product A release type"

class ProductBRelease(IProductRelease):
	
	def get_release_date(self):
		return "Product B release date"
	
	def get_sw_release_version(self):
		return "Product B sw release version"
	
	def get_release_type(self):
		return "Product B release type"

class ProductReleaseFactory():
	def __init__(self, product_type):
		self.product_type = product_type
	
	def get_product_release(self):
		if self.product_type == "A":
			return ProductARelease(self.product_type)
		if self.product_type == "B":
			return ProductBRelease(self.product_type)
		else:
			raise Exception(f"{self.product_type} not found")
		# Any new product type can be added by extending this Factroy class
