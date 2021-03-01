import os
import re, string, unicodedata
import nltk
import shutil
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
import math

file='C:\\Users\\hp\\Desktop\\RT'



def createDictionary():
    ad={}
    d17=os.getcwd()
    os.chdir(file)
    fi= os.listdir(os.getcwd())
    fi2=fi

    for jd in fi2:
          with open(jd, 'r') as f:
              words=f.read()
              g2=words.lower()
              f3=g2.split()
              k1=[',']
              k2=['!']
              k3=['?']
              k4=['.']
              k5=k1+k2+k3+k4
              g5=f.name
              gp=ad.keys()
              for i in f3:
                d1=i[-1]
                if d1 in k5:
                  k=i[:-1]
                  i=k
                if i not in gp:
                    t=g5
                    ad[i] = [t]
                else:
                  if jd in ad[i]:
                      continue
                  else:
                      ad[i] = ad[i]+[g5]

    return ad, fi

postlist,doclist =createDictionary()
#print(postlist['telephon'])



"""
returns list of docIDs that results from 'AND' operation between left and right operands
params:
    left_operand:   docID list on the left
    right_operand:  docID list on the right
"""
def AND(left_operand,right_operand):
    # perform 'merge'
    result = []                                 # results list to be returned
    l_index = 0                                 # current index in left_operand
    r_index = 0                                 # current index in right_operand
    l_skip = len(left_operand) # skip pointer distance for l_index
    r_skip = len(right_operand) # skip pointer distance for r_index
    c=0

    left_operand=list(set(left_operand))
    right_operand=list(set(right_operand))
    left_operand=sorted(left_operand)
    right_operand=sorted(right_operand)

    d1={}
    
    for i in left_operand:
        if i not in d1:
            d1[i]=1
        else:
            d1[i]+=1

    for i in right_operand:
        if i not in d1:
            d1[i]=1
        else:
            d1[i]+=1
     
    for i,j in d1.items():
        if j==2:
            result.append(i)
            c+=1
    result=list(set(result))
    
    #print(result) 
    return result,c        












#def AND(S1,S2):
    #ans=[]
    #i=0
    #j=0
    #c=0
    #while (i<len(S1) and j<len(S2)):
        #c+=1
        #if (S1[i]==S2[j]):
            #ans.append(S1[i])
            #i=i+1
            #j=j+1
        #elif (i<j):
            #i=i+1
        #else:
            #j=j+1
    #return ans,c
def OR(left_operand, right_operand):
    result = []     
    l_index = 0 
    r_index = 0  
    c=0
    y1=0
    y2=0  
    jkp=[]

    sorted(left_operand)
    #print(left_operand)
    sorted(right_operand)
    jk1=len(left_operand)
    jk2=len(right_operand)
    
    while (l_index < jk1 or r_index < jk2):
        c+=1
        if (l_index < jk1 and r_index < jk2):
            l1=l_index
            r1=r_index
            l_item = left_operand[l1] 
            r_item = right_operand[r1] 
            
            if (l_item==r_item):
                result.append(l_item)
                jkp=result
                y1=y1+1
                y2=y2+1
                l_index=y1 
                r_index=y2

            
            elif (l_item > r_item):
                result.append(r_item)
                y2+=1
                r_index=y2 

            
            else:
                result.append(l_item)
                y1+=1
                l_index = y1

       
        elif (l_index >= jk1):
            ri=r_index
            r_item = right_operand[ri]
            result.append(r_item)
            y2+=1
            r_index=y2 

       
        else:
            li=l_index
            l_item = left_operand[li]
            result.append(l_item)
            y1+=1
            l_index=y1
    #print("Ankit")
    #result=list(set(result))
    return result,c



#def OR(S1,S2):
    #ans1=[]
    #i=0
    #j=0
    #c=0
    #for i in S2:
        #S1.append()
    #print(S1)
    #ans1=list(set(S1))
    #c+=1
    #return ans1,c
    #while (i<len(S1) and j<len(S2)):
        #c=c+1
        #if (S1[i]==S2[j]):
            #ans.append(S1[i])
            #i=i+1
            #j=j+1
        #elif (i<j):
            #ans.append(S1[i])
            #i=i+1
        #else:
            #ans.append(S2[j])
            #j=j+1
            
    #while i < len(S1): 
        #print(S1[i])
        #c=c+1
        #ans.append(S1[i])
        #i+=1
  
    #while j < len(S2): 
        #ans.append(S2[j])
        #j+=1
        #c=c+1
    #ans=set(ans)
    #ans=list(ans)
    #print(len(ans))
    #return ans,c   


def notAND(S1,S2):
    ans,c=AND(S1,list(set(S2)^set(doclist)))
    #print(set(S2)^set(doclist))
    #print()
    #print(S1)

    return ans,c

def notOR(S1,S2):
    ans,c=OR(S1,list(set(S2)^set(doclist)))
    #print(set(S2))
    #print()
    #print(set(doclist))
    #print()
    #print(list(set(S2)^set(doclist)))
    #print()
    #print(ans)
    return ans,c


#stop_words = set(stopwords.words('english'))  
#query=input('Enter Query:')

def to_lowercase(words):
    lower_word = [] # Initialization to save the lower case character
    for word in words: #Iterate through each word in filr
        new_word = word.lower() #convert to lower case
        lower_word.append(new_word + " ") #append the normalized word to the text
        
    return lower_word



def stem_words(words):
    stemmer = LancasterStemmer()
    stems_words = []
    for word in words:
        stem = stemmer.stem(word)
        stems_words.append(stem)
        stems_words.append(' ')#add space between words
    return stems_words

def strip_list_noempty(res):
    k1=[]
    newlist = (i.strip() if hasattr(i, 'strip') else i for i in res)
    k1=[item for item in newlist if item or not hasattr(item, 'strip')]
    return k1
stop_words = set(stopwords.words('english'))  
query=input('Enter Query:')
query.replace(","," ",2)

#print(query)
#words = nltk.word_tokenize(query)
s=query.lower()
#print(s)
tokenizer=RegexpTokenizer(r'\w+')
tokens=tokenizer.tokenize(s)
filtered_content=[w for w in tokens if not w in stop_words]
processed_content=to_lowercase(filtered_content)
processed_content=[''.join(c for c in s if c not in string.punctuation) for s in processed_content]
processed_content=[x.strip(' ') for x in processed_content] 
processed_content=stem_words(processed_content)

#print(processed_content)

#processed_content = [x.strip(' ') for x in processed_content]
#print(processed_content)

res=[] 
#for ele in processed_content: 
    #if ele.strip():
        #res.append(ele) 
res=processed_content
res=strip_list_noempty(res)


#for i in range(len(res)):
    #print(postlist[res[i]])

sequence=input('Enter Sequence: ')
sequence=sequence[1:-1]

li = list(sequence.split(","))
for i in range(len(li)):
    li[i]=li[i].strip()
#print(li)

def process(S1,S2,exp):
    if (exp=='OR'):
        S,c= OR(S1,S2)
    elif(exp=='AND'):
        S,c= AND(S1,S2)
    elif(exp=='OR NOT'):
        S,c= notOR(S1,S2)
    else :
        S,c= notAND(S1,S2)
    return S,c
#print(postlist)
S=postlist[res[0]]
c=0
for i in range(1,len(res)):
    S1=postlist[res[i]]
    S,c1=process(S,S1,li[i-1])
    c=c+c1
    
print('Number of documents Matched',len(S))
print('Number of comparisons',c)
print('Documents Matched')
#for i in S:
    #print(i)
