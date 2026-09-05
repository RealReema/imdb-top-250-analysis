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
df = pd.read_csv('imdb_top_250.csv')

df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['grossWorldwide'] = pd.to_numeric(df['grossWorldwide'], errors='coerce')
df['averageRating'] = pd.to_numeric(df['averageRating'], errors='coerce')
df['numVotes'] = pd.to_numeric(df['numVotes'], errors='coerce')
df['runtimeMinutes'] = pd.to_numeric(df['runtimeMinutes'], errors='coerce')

print("Missing budget:", df['budget'].isna().sum())
print("Missing grossWorldwide:", df['grossWorldwide'].isna().sum())

clean_df = df.dropna(subset=['budget', 'grossWorldwide'])

currency_fixes = {
    'Life Is Beautiful': 20_000_000,
    'The Handmaiden': 8_800_000,
    'Princess Mononoke': 21_000_000,
    'Spirited Away': 19_200_000,
    'Dangal': 11_000_000,
    '3 Idiots': 12_000_000,
    'Your Name.': 7_500_000,
}

for title, correct_budget in currency_fixes.items():
    clean_df.loc[clean_df['primaryTitle'] == title, 'budget'] = correct_budget

plt.figure(figsize=(10, 6))
plt.scatter(clean_df['budget'], clean_df['grossWorldwide'], alpha=0.6, color='#5608CC')
plt.xlabel('Budget ($)')
plt.ylabel('Worldwide Gross ($)')
plt.title('Budget vs Worldwide Gross - Top 250 IMDb Movies')
plt.savefig('budget_vs_revenue.png', dpi=150, bbox_inches='tight')
plt.show()

clean_df['roi_ratio'] = clean_df['grossWorldwide'] / clean_df['budget']
top_roi = clean_df[['primaryTitle', 'budget', 'grossWorldwide', 'roi_ratio']].sort_values('roi_ratio', ascending=False).head(10)
print(top_roi)
