import streamlit as st
import pandas as pd
import folium
import numpy as np
from streamlit_folium import folium_static
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Retrieve the username from the query string
username = st.experimental_get_query_params().get('username', [''])[0]


###############UI
# Add a title to your app
st.title('Restaurant recommendation app')

# Display a personalized welcome message
if username:
    st.write(f"Welcome to the app, {username}!")
else:
    st.write('Please log in to access the app.')

# Add text to your app
st.write('We are here to help You have a great time')

# Add an input widget
location = st.text_input('Enter your location: ')

# Add an input widget
cuisine = st.text_input('Enter your favorite cuisine: ')
st.write('Let\'s help you to choose: Eastern European, Mediterranean, European, Healthy, Central European, Grill,\
            ,Croatian, Central European, Vegetarian Friendly, Vegan Options, Gluten Free Options, \
           Brew Pub, Healthy, Gastropub,Dinner, Breakfast, Lunch, Brunch, Drinks.')


image_file = "pictures/restoran.jpg"  # Replace with the path to your image file
st.image(image_file, caption="Restaurant")

try:
    ####
    data = pd.read_csv('updated_restaurants1.csv')

    #########Location recommendation :
    location = location.replace(',', '')
    location = location.split(' ')
    data2 = data[data['Location'].str.contains(location[0], case=False)]
    l = data2.shape[0]
    i = 1
    while l > 20 and len(location) > i:
        data22 = data2[data2['Location'].str.contains(location[i], case=False)]
        l2 = data22.shape[0]
        if l2 > 20:
            data2 = data22
        else:
            break

        i += 1

    if data2.empty:
        st.write('No restaurants found for the specified location.')
    else:
        # Function to create a map with restaurant locations
        def create_map(data):
            # Create a map centered on the first restaurant's coordinates
            map_center = [data['Latitude'].iloc[0], data['Longitude'].iloc[0]]
            m = folium.Map(location=map_center, zoom_start=12)

            # Add markers for each restaurant
            for _, row in data.iterrows():
                restaurant_name = row['Restaurant Name']
                latitude = row['Latitude']
                longitude = row['Longitude']
                popup_text = f'Restaurant: {restaurant_name}<br>Latitude: {latitude}<br>Longitude: {longitude}'
                folium.Marker([latitude, longitude], popup=popup_text).add_to(m)

            return m

        ############ Syst cuisin
        # Add an input widget

        restaurant = data2['Restaurant Name']
        data2['Cuisine'] = data2['Cuisine'].str.replace(',', '')
        tfv = TfidfVectorizer(min_df=10, max_features=None,
                              strip_accents='unicode', analyzer='word', token_pattern=r'\w{1,}',
                              ngram_range=(1, 3),
                              stop_words='english')

        # Fitting the TF-IDF on the 'overview' text
        tfv = TfidfVectorizer(min_df=1, max_df=0.9)
        tfv_matrix = tfv.fit_transform(data2['Cuisine'])

        # Convert TF-IDF matrix to DataFrame
        tfidf_df = pd.DataFrame(tfv_matrix.toarray(), columns=tfv.get_feature_names_out())
        ######### Cuisine

        cuisine = cuisine.replace(',', ' ')
        # Initialize the "TfidfVectorizer" object.
        vectorizer_features = tfv.transform([cuisine])
        new_text_vector = pd.DataFrame(vectorizer_features.toarray())
        new_text_vector = np.array(new_text_vector)

        # Compute cosine similarity between new element and existing elements
        similarity_scores = cosine_similarity(new_text_vector, tfv_matrix)

        # Reverse mapping of indices and movie titles
        indices = pd.Series(data2.index, index=data2['Restaurant Name']).drop_duplicates()
        similarity_scores_sorted = sorted(list(enumerate(similarity_scores[0])), key=lambda x: x[1], reverse=True)

        # Create data3:
        rest_name = []
        res_local = []
        rest_review = []
        rest_cuisine = []
        for i in range(5):
            rest_name.append(data2.iloc[similarity_scores_sorted[i][0]][0])
            res_local.append(data2.iloc[similarity_scores_sorted[i][0]][1])
            rest_review.append(data2.iloc[similarity_scores_sorted[i][0]][2])
            rest_cuisine.append(data2.iloc[similarity_scores_sorted[i][0]][3])

        data3 = {
            'Restaurant Name': rest_name,
            'Location': res_local,
            'Review': rest_review,
            'Cuisine': rest_cuisine
        }

        data3 = pd.DataFrame(data3)

        # Assuming you have a DataFrame called restaurant_data with 'Restaurant Name' and 'Review' columns
        sorted_restaurants = data3.sort_values(by='Review', ascending=False)['Restaurant Name']

        # Add a button
        if st.button('Search'): 
            if sorted_restaurants.empty:
                st.write('No restaurants found based on your cuisine preference.')
            else:
                st.write('Based on your information, you might like these restaurants:')
                # Print the restaurant names sorted by review
                for i in range(5):
                    st.write(sorted_restaurants[i])
        
        

        # Create a map with the recommended restaurants
        map_data = data[data['Restaurant Name'].isin(data3['Restaurant Name'])]
        map = create_map(map_data)
        folium_static(map)

except FileNotFoundError:
    st.write('Restaurant data file not found. Please make sure the file exists.')
