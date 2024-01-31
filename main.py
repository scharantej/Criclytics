
# Import necessary libraries
from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def homepage():
    # Render the index.html template
    return render_template('index.html')

# Define the route for the analysis page
@app.route('/analysis')
def analysis():
    # Fetch the cricket data from a database or API
    cricket_data = pd.read_csv('cricket_data.csv')

    # Prepare the data for visualization
    batting_data = cricket_data[['Player', 'Runs', 'Average']]
    bowling_data = cricket_data[['Player', 'Wickets', 'Economy']]
    fielding_data = cricket_data[['Player', 'Catches', 'Stumpings']]

    # Create visualizations
    fig, axes = plt.subplots(3, 1, figsize=(10, 15))

    batting_data.plot.bar(x='Player', y='Runs', ax=axes[0])
    axes[0].set_xlabel('Player')
    axes[0].set_ylabel('Runs')
    axes[0].set_title('Top Batsmen')

    bowling_data.plot.bar(x='Player', y='Wickets', ax=axes[1])
    axes[1].set_xlabel('Player')
    axes[1].set_ylabel('Wickets')
    axes[1].set_title('Top Bowlers')

    fielding_data.plot.bar(x='Player', y='Catches', ax=axes[2])
    axes[2].set_xlabel('Player')
    axes[2].set_ylabel('Catches')
    axes[2].set_title('Top Fielders')

    # Save the visualizations
    plt.savefig('visualizations.png')

    # Render the analysis.html template with the visualizations
    return render_template('analysis.html', visualizations='visualizations.png')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
