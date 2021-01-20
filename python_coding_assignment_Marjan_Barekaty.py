#!/usr/bin/env python
# coding: utf-8

# ## Python  Coding  Assignment 

# In[3]:


iteration = 10000


# In[4]:


while iteration > 1:
    number = list(map(int, input("Enter the integer number: ").split()))
    
    
    if len(number)  == 2:
        a = str(number[0]); b = str(number[1])
        value_a = []; value_b = []
        for i in a:
            value_a.append(i)
        for j in b:
            value_b.append(j)
            
            ##Reversed separated numbers based on the length of the number
            
        A= [value_a[len(value_a)-K-1] for K in range(len(value_a))]
        B= [value_b[len(value_b)-K-1] for K in range(len(value_b))]
       
         ## Reversed joined numbers
        v_a = int(''.join(A))
        v_b = int(''.join(B))
        
        ### calculating the sum of reversed numbers

        print("The number: ", v_a + v_b)
        value_a = []; value_b = []
    elif len(number) == 1:
        print('The number: ', number[0])
    else:
        print('No Input Provided: ', 0)
        break
    iteration -= 1


# In[ ]:




