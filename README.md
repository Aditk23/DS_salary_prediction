# Data Scientist Salary Prediction: Project Overview 
* Created a tool that estimates data science salaries to help data scientists negotiate their income when they get a job.
* Scraped around 700 job descriptions from glassdoor using python and selenium
* Feature engineering performed to find out how companies value on skills like python,SQL,etc. 
* Created multiple, lasso, logarithmic, support vector regression model. Also optimized random forest model using GridSearchCV.


## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium  
**Web Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905**Referred Repo:** https://github.com/PlayingNumbers/ds_salary_proj/


## Web Scraping
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:
*	Job title
*	Salary Estimate
*	Job Description
*	Rating
*	Company Name
*	Location
*	Company Size
*	Company Founded Year
*	Type of Ownership 
*	Industry
*	Sector
*	Revenue


## Data Cleaning
After scraping the data, I realized that for more than 70% companies salary estimate was not available. As this was our dependent variable i tried to fill these values manually by google search. Also following changes were made:
*	Parsed numeric data out of salary as Rupees symbol was present
*	Removed rows without salary for companies where salary was not available on google.
*	Removed rating out of company name 
*	Transformed founded date into age of company 
*	Made columns for if different skills were listed in the job description:
    * Python  
    * SQL  
    * Excel  
    * Tableau  
    * Spark 
*	Column for simplified job title and Seniority was added


## Data Visualization
Data visualization was performed and I came across various conclusions:
*	Bangalore provided most job opportunities
*	Cognizant had most job openings for data scientist positions
*	Among various Data SCience post like Data Analyst, Data Engineer, MLE and Data Scientist, Data Scientist was most in demend
*	MLE and Data Scientist positions are given highest average salary
*	Retail sector provides highest average salaries while Non-Profit provied the least
*	Along with Bangalore, Gurgaon, Hyderabad, Pune and Mumbai are leading locations in India for Data Science opportunities
*	Companies in Hyderabad, Bangalore and Gurgaon provides higher salaries than other cities.

![alt text](https://github.com/Aditk23/DS_salary_prediction/blob/main/Jobs_by_location.png "No. of jobs by location")
![alt text](https://github.com/Aditk23/DS_salary_prediction/blob/main/Post.png "Avg salary by Post")
![alt text](https://github.com/Aditk23/DS_salary_prediction/blob/main/Sector.png "Avg Salary by Sector")
![alt text](https://github.com/Aditk23/DS_salary_prediction/blob/main/Location.png "Avg Salary by Location")

## Model Building 

Firstly, all categorical variables were converted into dummy variables and train-test split was made with test size of 20% 

I tried Multiple Regression, Logarithmic Regression, Support Vector Regression and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model. Results were not as expected and MAE was very high for all the model, probably because more than 70% salary estimate was not employeer provided and was filled by a rough google search. 

## Model performance
The best model for this data was optimized Random Forest model with MAE around 400 which is very less in comparison to other regression model.

## Conclusion
The data obtained was looking fine till EDA and explained fairly well job distributions for data scientist accross India. But model prediction was not upto the mark as error terms were quite high. 
