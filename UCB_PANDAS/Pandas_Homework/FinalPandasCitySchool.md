

```python
import os
import pandas as pd
from collections import OrderedDict
```


```python
academy_file1=("PyCitySchools/raw_data/schools_complete.csv")
academy_file2=("PyCitySchools/raw_data/students_complete.csv")

schools_df=pd.read_csv(academy_file1)
students_df1=pd.read_csv(academy_file2)

students_df1.head()
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
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
#calculatios part from a district Level

#number of schools
total_schools=schools_df["School ID"].count()
print("Total_Schools:",total_schools)

#Total Budget
total_budget = schools_df["budget"].sum()
print("Total_Budget:",total_budget)

#number of students
total_students = len(students_df1["name"].unique())
print("TotalStudents:",total_students)

#Overall score total students *200
OverallScore = total_students*200
print("OverallScore", OverallScore)

#total math reading scores for all schools
total_math_score = students_df1["math_score"].sum()
total_reading_score = students_df1["reading_score"].sum()
print("Total_Math_Score:", total_math_score)
print("Total_Reading_Score:", total_reading_score)

totalm = totmath["math_score"].sum()
print(totalm)

#mtotal = new_coders_pd['math_score'].sum()
#print("mtotal:",mtotal)

totalMR = total_math_score + total_reading_score
print("TotalMR", totalMR)
#Average reading and math scores for all schools
avg_math_score = students_df1["math_score"].mean()
avg_reading_score = students_df1["reading_score"].mean()
print("Average_Math_Score:",avg_math_score)
print("Average_Reading_Score:", avg_reading_score)

#percentage of math passing math score for all schools
#percentageMath = (totalm/mtotal)*100
#print("PercentageMath:", percentageMath)
overallPerMath = (totalm/OverallScore)*100
print("OverallMath% :",overallPerMath)

passing_group_math_percentage = round((totalm/total_math_score)*100,2)
print("%PassingMathGroup", passing_group_math_percentage)   

passing_group_reading_percentage = round((totalr/total_reading_score)*100,2)
print("%PassingReadingGroup", passing_group_reading_percentage)   

overall_passing_percentage = (passing_group_math_percentage+passing_group_reading_percentage)/2
print("Overall_Passing_Percentage:", overall_passing_percentage)
```

    Total_Schools: 15
    Total_Budget: 24649428
    TotalStudents: 32715
    OverallScore 6543000
    Total_Math_Score: 3093857
    Total_Reading_Score: 3207155
    2480921
    TotalMR 6301012
    Average_Math_Score: 78.98537145774827
    Average_Reading_Score: 81.87784018381414
    OverallMath% : 37.91717866422131
    %PassingMathGroup 80.19
    %PassingReadingGroup 88.53
    Overall_Passing_Percentage: 84.36
    


```python
#group_school_math_sum = students_df1.loc[students_df1["math_score"]>=70].groupby('school').sum()

#group_school_math_sum
```


```python
#Overall cal culations in a tabular form 
district_score_calculations_df =pd.DataFrame({"Average_Math_Score":[avg_math_score],
                                  "Average_Reading_Score":[avg_reading_score],
                                  "TotalSchools":[total_schools],
                                  "TotalBudget":[total_budget],
                                  "TotalStudents":[total_students],
                                  "Overall_Score":[OverallScore],
                                  "Total_Math_Score":[total_math_score],
                                  "Total_Reading_Score":[total_reading_score],
                                  "%PassingMathGroup":[passing_group_math_percentage],
                                  "%PassingReadingGroup":[passing_group_reading_percentage],
                                  "%PassingOverallGroup":[overall_passing_percentage]            
                                  })
#score_cal= pd.DataFrame(columns=['eachScore','ScoresPercentage'],
                                  #index=['math','reading'])
#data = score_cal.loc(score_cal['eachaScore']=="Nan":"total_mscore")
district_score_calculations_df
#data
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
      <th>%PassingMathGroup</th>
      <th>%PassingOverallGroup</th>
      <th>%PassingReadingGroup</th>
      <th>Average_Math_Score</th>
      <th>Average_Reading_Score</th>
      <th>Overall_Score</th>
      <th>TotalBudget</th>
      <th>TotalSchools</th>
      <th>TotalStudents</th>
      <th>Total_Math_Score</th>
      <th>Total_Reading_Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>80.19</td>
      <td>84.36</td>
      <td>88.53</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>6543000</td>
      <td>24649428</td>
      <td>15</td>
      <td>32715</td>
      <td>3093857</td>
      <td>3207155</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_coders_pd = students_df1.iloc[:,[0,1,5,6]]
new_coders_pd.head()
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
      <th>Student ID</th>
      <th>name</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
totmath = new_coders_pd.loc[new_coders_pd["math_score"]>=70]

totmath.head()


stuTotal = len(new_coders_pd["name"].unique())
print("TotalStudents:",stuTotal)
```

    TotalStudents: 32715
    


```python
totalm = totmath["math_score"].sum()
print(totalm)

mtotal = new_coders_pd['math_score'].sum()
print("mtotal:",mtotal)

OverallScore = total_students*200
print("OverallScore", OverallScore)

percentageMath = (totalm/mtotal)*100
print("PercentageMath:", percentageMath)

overallPerMath = (totalm/OverallScore)*100
print("OverallMath% :",overallPerMath)
```

    2480921
    mtotal: 3093857
    OverallScore 6543000
    PercentageMath: 80.1886124665749
    OverallMath% : 37.91717866422131
    


```python
totreading = new_coders_pd.loc[new_coders_pd["reading_score"]>=70]
totreading.head()
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
      <th>Student ID</th>
      <th>name</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>97</td>
      <td>84</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Bryan Miranda</td>
      <td>94</td>
      <td>94</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Sheena Carter</td>
      <td>82</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
totalr = totreading["reading_score"].sum()
print(totalr)

rtotal = new_coders_pd['reading_score'].sum()
print("rtotal:",rtotal)

OverallScore = total_students*200
print("OverallScore", OverallScore)

percentageReading = (totalr/rtotal)*100
print("PercentageMath:", percentageReading)

overallPerReading = (totalr/OverallScore)*100
print("OverallMath% :",overallPerReading)
```

    2839146
    rtotal: 3207155
    OverallScore 6543000
    PercentageMath: 88.52537529367929
    OverallMath% : 43.39211370930766
    


```python
each_school_df=students_df1.iloc[:,[0,4,5,6]]
each_school_df.head()
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
      <th>Student ID</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
#group math score without condition
#grouped = each_school_df["math_score"].groupby(each_school_df['school']).sum()

#grouped
```


```python
#each_schools_math_average = each_school_df["math_score"].groupby(each_school_df["school"]).mean()
#each_schools_math_average
```


```python
#tm = round((school_math_sum["math_score"]/grouped)*100,2)
#tm1 = (school_math_sum["math_score"]/mtotal)*100

#print("Grouped:",tm)
```


```python
#school_reading_sum = each_school_df.loc[each_school_df["reading_score"]>=70].groupby("school").sum()
#school_reading_sum
```


```python
#grouped_reading = each_school_df["reading_score"].groupby(each_school_df['school']).sum()

#grouped_reading
```


```python
#totaleachReading = school_math_sum["reading_score"].sum()
#tr = round((school_math_sum["reading_score"]/grouped_reading)*100,2)
#print("Grouped:",tr,)
#tm1 = (school_math_sum["math_score"]/mtotal)*100

```


```python
#overall % passing group percentage
#overall_group_passing_percentage = round((tr+tm)/2,2)
#print("OverallGroupPassingPercentage:", overall_group_passing_percentage)
```


```python
#Budget table from schools data frame  
budget_info_pd =pd.DataFrame({"School":["Bailey High School","Johnson High School","Hernandez High School","Rodriguez High School",
                 "Figueroa High School","Huang High School","Ford High School","Wilson High School","Cabrera High School",
                 "Wright High School","Shelton High School","Thomas High School","Griffin High School","Pena High School",
                 "Holden High School"],
                       "Type":["District","District","District","District","District","District","District","Charter",
                         "Charter","Charter","Charter","Charter","Charter","Charter","Charter"],
                       "TotalBudget":["$3124928","$3094650","$3022020","$2547363","$1884411","$1910635","$1763916",
                                 "$1319574","$1081356","$1049400","$1056600","$1043130","$917500","$585858","$248087"], 
                        "Size":[4976,4761,4635,3999,2949,2917,2739,2283,1858,1800,1761,1635,1468,962,427] })          
#info_pd = pd.DataFrame(raw_data_info)

budget_info_pd
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
      <th>School</th>
      <th>Size</th>
      <th>TotalBudget</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>4976</td>
      <td>$3124928</td>
      <td>District</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Johnson High School</td>
      <td>4761</td>
      <td>$3094650</td>
      <td>District</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Hernandez High School</td>
      <td>4635</td>
      <td>$3022020</td>
      <td>District</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Rodriguez High School</td>
      <td>3999</td>
      <td>$2547363</td>
      <td>District</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Figueroa High School</td>
      <td>2949</td>
      <td>$1884411</td>
      <td>District</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Huang High School</td>
      <td>2917</td>
      <td>$1910635</td>
      <td>District</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Ford High School</td>
      <td>2739</td>
      <td>$1763916</td>
      <td>District</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Wilson High School</td>
      <td>2283</td>
      <td>$1319574</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Cabrera High School</td>
      <td>1858</td>
      <td>$1081356</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Wright High School</td>
      <td>1800</td>
      <td>$1049400</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Shelton High School</td>
      <td>1761</td>
      <td>$1056600</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Thomas High School</td>
      <td>1635</td>
      <td>$1043130</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Griffin High School</td>
      <td>1468</td>
      <td>$917500</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Pena High School</td>
      <td>962</td>
      <td>$585858</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Holden High School</td>
      <td>427</td>
      <td>$248087</td>
      <td>Charter</td>
    </tr>
  </tbody>
</table>
</div>




```python
#creating a data frame for Each school calcualtions

info_pd =pd.DataFrame({"School":["Bailey High School","Johnson High School","Hernandez High School","Rodriguez High School",
                 "Figueroa High School","Huang High School","Ford High School","Wilson High School","Cabrera High School",
                 "Wright High School","Shelton High School","Thomas High School","Griffin High School","Pena High School",
                 "Holden High School"],
                 "Averag Math Score":[77.048432,77.072464,77.289752,76.842711,76.711767,76.629414, 77.102592,
                                      83.274201,83.061895,83.682222,83.359455,83.418349,83.351499,83.839917,83.803279],
                   
                 "%PassingMath":[73.13,72.63,73.36,72.84,72.84,72.53,72.21,74.57,94.96,95.17,94.53,94.96,94.48,
                                94.56,95.59],
                  "Average Reading Score":[81.033963,80.966394,80.934412,80.744686,81.158020,81.182722,80.746258,
                                          83.989488,83.975780,83.955000,83.725724,83.848930,83.816757, 84.044699,83.814988],
                   
                 "%PassingReading":[66.66,65.97,66.69,66.25,65.99,65.68,68.43,93.91,94.11,93.35,93.74,93.31,
                                    93.34,94.64,92.64],      

                  "OverallPaasing%":[69.90, 69.30,70.03,69.54,69.26,68.94,71.50,94.44,94.64,93.94,94.35,93.90,93.95,
                                    95.12, 93.26] })


#info_pd = pd.DataFrame(raw_data_info)

info_pd
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
      <th>%PassingMath</th>
      <th>%PassingReading</th>
      <th>Averag Math Score</th>
      <th>Average Reading Score</th>
      <th>OverallPaasing%</th>
      <th>School</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>73.13</td>
      <td>66.66</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>69.90</td>
      <td>Bailey High School</td>
    </tr>
    <tr>
      <th>1</th>
      <td>72.63</td>
      <td>65.97</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>69.30</td>
      <td>Johnson High School</td>
    </tr>
    <tr>
      <th>2</th>
      <td>73.36</td>
      <td>66.69</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>70.03</td>
      <td>Hernandez High School</td>
    </tr>
    <tr>
      <th>3</th>
      <td>72.84</td>
      <td>66.25</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>69.54</td>
      <td>Rodriguez High School</td>
    </tr>
    <tr>
      <th>4</th>
      <td>72.84</td>
      <td>65.99</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>69.26</td>
      <td>Figueroa High School</td>
    </tr>
    <tr>
      <th>5</th>
      <td>72.53</td>
      <td>65.68</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>68.94</td>
      <td>Huang High School</td>
    </tr>
    <tr>
      <th>6</th>
      <td>72.21</td>
      <td>68.43</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>71.50</td>
      <td>Ford High School</td>
    </tr>
    <tr>
      <th>7</th>
      <td>74.57</td>
      <td>93.91</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>94.44</td>
      <td>Wilson High School</td>
    </tr>
    <tr>
      <th>8</th>
      <td>94.96</td>
      <td>94.11</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.64</td>
      <td>Cabrera High School</td>
    </tr>
    <tr>
      <th>9</th>
      <td>95.17</td>
      <td>93.35</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>93.94</td>
      <td>Wright High School</td>
    </tr>
    <tr>
      <th>10</th>
      <td>94.53</td>
      <td>93.74</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>94.35</td>
      <td>Shelton High School</td>
    </tr>
    <tr>
      <th>11</th>
      <td>94.96</td>
      <td>93.31</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>93.90</td>
      <td>Thomas High School</td>
    </tr>
    <tr>
      <th>12</th>
      <td>94.48</td>
      <td>93.34</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.95</td>
      <td>Griffin High School</td>
    </tr>
    <tr>
      <th>13</th>
      <td>94.56</td>
      <td>94.64</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>95.12</td>
      <td>Pena High School</td>
    </tr>
    <tr>
      <th>14</th>
      <td>95.59</td>
      <td>92.64</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>93.26</td>
      <td>Holden High School</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top Performing Schools (By Passing Rate) table
dis= info_pd.loc[info_pd["OverallPaasing%"]>=75.11].groupby("School")
dis.head(2)

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
      <th>%PassingMath</th>
      <th>%PassingReading</th>
      <th>Averag Math Score</th>
      <th>Average Reading Score</th>
      <th>OverallPaasing%</th>
      <th>School</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>74.57</td>
      <td>93.91</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>94.44</td>
      <td>Wilson High School</td>
    </tr>
    <tr>
      <th>8</th>
      <td>94.96</td>
      <td>94.11</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.64</td>
      <td>Cabrera High School</td>
    </tr>
    <tr>
      <th>9</th>
      <td>95.17</td>
      <td>93.35</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>93.94</td>
      <td>Wright High School</td>
    </tr>
    <tr>
      <th>10</th>
      <td>94.53</td>
      <td>93.74</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>94.35</td>
      <td>Shelton High School</td>
    </tr>
    <tr>
      <th>11</th>
      <td>94.96</td>
      <td>93.31</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>93.90</td>
      <td>Thomas High School</td>
    </tr>
    <tr>
      <th>12</th>
      <td>94.48</td>
      <td>93.34</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.95</td>
      <td>Griffin High School</td>
    </tr>
    <tr>
      <th>13</th>
      <td>94.56</td>
      <td>94.64</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>95.12</td>
      <td>Pena High School</td>
    </tr>
    <tr>
      <th>14</th>
      <td>95.59</td>
      <td>92.64</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>93.26</td>
      <td>Holden High School</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Bottom performing schools (by passing rate) Table
dis_bottom= info_pd.loc[info_pd["OverallPaasing%"]<=75.11].groupby("School")
dis_bottom.head()
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
      <th>%PassingMath</th>
      <th>%PassingReading</th>
      <th>Averag Math Score</th>
      <th>Average Reading Score</th>
      <th>OverallPaasing%</th>
      <th>School</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>73.13</td>
      <td>66.66</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>69.90</td>
      <td>Bailey High School</td>
    </tr>
    <tr>
      <th>1</th>
      <td>72.63</td>
      <td>65.97</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>69.30</td>
      <td>Johnson High School</td>
    </tr>
    <tr>
      <th>2</th>
      <td>73.36</td>
      <td>66.69</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>70.03</td>
      <td>Hernandez High School</td>
    </tr>
    <tr>
      <th>3</th>
      <td>72.84</td>
      <td>66.25</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>69.54</td>
      <td>Rodriguez High School</td>
    </tr>
    <tr>
      <th>4</th>
      <td>72.84</td>
      <td>65.99</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>69.26</td>
      <td>Figueroa High School</td>
    </tr>
    <tr>
      <th>5</th>
      <td>72.53</td>
      <td>65.68</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>68.94</td>
      <td>Huang High School</td>
    </tr>
    <tr>
      <th>6</th>
      <td>72.21</td>
      <td>68.43</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>71.50</td>
      <td>Ford High School</td>
    </tr>
  </tbody>
</table>
</div>




```python
#school_math_sum = each_school_df.loc[each_school_df["math_score"]>=70].groupby('school').sum()

#school_math_sum
```


```python
students_df1.head()
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
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Math Scores by grade
grade234 = students_df1.groupby(['grade','school'])[['math_score']].mean()   
#grade234
```


```python
# A Data frame for each shool to caluculate math_score mean() for all grades 
grades = OrderedDict([('school',["Bailey High School","Cabrera High School","Figueroa High School","Ford High School",         
                               "Griffin High School","Hernandez High School","Holden High School","Huang High School",         
                               "Johnson High School","Pena High School","Rodriguez High School","Shelton High School",      
                                "Thomas High School","Wilson High School","Wright High School"]),        

                    ("9th",[76.996772,83.094697,76.403037,77.361345,82.044010,77.438495,83.787402,77.027251,
                            77.187857,83.625455,76.859966,83.420755,83.590022,83.085578,83.264706]),
                    ("10th",[76.996772,83.154506,76.539974,77.672316,84.229064,77.337408,83.429825,75.908735,
                            76.691117,83.372000,76.612500,82.917411,83.087886,83.724422,84.010288]),
                    ("11th",[77.515588,82.765560,76.884344,76.918058,83.842105,77.136029,85.000000,76.446602,
                             77.491653,84.328125,76.395626,83.383495,83.498795,83.195326,83.836782]),
                    ("12th",[76.492218,83.277487,77.151369,76.179963,83.356164,77.186567,82.855422,77.225641,
                             76.863248,84.121547,77.690748,83.778976,83.497041,83.035794,83.644986])])
df=pd.DataFrame.from_dict(grades)
df

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
      <th>school</th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>76.996772</td>
      <td>76.996772</td>
      <td>77.515588</td>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.094697</td>
      <td>83.154506</td>
      <td>82.765560</td>
      <td>83.277487</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>76.403037</td>
      <td>76.539974</td>
      <td>76.884344</td>
      <td>77.151369</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>77.361345</td>
      <td>77.672316</td>
      <td>76.918058</td>
      <td>76.179963</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>82.044010</td>
      <td>84.229064</td>
      <td>83.842105</td>
      <td>83.356164</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>77.438495</td>
      <td>77.337408</td>
      <td>77.136029</td>
      <td>77.186567</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.787402</td>
      <td>83.429825</td>
      <td>85.000000</td>
      <td>82.855422</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>77.027251</td>
      <td>75.908735</td>
      <td>76.446602</td>
      <td>77.225641</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>77.187857</td>
      <td>76.691117</td>
      <td>77.491653</td>
      <td>76.863248</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>83.625455</td>
      <td>83.372000</td>
      <td>84.328125</td>
      <td>84.121547</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>76.859966</td>
      <td>76.612500</td>
      <td>76.395626</td>
      <td>77.690748</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>83.420755</td>
      <td>82.917411</td>
      <td>83.383495</td>
      <td>83.778976</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.590022</td>
      <td>83.087886</td>
      <td>83.498795</td>
      <td>83.497041</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.085578</td>
      <td>83.724422</td>
      <td>83.195326</td>
      <td>83.035794</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>83.264706</td>
      <td>84.010288</td>
      <td>83.836782</td>
      <td>83.644986</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Reading Scores by grade 
gradeReading = students_df1.groupby(['grade','school'])[['reading_score']].mean() 
#gradeReading
```


```python
#A Data frame for each shool to caluculate reading_score mean() for all grades
grades_Reading = OrderedDict([('school',["Bailey High School","Cabrera High School","Figueroa High School","Ford High School",         
                               "Griffin High School","Hernandez High School","Holden High School","Huang High School",         
                               "Johnson High School","Pena High School","Rodriguez High School","Shelton High School",      
                                "Thomas High School","Wilson High School","Wright High School"]),        

                    ("9th",[81.303155,83.676136,81.198598,80.632653,83.369193,80.866860,83.677165,
                            81.290284,81.260714,83.807273,80.993127,84.122642,83.728850,83.939778,83.833333]),
                    ("10th",[80.907183,84.253219,81.408912,81.262712,83.706897,80.660147,83.324561,81.512386,
                             80.773431,83.612000,80.629808,83.441964,84.254157,84.021452,83.812757]),
                    ("11th",[80.945643,83.788382,80.640339,80.403642,84.288089,81.396140,83.815534,81.417476,
                             80.616027,84.335938,80.864811,84.373786,83.585542,83.764608,84.156322]),
                    ("12th",[80.912451,84.287958,81.384863,80.662338,84.013699,80.857143,84.698795,80.305983,
                             81.227564,84.591160,80.376426,82.781671,83.831361,84.317673,84.073171])])         
                             
df1=pd.DataFrame.from_dict(grades_Reading)
df1
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
      <th>school</th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bailey High School</td>
      <td>81.303155</td>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cabrera High School</td>
      <td>83.676136</td>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Figueroa High School</td>
      <td>81.198598</td>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ford High School</td>
      <td>80.632653</td>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83.369193</td>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Hernandez High School</td>
      <td>80.866860</td>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Holden High School</td>
      <td>83.677165</td>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Huang High School</td>
      <td>81.290284</td>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Johnson High School</td>
      <td>81.260714</td>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>83.807273</td>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rodriguez High School</td>
      <td>80.993127</td>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Shelton High School</td>
      <td>84.122642</td>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Thomas High School</td>
      <td>83.728850</td>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Wilson High School</td>
      <td>83.939778</td>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Wright High School</td>
      <td>83.833333</td>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
    </tr>
  </tbody>
</table>
</div>




```python
#chocolate_ratings_df["Cocoa Percent"] = chocolate_ratings_df["Cocoa Percent"].replace("%","")
```


```python
#schools_df
```


```python
merge_table = pd.merge(info_pd, budget_info_pd, on="School")
merge_table
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
      <th>%PassingMath</th>
      <th>%PassingReading</th>
      <th>Averag Math Score</th>
      <th>Average Reading Score</th>
      <th>OverallPaasing%</th>
      <th>School</th>
      <th>Size</th>
      <th>TotalBudget</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>73.13</td>
      <td>66.66</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>69.90</td>
      <td>Bailey High School</td>
      <td>4976</td>
      <td>$3124928</td>
      <td>District</td>
    </tr>
    <tr>
      <th>1</th>
      <td>72.63</td>
      <td>65.97</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>69.30</td>
      <td>Johnson High School</td>
      <td>4761</td>
      <td>$3094650</td>
      <td>District</td>
    </tr>
    <tr>
      <th>2</th>
      <td>73.36</td>
      <td>66.69</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>70.03</td>
      <td>Hernandez High School</td>
      <td>4635</td>
      <td>$3022020</td>
      <td>District</td>
    </tr>
    <tr>
      <th>3</th>
      <td>72.84</td>
      <td>66.25</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>69.54</td>
      <td>Rodriguez High School</td>
      <td>3999</td>
      <td>$2547363</td>
      <td>District</td>
    </tr>
    <tr>
      <th>4</th>
      <td>72.84</td>
      <td>65.99</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>69.26</td>
      <td>Figueroa High School</td>
      <td>2949</td>
      <td>$1884411</td>
      <td>District</td>
    </tr>
    <tr>
      <th>5</th>
      <td>72.53</td>
      <td>65.68</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>68.94</td>
      <td>Huang High School</td>
      <td>2917</td>
      <td>$1910635</td>
      <td>District</td>
    </tr>
    <tr>
      <th>6</th>
      <td>72.21</td>
      <td>68.43</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>71.50</td>
      <td>Ford High School</td>
      <td>2739</td>
      <td>$1763916</td>
      <td>District</td>
    </tr>
    <tr>
      <th>7</th>
      <td>74.57</td>
      <td>93.91</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>94.44</td>
      <td>Wilson High School</td>
      <td>2283</td>
      <td>$1319574</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>8</th>
      <td>94.96</td>
      <td>94.11</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.64</td>
      <td>Cabrera High School</td>
      <td>1858</td>
      <td>$1081356</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>9</th>
      <td>95.17</td>
      <td>93.35</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>93.94</td>
      <td>Wright High School</td>
      <td>1800</td>
      <td>$1049400</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>10</th>
      <td>94.53</td>
      <td>93.74</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>94.35</td>
      <td>Shelton High School</td>
      <td>1761</td>
      <td>$1056600</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>11</th>
      <td>94.96</td>
      <td>93.31</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>93.90</td>
      <td>Thomas High School</td>
      <td>1635</td>
      <td>$1043130</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>12</th>
      <td>94.48</td>
      <td>93.34</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.95</td>
      <td>Griffin High School</td>
      <td>1468</td>
      <td>$917500</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>13</th>
      <td>94.56</td>
      <td>94.64</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>95.12</td>
      <td>Pena High School</td>
      <td>962</td>
      <td>$585858</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>14</th>
      <td>95.59</td>
      <td>92.64</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>93.26</td>
      <td>Holden High School</td>
      <td>427</td>
      <td>$248087</td>
      <td>Charter</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Scores by school spending (reasonble approximation) using bins and cut 
#create bins for the budget
bins = [585858, 917500, 1081356, 1763916, 1910635]

# Create the names for the four bins
group_names = ['$585858', '$917500-1081356', '$1081356-1763916', '$1763916-191063']

```


```python
# Cut postBudget from the school_df and place the new labels into bins
pd.cut(schools_df["budget"], bins, labels=group_names)

```




    0      $1763916-191063
    1      $1763916-191063
    2      $917500-1081356
    3                  NaN
    4              $585858
    5     $1081356-1763916
    6      $917500-1081356
    7                  NaN
    8                  NaN
    9                  NaN
    10     $917500-1081356
    11                 NaN
    12                 NaN
    13    $1081356-1763916
    14     $917500-1081356
    Name: budget, dtype: category
    Categories (4, object): [$585858 < $917500-1081356 < $1081356-1763916 < $1763916-191063]




```python
merge_table["TotalBudget"] = pd.cut(schools_df["budget"], bins, labels=group_names)

merge_table
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
      <th>%PassingMath</th>
      <th>%PassingReading</th>
      <th>Averag Math Score</th>
      <th>Average Reading Score</th>
      <th>OverallPaasing%</th>
      <th>School</th>
      <th>Size</th>
      <th>TotalBudget</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>73.13</td>
      <td>66.66</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>69.90</td>
      <td>Bailey High School</td>
      <td>3000-000</td>
      <td>$1763916-191063</td>
      <td>District</td>
    </tr>
    <tr>
      <th>1</th>
      <td>72.63</td>
      <td>65.97</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>69.30</td>
      <td>Johnson High School</td>
      <td>3000-000</td>
      <td>$1763916-191063</td>
      <td>District</td>
    </tr>
    <tr>
      <th>2</th>
      <td>73.36</td>
      <td>66.69</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>70.03</td>
      <td>Hernandez High School</td>
      <td>1000-2000</td>
      <td>$917500-1081356</td>
      <td>District</td>
    </tr>
    <tr>
      <th>3</th>
      <td>72.84</td>
      <td>66.25</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>69.54</td>
      <td>Rodriguez High School</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>District</td>
    </tr>
    <tr>
      <th>4</th>
      <td>72.84</td>
      <td>65.99</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>69.26</td>
      <td>Figueroa High School</td>
      <td>1000-2000</td>
      <td>$585858</td>
      <td>District</td>
    </tr>
    <tr>
      <th>5</th>
      <td>72.53</td>
      <td>65.68</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>68.94</td>
      <td>Huang High School</td>
      <td>3000-000</td>
      <td>$1081356-1763916</td>
      <td>District</td>
    </tr>
    <tr>
      <th>6</th>
      <td>72.21</td>
      <td>68.43</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>71.50</td>
      <td>Ford High School</td>
      <td>1000-2000</td>
      <td>$917500-1081356</td>
      <td>District</td>
    </tr>
    <tr>
      <th>7</th>
      <td>74.57</td>
      <td>93.91</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>94.44</td>
      <td>Wilson High School</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>8</th>
      <td>94.96</td>
      <td>94.11</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.64</td>
      <td>Cabrera High School</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>9</th>
      <td>95.17</td>
      <td>93.35</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>93.94</td>
      <td>Wright High School</td>
      <td>&lt;500</td>
      <td>NaN</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>10</th>
      <td>94.53</td>
      <td>93.74</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>94.35</td>
      <td>Shelton High School</td>
      <td>1000-2000</td>
      <td>$917500-1081356</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>11</th>
      <td>94.96</td>
      <td>93.31</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>93.90</td>
      <td>Thomas High School</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>12</th>
      <td>94.48</td>
      <td>93.34</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.95</td>
      <td>Griffin High School</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>13</th>
      <td>94.56</td>
      <td>94.64</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>95.12</td>
      <td>Pena High School</td>
      <td>3000-000</td>
      <td>$1081356-1763916</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>14</th>
      <td>95.59</td>
      <td>92.64</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>93.26</td>
      <td>Holden High School</td>
      <td>1000-2000</td>
      <td>$917500-1081356</td>
      <td>Charter</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Scores by school spending.Creating a group based off of the bins
regiment_groups = merge_table.groupby("TotalBudget")
regiment_groups.max()
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
      <th>%PassingMath</th>
      <th>%PassingReading</th>
      <th>Averag Math Score</th>
      <th>Average Reading Score</th>
      <th>OverallPaasing%</th>
      <th>School</th>
      <th>Size</th>
      <th>Type</th>
    </tr>
    <tr>
      <th>TotalBudget</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>$585858</th>
      <td>72.84</td>
      <td>65.99</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>69.26</td>
      <td>Figueroa High School</td>
      <td>1000-2000</td>
      <td>District</td>
    </tr>
    <tr>
      <th>$917500-1081356</th>
      <td>95.59</td>
      <td>93.74</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>94.35</td>
      <td>Shelton High School</td>
      <td>1000-2000</td>
      <td>District</td>
    </tr>
    <tr>
      <th>$1081356-1763916</th>
      <td>94.56</td>
      <td>94.64</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>95.12</td>
      <td>Pena High School</td>
      <td>3000-000</td>
      <td>District</td>
    </tr>
    <tr>
      <th>$1763916-191063</th>
      <td>73.13</td>
      <td>66.66</td>
      <td>77.072464</td>
      <td>81.033963</td>
      <td>69.90</td>
      <td>Johnson High School</td>
      <td>3000-000</td>
      <td>District</td>
    </tr>
  </tbody>
</table>
</div>




```python
#schools_df
```


```python
#Scores by school spending (reasonble approximation) using bins and cut 
#create bins for size in school_df
bins1 = [500,1000,2000,3000]

# Create the names for the four bins
group_names = ['<500', '1000-2000', '3000-000']

```


```python
# Cut postSize and place thenew lables into bins
pd.cut(schools_df["size"], bins1, labels=group_names)
```




    0      3000-000
    1      3000-000
    2     1000-2000
    3           NaN
    4     1000-2000
    5      3000-000
    6     1000-2000
    7           NaN
    8           NaN
    9          <500
    10    1000-2000
    11          NaN
    12          NaN
    13     3000-000
    14    1000-2000
    Name: size, dtype: category
    Categories (3, object): [<500 < 1000-2000 < 3000-000]




```python
#A table consists of new values in column size
merge_table["Size"] = pd.cut(schools_df["size"], bins1, labels=group_names)

merge_table
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
      <th>%PassingMath</th>
      <th>%PassingReading</th>
      <th>Averag Math Score</th>
      <th>Average Reading Score</th>
      <th>OverallPaasing%</th>
      <th>School</th>
      <th>Size</th>
      <th>TotalBudget</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>73.13</td>
      <td>66.66</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>69.90</td>
      <td>Bailey High School</td>
      <td>3000-000</td>
      <td>$3124928</td>
      <td>District</td>
    </tr>
    <tr>
      <th>1</th>
      <td>72.63</td>
      <td>65.97</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>69.30</td>
      <td>Johnson High School</td>
      <td>3000-000</td>
      <td>$3094650</td>
      <td>District</td>
    </tr>
    <tr>
      <th>2</th>
      <td>73.36</td>
      <td>66.69</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>70.03</td>
      <td>Hernandez High School</td>
      <td>1000-2000</td>
      <td>$3022020</td>
      <td>District</td>
    </tr>
    <tr>
      <th>3</th>
      <td>72.84</td>
      <td>66.25</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>69.54</td>
      <td>Rodriguez High School</td>
      <td>NaN</td>
      <td>$2547363</td>
      <td>District</td>
    </tr>
    <tr>
      <th>4</th>
      <td>72.84</td>
      <td>65.99</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>69.26</td>
      <td>Figueroa High School</td>
      <td>1000-2000</td>
      <td>$1884411</td>
      <td>District</td>
    </tr>
    <tr>
      <th>5</th>
      <td>72.53</td>
      <td>65.68</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>68.94</td>
      <td>Huang High School</td>
      <td>3000-000</td>
      <td>$1910635</td>
      <td>District</td>
    </tr>
    <tr>
      <th>6</th>
      <td>72.21</td>
      <td>68.43</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>71.50</td>
      <td>Ford High School</td>
      <td>1000-2000</td>
      <td>$1763916</td>
      <td>District</td>
    </tr>
    <tr>
      <th>7</th>
      <td>74.57</td>
      <td>93.91</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>94.44</td>
      <td>Wilson High School</td>
      <td>NaN</td>
      <td>$1319574</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>8</th>
      <td>94.96</td>
      <td>94.11</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.64</td>
      <td>Cabrera High School</td>
      <td>NaN</td>
      <td>$1081356</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>9</th>
      <td>95.17</td>
      <td>93.35</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>93.94</td>
      <td>Wright High School</td>
      <td>&lt;500</td>
      <td>$1049400</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>10</th>
      <td>94.53</td>
      <td>93.74</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>94.35</td>
      <td>Shelton High School</td>
      <td>1000-2000</td>
      <td>$1056600</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>11</th>
      <td>94.96</td>
      <td>93.31</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>93.90</td>
      <td>Thomas High School</td>
      <td>NaN</td>
      <td>$1043130</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>12</th>
      <td>94.48</td>
      <td>93.34</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.95</td>
      <td>Griffin High School</td>
      <td>NaN</td>
      <td>$917500</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>13</th>
      <td>94.56</td>
      <td>94.64</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>95.12</td>
      <td>Pena High School</td>
      <td>3000-000</td>
      <td>$585858</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>14</th>
      <td>95.59</td>
      <td>92.64</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>93.26</td>
      <td>Holden High School</td>
      <td>1000-2000</td>
      <td>$248087</td>
      <td>Charter</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Scores by school size.Creating a group based off of the bins
regiment_groups1 = merge_table.groupby("Size")
regiment_groups1.max()
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
      <th>%PassingMath</th>
      <th>%PassingReading</th>
      <th>Averag Math Score</th>
      <th>Average Reading Score</th>
      <th>OverallPaasing%</th>
      <th>School</th>
      <th>TotalBudget</th>
      <th>Type</th>
    </tr>
    <tr>
      <th>Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;500</th>
      <td>95.17</td>
      <td>93.35</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>93.94</td>
      <td>Wright High School</td>
      <td>$1049400</td>
      <td>Charter</td>
    </tr>
    <tr>
      <th>1000-2000</th>
      <td>95.59</td>
      <td>93.74</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>94.35</td>
      <td>Shelton High School</td>
      <td>$3022020</td>
      <td>District</td>
    </tr>
    <tr>
      <th>3000-000</th>
      <td>94.56</td>
      <td>94.64</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>95.12</td>
      <td>Pena High School</td>
      <td>$585858</td>
      <td>District</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Scores by school spending (reasonble approximation) using bins and cut 
#create bins for size in school_df
bin4 = ['Charter','District']

# Create the names for the four bins
group_names = ['District']
#group_names = ['Low', 'ok', 'good', 'great']
```


```python
# Cut postTestS labels=group_names)
```


```python
 #Cut postTestScore and place the scores into bins
#pd.cut(schools_df["type"], bin4,labels=group_names)
```
