# auto test framework based on python behave
- BDD framework - python behave
- send requests
- setup/teardown by access database
- verify response

# dependence
- pip install requests
- pip install behave

# structure
- libs: common libs
- features/steps: test step lib
- features/steps/`__init__`.py: include
- features/steps/<suite>/`__init__`.py: include
- features/suites: test suite dir


# how to run test
- cd http-api-test-framework-python-behave
- behave