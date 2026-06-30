"""Main program for content-based recommendation system."""

from data import ITEMS
from utils import get_recommendations


def show_items():
    print("\nAvailable Items:")
    print("-" * 30)
    for item in ITEMS:
        print("-", item)
    print()


def main():
    print("Content-Based Recommendation System")
    print("-" * 40)

    show_items()

    while True:
        user_input = input("Enter an item name (or type 'exit'): ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        recommendations = get_recommendations(user_input, ITEMS)

        if not recommendations:
            print("Item not found or no recommendations available.\n")
            continue

        print("\nBecause you liked:", user_input)
        print("You may also like:")
        print("-" * 30)

        for i, (item, score) in enumerate(recommendations, 1):
            print(f"{i}. {item} (similarity: {score})")

        print()


if __name__ == "__main__":
    main() 