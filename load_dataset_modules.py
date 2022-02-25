#!/usr/bin/env python
# coding: utf-8

# In[10]:


def unquote(string):
    """
    To avoid having entries like '"Book-Title"'
    """
    return string.strip().lstrip('"').rstrip('",""')
b= open("Books.csv", encoding="utf-8", errors="ignore")
next (b)
lines = b.readlines()
headers = list(map(unquote, lines[0].split(";")))
book = {}
for line in lines[1:]:
    line = line.split(";")
    book_id = unquote(line[0])
    title = unquote(line[1])
    author = unquote(line[2])
    year = unquote(line[3])
    
    book.setdefault(book_id, {})
    book[book_id][title]=  author, year


# In[11]:


def user_preference():
    f = open("Book-Ratings.csv", encoding="utf-8", errors="ignore")
    next(f)
    lines = f.readlines()
    #headers = list(map(unquote, lines[0].split(";")))
    user_preference= {}
    for line in lines[1:] :
        line = line.split(";")
        user_id = unquote(line[0])
        book_id = unquote(line[1])
        rscore = unquote(line[-1])
       
        if (book_id not in book.keys()):
            continue
        user_preference.setdefault(user_id, {})    
        user_preference[user_id][book_id] = book[book_id], float(rscore)
    return user_preference


# In[14]:


user_preference = user_preference()


# In[15]:


user_preference


# In[ ]:




