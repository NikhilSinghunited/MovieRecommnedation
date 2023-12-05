import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the dataset
df = pd.read_csv("spam.csv")

# Create a binary label 'spam' where spam is 1 and not spam is 0
df['spam'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.Message, df.spam, train_size=0.8)

# Vectorize the text data using CountVectorizer
v = CountVectorizer()
X_train_cv = v.fit_transform(X_train.values)
X_test_cv = v.transform(X_test)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_cv, y_train)

# Function to predict spam or not spam for given emails
def result(emails):
    new = [emails]
    emails_count = v.transform(new)
    x = model.predict(emails_count)
    # if x==0:
    #     return "Not spam"
    # else:
    #     return "Spam"
    return x


# Predict whether the given emails are spam or not spam
# predictions = predict_spam(emails_to_predict)
# print(predictions)
