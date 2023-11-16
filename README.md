# Indian Foods Recommendation System App

Live Demo: https://akk-indian-foods-recommendation-system-app.streamlit.app/


---------------------------------------

## About this Project:

Titled "Content Based Indian Foods Recommendation System App" is developed by using the dataset, download from kaggle, dataset is available in this repository. There are 4018 foods in this dataset. Suppose you select 1 food and it was delicious and you like it, so now you want more foods related to the food that eat and liked. This project will do similar work and recommend you closely related foods that you like.

## Why I built this project:

Today, all popular companies such as: 

<ul>
  <li>Netflix</li>
  <li>Amazon</li>
  <li>Daraz</li>
  <li>Facebook</li>
  <li>Youtube</li>
  <li>Google etc.</li>
</ul>
  
These all companies use recommended systems in their websites which can be anyone from these types of recommendation system i.e, content-based, collaborative or hybrid (both content-based and collaborative). Where you get similar things that you like most. So, it important for every Machine Learning Engineer to know about it.

---------------------------------------

## Steps:

<ol type="1">
  <li>Download Dataset from Kaggle</li>
  <li>Applying Preprocessing on Dataset: Fill null values, remove duplicates, remove unnecessary features and clean dataet.</li>
  <li>Create "tags" feature which contain all tags such as description of food, type of food and recipe of food etc.</li>
  <li>After creating tags, I apply stemming on "tags" column because there are many words such as lovely, loving, lover etc has same meaning as 'love'. It is necessary because next step is based on counting most frequent words of dataset. So, in that situation it is better to apply stemming to count them in one words category.</li>
  <li>Using scikit-learn "count vectorizer" I create vectors that contain most frequent words from the whole dataset.</li>
  <li>Then using scikit-learn "cosine similarity", I calculate similarity of each food with all foods available in dataset. Cosine Similarity range in between [0,1].</li>
  <li>At the end, I import this cosing similarity variable into binary format, and use it in streamlit app.</li>
</ol>

---------------------------------------

## Learning Outcomes:

<ul>
  <li>How to create vectors...</li>
  <li>How to calculate cosine similarity</li>
  <li>Model Deployment in Streamlit App</li>
</ul>

---------------------------------------

## How you can run it on your machine:

First, download all the files and folders from this repository. Then, create virtual environment.

Using Code:
```py -3 -m venv virtualEnv```

Then, installed all the libraries mentioned in 'requirements.txt' text file. 

Using Code:
```pip freeze > requirements.txt```

Finally, run this code in terminal to start streamlit app.

Using Code:
```streamlit run streamlit_app.py```

