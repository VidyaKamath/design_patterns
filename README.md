# Design Patterns example

This repository shows an example of using Factory, Abstract Factory Pattern.

- Factory Pattern is used to abstract out the responsibility of creating various `ProductRelease` objects from the client. This follows SRP.

- Abstract Factory pattern is implemented to enable the `notify_client_to_publish` to operate on different choices of `ProductReleaseFactory`.
    - Here, the `notify_client_to_publish` uses the interface `IProductReleaseFactory` without depending on the concrete Factory Class.

- Interface Segregation Principle
   - ProductARelease implements its interface IProductARelease which has only the methods needed by the ProductARelease class.
   - ProductBRelease implements its interface IProductBRelease which has only the methods needed by the ProductBRelease class.

- Liskov Substitution principle
   - `ProductA1Release is a child class of `ProductARelease` and does not violate LSP.
      - We can substitute the parent class instance with the child instance without breaking the code.
