"""Utility functions for content-based recommendation system."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_similarity_matrix(items):
    """Create TF-IDF matrix and compute cosine similarity."""
    titles = list(items.keys())
    descriptions = list(items.values())

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    similarity_matrix = cosine_similarity(tfidf_matrix)
    return titles, similarity_matrix


def get_recommendations(item_name, items, top_n=5):
    """Return top similar items based on content."""
    titles, similarity_matrix = build_similarity_matrix(items)

    if item_name not in items:
        return []

    index = titles.index(item_name)
    similarity_scores = list(enumerate(similarity_matrix[index]))

    # sort by similarity score (descending), skip itself
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i, score in similarity_scores:
        if titles[i] == item_name:
            continue
        recommendations.append((titles[i], round(score, 2)))
        if len(recommendations) == top_n:
            break

    return recommendations