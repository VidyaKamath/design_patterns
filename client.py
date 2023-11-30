from factory import IProductRelease, ProductReleaseFactory

def publish_release_info(product_release_info: IProductRelease):
	release_date = product_release_info.get_release_date()
	sw_release_version = product_release_info.get_sw_release_version()
	release_type = product_release_info.get_release_type()
	print(f"***** Product {product_release_info.product_type} *******")
	print(f"Release date: {release_date}")
	print(f"Release Version: {sw_release_version}")
	print(f"Release Type: {release_type}\n")


def notify_client(product_type):
	# Scenario 1 - Factory Pattern
	# Intent is to seperate the responsibility of object creation from the client

	# Adding new products will not impact the client code 
	# Creating the Product release object for a given product type is delegated to the Factory class.

	product_release_factory = ProductReleaseFactory(product_type)
	product_release_info = product_release_factory.get_product_release()
	publish_release_info(product_release_info)

if __name__ == "__main__":
	notify_client(product_type="A")
	notify_client(product_type="B")
