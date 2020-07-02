# Myntra-Price-Scraper
A very simple web scraper project that scrapes **https://myntra.com** at different views
to collect the product wise data located under that view.

```
Dependencies for this project:

[+] requests - used for fetching data from websites
[+] prettytable - used for displaying data in tabular format
```
<hr>
A view is the 'URI(Unique resource identifier)' part of the website.
<br><br>

For example consider the link ` https://xyz.com/abc`

Now this link has 2 parts, **https://xyz.com** is the **URL(unique resource locator)**
<br> while the **/abc** is the **URI(Unique Resource Identifier)** or **view** in this case.
<hr>

## Basic setup
```
To set up the project locally, follow the below steps:

1. Clone the repository locally (using git clone or zip download)
2. Open terminal and cd into the project repository (where you have cloned/downloaded the repo)
3. run command 'pip install -r requirements.txt', this will install the required dependencies
4. run command python app.py
```

## Adding Views
```
For adding more views for myntra, following steps must be followed
1. Create a constant in the 'constants.py' file
2. Add an enum for that constant in 'enums.py' under class 'EndpointMap' with the exactly same name as the constant name
3. Map the value of the original constant to the enum
4. Add the Enum to the 'ALL_ENDPOINTS_MAP' in 'enums.py'

Example - 

DUMMY_CONSTANT = "/dummy"  # added in constants.py

DUMMY_CONSTANT = constants.DUMMY_CONSTANT  # added under 'EndpointMap' enum class in 'enums.py'

ALL_ENDPOINTS_MAP = {
    1: ......
    2: ......
    3: ......
    4: EndpointMap.DUMMY_CONSTANT   # added the enum from the 'EndpointMap' enum class into the main endpoints map
}                                   # all the endpoints are fetched using this MAP in the menu

```
## Important Note

While adding constants, make sure to stick to the following conventions for better readability:
- Make sure to add the constant variable names in uppercase
- Make sure that the constant being added to the EndpointMap enum class has exactly the same name as that of the constant, in uppercase
 