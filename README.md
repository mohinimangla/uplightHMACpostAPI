# uplightHMACpostAPI
Creating a post request to generate HMAC token given a message
- User verification added so only a specific user can access the endpoint
- Secret key has been set in config json to generate the HMAC token
- the endpoint generates the HMAC token for the entire json object provided and based on that foloowing cases have been handled
    - if the data payload is not a json object, 400 error is thrown
    - if the data payload is empty 400 error is thrown
    - if the provided json already contains a `signature` field, 400 error is thrown

### Setup

1. install python and pip for running the dev server
2. this sets up the server to make request to the apis
3. run pip install -r requirements.py
4. run python main.py

### URL Endpoints

- /generate-token - post request returns a response with a JSON payload that includes a signature field with the generated HMAC token.

### Testing
    
- Run test.py python module in console
    
- Sample result: 
```	
>>> python unittests.py 
......
----------------------------------------------------------------------
Ran 6 tests in 0.028s

OK
```

## Application Structure
- `Endpoints` /generate-token is defined by registering the resource in main.py
- `Resource` is defined in resource.py. Here the query parameters are fetched from the request and logic is defined for parsing data models and formatting results for output
- `Configuration` contains the info to validate user authorization and key for generating HMAC token
- `Unit tests` have been created in unittest.py