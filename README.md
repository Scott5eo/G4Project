# G4Project
IB group 4 project (computer science)
Group Members: Dongjin Seo, Saksham Bajaj, Ushir Babhania, Amir Imam

Research Question: How can technology be used to estimate or predict the amount of water evaporated to air in a waterpark affected by desert climate and weather.

Materials used: Water sample from Aquaventure Waterpark, weather data from Yahoo weather api. 

Code: 
An api handling class that deals with the Yahoo Weather API.
A main class that calculates the water evaporated using weather information.

Equation used to estimate the evaporation rate will be:
gh = Θ A (xs - x)

where
gh = amount of evaporated water per hour (kg/h)

Θ = (25 + 19 v) = evaporation coefficient (kg/m2h)

v = velocity of air above the water surface (m/s)

A = water surface area (m2)

xs = maximum humidity ratio of saturated air at the same temperature as the water surface (kg/kg)  (kg H2O in kg Dry Air)

x = humidity ratio air (kg/kg) (kg H2O in kg Dry Air)
SOURCE: https://www.engineeringtoolbox.com/evaporation-water-surface-d_690.html


Dependencies:
Weather-api: pip install weather-api
