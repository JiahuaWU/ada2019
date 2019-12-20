# Secrets Behind Recipes
data story link: http://ty-dong.github.io

# Abstract
Cooking is an important skill for everyone, no matter where they live. After evolving for centuries, what people eat everyday has grown into systems. Every country has their own style of eating and the styles diverge from region to region. Through the recipes, we can know what is frequently eaten by the people of one country and how they usually cook. We can even go further, find the relationships between what people eat and how their health conditions are, and dig out all the secrets behind the recipes.

In this project, we want to show the different cooking choices of ingredients, seasoning, etc. among countries. Then we will try to link the recipe features with people's health condition to find out if there is something in eating habits that influences people's health. Besides, using the instructions of cooking steps of each recipe, we will map the recipes to vector space so that we can measure the difference of recipes among countries. To go even further, we want to train a model to predict the flavors of a dish, given its recipe, so that we know the flavor preference of people in different countries. In the end, after all these analysis of people's preference, we hope to make a recommendation system so that we can recommend dishes to people if we know their previous beloved food or the ingredients they have.

# Research questions
How do eating habits vary in different countries?
- the most frequently used seasoning
- the most common cooking methods(boil, stew, fry, etc)
- the most frequently used ingredients (except seasoning) in general 

How are the different eating habits related to health?
- Analyze correlation between some health indices like the life span, overweight rate, high blood pressure, etc with common seasonings and cooking methods.
- find relationshp between some common food-related disease and eating habits: cancer, obesity. We will get the death rate of some food-related diseases in different countries and then compare them with their different eating habits, for example, cooking methods and main ingredients or seasoning in foods.

# Dataset
The two dataset about recipes we used are collected from Kaggle (https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions). One of them contains 230185 different recipes scraped from Food.com (https://www.food.com/" and includes information about the cooking steps, ingredients, time needed, tags, etc. Through the tags of the recipes, we could figure out where the dish originates from. By matching the countries with recipes, we get 96286 recipes from 51 different countries.

The other dataset is about ratings and comments on the recipes by the users of Food.com. The reviews and the corresponding recipe id enable NLP analysis of people's feedback towards recipes. 

To learn the relationship between recipes and health, we use datasets about noncommunicable diseases (https://www.who.int/data/gho/data/themes/noncommunicable-diseases/GHO/noncommunicable-diseases") and body mass index (BMI) (https://www.who.int/data/gho/data/themes/theme-details/GHO/body-mass-index-(bmi)) from WHO in 2016. The GDP dataset from The World Bank (https://data.worldbank.org/indicator/NY.GNP.PCAP.CD) is also used to balance the influence of economy on citizens' health conditions.

# A list of internal milestones up until project milestone 3

17.11

- Download the required data
- Search for additional information on quantities of each ingredient usage corresponding to the recipes, scrape data to augment dataset.

23.11

- Data cleaning for newly found data (identification and removal of invalid data)
- Extract countries(regions) informations from raw dataset and classify recipes according to continents. It helps analysis distributions and patterns on different granularity level.
- Extract flavors from user description, using it as target label for further multi-class classification training. 
- Classify recipes by meal types, explore most common used ingredients and cooking method of each country

10.12

- build and test the correlation between food and disease occurance on the level of countries(regions)
- train classification model to predict flavors of recipes based on ingredients inputs.
- train regression model to predict nutritions of recipes based on ingredients and cooking methods.
- NLP processing for recipe instructions and ingredients to find similarities between different recipes and cluster them. It is also possible to establish recommendation system based on recipe similiarity. 
- implement recommendation system based on matrix factorization.

18.12

- Compare the effectiveness of trained model 
- Explore possibilities for the data visualization
- Summarize results and figures, find the best way to present them in datastory

23.12

- Comment and refactor our code
- Release of final notebook and datastory

# Contributions

Tianyang Dong: data cleaning, website design, data visualization.

Wei Jiang: health and seasoning relationship analysis, data visualization.

Huajian Qiu: similarity analsysis using PCA and t-SNE, data visualization.

Jiahua Wu: deep data cleaning, nutrition choropleth map, data visualization.
