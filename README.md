# Everyone can be a cook

# Abstract
Cooking is an important skill for everyone, especially for us students who do not live with families and have to cook for ourself occasionally. In the past, a good cook need to learn and remember all the ingredients and procedures for the dishes, but now, with the help of Internet, anyone can be a cook as long as they follow the instructions of recipes and practice a bit. 

In this project, we want to show the different cooking choices of ingredients, seasoning, etc. among countries and also give suggestions on which dishes to cook to satisfy one's need, based on his nationality and time planned for cooking, ingredients by hand, and so on. So our project contains two main parts: one is general analysis of recipes and the other is recommendation system for recipe. 

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

# Questions for TA
Do you have any suggestions for finding proper dataset in Europe especially in Switzerland?

Are there any suggestions on scraping the job information on websites like glassdoor or linkedIn?
