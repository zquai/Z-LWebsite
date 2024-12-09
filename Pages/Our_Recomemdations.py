import streamlit as st
import pandas as pd
import os

#### had to make a switching tab function for tab2 to link to tab1
def switch_tab(tab_name):
    st.session_state.active_tab = tab_name

### File Paths
RATINGS_FILE = "ratings.csv"  # For Z's Recommendations
RATINGS_FILE1 = "ratings1.csv"  # For Lucy's Recommendations

### Initialize or Load CSV Files
def initialize(file_path, columns):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame(columns=columns)

# Columns for ratings
COLUMNS = ["User", "Place", "Rating", "Timestamp"]

# initialize df
ratings_df = initialize(RATINGS_FILE, COLUMNS)
ratings_df1 = initialize(RATINGS_FILE1, COLUMNS)

### saves data
def save_ratings(dataframe, file_path):
    dataframe.to_csv(file_path, index=False)

### function to add ratings to a file
def add_rating(dataframe, file_path, user, place, rating):
    new_row = {"User": user, "Place": place, "Rating": rating, "Timestamp": pd.Timestamp.now()}
    updated_df = pd.concat([dataframe, pd.DataFrame([new_row])], ignore_index=True)
    save_ratings(updated_df, file_path) #shows where to assign the updated df
    return updated_df


tab1, tab2 = st.tabs(["Lucy's Recomendations", "Z's Recomendations"])

with tab1:
    st.title("Lucy's Recomendations")
    st.write("Rate your favorite places!")
    st.write('Your feedback is saved in the table at the bottom of the page and averaged below')
    

    st.subheader("Enter an ID below to leave a review")
    username = st.text_input("Enter your name or unique identifier:")

    st.subheader("Average Ratings of Lucy's Recomendations")
    st.markdown('<p style="font-size:12px; color:gray;">If your rating is not showing, refresh the page.</p>', unsafe_allow_html=True)
    if not ratings_df1.empty:
        avg_ratings1 = (
            ratings_df1.groupby("Place")["Rating"]
            .mean()
            .reset_index()
            .rename(columns={"Rating": "Average Rating"})
        )
        st.table(avg_ratings1)
    else:
        st.write("No ratings yet. Be the first to rate!")

###############Start Baseball block
    st.header("Baseball Games")
    st.image("baseball.jpg", caption="Baseball Game, Credit: ABC News")
    details = "Baseball in Korea is unlike any sporting event I’ve experienced. The energy is upbeat and the crowd has a song for every player and every occasion. I went to a game in both Incheon and in Busan and both times were super fun, even though I do not speak Korean"
    st.write(details)

    if username:  #checking if username is in place and allowing access to rating system
        #baseball rating
        rating_baseball = st.radio("Rate Baseball (1 to 5 stars):", options=[1, 2, 3, 4, 5], horizontal=True, key="rating_baseball")

        if st.button("Submit Baseball Rating"):
            ratings_df1 = add_rating(ratings_df1, RATINGS_FILE1, username, "Baseball", rating_baseball)
            st.success(f"Thank you, {username}, for your {rating_baseball}-star rating for Baseball!")
### END BASEBALL RATING BLOCK

###BUKHANSAN
    st.header("Bukhansan National Park")
    st.image("bukhansan.jpg", caption= "Bukhansan Park, Credit: Global Alliance of National Parks")
    details = "The hiking at Bukhansan National Park was my favorite in the Seoul and Incheon area! Because of its location, it provides a really pretty view of Seoul and the park itself is full of unique rock formations. The trails are more suited for intermediate hikers, as the trails climb in elevation quickly."
    st.write(details)
    if username:  #checking if username is in place and allowing access to rating system
        #baseball rating
        rating_buk = st.radio(
            "Rate Bukhansan National Park (1 to 5 stars):", options=[1, 2, 3, 4, 5], horizontal=True, key="rating_buk")

        if st.button("Submit Bukhansan Rating"):
            ratings_df1 = add_rating(ratings_df1, RATINGS_FILE1, username, "Bukhansan", rating_buk)
            st.success(f"Thank you, {username}, for your {rating_buk}-star rating for Bukhansan!")

######BUSAN
    st.header("Busan")
    st.image("Busan.JPG", caption = "Busan, Image taken by Lucy Cole")
    details = "Busan is a quick KTX train ride away from Seoul and it quickly became one of my favorite locations in South Korea. Here, I went to the beach, traveled over the ocean in cable cars, took the sky capsule trains at sunset, visited the iconic colorful homes in Gamcheon Culture Village, and viewed the city from above at Busan Tower. It’s hard to go wrong in such a wonderful city like Busan and this city is on my list of places I would like to travel back to!"
    st.write(details)
    if username:  #checking if username is in place and allowing access to rating system
        #busan rating
        rating_busan = st.radio(
            "Rate Busan (1 to 5 stars):", options=[1, 2, 3, 4, 5], horizontal=True, key="rating_busan")

        if st.button("Submit Busan Rating"):
            ratings_df1 = add_rating(ratings_df1, RATINGS_FILE1, username, "Busan", rating_busan)
            st.success(f"Thank you, {username}, for your {rating_busan}-star rating for Busan!")
#########Busan end

    st.header("Jeju Island")
    st.image("jeju.jpg", caption= "Jeju Island, Credit: New 7 Wonders")
    details = "Often referred to as the Hawaii of Korea, Jeju Island has some of the prettiest lava rock formations I have seen. The cities in Jeju are small, but the island is an outdoor enthusiast's dream. Jeju is also known for their tangerines, and you can find orange-themed trinkets on every corner. Plus, you can get some of the best-tasting oranges and orange treats! "
    st.write(details)
    if username:  #checking if username is in place and allowing access to rating system
        #jeju rating
        rating_jeju = st.radio(
            "Rate Jeju Island (1 to 5 stars):", options=[1, 2, 3, 4, 5], horizontal=True, key="jeju")

        if st.button("Submit Jeju Island Rating"):
            ratings_df1 = add_rating(ratings_df1, RATINGS_FILE1, username, "Jeju", rating_jeju)
            st.success(f"Thank you, {username}, for your {rating_jeju}-star rating for Jeju Island!")

    st.header("Osaka, Japan")
    st.image("osaka.jpg", caption= "Osaka, Japan, Credit: Borders of Adventure")
    details = " A quick hour and a half flight away from Incheon International Airport, Osaka has enough charm to keep a tourist there for weeks! Between three full days, I managed to see most of the tourist attractions in both Osaka and Kyoto, but all of my stops were lightning fast and the days were packed. This was one of my favorite weekends while studying abroad and I would love to one day explore more of Japan."
    st.write(details)
    if username:  #checking if username is in place and allowing access to rating system
        #japan rating
        rating_osaka = st.radio(
            "Rate Osaka (1 to 5 stars):", options=[1, 2, 3, 4, 5], horizontal=True, key="osaka")

        if st.button("Submit Osaka Rating"):
            ratings_df1 = add_rating(ratings_df1, RATINGS_FILE1, username, "Osaka", rating_busan)
            st.success(f"Thank you, {username}, for your {rating_osaka}-star rating for Osaka!")


### Display table for Lucy's ratings
    st.subheader("Ratings History")
    st.dataframe(ratings_df1)

with tab2:
    st.header("Z's Recomendations")

    st.header("Here are my favorite places!")
    st.header("Leave a rating for your favorite places")
    st.write("Please enter an ID on Lucy's recomendations page")

    st.write('Your feedback is saved in the table at the bottom of the page and averaged below')
    st.markdown('<p style="font-size:12px; color:gray;">If your rating is not showing, refresh the page.</p>', unsafe_allow_html=True)
########table of averages
    st.subheader("Average Ratings")
    if not ratings_df.empty:
        avg_ratings = (
            ratings_df.groupby("Place")["Rating"]
            .mean()
            .reset_index()
            .rename(columns={"Rating": "Average Rating"})
        )
        st.table(avg_ratings)
    else:
        st.write("No ratings yet. Be the first to rate!")

    # Myeongdong info
    st.subheader("Myeongdong")
    st.image("myeongdong.jpg", caption="Myeongdong, Credit: GPS my City")
    st.write("I love shopping, so I love going to Myeongdong. There are lots of cool shops!")

    if username:  #checking if username is in place and allowing access to rating system
        #Myongdong rating
        rating_myeongdong = st.radio("Rate Myeongdong (1 to 5 stars):", options=[1, 2, 3, 4, 5], horizontal=True, key="myeongdong_rating")

        if st.button("Submit Myeongdong Rating"):
            ratings_df = add_rating(ratings_df, RATINGS_FILE, username, "Myeongdong", rating_myeongdong)
            st.success(f"Thank you, {username}, for your {rating_myeongdong}-star rating for Myeongdong!")
#######END MYEONGDONG


    #Dongmyo info
    st.subheader("Dongmyo Flea Market")
    st.image("dongmyo1.jpg", caption="Dongmyo Flea Market, Credit: I Seoul U")
    st.write("Dongmyo Flea Market is where I find all the best deals. If you like thrifting, you'll love it here!")

    if username:
        # Dongmyo ratings
        rating_dongmyo = st.radio(
            "Rate Dongmyo (1 to 5 stars):", options=[1, 2, 3, 4, 5], horizontal=True, key="dongmyo_rating"
        )

        if st.button("Submit Dongmyo Rating"):
            ratings_df = add_rating(ratings_df, RATINGS_FILE, username, "Dongmyo", rating_dongmyo)
            st.success(f"Thank you, {username}, for your {rating_dongmyo}-star rating for Dongmyo!")

    #end Dongmyo Block

    # Eurwangni Beach info
    st.subheader("Eurwangni Beach")
    st.image("eurwangni.jpg", caption="Eurwangni Beach, Credit: Visit Korea")
    st.write("My friends and I love going to the beach in the summer. This beach has warm water and soft sand.")
    if username:  #checking if username is in place and allowing access to rating system
        #Eurwangni rating
        rating_eruwangni = st.radio("Rate Eurwangni Beach (1 to 5 stars):", options=[1, 2, 3, 4, 5], horizontal=True, key="rating_eurwangni")

        if st.button("Submit Eurwangni Rating"):
            ratings_df = add_rating(ratings_df, RATINGS_FILE, username, "Eurwangni Beach", rating_eruwangni)
            st.success(f"Thank you, {username}, for your {rating_eruwangni}-star rating for Eurwangni Beach!")
    
    ### End Eurwangni

    st.subheader("Hongdae")
    st.image("hongdae.jpg", caption="Hongdae Street, Credit: Why Not Ju")
    details= "If you like partying, fashion, and good food, you'll love Hongdae. This area is located right by Hongik Universtiy and it's where many college students and foreigners go to have a fun night. Night life lasts until the early hours of the morning"
    st.write(details)

    if username:  #checking if username is in place and allowing access to rating system
        #hongdae rating
        rating_hongdae = st.radio("Rate Hongdae (1 to 5 stars):", options=[1, 2, 3, 4, 5], horizontal=True, key="hongdae_rating")

        if st.button("Submit Hongdae Rating"):
            ratings_df = add_rating(ratings_df, RATINGS_FILE, username, "Hondgae", rating_hongdae)
            st.success(f"Thank you, {username}, for your {rating_hongdae}-star rating for Hongdae!")
###### End Hongdae block

    st.subheader("Taiwan")
    st.image("Taiwan.JPG", caption="Taiwan, Credit: State Magazine")
    details= "Taiwan is a very culturally diverse place. I went there for the LGBT Pride march! It was a lot of fun seeing the fun fashion and people being unapolagetically themselves. I would recomend getting Bubble Tea in Taiwan, it was the best I'd ever had!"
    st.write(details)

    if username:  #checking if username is in place and allowing access to rating system
        #hongdae rating
        rating_taiwan = st.radio("Rate Taiwan (1 to 5 stars):", options=[1, 2, 3, 4, 5], horizontal=True, key="taiwan_rating")

        if st.button("Submit Taiwan Rating"):
            ratings_df = add_rating(ratings_df, RATINGS_FILE, username, "Taiwan", rating_taiwan)
            st.success(f"Thank you, {username}, for your {rating_taiwan}-star rating for Taiwan!")
###### end taiwan

    # Display Average Ratings
    st.subheader("Average Ratings")
    if not ratings_df.empty:
        avg_ratings = (
            ratings_df.groupby("Place")["Rating"]
            .mean()
            .reset_index()
            .rename(columns={"Rating": "Average Rating"})
        )
        st.table(avg_ratings)
    else:
        st.write("No ratings yet. Be the first to rate!")

    # Display the Ratings Table
    st.subheader("Ratings History")
    st.dataframe(ratings_df)