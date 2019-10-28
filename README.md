# What should I know to find a job?

# Abstract
Job landing is the most concerned topic among university students. There are several aspects that interest the job hunters: where are the potential employers and what the employers need. United States has become one of the most popular working places for many years, especially for the computer-science-related workers, because IT technology is really thriving there. This leads many foreign graduates attentive to working there. Based on this fact, this project aims at exploring the changes of foreign CS-related labor force characteristics in US over the last decades, meanwhile investigating the changing need for these positions.

We will show the different figures of H1B issued among the states and through the time, the preferences of companies regarding skills, programming languages and the benefit and welfare they can offer. We will identify the most demanding skill which appears most frequently as keyword in job description so that this study can serve as a reference for people who hope to find a job in America.
# Research questions
1. What is the difference of need for programmers among states and through years? 

2. What is the most hot programming language for companies?

3. What is the most demanding skill? What is the relavence of requirements among different positions?

# Dataset
The first dataset we will use is published by the United States Department of Labor (https://www.foreignlaborcert.doleta.gov/performancedata.cfm). H1B applications from 2014 to 2019 are available on the website and are presented in .csv form. We consider these dataset reasonable for our study because once the employer would like to apply for H1B visa for the worker, this means the position the employer offers is really in need. Company location, job title, salary and many other informations are provided in the datasets. 

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

