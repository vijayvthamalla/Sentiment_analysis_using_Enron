import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

data = pd.read_csv(r"D:\Github\NLP\Spam_classification\emails.csv")

def clean_email_text(email_text):
    
    pattern = r"Message-ID.*Content-Transfer-Encoding: 7bit"
    email_text = re.sub(pattern, "", email_text, flags=re.DOTALL)
    lines = email_text.split("\n")
    res = []

    for line in lines:
        if "X-" not in line:
            line.replace("\t"," ")
            res.append(line)
    
    return " ".join(res)

data["processed_message"] = data['message'].apply(clean_email_text)

def replace_empty_string_with_Null(text):
    if text == "":
        return None
    return text

data.processed_message = data.processed_message.apply(replace_empty_string_with_Null)

null_values = data.processed_message.isnull()

data.dropna(subset=['processed_message'], inplace = True)

def remove_punctuations_and_special_characters(text):
    
# regular expressions:
#     pattern = r"[^\w\s]"
#     return re.sub(pattern, '', text)
# or we can simply use string.punctuation as 
#        ''.join(char for char in text if char not in string.punctuation)

    return re.sub(r'[^\w\s]','',text)

data.processed_message = data.processed_message.apply(lambda x: remove_punctuations_and_special_characters(x))

stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()

def preprocessing_text(text):
    
    tokens = word_tokenize(text)
    
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    
    return ' '.join(lemmatized_tokens)

data.processed_message = data.processed_message.apply(preprocessing_text)

data.to_csv("preprocessed_data.csv")