import pandas as pd

data = {
    'review_id': [1, 2, 3, 4],
    'customer_name': ['John Doe', 'MARY SMITH', 'alice brown', 'Bob Jones'],
    'review_text': [
        'Great product!!!', 
     'Not bad, but could be better...', 
        'AWESOME ITEM', 
        'poor quality :('
    ],
    'product_category': ['Electronics', 'Clothing', 'Electronics', 'Home']
}
df = pd.DataFrame(data)
print(df)
# change lower() and upper
print(df["customer_name"].str.lower())

'''
Real-World Application: In a customer database, 
names may be entered in mixed cases (e.g., "JOHN", "john", "John"). 
Converting to lowercase ensures consistency for matching or grouping.

'''

# . str.strip()  Clean up messy text data, such as reviews with extra spaces.
df["review_text"]=df["review_text"].str.strip()

print(df["review_text"])


''''
Real-World Application: In user-submitted data (e.g., survey responses), extra spaces are common.
Stripping them ensures clean text for analysis or natural language processing (NLP).
'''

#str.replace()  Fixes unwanted characters or standardizes words (e.g., change "poor" to "bad").

import pandas as pd

data = {
    'customer_name': ['John Doe', 'MARY SMITH', 'alice brown', 'Bob Jones'],
    'review': ['Great product!!!', 'Not bad, but ok...', 'AWESOME BUY', 'poor quality :(']
}
df = pd.DataFrame(data)
print(df)

# Replace "!!!" with "!" in reviews
df['review'] = df['review'].str.replace('!!!', '!', regex=False)
print(df['review'])


# str.contains() Helps find rows with specific keywords, like positive or negative feedback. 

# Find reviews with the word "great"
has_great = df['review'].str.contains('great', case=False, na=False)
print(df[has_great])

'''
Real-Life Use: In customer reviews, you might search for words like "awesome" or
"terrible" to identify happy or unhappy customers for further action
'''

# str.split() Breaks text into pieces based on a separator (like a space or comma).

# Split customer names into first and last names
df[['first_name', 'last_name']] = df['customer_name'].str.split(' ', expand=True)
print(df[['customer_name', 'first_name', 'last_name']])

'''
Real-Life Use: In an employee database, 
splitting names into first and last names helps with sorting or sending personalized emails.
'''

# str.len() Counts how many characters are in each text.

# Count characters in each review
df['review_length'] = df['review'].str.len()
print(df[['review', 'review_length']])

'''
Real-Life Use: In social media analysis,
longer comments might indicate more detailed feedback, which you can prioritize.
'''

# str.startswith(), str.endswith()  Checks if text starts or ends with a specific word or character

# Find reviews ending with "!"
excited_reviews = df[df['review'].str.endswith('!')]
print(excited_reviews)

# import titanic
df = pd.read_csv('titanic.csv')
df['Name']


# replace
df['title'] = df['title'].str.replace('Ms.','Miss.')
df['title'] = df['title'].str.replace('Mlle.','Miss.')



# filtering
# startswith/endswith
df[df['firstname'].str.endswith('A')]
# isdigit/isalpha...
df[df['firstname'].str.isdigit()]


# applying regex
# contains
# search john -> both case
df[df['firstname'].str.contains('john',case=False)]
# find lastnames with start and end char vowel
df[df['lastname'].str.contains('^[^aeiouAEIOU].+[^aeiouAEIOU]$')]


# Common Functions
# lower/upper/capitalize/title
df['Name'].str.upper()
df['Name'].str.capitalize()
df['Name'].str.title()
# len
df['Name'][df['Name'].str.len() == 82].values[0]
# strip
"                   nitish                              ".strip()
df['Name'].str.strip()