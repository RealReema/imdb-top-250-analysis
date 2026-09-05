import pandas as pd
import matplotlib.pyplot as plt
import ast

plt.rcParams['figure.facecolor'] = '#050505'
plt.rcParams['axes.facecolor'] = '#050505'
plt.rcParams['savefig.facecolor'] = '#050505'
plt.rcParams['text.color'] = '#d4d2d8'
plt.rcParams['axes.labelcolor'] = '#d4d2d8'
plt.rcParams['xtick.color'] = '#777777'
plt.rcParams['ytick.color'] = '#777777'
plt.rcParams['axes.edgecolor'] = '#333333'
watched = pd.read_csv('watched.csv')
imdb = pd.read_csv('imdb_top_250.csv')

merged_watched = pd.merge(watched, imdb, left_on='Name', right_on='primaryTitle', how='inner')

print("Number of common movies:", len(merged_watched))

percentage = (len(merged_watched) / 250) * 100
print(f"Watched {percentage:.1f}% of IMDb Top 250")

merged_watched['genres'] = merged_watched['genres'].apply(ast.literal_eval)
all_genres = merged_watched['genres'].explode()
genre_counts = all_genres.value_counts()
print(genre_counts)

plt.figure(figsize=(10, 6))
plt.bar(genre_counts.index, genre_counts.values, color='#5608CC')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Genres Watched from IMDb Top 250')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('genres_watched.png', dpi=150, bbox_inches='tight')
plt.show()
