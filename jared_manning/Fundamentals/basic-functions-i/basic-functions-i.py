
# coding: utf-8

# In[15]:


def a():
    return 5


print(a())

# => 5


# In[16]:


def b():
    return 5


print(b()+b())

# => 10


# In[17]:


def c():
    return 5
    return 10


print(c())

# => 5


# In[18]:


def d():
    return 5
    print(10)


print(d())

# => 5


# In[19]:


def e():
    print(5)


z = e()
print(z)

# => 5
# => None


# In[21]:


def f(b, c):
    print(b+c)


print(f(1, 2) + f(2, 3))

# => None ✗


# In[22]:


def g(b, c):
    return str(b)+str(c)


print(g(2, 5))

# => "25" ✗


# In[23]:


def h():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7


print(h)

# => <something about functions or maybe a reference number or memory address or something>


# In[24]:


def i(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3


print(i(2, 3))
print(i(5, 3))
print(i(2, 3) + i(5, 3))

# => 7
# => 14
# => 21


# In[25]:


def j(b, c):
    return b+c
    return 10


print(j(3, 5))

# => 8


# In[26]:


y = 500
print(y)


def k():
    y = 300
    print(y)


print(y)
k()
print(y)

# => 500
# => 500
# => 300
# => 300 ✗


# In[27]:


x = 500
print(x)


def l():
    x = 300
    print(x)
    return x


print(x)
l()
print(x)

# => 500
# => 500
# => 300
# => 300 ✗ ... dang, really thought the return might mutate x. Probably doesn't do that because x is not reassigned
#              outside of the scope of l(). Oh hey, maybe the next one will do just that!


# In[28]:


w = 500
print(w)


def m():
    w = 300
    print(w)
    return w


print(w)
w = m()
print(w)

# => 500
# => 500
# => 300
# => 300 ✓ nailed it.


# In[29]:


def n():
    print(1)
    o()
    print(2)


def o():
    print(3)


n()

# => 1
# => 3
# => 2


# In[30]:


def p():
    print(1)
    x = q()
    print(x)
    return 10


def q():
    print(3)
    return 5


x = p()
print(x)

# => 1
# => 3
# => 5
# => 10

