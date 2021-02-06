#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:03:07 2021

@author: apple
"""
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd
#from selenium.webdriver.chrome.options import Options

#chrome_options = Options()
# maximized window
#chrome_options.add_argument("--start-maximized")

def get_jobs(keyword, num_jobs, verbose,sleep_time):
    
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    #options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Firefox(executable_path="/Users/apple/Desktop/Data Science/DS_Salary/geckodriver")
    driver.set_window_size(1120, 1000)
    url = 'https://www.glassdoor.co.in/Job/data-scientist-jobs-SRCH_KO0,14.htm'
    driver.get(url)
    driver.maximize_window()

    jobs = []

    
    

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(sleep_time)

    
        try:
            driver.find_element_by_class_name("main").click()
        except ElementClickInterceptedException:
            pass
        
  

        try:
            driver.find_element_by_class_name("SVGInline-svg").click()  #clicking to the X.
        except NoSuchElementException:
            pass


        #Going through each job in this page
        job_buttons = driver.find_elements_by_class_name("react-job-listing")  #jl for Job Listing. These are the buttons we're going to click.
        #print(job_buttons)
        for job_button in job_buttons:  
            #print(1)
            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            job_button.click()  #You might 
            time.sleep(1)
            
        #Test for the "Sign Up" prompt and get rid of it.


            try:
                driver.find_element_by_class_name("main").click()
            except ElementClickInterceptedException:
                pass

            
            try:
                driver.find_element_by_css_selector('[alt="Close"]').click() #clicking to the X.
            except NoSuchElementException:
                pass
        
            time.sleep(.1)
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    company_name = driver.find_element_by_xpath('.//div[@class="css-87uc0g e1tk4kwz1"]').text
                    location = driver.find_element_by_xpath('.//div[@class="css-56kyx5 e1tk4kwz5"]').text
                    job_title = driver.find_element_by_xpath('.//div[@class="css-1vg6q84 e1tk4kwz4"]').text
                    job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                    collected_successfully = True
                except:
                    time.sleep(5)

            try:
                salary_estimate = driver.find_element_by_xpath('.//span[@class="css-56kyx5 css-16kxj2j e1wijj242" and @data-test="detailSalary"]').text
            except NoSuchElementException:
                salary_estimate = -1 #You need to set a "not found value. It's important."
            
            try:
                rating = driver.find_element_by_xpath('.//span[@class="css-1m5m32b e1tk4kwz2"]').text
            except NoSuchElementException:
                rating = -1 #You need to set a "not found value. It's important."

            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            #Going to the Company tab...
            #clicking on this:
            #<div class="tab" data-tab-type="overview"><span>Company</span></div>
            

            try:
                #driver.find_element_by_xpath('.//div[@class="css-lt549m ef7s0la1" and @data-tab-type="overview"]').click()
                #element = driver.find_element_by_xpath('.//div[@class="css-lt549m ef7s0la1" and @data-tab-type="overview"]')
                webdriver.ActionChains(driver).double_click(driver.find_element_by_xpath('.//div[@class="css-lt549m ef7s0la1" and @data-test="overview"]')).perform()
                #webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()
                try:
                    size = driver.find_element_by_xpath('.//span[text()="Size"]/following::span[@class="css-i9gxme e1pvx6aw2"]').text
                except NoSuchElementException:
                    size = -1

                try:
                    founded = driver.find_element_by_xpath('.//span[text()="Founded"]/following::span[@class="css-i9gxme e1pvx6aw2"]').text
                except NoSuchElementException:
                    founded = -1

                try:
                    type_of_ownership = driver.find_element_by_xpath('.//span[text()="Type"]/following::span[@class="css-i9gxme e1pvx6aw2"]').text
                except NoSuchElementException:
                    type_of_ownership = -1

                try:
                    industry = driver.find_element_by_xpath('.//span[text()="Industry"]/following::span[@class="css-i9gxme e1pvx6aw2"]').text
                except NoSuchElementException:
                    industry = -1

                try:
                    sector = driver.find_element_by_xpath('.//span[text()="Sector"]/following::span[@class="css-i9gxme e1pvx6aw2"]').text
                except NoSuchElementException:
                    sector = -1

                try:
                    revenue = driver.find_element_by_xpath('.//span[text()="Revenue"]/following::span[@class="css-i9gxme e1pvx6aw2"]').text
                except NoSuchElementException:
                    revenue = -1


            except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                size = 0
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1

                
            if verbose:
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            "Size" : size,
            "Founded" : founded,
            "Type of ownership" : type_of_ownership,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue,
            })
            #add job to jobs

        #Clicking on the "next page" button
        try:
            driver.find_element_by_xpath('.//li[@class="css-1yshuyv e1gri00l3"]//a').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.







