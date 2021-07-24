
# coding: utf-8

# In[108]:


# find random neighbor value
import random
def neighbor():
    u = random.uniform(-1, 1)
    return u


# In[109]:


# find random neighbor_y value
import random
def neighbor_y():
    y = random.randint(-1,1)
    return y


# In[110]:


# compute the probability
import math

def probability(z0, z1, T):
    if z1 > z0:
        return 1
    
    p = math.exp((z1 - z0)/T)
    return p


# In[111]:


# task 2a function
import random
import math

def function_a(u):
    z = u*math.sin(1/(0.01 + u**2)) + u**3*math.sin(1/(0.001 + u**4))
    return z


# In[112]:


# task 2b function
import random
import math

def function_b(u,v):
    z = u*v**2*math.sin(v/(0.01 + u**2)) + u**3*v**2*math.sin(v**3/(0.001 + u**4))
    return z


# In[113]:


# task 2c function
import random
import math

def function_c(u,v,w):
    z = (u*v**2 + math.sin(math.pi*w))*math.sin(v/(0.01 + u**2))*math.sin(math.pi*w/2) + u**3*v**2*w*math.sin(v**3/(0.001*(math.sin(math.pi*w/2))**2 + u**4 + (w-1)**2))
    return z


# In[114]:


# task 2d function
import random
import math

def function_d(u,v,w,y):
    z = ((u*v**2 + math.sin(math.pi*w))*math.sin(v/(0.01 + u**2))*math.sin(math.pi*w/2) + u**3*v**2*w*math.sin(v**3/(0.001*(math.sin(math.pi*w/2))**2 + u**4 + (w-1)**2)))*y
    return z


# In[115]:


#z0: current cost, u0: current solution
#z1: new cost, u1: new solution
def anneal_a(u):
    u0 = u
    ug = 0.0
    z0 = function_a(u0)
    T = 1000
    T_min = 1
    alpha = 0.99
    while T > T_min:
        u1 = neighbor()
        z1 = function_a(u1)
        p = probability(z0, z1, T)
        if p > random.uniform(0, 1):
            u0 = u1
            z0 = z1
        if function_a(u0) > function_a(ug):
            ug = u0
            z0 = z1
                
        #T is temperature
        T = T*alpha
        
        print(T, ug, z0)
        
    return ug, function_a(ug)


# In[116]:


#z0: current cost, u0: current solution
#z1: new cost, u1: new solution
def anneal_b(u,v):
    u0 = u
    v0 = v
    ug = 0.0
    vg = 0.0
    z0 = function_b(u0,v0)
    T = 1000
    T_min = 1
    alpha = 0.99
    while T > T_min:
        u1 = neighbor()
        v1 = neighbor()
        z1 = function_b(u1,v1)
        p = probability(z0, z1, T)
        if p > random.uniform(0, 1):
            u0 = u1
            v0 = v1
            z0 = z1
        if function_b(u0,v0) > function_b(ug,vg):
            ug = u0
            vg = v0
            z0 = z1
                
        #T is temperature
        T = T*alpha
        
        print(T, ug, vg, z0)
        
    return ug, vg, function_b(ug,vg)


# In[117]:


#z0: current cost, u0: current solution
#z1: new cost, u1: new solution
def anneal_c(u,v,w):
    u0 = u
    v0 = v
    w0 = w
    ug = 0.0
    vg = 0.0
    wg = 0.0
    z0 = function_c(u0,v0,w0)
    T = 1000
    T_min = 1
    alpha = 0.99
    while T > T_min:
        u1 = neighbor()
        v1 = neighbor()
        w1 = neighbor()
        z1 = function_c(u1,v1,w1)
        p = probability(z0, z1, T)
        if p > random.uniform(0, 1):
            u0 = u1
            v0 = v1
            w0 = w1
            z0 = z1
        if function_c(u0,v0,w0) > function_c(ug,vg,wg):
            ug = u0
            vg = v0
            wg = w0
            z0 = z1
                
        #T is temperature
        T = T*alpha
        
        print(T, ug, vg, wg, z0)
        
    return ug, vg, wg, function_c(ug,vg,wg)


# In[118]:


#z0: current cost, u0: current solution
#z1: new cost, u1: new solution
def anneal_d(u,v,w,y):
    u0 = u
    v0 = v
    w0 = w
    y0 = y
    ug = 0.0
    vg = 0.0
    wg = 0.0
    yg = 0
    z0 = function_d(u0,v0,w0,y0)
    T = 1000
    T_min = 1
    alpha = 0.99
    while T > T_min:
        u1 = neighbor()
        v1 = neighbor()
        w1 = neighbor()
        y1 = neighbor_y()
        z1 = function_d(u1,v1,w1,y1)
        p = probability(z0, z1, T)
        if p > random.uniform(0, 1):
            u0 = u1
            v0 = v1
            w0 = w1
            y0 = y1
            z0 = z1
        if function_d(u0,v0,w0,y0) > function_d(ug,vg,wg,yg):
            ug = u0
            vg = v0
            wg = w0
            yg = y0
            z0 = z1
                
        #T is temperature
        T = T*alpha
        
        print(T, ug, vg, wg, yg, z0)
        
    return ug, vg, wg, yg, function_d(ug,vg,wg,yg)


# In[119]:


anneal_a(1)


# In[120]:


anneal_b(1,1)


# In[121]:


anneal_c(1,1,1)


# In[122]:


anneal_d(1,1,1,1)

