# A/B Testing for Comparing Conversion of Bidding Methods

## Business Problem

Facebook recently introduced a new bidding type called "average bidding" as an alternative to the existing "maximum bidding" method. One of our clients, bombabomba.com, has decided to test this new feature and wants to conduct an A/B test to determine if average bidding brings more conversions compared to maximum bidding. The A/B test has been running for 1 month, and bombabomba.com now expects you to analyze the results of this A/B test. The ultimate success metric for bombabomba.com is the "Purchase" metric, so the focus should be on analyzing the Purchase metric for statistical testing.

## Dataset

The dataset contains website information for a company, including the number of ad impressions, clicks on ads, and the revenue generated from those clicks. There are two separate datasets for the control and test groups, stored in the "ab_testing.xlsx" file on separate sheets. The control group was subjected to Maximum Bidding, while the test group was subjected to Average Bidding.

- Impression: Number of ad impressions
- Click: Number of clicks on ads
- Purchase: Number of products purchased after clicking the ads
- Earning: Revenue generated from the purchased products

## Project Tasks

### Task 1: Data Preparation and Analysis

- Read the dataset "ab_testing.xlsx" containing control and test group data.
- Analyze the control and test group data.
- Concatenate the control and test group data after analysis.

### Task 2: Definition of A/B Test Hypothesis

- Define the hypothesis.
- Analyze the purchase (revenue) means for the control and test groups.

### Task 3: Conducting the Hypothesis Test

- Perform assumption checks: Normality Assumption and Homogeneity of Variances.
- Based on the results of the assumption checks, select the appropriate test.
- Interpret the test results based on the obtained p-value.

### Task 4: Analysis of the Results

- State which test was used and explain the reasons.
- Provide recommendations to the client based on the test results.

If you need further assistance, please let me know.
