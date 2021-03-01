import os
import re, string, unicodedata
import nltk
import shutil
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer


#file='/home/vikas/Downloads/stories'

#Preprocessed File 
def preprocess_file(file):
    
    f=open(file,'r',errors='ignore')
    f_content = f.read()#f_content is the content of the file
    print(f.name)
    stop_words=set(stopwords.words('english')) # total Stopwords   
    s=f_content.lower()
    f24=s
    tokenizer=RegexpTokenizer(r'\w+')
    tokens=tokenizer.tokenize(f24) #Tokenization
    tokens1=tokens
    #words = nltk.word_tokenize(f_content)
    #filtered_content = [w for w in words if not w in stop_words]
    filtered_words=[w for w in tokens1 if not w in stop_words] #Stopwordsremoval
    processed_content=to_lowercase(filtered_words)
    processed_content=[''.join(c for c in s if c not in string.punctuation) for s in processed_content] #Removing Punctuation 
    processed_content = [x.strip(' ') for x in processed_content] 
    processed_content=stem_words(processed_content)
    #s1=" "
    #gh=processed_content + s1

    f.close()
    with open(file, 'w') as out:
            out.writelines(processed_content)
    shutil.move(file,'C:\\Users\\hp\\Desktop\\RT')
    out.close()

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






os.chdir(r"C:/")
your_path = r'C:\Users\hp\Desktop\stories'
files = os.listdir(r"/Users/hp/Desktop/stories/")
#i=0
#j =0
# This code will iterate over all the files in the folder stories
for file in files:
    #This condition check if the folder is a subdirectory it will again list the subdierctory and read individual file
    complete_file= os.path.join(your_path,file) #find the complete file name by joining directory name with the file name
    #This will check for subdirectory and then try to list all files inside the subdirectory
    if os.path.isdir(complete_file):
        x = os.listdir(complete_file)
        sub_files = os.listdir(complete_file)
        for s_file in sub_files:
            preprocess_file(os.path.join(complete_file,s_file))
           
    else:
        preprocess_file(complete_file)

