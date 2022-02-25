#!/usr/bin/env python
# coding: utf-8

# In[1]:


def  squared_euclidean_similarity(user_preference, user1, user2):
    sum = 0
    try:
        from math import sqrt
        for book in user_preference[user1]:
            if book in user_preference[user2]:
                print ( "Books they both read in common, Authors and year of publication: ", user_preference[user1][book][0] ,":", "user1 rating:" ,  user_preference[user1][book][1] , "user2 rating: ", user_preference[user2][book][1] )
                sum = sum + pow(user_preference[user1][book][1] - user_preference[user2][book][1],2)
        return  1/(sum)
    except KeyError:
        print ('Enter the correct user_id')
    except ZeroDivisionError:
        print ("Enter two differnt users who have commonly rated a book as division of zero is not mathematically valid")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except:
        print ("some othe exception happened, check if you have entered the correct userid")
    else:
        print ("No exception")
    


# In[27]:


def minkowski_distance_similarity(user_preference, user1,user2, p):
    total = 0
    try:
        for book in user_preference[user1]:
            if book in user_preference[user2]:
                print ( "Books they both read in common, Authors and year of publication: ", user_preference[user1][book][0] ,":", "user1 rating:" ,  user_preference[user1][book][1] , "user2 rating: ", user_preference[user2][book][1] )

                num1 = abs(user_preference[user1][book][1]-user_preference[user2][book][1])
                num2 = pow(num1, p)
                total = total + (num2**1/p)
        return 1/total
          
    except KeyError:
        print ('Enter the correct user_id')
    except ZeroDivisionError:
        print ("Enter two differnt users who have commonly rated a book as division by zero is not mathematically valid")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except:
        print ("some othe exception happened, check if you have entered the correct userid")
    else:
        print ("No exception")
    finally:
            print ("Goodbye")


# In[28]:


def Spearman_Correlation(user_preference, user1,user2):
    output = 0
    n = len(user_preference[user1])
    n2 = (n **2 )
    list1= []
    list2 =[]
    for book in user_preference[user1]:
        if book in user_preference[user2]:
            a = user_preference[user1][book][1]
            list1.append(a)
            b = user_preference[user2][book][1]
            list2.append(b)
            a1 = [[x1, len(list1)-(sorted(list1).index(x1))] for x1 in list1]
            b1 = [[y1, len(list2)-(sorted(list2).index(y1))] for y1 in list2]
            out = list(zip(a1, b1))
            d2 = 0
            for value in out:
                d = (abs(value[0][1]-value[1][1]))
                d2 = d2 + (d * d)
            output = output + (1-((6 * d2)/(n * (n2 - 1))))
            return output
        else:
            print("input have arrrays of different lenght")


# In[29]:


def chebyshev_similarity(user_preference, user1,user2):
    try:
        for book in user_preference[user1]:
            if book in user_preference[user2]:
                print ( "Books they both read in common, Authors and year of publication: ", user_preference[user1][book][0] ,":", "user1 rating:" ,  user_preference[user1][book][1] , "user2 rating: ", user_preference[user2][book][1] )
                num= (abs(user_preference[user1][book][1]-user_preference[user2][book][1]))
                list = [ num ]
                return 1/max(list)
    except KeyError:
        print ('Enter the correct user_id')
    except ZeroDivisionError:
        print ("Enter two differnt users who have commonly rated a book as division by zero is not mathematically valid")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except:
        print ("some othe exception happened, check if you have entered the correct userid")
    else:
        print ("No exception")


# In[30]:


def hamming_distance(user_preference, user1,user2):
    try:
        dist_counter = 0
        for book in range (len(user_preference[user1])):
            if user_preference[user1] != user_preference[user2] :
                dist_counter += 1                 
        return 1/dist_counter
    except KeyError:
        print ('Enter the correct user_id')
    except ZeroDivisionError:
        print ("Enter two differnt users who have commonly rated a book as division by zero is not mathematically valid")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except:
        print ("some othe exception happened, check if you have entered the correct userid")
    else:
        print ("No exception")


# In[31]:


def Cosine_similarity(user_preference, user1,user2):
    try:
        total = 0
        from math import sqrt
        for book in user_preference[user1]:
            if book in user_preference[user2]:
                print ( "Books they both read in common, Authors and year of publication: ", user_preference[user1][book][0] ,":", "user1 rating:" ,  user_preference[user1][book][1] , "user2 rating: ", user_preference[user2][book][1] )
                
                numerator= (user_preference[user1][book][1] * user_preference[user2][book][1]) 
                denominator= sqrt(pow(user_preference[user1][book][1],2)) * sqrt(pow(user_preference[user2][book][1],2)) 
                total= total + numerator/denominator
        return total
          
    except KeyError:
        print ('Enter the correct user_id')
    except ZeroDivisionError:
        print ("Enter two differnt users who have commonly rated at least two book as division by zero is not mathematically valid")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except:
        print ("some othe exception happened, check if you have entered the correct userid")
    else:
        print ("No exception")
    finally:
        print ("Goodbye")


# In[ ]:





# In[32]:


def mean(a):
    list = [a]
    return sum(list)/len(list)
def Pearson_Correlation(user_preference, user1,user2):
    from math import sqrt
    total = 0
    try:
        for book in user_preference[user1]: 
            if book in user_preference[user2]:
                print ( "Books they both read in common, Authors and year of publication: ", user_preference[user1][book][0] ,":", "user1 rating:" ,  user_preference[user1][book][1] , "user2 rating: ", user_preference[user2][book][1] )

                num1 = user_preference[user1][book][1] - mean ( user_preference[user1][book][1] )
                num2 = user_preference[user2][book][1] - mean ( user_preference[user2][book][1] )
                numerator= num1 * num2
                den1 = pow(user_preference[user1][book][1] - mean (user_preference[user1][book][1]),2)
                den2 = pow(user_preference[user1][book][1] - mean (user_preference[user2][book][1]),2)
                denominator = den1 * den2
                total = total + numerator/denominator
                return total
    except KeyError:
        print ('Enter the correct user_id')
    except ZeroDivisionError:
        print ("Enter two differnt users who have commonly rated more than a book as division by zero is not mathematically valid")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except:
        print ("some othe exception happened, check if you have entered the correct userid")
    else:
        print ("No exception")
    finally:
        print ("Goodbye")


# In[ ]:





# In[ ]:




