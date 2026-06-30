# Recommendation System

This project is a simple **content-based recommendation system** developed in Python as part of the **CODSOFT AI Internship**. It suggests similar items based on their content using text similarity techniques.

## How It Works

The system takes an item as input from the user and compares it with other items in the dataset. It uses **TF-IDF vectorization** to convert text into numerical form and then calculates **cosine similarity** to find how closely items are related.

Based on the similarity scores, it recommends the most relevant items.

## Features

* Takes an item name as input from the user
* Finds similar items based on content
* Uses TF-IDF and cosine similarity for comparison
* Displays ranked recommendations
* Simple terminal-based interface

## Technologies Used

* Python 3
* Scikit-learn

## Project Structure

```text
RecommendationSystem/
├── recommender.py
├── data.py
├── utils.py
└── README.md
```

## How to Run

1. Install required library:

```bash
pip install scikit-learn
```

2. Run the program:

```bash
python recommender.py
```

3. Enter an item name when prompted (for example: *Inception*) to get recommendations.

## Example Output

```text
If you liked 'Inception', you may also enjoy:
--------------------------------------------
1. Interstellar (similarity: 0.82)
2. The Matrix (similarity: 0.78)
3. Shutter Island (similarity: 0.71)
```

## Future Improvements

* Add more items to improve recommendation quality
* Use larger real-world datasets
* Improve UI using a web interface (Flask or Streamlit)
* Add user history-based recommendations

## Author

Developed as part of the **CODSOFT AI Internship**
