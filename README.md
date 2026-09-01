# IMDb Top 250 Analysis

Analyzing the IMDb Top 250 Movies dataset with Python, and comparing it with my own Letterboxd ratings and watch history.

## What I did

- Cleaned the dataset (budget, revenue, ratings, genres, etc.)
- Found that several foreign films had their budgets listed in local currency instead of USD (Life Is Beautiful showed a $15 billion budget, which is obviously wrong). Looked up the real numbers and fixed them.
- Looked at how budget relates to worldwide gross
- Compared my Letterboxd ratings to the IMDb average for movies I've rated
- Checked which genres I watch most out of the Top 250

## Data source

The IMDb dataset is from Kaggle: [Top 250 Movies on IMDb in 2026](https://www.kaggle.com/datasets/arjunsinghgangwar/top-250-movies-on-imdb-in-2026) by Arjun Singh Gangwar (MIT License).

## Files

- `budget_analysis.py` - cleans the data, fixes the currency errors, plots budget vs revenue
- `letterboxd_ratings.py` - compares my ratings to IMDb averages
- `letterboxd_watched.py` - genre breakdown + % of the list I've watched
- `imdb_top_250.csv` - the dataset
- `ratings.csv` / `watched.csv` - my Letterboxd exports

## Some things I found

Budget vs revenue isn't a straight line - some cheap movies (Rocky, Gone with the Wind) made way more relative to their budget than expensive ones.

Out of 18 movies I rated that are also in the Top 250, I mostly agree with the average IMDb rating, except for Fight Club and A Clockwork Orange, which I rated way lower than everyone else.

I've watched 38/250 movies on the list (15.2%), and it's mostly Drama by a lot.

## Tools

Python, pandas, matplotlib
