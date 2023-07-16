
# A/B Testing: Comparing Conversion of Bidding Methods

## Business Problem

Facebook recently introduced a new bidding method called "average bidding" as an alternative to their existing "maximum bidding" method. One of our clients, bombabomba.com, has decided to test this new feature and wants to determine if average bidding brings in higher conversions compared to maximum bidding. The A/B test has been running for 1 month, and bombabomba.com now expects you to analyze the results. The ultimate success metric for bombabomba.com is "Purchase". Therefore, the focus for statistical testing should be on the "Purchase" metric.

## Dataset Story

This dataset contains website information for a company, including data on the number of ads viewed, ads clicked, purchases made, and earnings generated. It consists of two separate data sets: Control Group and Test Group. These data sets are stored on separate sheets in the `ab_testing.xlsx` Excel file. The Control Group represents Maximum Bidding, while the Test Group represents Average Bidding.

- **impression**: Number of ad impressions
- **Click**: Number of ad clicks
- **Purchase**: Number of product purchases made after clicking the ads
- **Earning**: Earnings generated after product purchases

## Project Tasks

### A/B Testing (Independent Two-Sample T-Test)

1. Formulate hypotheses:
   - H0: M1 = M2 (There is no difference between Maximum Bidding and Average Bidding)
   - H1: M1 != M2 (There is a difference between the control and test groups)
   
2. Assumption checks:
   - Perform normality assumption tests (Shapiro-Wilk test) on the "Purchase" variable for the control and test groups.
   - Perform a homogeneity of variances test (Levene's test) for the control and test groups.
   
3. Apply the hypothesis test:
   - If the assumptions are met, perform an independent two-sample t-test on the "Purchase" variable for the control and test groups.
   - If the assumptions are not met, perform a Mann-Whitney U test.
   
4. Interpret the results based on the p-value.

### Task 1: Data Preparation and Analysis

- Read the data set comprising control and test groups from `ab_testing.xlsx` file.
- Assign the control and test group data to separate variables.
- Analyze the control and test group data.
- Concatenate the control and test group data.

### Task 2: Defining the Hypothesis for A/B Testing

- Define the hypotheses for the A/B test.

### Task 3: Conducting the Hypothesis Test

#### A/B Testing (Independent Two-Sample T-Test)

- Perform assumption checks (normality assumption and homogeneity of variances).
- Based on the assumption test results, choose the appropriate test (independent two-sample t-test or Mann-Whitney U test).
- Interpret the results based on the p-value.

### Task 4: Result Analysis

- Specify the test used and provide the reasons for selecting that test.
- Provide recommendations to the client based on the test results.

Feel free to customize the text or make any necessary modifications to suit your specific project requirements.

