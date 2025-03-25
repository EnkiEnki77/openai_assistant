# API's allow one program to interface with another. Think about how Windows, Linux, and Mac offer
# a GUI to allow you to interface with your computer without having to run bash commands for every single
# thing you want to do. API's allow your software to interface with another piece of software without
# having to implement the other software yourself. They abstract away implementation details of the
# software being interfaced with.

# The key word is interface. A tv remote is an interface to interact with your TV. The tv remote
# only exposes the buttons, not the underlying circuitry and processes that actually control the tv.
# Just as a server hosting a REST API only exposes the endpoints, not the underlying code that backs said
# endpoints. API's allow your software to interface with certain features of another piece of software
# without needing to care about the implementation details of said feature. Implementation details are
# abstracted away.

# A REST API is an API hosted on a web server that provides RESTful endpoints to interface with functionality
# of the server.


# A module is the smallest piece of software, its a set of methods or functions ready to be used somewhere
# else. A module is just a file containing code which you use somewhere else. If a file is executed directly
# it's a script, if it's imported into and executed from another file then it's a module.
# Modules help you organize and make code more reusable.
# Modules can contain functions, classes, or variables.

# A package is essentially a collection of related modules grouped together into a folder. You can then
# import the package into a file and have access to all these related modules through a single interface.
# packages will contain an __init__ file, indicating it's a package, not just a normal directory.
# Packages help manage larger code bases by organizing related modules together.
# Packages can also contain sub packages.

# A library is a collection of both multiple pakages and modules that provide specific functionality. You
# don't have to write the code yourself. It's already written for you, just import the library and
# utilize it's API.
# When you utilize a library in your application the endpoints made available through the Library are the
# libraries API. Any interface that abstracts away implementation details is an API.
# Library is essentially synonymous with package, it's a catch all term. The difference comes in how the
# library/package is intended to be used. A library package such as numpy or pandas is intended to be
# imported and used across various applications for their reusable functionality. Whereas project-specific
# packages are likely intended to simply organize related modules together in the scope of a single application
# So to reiterate, packages used to simply organize related modules in the scope of a single application
# are simply packages. Packages that contain reusable functionality useful across multiple applications
# would be considered libraries. Though some people may still call them packages.
# Lastly, when a package/library is imported you are interacting with it's API, because it's implementation
# details are abstracted away, but their endpoints are exposed for you to interface with through the import.

# In the context of a single application, packages are primarily utilized for structure, they collect
# related modules together. You can take this even further by having sub packages, which have their own
# collection of modules.
# Libraries on the other hand, which are technically packages as well because they are a collection of
# modules and sub packages the same as a package, are less about adding structure to a single application
# and more about offering reusable functionality across multiple applications. Though a lot of the times
# the terms package and library will be used interchangeably.

# A framework is often times larger and more structured than a library, it provides a foundation and set
# of rules for building out applications. Meaning it's more opinionated. Unlike libraries, which give you
# the tools but leave you to make your own decisions about how to structure things in your app,
# frameworks have specific outlook and rules you must follow when using them. This speeds up development,
# because everything is already laid out for you in an efficient, organized way.
# Think of it like the skeleton to a house that guides you on how you should build the rest of the house.
# Django and NextJS are frameworks.




# Say you want to build something, you wouldnt build it without the proper tools. You could write absolutely
# everything you need for a piece of software from scratch, but this would be extremely time consuming to do
# especially for tools that youd likely use in pretty much every piece of software.
# This is where SDK's come into play, they are essentially a virtual tool box. Inside youll typically find
# files called libraries

# An SDK is essentially a toolbox for developing, building, and debugging an entire app in given ecosystem
# It can include modules, packages, libraries, frameworks, debuggers, etc. The Android SDK for example gives
# absolutely everything youd need to to build out Android apps.

# It's a full tool box containing everything youd need to build out an app in a given ecosystem, including
# modules, packages, libraries, frameworks, compilers, debuggers, and API, etc.

