
### Heroes Of Pymoli Data Analysis
* Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

* Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
-----

### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.


```python
# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
```

## Player Count

* Display the total number of players



```python

total_players = len(purchase_data["SN"].value_counts())


player_count = pd.DataFrame({"Total Players":[total_players]})
player_count
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>576</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame



```python
number_of_uniq_items = len((purchase_data["Item ID"]).unique())
avg_price = (purchase_data["Price"]).mean()
number_of_purchases = (purchase_data["Purchase ID"]).count()
tot_rev = (purchase_data["Price"]).sum()


summary_df = pd.DataFrame({"Number of Unique Items":[number_of_uniq_items],
                           "Average Price":[avg_price], 
                           "Number of Purchases": [number_of_purchases], 
                           "Total Revenue": [tot_rev]})


summary_df.style.format({'Average Price':"${:,.2f}",
                         'Total Revenue': '${:,.2f}'})
```




<style  type="text/css" >
</style>  
<table id="T_5feb87e4_37ab_11e9_ae23_14abc5ca1786" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Number of Unique Items</th> 
        <th class="col_heading level0 col1" >Average Price</th> 
        <th class="col_heading level0 col2" >Number of Purchases</th> 
        <th class="col_heading level0 col3" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_5feb87e4_37ab_11e9_ae23_14abc5ca1786level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_5feb87e4_37ab_11e9_ae23_14abc5ca1786row0_col0" class="data row0 col0" >183</td> 
        <td id="T_5feb87e4_37ab_11e9_ae23_14abc5ca1786row0_col1" class="data row0 col1" >$3.05</td> 
        <td id="T_5feb87e4_37ab_11e9_ae23_14abc5ca1786row0_col2" class="data row0 col2" >780</td> 
        <td id="T_5feb87e4_37ab_11e9_ae23_14abc5ca1786row0_col3" class="data row0 col3" >$2,379.77</td> 
    </tr></tbody> 
</table> 



## Gender Demographics

* Percentage and Count of Male Players


* Percentage and Count of Female Players


* Percentage and Count of Other / Non-Disclosed





```python

gender_stats = purchase_data.groupby("Gender")


gender_count = gender_stats.nunique()["SN"]

per_of_players = gender_count / total_players * 100


gender_demo = pd.DataFrame({"Percentage of Players": per_of_players, "Total Count": gender_count})


gender_demo.index.name = None


gender_demo.sort_values(["Total Count"], ascending = False).style.format({"Percentage of Players":"{:.2f}"})


```




<style  type="text/css" >
</style>  
<table id="T_8829f540_37ab_11e9_8a84_14abc5ca1786" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Percentage of Players</th> 
        <th class="col_heading level0 col1" >Total Count</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_8829f540_37ab_11e9_8a84_14abc5ca1786level0_row0" class="row_heading level0 row0" >Male</th> 
        <td id="T_8829f540_37ab_11e9_8a84_14abc5ca1786row0_col0" class="data row0 col0" >84.03</td> 
        <td id="T_8829f540_37ab_11e9_8a84_14abc5ca1786row0_col1" class="data row0 col1" >484</td> 
    </tr>    <tr> 
        <th id="T_8829f540_37ab_11e9_8a84_14abc5ca1786level0_row1" class="row_heading level0 row1" >Female</th> 
        <td id="T_8829f540_37ab_11e9_8a84_14abc5ca1786row1_col0" class="data row1 col0" >14.06</td> 
        <td id="T_8829f540_37ab_11e9_8a84_14abc5ca1786row1_col1" class="data row1 col1" >81</td> 
    </tr>    <tr> 
        <th id="T_8829f540_37ab_11e9_8a84_14abc5ca1786level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_8829f540_37ab_11e9_8a84_14abc5ca1786row2_col0" class="data row2 col0" >1.91</td> 
        <td id="T_8829f540_37ab_11e9_8a84_14abc5ca1786row2_col1" class="data row2 col1" >11</td> 
    </tr></tbody> 
</table> 




## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender




* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
purchase_count = gender_stats["Purchase ID"].count()

avg_purchase_price = gender_stats["Price"].mean()


avg_purchase_total = gender_stats["Price"].sum()


avg_purchase_per_person = avg_purchase_total/total_count_gender


gender_demo = pd.DataFrame({"Purchase Count": purchase_count, 
                                    "Average Purchase Price": avg_purchase_price,
                                    "Average Purchase Value":avg_purchase_total,
                                    "Avg Purchase Total per Person": avg_purchase_per_person})

gender_demo.index.name = "Gender"


gender_demo.style.format({"Average Purchase Value":"${:,.2f}",
                                  "Average Purchase Price":"${:,.2f}",
                                  "Avg Purchase Total per Person":"${:,.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_9862cada_37ab_11e9_9633_14abc5ca1786" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Average Purchase Value</th> 
        <th class="col_heading level0 col3" >Avg Purchase Total per Person</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Gender</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_9862cada_37ab_11e9_9633_14abc5ca1786level0_row0" class="row_heading level0 row0" >Female</th> 
        <td id="T_9862cada_37ab_11e9_9633_14abc5ca1786row0_col0" class="data row0 col0" >113</td> 
        <td id="T_9862cada_37ab_11e9_9633_14abc5ca1786row0_col1" class="data row0 col1" >$3.20</td> 
        <td id="T_9862cada_37ab_11e9_9633_14abc5ca1786row0_col2" class="data row0 col2" >$361.94</td> 
        <td id="T_9862cada_37ab_11e9_9633_14abc5ca1786row0_col3" class="data row0 col3" >$4.47</td> 
    </tr>    <tr> 
        <th id="T_9862cada_37ab_11e9_9633_14abc5ca1786level0_row1" class="row_heading level0 row1" >Male</th> 
        <td id="T_9862cada_37ab_11e9_9633_14abc5ca1786row1_col0" class="data row1 col0" >652</td> 
        <td id="T_9862cada_37ab_11e9_9633_14abc5ca1786row1_col1" class="data row1 col1" >$3.02</td> 
        <td id="T_9862cada_37ab_11e9_9633_14abc5ca1786row1_col2" class="data row1 col2" >$1,967.64</td> 
        <td id="T_9862cada_37ab_11e9_9633_14abc5ca1786row1_col3" class="data row1 col3" >$4.07</td> 
    </tr>    <tr> 
        <th id="T_9862cada_37ab_11e9_9633_14abc5ca1786level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_9862cada_37ab_11e9_9633_14abc5ca1786row2_col0" class="data row2 col0" >15</td> 
        <td id="T_9862cada_37ab_11e9_9633_14abc5ca1786row2_col1" class="data row2 col1" >$3.35</td> 
        <td id="T_9862cada_37ab_11e9_9633_14abc5ca1786row2_col2" class="data row2 col2" >$50.19</td> 
        <td id="T_9862cada_37ab_11e9_9633_14abc5ca1786row2_col3" class="data row2 col3" >$4.56</td> 
    </tr></tbody> 
</table> 



## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table



```python

age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


purchase_data["Age Group"] = pd.cut(purchase_data["Age"],age_bins, labels=group_names)
purchase_data


age_grouped = purchase_data.groupby("Age Group")


total_count_age = age_grouped["SN"].nunique()


percentage_by_age = (total_count_age/total_players) * 100


age_demographics = pd.DataFrame({"Percentage of Players": percentage_by_age, "Total Count": total_count_age})


age_demographics.index.name = None


age_demographics.style.format({"Percentage of Players":"{:,.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Percentage of Players</th> 
        <th class="col_heading level0 col1" >Total Count</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786level0_row0" class="row_heading level0 row0" ><10</th> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row0_col0" class="data row0 col0" >2.95</td> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row0_col1" class="data row0 col1" >17</td> 
    </tr>    <tr> 
        <th id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786level0_row1" class="row_heading level0 row1" >10-14</th> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row1_col0" class="data row1 col0" >3.82</td> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row1_col1" class="data row1 col1" >22</td> 
    </tr>    <tr> 
        <th id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786level0_row2" class="row_heading level0 row2" >15-19</th> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row2_col0" class="data row2 col0" >18.58</td> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row2_col1" class="data row2 col1" >107</td> 
    </tr>    <tr> 
        <th id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786level0_row3" class="row_heading level0 row3" >20-24</th> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row3_col0" class="data row3 col0" >44.79</td> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row3_col1" class="data row3 col1" >258</td> 
    </tr>    <tr> 
        <th id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786level0_row4" class="row_heading level0 row4" >25-29</th> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row4_col0" class="data row4 col0" >13.37</td> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row4_col1" class="data row4 col1" >77</td> 
    </tr>    <tr> 
        <th id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786level0_row5" class="row_heading level0 row5" >30-34</th> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row5_col0" class="data row5 col0" >9.03</td> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row5_col1" class="data row5 col1" >52</td> 
    </tr>    <tr> 
        <th id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786level0_row6" class="row_heading level0 row6" >35-39</th> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row6_col0" class="data row6 col0" >5.38</td> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row6_col1" class="data row6 col1" >31</td> 
    </tr>    <tr> 
        <th id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786level0_row7" class="row_heading level0 row7" >40+</th> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row7_col0" class="data row7 col0" >2.08</td> 
        <td id="T_035a7bfa_37ab_11e9_a65b_14abc5ca1786row7_col1" class="data row7 col1" >12</td> 
    </tr></tbody> 
</table> 



## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
purchase_count_age = age_grouped["Purchase ID"].count()


avg_purchase_price_age = age_grouped["Price"].mean()


total_purchase_value = age_grouped["Price"].sum()


avg_purchase_per_person_age = total_purchase_value/total_count_age


age_demographics = pd.DataFrame({"Purchase Count": purchase_count_age,
                                 "Average Purchase Price": avg_purchase_price_age,
                                 "Total Purchase Value":total_purchase_value,
                                 "Average Purchase Total per Person": avg_purchase_per_person_age})


age_demographics.index.name = None


age_demographics.style.format({"Average Purchase Price":"${:,.2f}",
                               "Total Purchase Value":"${:,.2f}",
                               "Average Purchase Total per Person":"${:,.2f}"})

```




<style  type="text/css" >
</style>  
<table id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
        <th class="col_heading level0 col3" >Average Purchase Total per Person</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786level0_row0" class="row_heading level0 row0" ><10</th> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row0_col0" class="data row0 col0" >23</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row0_col1" class="data row0 col1" >$3.35</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row0_col2" class="data row0 col2" >$77.13</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row0_col3" class="data row0 col3" >$4.54</td> 
    </tr>    <tr> 
        <th id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786level0_row1" class="row_heading level0 row1" >10-14</th> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row1_col0" class="data row1 col0" >28</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row1_col1" class="data row1 col1" >$2.96</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row1_col2" class="data row1 col2" >$82.78</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row1_col3" class="data row1 col3" >$3.76</td> 
    </tr>    <tr> 
        <th id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786level0_row2" class="row_heading level0 row2" >15-19</th> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row2_col0" class="data row2 col0" >136</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row2_col1" class="data row2 col1" >$3.04</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row2_col2" class="data row2 col2" >$412.89</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row2_col3" class="data row2 col3" >$3.86</td> 
    </tr>    <tr> 
        <th id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786level0_row3" class="row_heading level0 row3" >20-24</th> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row3_col0" class="data row3 col0" >365</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row3_col1" class="data row3 col1" >$3.05</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row3_col2" class="data row3 col2" >$1,114.06</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row3_col3" class="data row3 col3" >$4.32</td> 
    </tr>    <tr> 
        <th id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786level0_row4" class="row_heading level0 row4" >25-29</th> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row4_col0" class="data row4 col0" >101</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row4_col1" class="data row4 col1" >$2.90</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row4_col2" class="data row4 col2" >$293.00</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row4_col3" class="data row4 col3" >$3.81</td> 
    </tr>    <tr> 
        <th id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786level0_row5" class="row_heading level0 row5" >30-34</th> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row5_col0" class="data row5 col0" >73</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row5_col1" class="data row5 col1" >$2.93</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row5_col2" class="data row5 col2" >$214.00</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row5_col3" class="data row5 col3" >$4.12</td> 
    </tr>    <tr> 
        <th id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786level0_row6" class="row_heading level0 row6" >35-39</th> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row6_col0" class="data row6 col0" >41</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row6_col1" class="data row6 col1" >$3.60</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row6_col2" class="data row6 col2" >$147.67</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row6_col3" class="data row6 col3" >$4.76</td> 
    </tr>    <tr> 
        <th id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786level0_row7" class="row_heading level0 row7" >40+</th> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row7_col0" class="data row7 col0" >13</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row7_col1" class="data row7 col1" >$2.94</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row7_col2" class="data row7 col2" >$38.24</td> 
        <td id="T_035daf64_37ab_11e9_9d6c_14abc5ca1786row7_col3" class="data row7 col3" >$3.19</td> 
    </tr></tbody> 
</table> 



## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python
spender_stats = purchase_data.groupby("SN")


purchase_count_spender = spender_stats["Purchase ID"].count()


avg_purchase_price_spender = spender_stats["Price"].mean()


purchase_total_spender = spender_stats["Price"].sum()


top_spenders = pd.DataFrame({"Purchase Count": purchase_count_spender,
                             "Average Purchase Price": avg_purchase_price_spender,
                             "Total Purchase Value":purchase_total_spender})


formatted_spenders = top_spenders.sort_values(["Total Purchase Value"], ascending=False).head()


formatted_spenders.style.format({"Average Purchase Total":"${:,.2f}",
                                 "Average Purchase Price":"${:,.2f}", 
                                 "Total Purchase Value":"${:,.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >SN</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786level0_row0" class="row_heading level0 row0" >Lisosia93</th> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row0_col0" class="data row0 col0" >5</td> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row0_col1" class="data row0 col1" >$3.79</td> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row0_col2" class="data row0 col2" >$18.96</td> 
    </tr>    <tr> 
        <th id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786level0_row1" class="row_heading level0 row1" >Idastidru52</th> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row1_col0" class="data row1 col0" >4</td> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row1_col1" class="data row1 col1" >$3.86</td> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row1_col2" class="data row1 col2" >$15.45</td> 
    </tr>    <tr> 
        <th id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786level0_row2" class="row_heading level0 row2" >Chamjask73</th> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row2_col0" class="data row2 col0" >3</td> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row2_col1" class="data row2 col1" >$4.61</td> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row2_col2" class="data row2 col2" >$13.83</td> 
    </tr>    <tr> 
        <th id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786level0_row3" class="row_heading level0 row3" >Iral74</th> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row3_col0" class="data row3 col0" >4</td> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row3_col1" class="data row3 col1" >$3.40</td> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row3_col2" class="data row3 col2" >$13.62</td> 
    </tr>    <tr> 
        <th id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786level0_row4" class="row_heading level0 row4" >Iskadarya95</th> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row4_col0" class="data row4 col0" >3</td> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row4_col1" class="data row4 col1" >$4.37</td> 
        <td id="T_0362d01c_37ab_11e9_97b9_14abc5ca1786row4_col2" class="data row4 col2" >$13.10</td> 
    </tr></tbody> 
</table> 



## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python
items = purchase_data[["Item ID", "Item Name", "Price"]]


item_stats = items.groupby(["Item ID","Item Name"])


purchase_count_item = item_stats["Price"].count()


purchase_value = (item_stats["Price"].sum()) 


item_price = purchase_value/purchase_count_item


most_popular_items = pd.DataFrame({"Purchase Count": purchase_count_item, 
                                   "Item Price": item_price,
                                   "Total Purchase Value":purchase_value})


popular_formatted = most_popular_items.sort_values(["Purchase Count"], ascending=False).head()


popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786" > 
<thead>    <tr> 
        <th class="blank" ></th> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Item Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item ID</th> 
        <th class="index_name level1" >Item Name</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786level0_row0" class="row_heading level0 row0" >178</th> 
        <th id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786level1_row0" class="row_heading level1 row0" >Oathbreaker, Last Hope of the Breaking Storm</th> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row0_col0" class="data row0 col0" >12</td> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row0_col1" class="data row0 col1" >$4.23</td> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row0_col2" class="data row0 col2" >$50.76</td> 
    </tr>    <tr> 
        <th id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786level0_row1" class="row_heading level0 row1" >145</th> 
        <th id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786level1_row1" class="row_heading level1 row1" >Fiery Glass Crusader</th> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row1_col0" class="data row1 col0" >9</td> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row1_col1" class="data row1 col1" >$4.58</td> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row1_col2" class="data row1 col2" >$41.22</td> 
    </tr>    <tr> 
        <th id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786level0_row2" class="row_heading level0 row2" >108</th> 
        <th id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786level1_row2" class="row_heading level1 row2" >Extraction, Quickblade Of Trembling Hands</th> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row2_col0" class="data row2 col0" >9</td> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row2_col1" class="data row2 col1" >$3.53</td> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row2_col2" class="data row2 col2" >$31.77</td> 
    </tr>    <tr> 
        <th id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786level0_row3" class="row_heading level0 row3" >82</th> 
        <th id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786level1_row3" class="row_heading level1 row3" >Nirvana</th> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row3_col0" class="data row3 col0" >9</td> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row3_col1" class="data row3 col1" >$4.90</td> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row3_col2" class="data row3 col2" >$44.10</td> 
    </tr>    <tr> 
        <th id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786level0_row4" class="row_heading level0 row4" >19</th> 
        <th id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786level1_row4" class="row_heading level1 row4" >Pursuit, Cudgel of Necromancy</th> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row4_col0" class="data row4 col0" >8</td> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row4_col1" class="data row4 col1" >$1.02</td> 
        <td id="T_03661a7a_37ab_11e9_85b3_14abc5ca1786row4_col2" class="data row4 col2" >$8.16</td> 
    </tr></tbody> 
</table> 



## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame




```python

popular_formatted = most_popular_items.sort_values(["Total Purchase Value"],
                                                   ascending=False).head()

popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})
```




<style  type="text/css" >
</style>  
<table id="T_03690448_37ab_11e9_b62a_14abc5ca1786" > 
<thead>    <tr> 
        <th class="blank" ></th> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchase Count</th> 
        <th class="col_heading level0 col1" >Item Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item ID</th> 
        <th class="index_name level1" >Item Name</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_03690448_37ab_11e9_b62a_14abc5ca1786level0_row0" class="row_heading level0 row0" >178</th> 
        <th id="T_03690448_37ab_11e9_b62a_14abc5ca1786level1_row0" class="row_heading level1 row0" >Oathbreaker, Last Hope of the Breaking Storm</th> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row0_col0" class="data row0 col0" >12</td> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row0_col1" class="data row0 col1" >$4.23</td> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row0_col2" class="data row0 col2" >$50.76</td> 
    </tr>    <tr> 
        <th id="T_03690448_37ab_11e9_b62a_14abc5ca1786level0_row1" class="row_heading level0 row1" >82</th> 
        <th id="T_03690448_37ab_11e9_b62a_14abc5ca1786level1_row1" class="row_heading level1 row1" >Nirvana</th> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row1_col0" class="data row1 col0" >9</td> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row1_col1" class="data row1 col1" >$4.90</td> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row1_col2" class="data row1 col2" >$44.10</td> 
    </tr>    <tr> 
        <th id="T_03690448_37ab_11e9_b62a_14abc5ca1786level0_row2" class="row_heading level0 row2" >145</th> 
        <th id="T_03690448_37ab_11e9_b62a_14abc5ca1786level1_row2" class="row_heading level1 row2" >Fiery Glass Crusader</th> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row2_col0" class="data row2 col0" >9</td> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row2_col1" class="data row2 col1" >$4.58</td> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row2_col2" class="data row2 col2" >$41.22</td> 
    </tr>    <tr> 
        <th id="T_03690448_37ab_11e9_b62a_14abc5ca1786level0_row3" class="row_heading level0 row3" >92</th> 
        <th id="T_03690448_37ab_11e9_b62a_14abc5ca1786level1_row3" class="row_heading level1 row3" >Final Critic</th> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row3_col0" class="data row3 col0" >8</td> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row3_col1" class="data row3 col1" >$4.88</td> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row3_col2" class="data row3 col2" >$39.04</td> 
    </tr>    <tr> 
        <th id="T_03690448_37ab_11e9_b62a_14abc5ca1786level0_row4" class="row_heading level0 row4" >103</th> 
        <th id="T_03690448_37ab_11e9_b62a_14abc5ca1786level1_row4" class="row_heading level1 row4" >Singed Scalpel</th> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row4_col0" class="data row4 col0" >8</td> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row4_col1" class="data row4 col1" >$4.35</td> 
        <td id="T_03690448_37ab_11e9_b62a_14abc5ca1786row4_col2" class="data row4 col2" >$34.80</td> 
    </tr></tbody> 
</table> 




```python

```
