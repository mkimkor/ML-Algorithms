
# coding: utf-8

# In[26]:


#Heuristic used: the number of misplaced tiles
#A* minimizes estimated total path cost: f(n) = g(n) + h(n)
def A_star_function():
    
    x = input("initial_state: ")
    num = x.split()
    
    goal = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    
    g = 0
    h = 0
    for i in range(len(goal)):
        if (num[i] != goal[i]):
            h += 1
            f = g + h

    print('g(n):' + str(g), ' h(n):' + str(h), 'f(n):'+ str(f))


# In[27]:


A_star_function()

