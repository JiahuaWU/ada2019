# Secrets Behind Recipes

# Abstract
Cooking is an important skill for everyone, no matter where they live. After evolving for centuries, what people eat everyday has grown into systems. Every country has their own style of eating and the styles diverge from region to region. Through the recipes, we can know what is frequently eaten by the people of one country and how they usually cook. We can even go further, find the relationships between what people eat and how their health conditions are, and dig out all the secrets behind the recipes.

In this project, we want to show the different cooking choices of ingredients, seasoning, etc. among countries. Then we will try to link the recipe features with people's health condition to find out if there is something in eating habits that influences people's health. Besides, using the instructions of cooking steps of each recipe, we will map the recipes to vector space so that we can measure the difference of recipes among countries. To go even further, we want to train a model to predict the flavors of a dish, given its recipe, so that we know the flavor preference of people in different countries. In the end, after all these analysis of people's preference, we hope to make a recommendation system so that we can recommend dishes to people if we know their nationality.

# Research questions
1. What is the difference of need for programmers among states and through years? 

2. What are the most popular skills in terms of job requirement?

3. What is the relavence of requirements among different positions?

# Dataset
The first dataset we will use is published by the United States Department of Labor (https://www.foreignlaborcert.doleta.gov/performancedata.cfm). H1B applications from 2014 to 2019 are available on the website and are available in .csv format. We consider these dataset suitable for our study as the employers only apply a H1B visa for the candidates when they are hired. Company location, job title, salary and other information are provided in the datasets. 

Our second step is to scrape the job advertisements from job seeking websites (e.g. LinkdIn, Glassdor), where the job description and requirements can be obtained. API service is provided by most of the websites. With these information, we can go further to analyze the change of need for various positions, skills, programming languages of the companies.   
# A list of internal milestones up until project milestone 2

03.11

- Download the required data
- Search for scrapable websites online or other sources containing information on job requirement and job descriptions corresponding to the information(company, job title, location, etc.) in the H1B dataset.

10.11

- Data cleaning for newly found data (identification and removal of invalid data)
- Continue the search for available data sources if not yet finished. 
- NLP processing for job requirement and job description to find similarities between different jobs and cluster them. We may also pick out some most needed skills across different regions or companies. It is also possible to establish link between salaries and skills and the potential contributions of the skills to the salary obtained.  
- Analysis of the H1B dataset.

17.11

- Explore possibilities for the data visualization
- Decide which visualization format is the best.
- NLP processing if not yet finished.
- Release of initial notebook.

24.11

- Comment and debug our code
- Set up our goals and plans for the next milestone.
