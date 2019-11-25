# Everyone can be a cook

# Abstract
Cooking is an important skill for everyone, especially for us students who do not live with families and have to cook for ourself occasionally. In the past, a good cook need to learn and remember all the ingredients and procedures for the dishes, but now, with the help of Internet, anyone can be a cook as long as they follow the instructions of recipes and practice a bit. 

In this project, we want to show the different cooking choices of ingredients, seasoning, etc. among countries and also give suggestions on which dishes to cook to satisfy one's need, based on his nationality and time planned for cooking, ingredients by hand, and so on. So our project contains two main parts: one is general analysis of recipes and the other is recommendation system for recipe. 

# Research questions
How do eating habits vary in different countries?
- the most used seasoning
- the most common main dish
- the most common cooking methods(boil, stir, fry, etc)

What makes foods popular worldwide?
- Cooking complexity: cooking time + number of ingredients types
- Health index: cuisine nutrition
- Ingredient selection: main dish, seasoning
- Cooking method

How are the different eating habits related to health?
- the life span( developed/developing)
- some common food-related disease: cancer, obesity

The recommendation systems for food
- according to historical beloved food and ratings
- according to the ingredients we have

# Dataset
The first dataset we will use is published by the United States Department of Labor (https://www.foreignlaborcert.doleta.gov/performancedata.cfm). H1B applications from 2014 to 2019 are available on the website and are available in .csv format. We consider these dataset suitable for our study as the employers only apply a H1B visa for the candidates when they are hired. Company location, job title, salary and other information are provided in the datasets. 

Our second step is to scrape the job advertisements from job seeking websites (e.g. LinkdIn, Glassdor), where the job description and requirements can be obtained. API service is provided by most of the websites. With these information, we can go further to analyze the change of need for various positions, skills, programming languages of the companies.   
# A list of internal milestones up until project milestone 3

17.11

- Change Topic to "Everyone can be a cook"
- Download the required data
- Search for additional information on quantities of each ingredient usage corresponding to the recipes, scrape data to augment dataset.

23.11

- Data cleaning for newly found data (identification and removal of invalid data)
- Extract countries(regions) informations from raw dataset and classify recipes according to continents. It helps analysis distributions and patterns on different granularity level.
- Extract flavors from user description, using it as target label of further multi-class classification training. 
- Classify recipes by meal types, explore most common used ingredients and cooking method of each country

10.12

- train classification model to predict flavors of recipes based on ingredients inputs.
- train regression model to predict nutritions of recipes based on ingredients and cooking method.
- NLP processing for recipe instructions and ingredients to find similarities between different recipes and cluster them. It is also possible to establish recommendation system based on recipe similiarity. 
- implement recommendation system based on matrix factorization.

18.12

- Compare the effectiveness of trained model 
- Explore possibilities for the data visualization
- Summarize results and figures, find the best way to present them in datastory

23.12

- Comment and refactor our code
- Release of final notebook and datastory

# Questions for TA
Do you have any suggestions for recommendation system? Is it consistent with the rest of our project?  
Is it enough to only recommend recipes to those users already in dataset?  
