# Aviation Accidents Data Analysis ✈️

## Description

This project is divided into two main phases: data cleaning and transformation, and data analysis and visualization. It utilizes a dataset of aviation accidents to extract meaningful insights, explore trends, and generate useful visualizations.

## Dataset

The dataset used for this project can be found [here](https://proai-datasets.s3.eu-west-3.amazonaws.com/aviation-accidents.csv). It contains information on various aviation accidents, including dates, fatalities, and other relevant details.

## Project Structure

- **data_cleaning.py**: Script for data cleaning and transformation.
- **data_analysis.py**: Script for data analysis and visualization.
- **README.md**: Project documentation.
- **requirements.txt**: List of required Python packages.

## Data Cleaning and Transformation

In the first phase, we perform several steps to clean and transform the dataset:

1. **Subset Creation**: We create a subset of the dataset focusing only on relevant columns for our analysis.
2. **Handling Missing Data**: We remove records with missing values in the 'fatalities' column and treat certain problematic symbols (e.g., '-', '?') as missing data.
3. **Data Type Conversion**:
   - **Date**: Convert the 'date' column to datetime format, ensuring proper handling of various date formats.
   - **Fatalities**: Transform the 'fatalities' column to handle values expressed as sums (e.g., '45+7') and convert to numeric format.
   - **Year**: Extract and convert the year from the 'date' column for uniformity and ease of analysis.

## Data Analysis and Visualization

In the second phase, we perform data analysis and generate visualizations to answer key questions:

1. ** Which country had the highest number of accidents?**
   - **Visualization**: Bar chart showing the number of accidents per country.
2. ** Which days of the week had the highest number of accidents?**
   - **Visualization**: Bar chart showing the number of accidents by day of the week.
3. ** How did aviation accidents differ by category?**
   - **Visualization**: Bar chart displaying the distribution of accidents by category.
4. **✈ What are the safest operators?**
   - **Visualization**: Table showing the top 5 operators with more than 5 accidents but no fatalities.
5. ** What are the most dangerous aircraft types?**
   - **Visualization**: Table listing the top 5 aircraft types with the highest number of fatalities.
6. ** How have aviation accidents evolved between 1919 and 2023?**
   - **Visualization**: Line chart showing the trend of accidents from 1919 to 2023.
7. ** How have aviation accidents evolved after September 11, 2001?**
   - **Visualization**: Bar plot comparing the number of accidents before and after September 11, 2001.

### Visualizations

To illustrate the insights from the data analysis, the following visualizations were created:

- **Bar charts** for questions 1, 2, and 3.
- **Tables** for questions 4 and 5.
- **Line chart** for question 6.
- **Bar plot** for question 7.
- **Cartogram** for a final comprehensive geographical representation of the data.
