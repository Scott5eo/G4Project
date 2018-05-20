# G4Project
IB group 4 project (computer science)
Group Members: Dongjin Seo, Saksham Bajaj, Ushir Babhania, Amir Imam

Research Question: How can technology be used to estimate or predict the amount of water evaporated to air in a waterpark affected by desert climate and weather.

Materials used: Water sample from Aquaventure Waterpark, weather data from Yahoo weather api. 

Code: 
An api handling class that deals with the Yahoo Weather API.
A main class that calculates the water evaporated using weather information.

Equation used to estimate the evaporation rate will be the US EPA evaporation equation:
E = 7.4PA(0.447W)^0.78 / (T + 459.67), where 
E = Evaporation Rate (Gallons/Day)
A = Pool Surface Area (ft2)
W = Wind Speed Above Pool (mph)
P = Water's Vapor Pressure (mmHG) at Ambient Temperature
T = Temperature (°F)
