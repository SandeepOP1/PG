import streamlit as st
import pickle
import pandas as pd
from iteration_utilities import unique_everseen
from iteration_utilities import duplicates

def recommend(higher_studies):
    pg_index = pg[pg['INPUT'] == higher_studies].index[0]
    distances = similarity[pg_index]
    pg_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]

    recommended_studies = []
    for i in pg_list:
        recommended_studies.append(pg.iloc[i[0]].PG)
    recommended_studies1 = set(recommended_studies)
    return recommended_studies1

def recommend_UG(higher_studies):
    pg_index = pg[pg['UG'] == higher_studies].index[0]
    distances = similarity[pg_index]
    pg_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]

    recommended_studies = []
    for i in pg_list:
        recommended_studies.append(pg.iloc[i[0]].PG)
    recommended_studies1 = set(recommended_studies)
    return recommended_studies1

def recommend_Spec(higher_studies):
    pg_index = pg[pg['SPECIALIZATION'] == higher_studies].index[0]
    distances = similarity[pg_index]
    pg_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]

    recommended_studies = []
    for i in pg_list:
        recommended_studies.append(pg.iloc[i[0]].PG)
    recommended_studies1 = set(recommended_studies)
    return recommended_studies1



pg_dict = pickle.load(open('pg_dict.pkl','rb'))
pg = pd.DataFrame(pg_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.markdown(""" <h1 align="Center"><font face="Algerian" color="#800000"><font size = "6"><b>Higher Studies Recommendation System</b></font></h1>""", True)

UG1 = set(pg['UG'].values)
key_ug = st.selectbox('Select your Under Graduate', UG1)


Spec1 = set(pg['SPECIALIZATION'].values)
key_spec = st.selectbox('Select your Stream', Spec1)

#Skill1 = set(pg['SKILLS'].values)
#selected_skills = st.selectbox('Select your Skills', Skill1)

#key_skill = st.multiselect('Select Your Skills', Skill1)
#skill = pd.Series(key_skill)
#skill_1 = skill.values

interests = set(pg['INTERESTS'].values)
key_interest = st.multiselect('Select Your Interests', interests)
interest = pd.Series(key_interest)
interests = interest.values

#Input = selected_skills


if st.button('Recommend'):
    recommendation = []
    for i in interests:
        recommendation.extend(recommend(i))

    recommendation.extend(recommend_UG(key_ug))
    recommendation.extend(recommend_Spec(key_spec))

    recommendations = recommendation
    st.write(recommendation)
    result = pd.DataFrame(unique_everseen(duplicates(recommendations)))




#container = st.container()
#st.write('You selected:', skill_1)


    #result = pd.DataFrame(set(recommendation))
    #recommendations = result[0]

  #  st.write(recommendations)