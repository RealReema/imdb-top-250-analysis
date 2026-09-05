import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.facecolor'] = '#050505'
plt.rcParams['axes.facecolor'] = '#050505'
plt.rcParams['savefig.facecolor'] = '#050505'
plt.rcParams['text.color'] = '#d4d2d8'
plt.rcParams['axes.labelcolor'] = '#d4d2d8'
plt.rcParams['xtick.color'] = '#777777'
plt.rcParams['ytick.color'] = '#777777'
plt.rcParams['axes.edgecolor'] = '#333333'
lb = pd.read_csv('ratings.csv')
imdb = pd.read_csv('imdb_top_250.csv')

merged = pd.merge(lb, imdb, left_on='Name', right_on='primaryTitle', how='inner')

print("Number of common movies:", len(merged))

merged['my_rating_scaled'] = merged['Rating'] * 2
merged['difference'] = merged['my_rating_scaled'] - merged['averageRating']

biggest_gaps = merged[['Name', 'my_rating_scaled', 'averageRating', 'difference']].sort_values('difference')
print(biggest_gaps)

plt.figure(figsize=(10, 6))
plt.scatter(merged['averageRating'], merged['my_rating_scaled'], color='#5608CC', alpha=0.7)
plt.plot([0, 10], [0, 10], color='#777777', linestyle='--')
plt.xlabel('IMDb Average Rating')
plt.ylabel('My Rating (scaled to 10)')
plt.title('My Ratings vs IMDb Average - Common Movies')
plt.savefig('my_ratings_vs_imdb.png', dpi=150, bbox_inches='tight')
plt.show()
