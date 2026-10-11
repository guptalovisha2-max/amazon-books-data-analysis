
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read data from CSV file
df = pd.read_csv("books.csv")

# Step 2: Display all books
print("===== AMAZON BOOKS ANALYSIS =====")
print("\nAll Books:")
print(df)

# Step 3: Calculate average price
average_price = df["Price"].mean()
print("\nAverage Book Price:", average_price)

# Step 4: Find highest rating
highest_rating = df["Rating"].max()

print("Best Rated Book:", df.loc[df["Rating"].idxmax(), "Name"])
print("Lowest Rated Book:", df.loc[df["Rating"].idxmin(), "Name"])
print("Average Rating:", round(df["Rating"].mean(), 2))

# Step 5: Find most expensive book
expensive_book = df.loc[df["Price"].idxmax(), "Name"]
print("Most Expensive Book:", expensive_book)

# Step 6: Find top-rated book
top_book = df.loc[df["Rating"].idxmax(), "Name"]
print("Top-Rated Book:", top_book)

# Step 7: Display books rated 4.5 or above
print("\nBooks Rated 4.5 or Above:")
print(df[df["Rating"] >= 4.5])

# Step 8: Create a bar chart
plt.figure(figsize=(8, 5))

bars = plt.bar(
    df["Name"],
    df["Price"],
    color="teal",
    edgecolor="black"
)

plt.bar_label(bars, fmt="₹%.0f", padding=4)


plt.title("Book Price Comparison")
plt.xlabel("Book Name")
plt.ylabel("Price (Rs.)")

plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("book_price_chart.png", dpi=300, bbox_inches="tight")
plt.show()

# Ratings comparison chart
plt.figure(figsize=(8, 5))

rating_bars = plt.bar(
    df["Name"],
    df["Rating"],
    color="slateblue",
    edgecolor="black"
)

plt.bar_label(rating_bars, fmt="%.1f", padding=4)
plt.title("Book Ratings Comparison")
plt.xlabel("Book Name")
plt.ylabel("Rating out of 5")
plt.ylim(0, 5)
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("book_ratings_chart.png", dpi=300, bbox_inches="tight")
plt.show()

  