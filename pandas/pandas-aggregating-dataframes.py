"""
Data Dictionary: About the dataset 'sales'
- Sales data from Walmart, a big-box retail store w/ thousands of locations across the U.S.
-- Contains weekly sales (in $USD) in different US stores (store) in US dollars (weekly_sales) by store department unique ID (dept)
-- Info about whether it was a holiday week (is_holiday), avg temp during the week in that location in Celcius (temp_c), avg fuel price (in $/ltr) (fuel_price), national unemployment rate that week (unemp)
"""

# sales is available and pandas is loaded as pd

# Explore your new DataFrame first by printing the first few rows of the sales DataFrame.
print(sales.head())
   store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
0      1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
1      1    A           1 2010-03-05      21827.90       False          8.056                 0.693         8.106
2      1    A           1 2010-04-02      57258.43       False         16.817                 0.718         7.808
3      1    A           1 2010-05-07      17413.94       False         22.528                 0.749         7.808
4      1    A           1 2010-06-04      17558.09       False 

# Print information about the columns in sales.
print(sales.info())

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10774 entries, 0 to 10773
Data columns (total 9 columns):
 #   Column                Non-Null Count  Dtype         
---  ------                --------------  -----         
 0   store                 10774 non-null  int64         
 1   type                  10774 non-null  object        
 2   department            10774 non-null  int32         
 3   date                  10774 non-null  datetime64[ns]
 4   weekly_sales          10774 non-null  float64       
 5   is_holiday            10774 non-null  bool          
 6   temperature_c         10774 non-null  float64       
 7   fuel_price_usd_per_l  10774 non-null  float64       
 8   unemployment          10774 non-null  float64       
dtypes: bool(1), datetime64[ns](1), float64(4), int32(1), int64(1), object(1)
memory usage: 641.9+ KB
None

# Print the mean of the weekly_sales column.
print(sales["weekly_sales"].mean())
23843.95014850566

# Print the median of the weekly_sales column.
print(sales["weekly_sales"].median())
12049.064999999999

"""
The mean weekly sales amount is almost double the median weekly sales amount! 
There are a few very high sales weeks that are making the mean so much higher than the median.
"""

 # Print the maximum of the date column.
print(sales["date"].max())
2012-10-26 00:00:00

 # Print the minimum of the date column.
print(sales["date"].min())
2010-02-05 00:00:00

"""
This dataset includes weekly sales from February 2010 to October 2012
"""
# create A custom IQR function = 75th percentile minus the 25th percentile
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
# Use the custom iqr (inter-quartile range) function pre-defined along with .agg() to print the IQR of the temperature_c column of sales.
# Print IQR of the temperature_c column
print(sales["temperature_c"].agg(iqr))
16.583333333333336

# Update the column selection to use the custom iqr function with .agg() to print the IQR of temperature_c, fuel_price_usd_per_l, and unemployment, in that order.
# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))
temperature_c           16.583
fuel_price_usd_per_l     0.073
unemployment             0.565
dtype: float64

# add new aggregation: median - Update the aggregation functions called by .agg(): include iqr and np.median in that order.
# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))
        temperature_c  fuel_price_usd_per_l  unemployment
iqr            16.583                 0.073         0.565
median         16.967                 0.743         8.099
# Avenues for future analysis:
# 1. what is UP w/ the diff btw iqr & median fuel price?
# 2. what is UP w/ the diff btw iqr & median unemployment? 

# About the dataset: sales_1_1, which contains the sales data for department 1 of store 1. 
import pandas as pd.

# Sort the rows of sales_1_1 by the date column in ascending order.
# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date")

# Get the cumulative sum of weekly_sales and add it as a new column of sales_1_1 called cum_weekly_sales.
# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()

# Get the cumulative maximum of weekly_sales, and add it as a column called cum_max_sales.
# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()

# Print the date, weekly_sales, cum_weekly_sales, and cum_max_sales columns.
# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
         date  weekly_sales  cum_weekly_sales  cum_max_sales
0  2010-02-05      24924.50          24924.50       24924.50
1  2010-03-05      21827.90          46752.40       24924.50
2  2010-04-02      57258.43         104010.83       57258.43
3  2010-05-07      17413.94         121424.77       57258.43
4  2010-06-04      17558.09         138982.86       57258.43
5  2010-07-02      16333.14         155316.00       57258.43
6  2010-08-06      17508.41         172824.41       57258.43
7  2010-09-03      16241.78         189066.19       57258.43
8  2010-10-01      20094.19         209160.38       57258.43
9  2010-11-05      34238.88         243399.26       57258.43
10 2010-12-03      22517.56         265916.82       57258.43
11 2011-01-07      15984.24         281901.06       57258.43


# Dropping duplicates
# About the dataset: sales_1_1, which contains the sales data for department 1 of store 1. 
import pandas as pd

# Remove rows of sales with duplicate pairs of store and type and save as store_types and print the head.
# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store", "type"])
print(store_types.head())
      store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
0         1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
901       2    A           1 2010-02-05      35034.06       False          4.550                 0.679         8.324
1798      4    A           1 2010-02-05      38724.42       False          6.533                 0.686         8.623
2699      6    A           1 2010-02-05      25619.00       False          4.683                 0.679         7.259
3593     10    B           1 2010-02-05      40212.84       False         12.411                 0.782         9.765

# Remove rows of sales with duplicate pairs of store and department and save as store_depts and print the head.
# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store", "department"])
print(store_depts.head())
    store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
0       1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
12      1    A           2 2010-02-05      50605.27       False          5.728                 0.679         8.106
24      1    A           3 2010-02-05      13740.12       False          5.728                 0.679         8.106
36      1    A           4 2010-02-05      39954.04       False          5.728                 0.679         8.106
48      1    A           5 2010-02-05      32229.38       False          5.728                 0.679         8.106

# Subset the rows that are holiday weeks using the is_holiday column, and drop the duplicate dates, saving as holiday_dates.
# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]].drop_duplicates(subset="date")

# Select the date column of holiday_dates, and print.
# Print date col of holiday_dates
print(holiday_dates["date"])
498    2010-09-10
691    2011-11-25
2315   2010-02-12
6735   2012-09-07
6810   2010-12-31
6815   2012-02-10
6820   2011-09-09
#The holiday weeks correspond to the Superbowl in February, Labor Day in September, Thanksgiving in November, and Christmas in December.

#Counting categorical variables
##store_types and store_depts DataFrames you created in the last exercise are available, and pandas is imported as pd