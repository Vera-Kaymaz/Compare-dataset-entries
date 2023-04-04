#!/usr/bin/env python
# coding: utf-8

# In[1]:


id_1 = "#3"
grade_1 = "B"
test_score_1 = 89

id_2 = "#6"
grade_2 = "B"
test_score_2 = 77

no_duplicates = id_1 != id_2
print("No duplicate entries: ")
print(no_duplicates)

same_grade = grade_1 == grade_2 
print("Same grade : ")
print(same_grade)

higher_score = test_score_1 > test_score_2
print("id_1 has a higher score: ")
print(higher_score)

