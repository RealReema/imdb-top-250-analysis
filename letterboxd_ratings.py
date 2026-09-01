import pandas as pd
import matplotlib.pyplot as plt

lb = pd.read_csv('ratings.csv')
imdb = pd.read_csv('imdb_top_250.csv')

merged = pd.merge(lb, imdb, left_on='Name', right_on='primaryTitle', how='inner')

print("Number of common movies:", len(merged))

merged['my_rating_scaled'] = merged['Rating'] * 2
merged['difference'] = merged['my_rating_scaled'] - merged['averageRating']

biggest_gaps = merged[['Name', 'my_rating_scaled', 'averageRating', 'difference']].sort_values('difference')
print(biggest_gaps)

plt.figure(figsize=(10, 6))
plt.scatter(merged['averageRating'], merged['my_rating_scaled'], color='purple', alpha=0.7)
plt.plot([0, 10], [0, 10], color='gray', linestyle='--')
plt.xlabel('IMDb Average Rating')
plt.ylabel('My Rating (scaled to 10)')
plt.title('My Ratings vs IMDb Average - Common Movies')
plt.show()
