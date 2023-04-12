# COVID-19 vaccination tracker

Building an interactive multi-page dashboard app to visualize COVID-19 vaccination data, specifically: 
1. New COVID-19 cases and new vaccinations throughout the pandemic (page 1). 
2. Top countries for each vaccine manufacturer (page 2)
3. Market share of each vaccine manufacturer per country (page 3)

## Data 

Obtained from Our World in Data COVID-19 GitHub repository. The data in this repository is regularly updated and every time you run the app, the most recent dataset is used. 

More info about the data can be found [here](https://github.com/owid/covid-19-data/blob/master/public/data/README.md).

## To run the app 

1. Download `Vaccine dashboard` folder and open it with Python IDE
2. Install and import required libraries to your environment
4. Click on the generated URL to run the app on the browser

Check out the `notebook.ipynb` file to see how the graphs for the dashboard were created! 


## Page 1 demo 
![](cases_vaccinations_by_country.gif)

## Page 2 demo 
![](manufacturer_top_countries.gif)


## Page 3 demo 
![](manufacturers_by_country.gif)


## Bonus bubble plot 
Illustrates how higher income countries had earlier access and faster immunization rates compared to lower income countries 
![](vaccination_gdp.gif)
