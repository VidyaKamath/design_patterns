from factory import IProductReleaseFactory, ProductReleaseFactory_1, ProductReleaseFactory_2

def notify_client_to_publish(product_release_factory: IProductReleaseFactory, product_type):
	# Factory Pattern: Intent is to seperate the 
	# responsibility of object creation from the client

	# Adding new products will not impact the client code 
	# Creating the Product release object for a given factory and 
	# product type is delegated to the Factory class.

	product_release_info = product_release_factory.get_product_release(product_type)
	product_release_info.publish_release_info()

if __name__ == "__main__":
	# suppose the client gets notified about the publish of the 

	notify_client_to_publish(ProductReleaseFactory_1(), "A")
	notify_client_to_publish(ProductReleaseFactory_1(), "B")
	notify_client_to_publish(ProductReleaseFactory_1(), "A1")
	notify_client_to_publish(ProductReleaseFactory_1(), "B1")

	notify_client_to_publish(ProductReleaseFactory_2(), "A")
	notify_client_to_publish(ProductReleaseFactory_2(), "B")
	notify_client_to_publish(ProductReleaseFactory_2(), "A2")
	notify_client_to_publish(ProductReleaseFactory_2(), "B2")
