# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!

# Load the CSV file and store as netflix_df
netflix_df = pd.read_csv('netflix_data.csv')

# Filter the data to remove TV shows and store as netflix_subset
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']

#Investigate the Netflix movie data, keeping only the columns "title", "country", "genre", "release_year", "duration", and saving this into a new DataFrame called netflix_movies
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

# Filter netflix_movies to find the movies that are shorter than 60 minutes, saving the resulting DataFrame as short_movies; inspect the result to find possible contributing factors
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# Using a for loop and if/elif statements to assign colors
colors = []
for genre in netflix_movies['genre']:
    if genre == 'Children':
        colors.append('blue')
    elif genre == 'Documentaries':
        colors.append('green')
    elif genre == 'Stand-Up':
        colors.append('red')
    else:
        colors.append('gray')
        
# Initialize a figure object and create a scatter plot
fig, ax = plt.subplots()
scatter = ax.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)

# Labeling the axes and title
ax.set_xlabel('Release year')
ax.set_ylabel('Duration (min)')
ax.set_title('Movie Duration by Year of Release')

# Display the plot
plt.show()


# Inspecting the plot to answer the question
answer = "maybe"  # Answer can be "yes", "no", or "maybe" based on the plot inspection
