# Regression Project - Zilow
Project Description: develop a machine learning model that will predict Single Unit Properties using Zillow dataset

    Conditions: Utilize data only from the May-August 2017 period

    Challenges: 

        * Defining Single Unit Property and relevant useid codes

        * Untidy Data: Null Values, Duplicates, Outliers 

        * Identify County specific data using FIPS codes

            * Calculate Tax Rate by County

            * Cross correlations in data

Project Findings:

    * As suspected, square feet was a primary driver but other suspected features such as useid (type of Single Unit Propery) and age of home were not

    * The predictive value of the models employed declined as Single Unit Property values grew and RMSEs widened

        * However, did offer predictive value overall beating benchmarkes.  Model predictive value high sub $250k value

    * It would be easy to write this phenomena off to outliers but the distribution of the data was normal with long but consistent tail bservations. 

Conclusion: The Polynomial Regressor algorithm offered the most predictive value

    * Tortoise vs Hare: steadily outperformed as Single Unit Property Values increased vs other models

    * The Polynomial Regressor was able to capture information further out on the distribution curve than the other models.  My assumption is that there are other features that need to be explored that weren't in this project

    * My suspicions are corroborated by the heavy correlations between square feet and baths/beds in thd data set explored.  

    * Additionally, during the data exploration stage, I observed some relationship between the age of the Units and taxes with seemed anomolous and counter-intuitive

Next Steps: My suspicions are that location may have strong predictive value and would be worth exploring

    * I started to see this as I got towards the end of the project and started incorporating County specific information into the information

    * It reinforced some of the questions about the relationship between older age and higher taxes found during data exploration

    * I believe it would be worth exploring whether Single Unit Property Values are also largely driven by location which would explain an interest in older more established or historic neighborhoods.


### Project Objectives

- Data Pipeline: Acquire data from SQL database and convert into a panda dataframe, prepare the data for exploration, explore the data and document key takeaways, visualize feature attributes and incorporate into machine learning model.

- Document progress and present results in Jupyter Notebook

- Create modules (acquire.py, prepare.py) that make process repeateable for 3rd party

- Present thought process and modeling results to cohort utilizing Jupyter Notebook as presentation material

- Be prepared to handle questions about code, process, findings, key takeaways, and model.

### Project Goals

- Find drivers for Sinn=gle Unit Property Prices in the telco data that can be utilized to construct predictive model

- Construct a machine learning classification model that accurately predicts Single Unit Property Prices while maximizing for recall

- Document the process so that 3rd party can read like a report and easily follow along/replicate


### Audience
- Target audience for my notebook walkthrough is the Codeup Data Science Florence Cohort and instructors

### Deliverables
-  Jupyter Notebook Report showing process and analysis with the goal of finding drivers for Single Unit Property Prices. This notebook should be commented and documented well enough to be read like a report or walked through as a presentation.

- README.md file containing the project description with goals, a data dictionary, project planning (lay out your process through the data science pipeline), instructions or an explanation of how someone else can recreate your project and findings (What would someone need to be able to recreate your project on their own?), key findings, recommendations, and takeaways from your project.

- CSV file ... 

- individual modules, .py files, that hold functions to acquire and prepare data.

- Jupyter notebook walkthrough presentation with a high-level overview of youproject (5 minutes max). 

### Pipeline Stages Breakdown ==> Plan

-Create README.md with data dictionary, project and business goals, come up with initial hypotheses.

- Set project goals and define deliverables

### Pipeline Stages Breakdown ==> Acquire

- Write function that establish connectivity to SQL Ace, run an SQL query on the zillow database and pulls relevant tables and data

- Convert imported data into dataframe

- Complete some initial data summarization (.info(), .describe(), .value_counts(), ...).

- store functions in acquire.py

### Pipeline Stages Breakdown ==> Prepare

- prepare.py module

    - Store functions that are needed to prepare data; making sure module contains the necessary imports to run code. Final function should do the following:

        - Split data into train/validate/test.

        -  Handle Missing Values.

        - Handle erroneous data and/or address outliers 

        - Encode variables as needed.

        - Create any new features, if you decided to make any for this project.

-  Notebook

    - Explore missing values and document takeaways/action plans for handling them.

    - Is 'missing' equivalent to 0 (or some other constant value) in the specific case of this variable?

    - Replace the missing values with a value it is most likely to represent, like mean/median/mode?

    - Remove the variable (column) altogether because of the percentage of missing data?

    - Remove individual observations (rows) with a missing value for that variable?

    - Explore data types and adapt types or data values as needed to have numeric represenations of each attribute.

### Pipeline Stages Breakdown ==> Explore
- Notebook

    - Answer key questions, formulate hypotheses, and figure out the drivers of Single Unit Property Prices. Run statistical tests in data exploration. 

    - Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). Goal is to identify features that are related to Single Unit Property Prices (target), identify any data integrity issues, and understand 'how the data works'. 

    - Summarize conclusions, provide clear answers to specific questions, and summarize any takeaways/action plan from the work above.

### Pipeline Stages Breakdown ==> Modeling and Evaluation

- Notebook

    - Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document steps.

    -  Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.

    - Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.

    - Feature Selection: Are there any variables that seem to provide limited to no additional information? 

    - Based on the evaluation of your models using the train and validate datasets, choose best model that you will try with your test data, once.

    - Test the final model on your out-of-sample data (the testing dataset), summarize the performance, interpret and document your results.

### Initial thoughts and Hypothesis

- I suspect square footage will be a primary Value driver along with age and type of property

### Repeating processes and results
- the final notebook provides a detailed step by step process that should easily be followed once the data is imported.  

- The data acquire functions and data prepare functions will do the heavy lifting but anyone looking to recreate the study will need to write their own env.py file containing their SQL access data.  

- Key Takeaways are provided at each important step to guide the reader in the though process and enable them to act on their own thoughts and interact with the process. 


## Data Dictionary
|  Single Unit Property Defined: Single Unit Properties: A housing unit is a single unit within a larger structure that can be used by an individual or household to eat, sleep, and live. The unit can be in any type of residence, such as a house, apartment, or mobile home, and may also be a single unit in a group of rooms.|


|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
| Single Unit Property |  housing unit is a single unit within a larger structure that can be used by an individual or household to eat, sleep, and live |
| bathroomcnt | float64   | number of bathrooms including partials   |
| bedrooomcnt   | float64 | number of bedrooms |
| calculatedfinishedsquarefeet  | float64 | total liveable square feet|
| propertylandusetypeid | float64 | type of land use property zoning|
| taxamount | float64 | total assessed property taxes|
| fips  | float64 | Federal Information Processing Standard (source: https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt)|
| parcelid  | float64 | unique lot identifier |
| transactiondate  | object | date of property sale |


