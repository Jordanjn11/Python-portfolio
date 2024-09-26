# the dataframe homelessness is available and pandas is loaded as pd.
# Print the head of the homelessness data
print(homelessness.head())

               region       state  individuals  family_members  state_pop
0  East South Central     Alabama       2570.0           864.0    4887681
1             Pacific      Alaska       1434.0           582.0     735139
2            Mountain     Arizona       7259.0          2606.0    7158024
3  West South Central    Arkansas       2280.0           432.0    3009733
4             Pacific  California     109008.0         20964.0   39461588

# Print information about homelessness
print(homelessness.info())

<class 'pandas.core.frame.DataFrame'>
Int64Index: 51 entries, 0 to 50
Data columns (total 5 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   region          51 non-null     object 
 1   state           51 non-null     object 
 2   individuals     51 non-null     float64
 3   family_members  51 non-null     float64
 4   state_pop       51 non-null     int64  
dtypes: float64(2), int64(1), object(2)
memory usage: 2.4+ KB
None

# Print the shape of homelessness
print(homelessness.shape)

(51, 5)

# Print a description of homelessness
print(homelessness.describe())

       individuals  family_members  state_pop
count       51.000          51.000  5.100e+01
mean      7225.784        3504.882  6.406e+06
std      15991.025        7805.412  7.327e+06
min        434.000          75.000  5.776e+05
25%       1446.500         592.000  1.777e+06
50%       3082.000        1482.000  4.461e+06
75%       6781.500        3196.000  7.341e+06
max     109008.000       52070.000  3.946e+07

# You can see that the average number of homeless individuals in each state is about 7226.


# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)
[['East South Central' 'Alabama' 2570.0 864.0 4887681]
 ['Pacific' 'Alaska' 1434.0 582.0 735139]
 ['Mountain' 'Arizona' 7259.0 2606.0 7158024]
 ['West South Central' 'Arkansas' 2280.0 432.0 3009733]
 ['Pacific' 'California' 109008.0 20964.0 39461588]
 ['Mountain' 'Colorado' 7607.0 3250.0 5691287]
 ['New England' 'Connecticut' 2280.0 1696.0 3571520]
 ['South Atlantic' 'Delaware' 708.0 374.0 965479]
 ['South Atlantic' 'District of Columbia' 3770.0 3134.0 701547]
 ['South Atlantic' 'Florida' 21443.0 9587.0 21244317]
 ['South Atlantic' 'Georgia' 6943.0 2556.0 10511131]
 ['Pacific' 'Hawaii' 4131.0 2399.0 1420593]
 ['Mountain' 'Idaho' 1297.0 715.0 1750536]
 ['East North Central' 'Illinois' 6752.0 3891.0 12723071]
 ['East North Central' 'Indiana' 3776.0 1482.0 6695497]
 ['West North Central' 'Iowa' 1711.0 1038.0 3148618]
 ['West North Central' 'Kansas' 1443.0 773.0 2911359]
 ['East South Central' 'Kentucky' 2735.0 953.0 4461153]
 ['West South Central' 'Louisiana' 2540.0 519.0 4659690]
 ['New England' 'Maine' 1450.0 1066.0 1339057]
 ['South Atlantic' 'Maryland' 4914.0 2230.0 6035802]
 ['New England' 'Massachusetts' 6811.0 13257.0 6882635]
 ['East North Central' 'Michigan' 5209.0 3142.0 9984072]
 ['West North Central' 'Minnesota' 3993.0 3250.0 5606249]
 ['East South Central' 'Mississippi' 1024.0 328.0 2981020]
 ['West North Central' 'Missouri' 3776.0 2107.0 6121623]
 ['Mountain' 'Montana' 983.0 422.0 1060665]
 ['West North Central' 'Nebraska' 1745.0 676.0 1925614]
 ['Mountain' 'Nevada' 7058.0 486.0 3027341]
 ['New England' 'New Hampshire' 835.0 615.0 1353465]
 ['Mid-Atlantic' 'New Jersey' 6048.0 3350.0 8886025]
 ['Mountain' 'New Mexico' 1949.0 602.0 2092741]
 ['Mid-Atlantic' 'New York' 39827.0 52070.0 19530351]
 ['South Atlantic' 'North Carolina' 6451.0 2817.0 10381615]
 ['West North Central' 'North Dakota' 467.0 75.0 758080]
 ['East North Central' 'Ohio' 6929.0 3320.0 11676341]
 ['West South Central' 'Oklahoma' 2823.0 1048.0 3940235]
 ['Pacific' 'Oregon' 11139.0 3337.0 4181886]
 ['Mid-Atlantic' 'Pennsylvania' 8163.0 5349.0 12800922]
 ['New England' 'Rhode Island' 747.0 354.0 1058287]
 ['South Atlantic' 'South Carolina' 3082.0 851.0 5084156]
 ['West North Central' 'South Dakota' 836.0 323.0 878698]
 ['East South Central' 'Tennessee' 6139.0 1744.0 6771631]
 ['West South Central' 'Texas' 19199.0 6111.0 28628666]
 ['Mountain' 'Utah' 1904.0 972.0 3153550]
 ['New England' 'Vermont' 780.0 511.0 624358]
 ['South Atlantic' 'Virginia' 3928.0 2047.0 8501286]
 ['Pacific' 'Washington' 16424.0 5880.0 7523869]
 ['South Atlantic' 'West Virginia' 1021.0 222.0 1804291]
 ['East North Central' 'Wisconsin' 2740.0 2167.0 5807406]
 ['Mountain' 'Wyoming' 434.0 205.0 577601]]

# Print the column index of homelessness
print(homelessness.columns)
Index(['region', 'state', 'individuals', 'family_members', 'state_pop'], dtype='object')

# Print the row index of homelessness
print(homelessness.index)
Int64Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
            49, 50],
           dtype='int64')

# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())
                region         state  individuals  family_members  state_pop
50            Mountain       Wyoming        434.0           205.0     577601
34  West North Central  North Dakota        467.0            75.0     758080
7       South Atlantic      Delaware        708.0           374.0     965479
39         New England  Rhode Island        747.0           354.0    1058287
45         New England       Vermont        780.0           511.0     624358

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)

print(homelessness_fam.head())
                region          state  individuals  family_members  state_pop
32        Mid-Atlantic       New York      39827.0         52070.0   19530351
4              Pacific     California     109008.0         20964.0   39461588
21         New England  Massachusetts       6811.0         13257.0    6882635
9       South Atlantic        Florida      21443.0          9587.0   21244317
43  West South Central          Texas      19199.0          6111.0   28628666


# Sorting by multiple columns
# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False])

# Print the top few rows
print(homelessness_reg_fam.head())
                region      state  individuals  family_members  state_pop
13  East North Central   Illinois       6752.0          3891.0   12723071
35  East North Central       Ohio       6929.0          3320.0   11676341
22  East North Central   Michigan       5209.0          3142.0    9984072
49  East North Central  Wisconsin       2740.0          2167.0    5807406
14  East North Central    Indiana       3776.0          1482.0    6695497

# Select the individuals column
individuals = homelessness["individuals"]

print(individuals.head())
0      2570.0
1      1434.0
2      7259.0
3      2280.0
4    109008.0
Name: individuals, dtype: float64


# Create a DataFrame called state_fam that contains only the state and family_members columns of homelessness, in that order.
# Select the state and family_members columns from dataframe homelessness
state_fam = homelessness[["state", "family_members"]]
# get the first few rows of the resulting subset
print(state_fam.head())
        state  family_members
0     Alabama           864.0
1      Alaska           582.0
2     Arizona          2606.0
3    Arkansas           432.0
4  California         20964.0

# Create a DataFrame called ind_state that contains the individuals and state columns of homelessness, in that order.
# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals", "state"]]

# get the first few rows of the resulting subset
print(ind_state.head())
   individuals       state
0       2570.0     Alabama
1       1434.0      Alaska
2       7259.0     Arizona
3       2280.0    Arkansas
4     109008.0  California

# Filter homelessness for cases where the number of individuals is greater than ten thousand, assigning to ind_gt_10k. View the printed result.
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] > 10000]

# See the result
print(ind_gt_10k)
                region       state  individuals  family_members  state_pop
4              Pacific  California     109008.0         20964.0   39461588
9       South Atlantic     Florida      21443.0          9587.0   21244317
32        Mid-Atlantic    New York      39827.0         52070.0   19530351
37             Pacific      Oregon      11139.0          3337.0    4181886
43  West South Central       Texas      19199.0          6111.0   28628666
47             Pacific  Washington      16424.0          5880.0    7523869

# Filter homelessness for cases where the USA Census region is "Mountain", assigning to mountain_reg. View the printed result.
# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness["region"] == "Mountain"]

# See the result
print(mountain_reg)
      region       state  individuals  family_members  state_pop
2   Mountain     Arizona       7259.0          2606.0    7158024
5   Mountain    Colorado       7607.0          3250.0    5691287
12  Mountain       Idaho       1297.0           715.0    1750536
26  Mountain     Montana        983.0           422.0    1060665
28  Mountain      Nevada       7058.0           486.0    3027341
31  Mountain  New Mexico       1949.0           602.0    2092741
44  Mountain        Utah       1904.0           972.0    3153550
50  Mountain     Wyoming        434.0           205.0     577601

# Filter homelessness for cases where the number of family_members is less than one thousand and the region is "Pacific", assigning to fam_lt_1k_pac. View the printed result.
# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]

# See the result
print(fam_lt_1k_pac)
<script.py> output:
        region   state  individuals  family_members  state_pop
    1  Pacific  Alaska       1434.0           582.0     735139
# Filter homelessness for cases where the USA census state is in the list of Mojave states, canu, assigning to mojave_homelessness. View the printed result.
# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)
      region       state  individuals  family_members  state_pop
2   Mountain     Arizona       7259.0          2606.0    7158024
4    Pacific  California     109008.0         20964.0   39461588
28  Mountain      Nevada       7058.0           486.0    3027341
44  Mountain        Utah       1904.0           972.0    3153550

# Add a new column to homelessness, named total, containing the sum of the individuals and family_members columns.
# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add another column to homelessness, named p_homeless, containing the proportion of the total homeless population to the total population in each state state_pop.
# Add p_homeless col as proportion of total homeless population to the state population
homelessness["p_homeless"] = homelessness["total"] / homelessness["state_pop"]

# See the result
print(homelessness)
                region                 state  individuals  family_members  state_pop     total  p_homelessness  p_homeless
0   East South Central               Alabama       2570.0           864.0    4887681    3434.0       7.026e-04   7.026e-04
1              Pacific                Alaska       1434.0           582.0     735139    2016.0       2.742e-03   2.742e-03
2             Mountain               Arizona       7259.0          2606.0    7158024    9865.0       1.378e-03   1.378e-03
3   West South Central              Arkansas       2280.0           432.0    3009733    2712.0       9.011e-04   9.011e-04
4              Pacific            California     109008.0         20964.0   39461588  129972.0       3.294e-03   3.294e-03
5             Mountain              Colorado       7607.0          3250.0    5691287   10857.0       1.908e-03   1.908e-03
6          New England           Connecticut       2280.0          1696.0    3571520    3976.0       1.113e-03   1.113e-03
7       South Atlantic              Delaware        708.0           374.0     965479    1082.0       1.121e-03   1.121e-03
8       South Atlantic  District of Columbia       3770.0          3134.0     701547    6904.0       9.841e-03   9.841e-03
9       South Atlantic               Florida      21443.0          9587.0   21244317   31030.0       1.461e-03   1.461e-03
10      South Atlantic               Georgia       6943.0          2556.0   10511131    9499.0       9.037e-04   9.037e-04
11             Pacific                Hawaii       4131.0          2399.0    1420593    6530.0       4.597e-03   4.597e-03
12            Mountain                 Idaho       1297.0           715.0    1750536    2012.0       1.149e-03   1.149e-03
13  East North Central              Illinois       6752.0          3891.0   12723071   10643.0       8.365e-04   8.365e-04
14  East North Central               Indiana       3776.0          1482.0    6695497    5258.0       7.853e-04   7.853e-04
15  West North Central                  Iowa       1711.0          1038.0    3148618    2749.0       8.731e-04   8.731e-04
16  West North Central                Kansas       1443.0           773.0    2911359    2216.0       7.612e-04   7.612e-04
17  East South Central              Kentucky       2735.0           953.0    4461153    3688.0       8.267e-04   8.267e-04
18  West South Central             Louisiana       2540.0           519.0    4659690    3059.0       6.565e-04   6.565e-04
19         New England                 Maine       1450.0          1066.0    1339057    2516.0       1.879e-03   1.879e-03
20      South Atlantic              Maryland       4914.0          2230.0    6035802    7144.0       1.184e-03   1.184e-03
21         New England         Massachusetts       6811.0         13257.0    6882635   20068.0       2.916e-03   2.916e-03
22  East North Central              Michigan       5209.0          3142.0    9984072    8351.0       8.364e-04   8.364e-04
23  West North Central             Minnesota       3993.0          3250.0    5606249    7243.0       1.292e-03   1.292e-03
24  East South Central           Mississippi       1024.0           328.0    2981020    1352.0       4.535e-04   4.535e-04
25  West North Central              Missouri       3776.0          2107.0    6121623    5883.0       9.610e-04   9.610e-04
26            Mountain               Montana        983.0           422.0    1060665    1405.0       1.325e-03   1.325e-03
27  West North Central              Nebraska       1745.0           676.0    1925614    2421.0       1.257e-03   1.257e-03
28            Mountain                Nevada       7058.0           486.0    3027341    7544.0       2.492e-03   2.492e-03
29         New England         New Hampshire        835.0           615.0    1353465    1450.0       1.071e-03   1.071e-03
30        Mid-Atlantic            New Jersey       6048.0          3350.0    8886025    9398.0       1.058e-03   1.058e-03
31            Mountain            New Mexico       1949.0           602.0    2092741    2551.0       1.219e-03   1.219e-03
32        Mid-Atlantic              New York      39827.0         52070.0   19530351   91897.0       4.705e-03   4.705e-03
33      South Atlantic        North Carolina       6451.0          2817.0   10381615    9268.0       8.927e-04   8.927e-04
34  West North Central          North Dakota        467.0            75.0     758080     542.0       7.150e-04   7.150e-04
35  East North Central                  Ohio       6929.0          3320.0   11676341   10249.0       8.778e-04   8.778e-04
36  West South Central              Oklahoma       2823.0          1048.0    3940235    3871.0       9.824e-04   9.824e-04
37             Pacific                Oregon      11139.0          3337.0    4181886   14476.0       3.462e-03   3.462e-03
38        Mid-Atlantic          Pennsylvania       8163.0          5349.0   12800922   13512.0       1.056e-03   1.056e-03
39         New England          Rhode Island        747.0           354.0    1058287    1101.0       1.040e-03   1.040e-03
40      South Atlantic        South Carolina       3082.0           851.0    5084156    3933.0       7.736e-04   7.736e-04
41  West North Central          South Dakota        836.0           323.0     878698    1159.0       1.319e-03   1.319e-03
42  East South Central             Tennessee       6139.0          1744.0    6771631    7883.0       1.164e-03   1.164e-03
43  West South Central                 Texas      19199.0          6111.0   28628666   25310.0       8.841e-04   8.841e-04
44            Mountain                  Utah       1904.0           972.0    3153550    2876.0       9.120e-04   9.120e-04
45         New England               Vermont        780.0           511.0     624358    1291.0       2.068e-03   2.068e-03
46      South Atlantic              Virginia       3928.0          2047.0    8501286    5975.0       7.028e-04   7.028e-04
47             Pacific            Washington      16424.0          5880.0    7523869   22304.0       2.964e-03   2.964e-03
48      South Atlantic         West Virginia       1021.0           222.0    1804291    1243.0       6.889e-04   6.889e-04
49  East North Central             Wisconsin       2740.0          2167.0    5807406    4907.0       8.450e-04   8.450e-04
50            Mountain               Wyoming        434.0           205.0     577601     639.0       1.106e-03   1.106e-03


# Add a column to homelessness, indiv_per_10k, containing the number of homeless individuals per ten thousand people in each state, using state_pop for state population.
# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"] 

# Subset rows where indiv_per_10k is higher than 20, assigning to high_homelessness.
# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k, assigning to high_homelessness_srt.
# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending=False)

# Select only the state and indiv_per_10k columns of high_homelessness_srt and save as result. Look at the result.
# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)
                   state  indiv_per_10k
8   District of Columbia         53.738
11                Hawaii         29.079
4             California         27.624
37                Oregon         26.636
28                Nevada         23.314
47            Washington         21.829
32              New York         20.392