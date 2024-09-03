from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
import os

app = Flask(__name__)

# Load and prepare the dataset
def load_data():
    data_path = os.path.join('data', 'historical_data.csv')
    data = pd.read_csv(data_path)
    data = data.dropna()  # Remove rows with NaN values
    return data

def train_models():
    data = load_data()

    # Define features and target variables
    features = ['impressions', 'engagement_rate', 'CTR']
    target_engagement_rate = 'future_engagement_rate'
    target_impressions = 'future_impressions'
    target_ctr = 'future_ctr'

    # Prepare data for training models
    X = data[features]
    y_engagement_rate = data[target_engagement_rate]
    y_impressions = data[target_impressions]
    y_ctr = data[target_ctr]  # Corrected this line to use 'y_ctr' instead of overwriting 'y_impressions'

    # Train model for future engagement rate
    model_engagement_rate = LinearRegression()
    model_engagement_rate.fit(X, y_engagement_rate)

    # Train model for future impressions
    model_impressions = LinearRegression()
    model_impressions.fit(X, y_impressions)

    # Train model for future CTR
    model_ctr = LinearRegression()
    model_ctr.fit(X, y_ctr)

    return model_engagement_rate, model_impressions, model_ctr

model_engagement_rate, model_impressions, model_ctr = train_models()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        impressions = float(request.form['impressions'])
        engagement_rate = float(request.form['engagement_rate'])
        ctr = float(request.form['CTR'])

        # Create a DataFrame for the new data
        new_data = pd.DataFrame({'impressions': [impressions], 'engagement_rate': [engagement_rate], 'CTR': [ctr]})

        # Predict future engagement rate and future impressions
        predicted_future_engagement_rate = model_engagement_rate.predict(new_data)[0]
        predicted_future_impressions = model_impressions.predict(new_data)[0]
        predicted_future_ctr = model_ctr.predict(new_data)[0]

        # Calculate future engagement based on predicted values
        future_engagement = predicted_future_engagement_rate * predicted_future_impressions

        return render_template('results.html', impressions=impressions, engagement_rate=engagement_rate, CTR=ctr,
                               future_engagement_rate=predicted_future_engagement_rate, future_impressions=predicted_future_impressions, future_engagement=future_engagement, future_ctr=predicted_future_ctr)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)