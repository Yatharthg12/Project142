import pandas as pd 
import numpy as np 

df = pd.read_csv('final.csv')
C = df['vote_average'].mean()
m = df['vote_count'].quantile(0.9)
q_movies = df.copy().loc[df['vote_count']>=m]

def weighted_rating(x, m = m, C = C):
    v = x['vote_count']
    R = x['vote_average']

    return (v/(v+m)*R)+(m/(m+v)*C)

q_movies['score'] = q_movies.apply(weighted_rating, axis = 1)
q_movies = q_movies.sort_value('score', ascending = False)
output = q_mmovies[['title', 'vote_count', 'vote_average', 'poster_link']].head(20).values.tolist()