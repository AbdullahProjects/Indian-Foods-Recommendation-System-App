import streamlit as st
import pickle as pk
# import requests
                                                                         
dataset = pk.load(open("imported from jupiter notebook/dataset.pkl","rb"))
n_dataset = pk.load(open("imported from jupiter notebook/new_dataset.pkl","rb"))
similarity_recommender = pk.load(open("imported from jupiter notebook/similarity_recommender.pkl","rb"))


def recommend_food(food_name):
    
    food_index = n_dataset[n_dataset["name"] == food_name].index[0]

    # Use the new_food_index to get recommendations from the similarity matrix
    distances = similarity_recommender[food_index]
    recommend_foods = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    # Get details of the selected food
    current_food = [n_dataset.iloc[food_index][0], n_dataset.iloc[food_index][1]]

    # Get details of recommended foods
    food_list = []
    food_image = []
    for i in recommend_foods:
        index = i[0]
        food_list.append(n_dataset.iloc[index][0])
        food_image.append(n_dataset.iloc[index][1])

    return current_food, food_list, food_image




st.title("Indian Foods Recommendation App")
food_name = st.selectbox("Select the Food: ", n_dataset["name"].unique())
if st.button("Recommend"):
    current,name,poster = recommend_food(food_name)
    print(current)
    st.header("You Search It:")
    st.write(current[0])
    st.image(current[1])

    st.header("Recommendations For You:")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"{1}. "+name[0])
        st.image(poster[0])
    with col2:
        st.write(f"{2}. "+name[1])
        st.image(poster[1])
    

    col3, col4 = st.columns(2)
    with col3:
        st.write(f"{3}. "+name[2])
        st.image(poster[2])
    with col4:
        st.write(f"{4}. "+name[3])
        st.image(poster[3])

    col5, col6 = st.columns(2)
    with col5:
        st.write(f"{5}. "+name[4])
        st.image(poster[4])
    with col6:
        st.write(f"{6}. "+name[5])
        st.image(poster[5])
