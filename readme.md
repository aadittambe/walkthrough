# South Carolina schools explorer

## About

This repository contains the data and code used to produce a South Carolina public schools dashboard for The Post & Courier. 

School data comes from the [South Carolina Department of Education](https://ed.sc.gov/data/report-cards/sc-school-report-card/)’s annual report cards and additional data files for the years 2017-2021. Academic performance data based on state tests is not available for 2020. (Tests were canceled that year because of COVID-19.)

### Accessing processed data

Instructions for where the process data can be accessed. Basic description of what this data is, how it was cleaned, where the cleaning script can be found.

### Internal database

The two processed CSVs are loaded into Datasette, an open-source tool for exploring and publishing data. The application can be viewed [here](https://sc-education-data-app.herokuapp.com/).

### External dashboard

To visualize and present some of the variables from the processed data, we loaded the CSVs into a Flask-based web application. The framework depends on Jinja2, a templating engine for Python. Jinja2’s templating inheritance made it possible for us to create a similar layout for district, school and homepages, and Flask made it possible for us to load data in from a CSV. When the app is ready for publishing, Flask uses it Frozen-Flask, to “freeze” the application into a bunch of static files, which can be uploaded to an FTP server.

To run the application, from a command prompt, open the directory:

```
cd public-dashboard
```

Then, use `pipenv` to create a virtual environment. Run:

```
pipenv shell
```

Next, install the Python packages, by running:

```
pipenv install
```

*Instructions for setting up a virtual environment can be found [here](https://pipenv.pypa.io/en/latest/install/).*

Use Python3 to run the Flask application. Run:

```
python3 app.py
```

Visit `[localhost:5000/](localhost:5000/)` in a browser to view and develop the application.

Once the application is developed, and ready to be built, run:

```
python3 freeze.py
```

This command will create a build directory, with flat HTML files.

#### Application functionality, helper scripts and miscellanous code snippets

##### Geocoding

Before the data is loaded into the application, we are using two scripts to geocode schools and school districts. These scripts were written to build maps and load them into the web application.

**a. Getting coordinates for schools**
We used a Python notebook, which can be found [here](/public-dashboard/geocoding/a-get-school-coords/getcoords.ipynb), to query the open-source Nominatim API to get latitude and longitude information for schools in the state.

**b. Matching geojsons to district data**

After getting a geojson of South Carolina's school districts, we used used R’s geojson.io package to join demographic features of school districts to geometries of districts. The script performing the join can be found [here](/public-dashboard/geocoding/b-match-geojsons-and-districts.Rmd). 

##### Application search

The search functionality within the application is handled by a JavaScript library called [Fuse.js](https://fusejs.io/). The script powering the search functions can be found [here](/public-dashboard/static/search.js)


##### Charts

The application uses a JavaScript library called [D3](https://d3js.org/) to build charts at scale. The functions for building charts can be found in the [district template HTML file](/public-dashboard/templates/district.html).

##### Maps
The application uses a JavaScript library called [Leaflet](https://leafletjs.com/) to build maps. The scripts for building maps can be found in the [template HTML file](/public-dashboard/templates/index.html).

