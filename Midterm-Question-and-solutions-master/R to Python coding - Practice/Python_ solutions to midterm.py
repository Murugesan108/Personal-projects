import os
import pandas as pd
import numpy as np

print os.getcwd()

#Currently in the Midterm test solutions folder 

#Let's read the Titanic dataset

#Listing the folders in the current dataset
dir_list =  os.listdir(os.getcwd())

req_file = filter(lambda x: 'Titanic' in x, dir_list)

#Assuming we get only one value 

t_file = pd.read_csv(req_file[0])

print t_file.head()
print t_file.dtypes
print t_file.describe()

print "Null values: \n" , t_file.isnull().sum()


#Question 1

t_file_max = t_file[t_file.Age == t_file.Age.max()]
#Add proper brackets
t_file1 = t_file[(t_file['Age'] == max(t_file['Age'])/2) & (t_file['Survived'] == 0)]


q1_answer = t_file1.loc[(t_file1.PassengerId - t_file_max.PassengerId.values).abs().idxmin()]

print(q1_answer)


#Question 2

#If ascending has 1 - then ascending order else descending
t_file_sort = t_file.sort(['Pclass','Fare','Age'],ascending = [0,0,1])

q2_answer = t_file_sort.iloc[0]['Ticket']

#Brownie question

brownie_index = t_file_sort[(t_file_sort.Sex == "male") & (t_file_sort.Age % 2 == 0) &
                 (t_file_sort.Pclass == 1)][0:1].index

print np.where((t_file_sort.index.values) == (brownie_index.values))

print t_file_sort.index.get_loc(brownie_index.values[0])


#Question 3

t1 = t_file[(t_file.Sex == "male") & (t_file.Survived == 1) & (t_file.Embarked == "S") & (t_file.Pclass == 3)]
t2 = t_file[(t_file.Sex == "female") & (t_file.Survived == 0) & (t_file.Embarked == "C") & (t_file.Pclass == 1)]

t3 = t1.append(t2)

q3_answer = len(t3['Ticket'].unique())



#Question 4

t_4 = t_file
t_4.loc[t_4.Name.str.contains('Miss.'),'Sex'] = 'Girl'
t_4.loc[t_4.Name.str.contains('Master.'),'Sex'] = 'Boy'

q4_answer = t_4



#Question 5 - Factors (skipped)

#Question 6

data = t_file

data.loc[data.Pclass == 1,'Pclass'] = "First"
data.loc[data.Pclass == 2,'Pclass'] = "Second"
data.loc[data.Pclass == 3,'Pclass'] = "Third"

# a)

melt_data = pd.melt(data, id_vars = ['Sex','Pclass'])
melt_data = melt_data[melt_data.variable == 'Fare']

q6_a_answer = pd.pivot_table(melt_data, values = 'value', index = ['Sex'], columns = ['Pclass'],
                  aggfunc = lambda x: sum(x)/len(x), fill_value = 0)
                  
             
# b) 

melt_data2 = pd.melt(data, id_vars = ['Pclass'])
melt_data2 = melt_data2[melt_data2.variable.isin(['Fare','Age'])]

#Filling na values with zero as of now

melt_no_na = melt_data2.fillna(0)

q6_a_answer = pd.pivot_table(melt_no_na, values = 'value', index = ['Pclass'], columns = ['variable'],
                  aggfunc = lambda x: sum(x)/len(x))
                  
                  
# Question 7
                  
                  
q7_data = t_file

t_dead = q7_data[q7_data.Survived == 0]
accident_year = 1912
count = 0
birth_year = 0

#iterrows() will loop through each row
for each in t_dead.iterrows():

    if (~np.isnan(each[1].Age)):
        birth_year = accident_year - each[1].Age 
    else:
        next
  
    if each[1].Sex == "male":
        init = "Mr." 
    else:
        init = "Mrs."
  
    print "The passenger named",init, each[1].Name,"who was born in", birth_year,"did not survive"
    
    if count == 50:
        break
            
    count += 1
    
            
#Question 8
#Instead of iris let's work on t_file with the same concept
#a
            
t_file_num = t_file.select_dtypes(include = [np.int64,np.float64])
 
new_t_file = pd.concat( [t_file_num,t_file_num.apply(lambda x: np.nansum(x), axis = 1)],axis = 1)
new_t_file.rename(columns = {0:'sum'},inplace = True)

q8_a_answer = new_t_file

#b

str_age = t_file['Age'].astype(str)
t_file_str = t_file.astype(str)

t_concat = t_file_str.apply(lambda x: x + "_", axis = 1).sum(axis = 1)


q8_b_answer = pd.concat([t_file,pd.DataFrame(t_concat.sum(axis = 1))],axis = 1)
#Skipping 9th Question. Very easy



 

