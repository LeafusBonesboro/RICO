# RICO
Stopping the Box Mafia

The main_code.py file is the cheat detection. Its a poisson distribution that detects outliers in the rates by the associates. 

The webscrape.py file is a webscraping tool that was made to automate the end of day task for the Amazon Workforce team. Right now its out of date
as it hasnt been used since I was there last year. 

The csv files are being used for automating csv files and putting them into a data form with pandas and excel. All of those files havent been uploaded.
The other files are dependencies for the webscaper. Right now ChromeDriver is active so it only will work with Chrome, but GeckoDriver is also 
in the code so it can be used for Firefox. The Geckodriver is currently hashed out. 

The scraper will be useful to quickly collect historical data and to analyze it. The current code just needs changes to file locations and then needs to get
the html tags for Selenium. Once the data has been collected and analyzed we will have some context to determine how many deviations are needed to detect outliers. 
Too many deviations and it becomes too sensitive and wont catch any cheaters. Too low and it will list everyone as a cheater. 

Analysis will consist of using historical data to understand the typical variations in the rate of items scanned and identify patterns or outliers 
that correspond to actual cheating behavior. This can help establish a baseline and inform the threshold for identifying significant deviations. The data
needed are the rates for all applicable shifts and all applicable associates. 

From this data a mean will be established and then the standard deviation can be made. We can then compare that data to the Poisson distribution.The Poisson distribution gives a good 
approximation for events with a known average rate. The better our model the better the results will be. 

Once the data is analyzed we compare the Poisson distribution agaisnt the mean and standard deviation of our dataset. We can then begin to look at setting a deviation and control lines. 
Then we can implement a system for monitoring and feedback. We then adjust the deviations based on the observations and feedback from the associates and the managers.

The deviations are just one tool to be considered when detecting if cheating behavior has occured. Investigation, additional data analysis, and 
specific context should also be used. This is to be a red flag to catch consistent abusers.

This tool can be used in real time. As soon as the data is available the script can run and scrape the data it needs and give accurate results. 

A GUI will be useful for users and can be made into an app. This is a tool that will be easy to use. 
