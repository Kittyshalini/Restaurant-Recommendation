# Restaurant-Recommendation
A simple Flask web app that recommends similar restaurants based on user input using cosine similarity and a pre-trained similarity matrix. Built with Python, Flask, and HTML/CSS.

## 🚀 Features

- Clean, responsive frontend using HTML and CSS
- Dropdown menu to select a restaurant
- Displays top 5 similar restaurants
- Lightweight and easy to run locally
- Environment variable support for configuration

## 🛠️ Tech Stack

- Python
- Flask
- Pandas
- Jinja2
- HTML/CSS
- Pickle (for loading saved data/similarity matrix)
- 

## 🧪 How It Works

1. The user selects a restaurant from a dropdown menu.
2. The app looks up similar restaurants from a precomputed cosine similarity matrix (`similarity.pkl`).
3. Top 5 similar restaurants are displayed.

## To use it

1. Download the zomato.csv dataset from - https://www.kaggle.com/datasets/absin7/zomato-bangalore-dataset?select=zomato.csv
2. Place the dataset in the content folder
3. Run the restaurantrecommendation.py file - (Takes some time to run) - python restaurantrecommendation.py
4. We get data.pkl and similarity.pkl as outputs
5. Then run the app.py - python app.py
6. Open http://127.0.0.1:5000 on your browser, you should be able to see the webpage
   
