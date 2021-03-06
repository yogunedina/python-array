'''
Author: Yewande Ogunedina
Question 2 - Midterm
ITMD 513
Title: Indexing and Slicing Arrays
'''

import numpy as np

#create array 
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

#reshape into 3 by 5 array 
a = a.reshape(3,5)
print(a)

#answer to question a. Select row 2 
row_a = a[2, :]
print("Answer to question a is :", row_a)

#answer to question b. select column 4
column_a = a[:, 4]
print("Answer to question b is :", column_a)

#answer to question c. select row 0 and 1 
row_c = a[[0,1 ],:]
print("Answer to question c is: ", row_c)

#answer to question d. select columns 2-4
question_d = a[:, [2,3,4]]
print("Answer to question d is :\n",question_d)

# Answer to question e. select element in row 1 and column 4 
row_2 = a[1, 4]
print("Answer to question e is :", row_2)

#answer to question f. all elements from row 1 and 2 that are columns 0,2,4
question_f = a[1, 0:5:2]
question_g = a[2, 0:15:2]
print("Answer to question f is:", question_f, question_g)
