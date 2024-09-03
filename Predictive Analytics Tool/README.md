The Predictive Analytics Tool was born from a personal need for a predictive social media analytics tool. In my current role, I analyse social media metrics and port forth ideas on improving engagement rates. This tool is designed to help me in my role by leveraging historical data to predict key marketing metrics that my company looks for, such as CTR’s (click-through rates)future impressions, engagement rates, and engagement volume.

The Predictive Analytics Tool uses past data which I have included in the historical_data.csv file. There is a section under app.py (def train_models(): ) which touches on predictive modelling and machine learning as the Predictive Analytics Tool takes in historical data and uses a linear regression model to predict future outcomes. I am excited to further my knowledge on how AI can be used to improve predictions and accuracy. I researched linear regression models as an extra challenge for myself and as this is more accurate than a simple calculation which doesn’t take historic data into account.
 
The Predicative Analytics Tool can be used to forecast impressions and engagements which will be useful for my monthly analytics reports and will help many people who work in analytics. It allows us marketers to anticipate trends and strategically create startegies for the future.
 
The future engagement rate is the estimated number of interactions by users (likes, comments, shares, clicks etc.) expected in the future based on past performance. Future impressions refer to the number of times a post will be shown to users, in the future. These metrics are key in analytics to evaluate whether the correct demographics are being shown content as well as if the content is interesting and tailored to the targeted users. CTR refers to the number of clicks you post/ad has received divided by the number of impressions.

app.py: Contains the Flask routes and handles user input.

A GET request and POST request is used. The GET request retrieves the server information and the POST request send the server data (from index.html).
It loads the data set, ensuring no row is missing data and returns the data as a pandas DataFrame and removes any rows with missing values.

def train_models(): contains three linear regression models.
Inputs: data - loads historical data; features - columns of the data set; future predictors e.g. target_engagement_rate.
Data preparation: ‘X’ contains features for the model; y_ctr, y_impressions, y_engagement_rate each hold the values that the model will predict
Finally to train the model linear regression models are created and returned to be stored in individual functions.

In Index the new values are taken from the form and converted to floats. The models are used to predict ctr, impression and engagement rate but engagement (volume) is calculated by multiplying the predicted engagement rate with the predicted impressions.

The results are displayed through the ‘results.html’ template.

index.html: The file contains the form for users to input their data (impressions, engagement rate, CTR). The form has three inputs: ctr, engagement rate and impressions that are limited to integers.

results.html: After the data is submitted and calculated, the results file displays the predicted future results. Here Flask’s Jinja is used.

historical_data.csv: This is where the historical (synthetic) data is stored. It is used to train the models. It includes columns for impressions, engagement rate, CTR, future engagement rate, future impressions, and future CTR.
styles.css: Here I have stored the fonts and styles. It changes the link colour and block colour etc.