# Multi-page_COVID-19_vaccination_dashboard_app

Building an interactive multi-page dashboard app to visualize COVID-19 vaccination data. 

## Data 

Obtained from Our World in Data COVID-19 GitHub repository.

More info about the data can be found [here](https://github.com/owid/covid-19-data/blob/master/public/data/README.md).

## To run the app 

1. Download `Vaccine dashboard` folder and open with PyCharm
2. Install and import libraries below to your environment
4. Click on the generated URL to run the app on the browser

```
import dash
from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
```

Check out the `notebook.ipynb` file to see how the graphs for the dashboard were created! 


## Page 1 demo 
![](cases_vaccinations_by_country.gif)

## Page 2 demo 
![](manufacturer_top_countries.gif)


## Page 3 demo 
![](manufacturers_by_country.gif)


## Bonus graph 
Illustrates how higher income countries had earilier access and faster immunization rates compared to lower income countries 
![](vaccination_gdp.gif)
