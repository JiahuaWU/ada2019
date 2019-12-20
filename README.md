# Secrets Behind Recipes
data story link: http://ty-dong.github.io

# Abstract
Cooking is an important skill for everyone, no matter where they live. After evolving for centuries, what people eat everyday has grown into systems. Every country has their own style of eating and the styles diverge from region to region. Through the recipes, we can know what is frequently eaten by the people of one country and how they usually cook. We can even go further, find the relationships between what people eat and how their health conditions are, and dig out all the secrets behind the recipes.

In this project, we want to show the different cooking choices of ingredients, seasoning, etc. among countries and also teir similarity of their way of cooking. Then we will try to link the recipe features with people's health condition to find out if there is something in eating habits that influences people's health. 

# Research questions
1) How do eating habits vary in different countries?
 
  We extract seasoning, ingredients and the cooking method from steps by using    NLP. Then we compare the frequency of used seasoning, cooking methods and   ingredients in different countries.

  --> Notebook: 1. Data Cleaning and Extraction
  
  
2) How similar the way of cooking in different countries?
  
  We analyze the cooking steps by using NLP and then do dimention reduction to observe in 3D to see how similar the cooking process in different countres.
  
  --> Notebook: 2. Similarity


3) How are the eating habits related to health?
  
  We aim to analyze correlation between some health indices like the life span, overweight rate, high blood pressure, etc with common seasonings and nutrition content. To make our result more convincing, we propose our naive model to control the variables in different countries by only taking the income into considerate. We select the suitable health indices which pass our sensitivity analysis test with gamma = 2.

  --> Notebook: 3. Incoporating WHO dataset 4. Relationship between eating habits and health
  
  
# Dataset
The two dataset about recipes we used are collected from Kaggle (https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions). One of them contains 230185 different recipes scraped from Food.com (https://www.food.com/" and includes information about the cooking steps, ingredients, time needed, tags, etc. Through the tags of the recipes, we could figure out where the dish originates from. By matching the countries with recipes, we get 96286 recipes from 51 different countries.

The other dataset is about ratings and comments on the recipes by the users of Food.com. The reviews and the corresponding recipe id enable NLP analysis of people's feedback towards recipes. 

To learn the relationship between recipes and health, we use datasets about noncommunicable diseases (https://www.who.int/data/gho/data/themes/noncommunicable-diseases/GHO/noncommunicable-diseases") and body mass index (BMI) (https://www.who.int/data/gho/data/themes/theme-details/GHO/body-mass-index-(bmi)) from WHO in 2016. The GDP dataset from The World Bank (https://data.worldbank.org/indicator/NY.GNP.PCAP.CD) is also used to balance the influence of economy on citizens' health conditions.


# Contributions

Tianyang Dong: data cleaning, website design, data visualization.

Wei Jiang: health and seasoning relationship analysis, data visualization.

Huajian Qiu: similarity analsysis using PCA and t-SNE, data visualization.

Jiahua Wu: deep data cleaning, nutrition choropleth map, data visualization.
