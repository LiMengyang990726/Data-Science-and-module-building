## To Get Started with the Data Analysis

### 1. Regarding our dataset
The chosen dataset is the "House Prices: Advanced Regression Techniques" Please click [here](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) for a better understanding for the background.

The API for downloading the dataset is:
`kaggle competitions download -c house-prices-advanced-regression-techniques`

### 2. Regarding the guidelines to Git and Data Science
Please check the following documents (credit to Anqi):

[Simple Git Guide for Data Analytics](https://github.com/anqitu/simple-git-guide-for-data-analytics)

[Learn about data science](https://github.com/orgs/ntuoss/teams/pandas/discussions/3)

### 3. Regarding the operation side
All members please migrate to the Discord channel and we will arrange regular online meeting for tracking progress

### 4. Web scraping
#### Why do do scrap data?
Should have a strong direction to go.

E.g. analyse how different skill set can lead to different salary level in the position as a data analyst in the jobs from glassdoor
#### Recommendation system

Algorithm1: Jaccard similarity

(A and B) / (A or B)

#### A way to make the HTML file that you copied looks nicer:

Go to `jsbeautifier`

Use `strip()` to clear out any unwanted things

To write in a file:
```
filename = "product.csv"
f = open(filename,"w")
headers = "attribute1,attribute2,attribute3,...,\n"
f.write(header)
...
f.close() # in order to open the file, you have to close it first
```

### References

[Intro to Web Scraping with Python and Beautiful Soup](https://www.youtube.com/watch?v=XQgXKtPSzUI&index=2&list=LLpPP1tfgf97VIYCfXKpMCVQ&t=0s)

[Scraping glassdoor and intro the Recommendation system](https://nycdatascience.com/blog/student-works/r-shiny/match-skill-job-simple-job-recommendation-system/)
