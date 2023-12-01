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

# Output
```
vkpailodi@wirelessprv-10-193-78-210 design_patterns % /opt/homebrew/bin/python3 /Users/vkpailodi/Work/Github/design_patterns/client.py
***** Product A *******
Release date: Product A release date
Release Version: Product A software release version
Release Type: Product A release type

***** Product B *******
Release date: Product B release date
Release Version: Product B sw release version
Release Type: Product B release type
Build Number: Product B build number

***** Product A1 *******
Release date: Product A1 release date
Release Version: Product A1 software release version
Release Type: Product A1 release type

***** Product B1 *******
Release date: Product B1 release date
Release Version: Product B1 sw release version
Release Type: Product B1 release type
Build Number: Product B1 build number

***** Product A *******
Release date: Product A release date
Release Version: Product A software release version
Release Type: Product A release type

***** Product B *******
Release date: Product B release date
Release Version: Product B sw release version
Release Type: Product B release type
Build Number: Product B build number

***** Product A2 *******
Release date: Product A2 release date
Release Version: Product A2 software release version
Release Type: Product A2 release type

***** Product B2 *******
Release date: Product B2 release date
Release Version: Product B2 sw release version
Release Type: Product B2 release type
Build Number: Product B2 build number
```
