import pandas as pd
import matplotlib.pyplot as plt
import ast

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
plt.bar(genre_counts.index, genre_counts.values, color='purple')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Genres Watched from IMDb Top 250')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
