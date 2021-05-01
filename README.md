# fake-news

dspd-project
DATA SCIENCE PRODUCT DEVELOPMENT-PROJECT



Dataset : https://www.kaggle.com/pontes/fake-news-sample

Reference to model: https://drive.google.com/file/d/1QREbyPeYZUxfQ7FSZmTuBnDAqEa9XzD3/view?usp=sharing

PROBLEM STATEMENT: Whether or not the content is fake news

DATABASE SCHEMA- FAKE NEWS APPLICATION

Metadata:

Input Entity:

input_id: unique identifier for each input

search_text: content provided by user

input_type: domain, url, content etc

processed_input: processed input suitable for our model

Output Entity:

id: unique identifier for each output

is_fake_news: whether or not the the content is classified as fake

probability_fake_content: Probability of content being fake

decision_threshold: threshold on the basis of which validity of fake content is decided

content_type: type of the content; reliable, political, hate etc
