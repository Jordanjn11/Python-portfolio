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