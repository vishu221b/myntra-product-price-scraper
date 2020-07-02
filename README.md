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
For example consider this link ```https://xyz.com/abc```

Now this link has 2 parts, **https://xyz.com** is the **URL(unique resource locator)**
<br> while the **/abc** is the **URI(Unique Resource Identifier)** or **view** in this case.
<hr>
Basic setup
<br>
<br>

```
To set up the project locally, follow the below steps:

1. Clone the repository locally (using git clone or zip download)
2. Open terminal and cd into the project repository (where you have cloned/downloaded the repo)
3. run command 'pip install -r requirements.txt', this will install the required dependencies
4. run command python app.py
```

**Note-**
All the new views must be added inside the **constants.py** file. More can be added in the same format
 same as the other views inside the file.