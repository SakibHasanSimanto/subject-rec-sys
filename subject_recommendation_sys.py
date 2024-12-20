# -*- coding: utf-8 -*-
"""scratchpad

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/empty.ipynb
"""

import pickle
import plotly.graph_objects as go
import streamlit as st 
import matplotlib.pyplot as plt 
import seaborn as sns

# Means
science_means = [9.332117, 8.671923, 8.119462, 7.050453, 8.955779, 9.474824, 8.042016, 8.195870, 6.289582, 6.919393]
com_means = [7.927571, 6.043922, 6.063442, 4.067117, 7.021984, 5.023222, 5.006547, 4.999193, 5.028257, 5.505126]
arts_means = [8.873849, 5.996650, 8.415892, 7.899371, 4.965835, 4.028224, 5.086825, 6.118331, 7.051516, 7.281090]
columns = ['English', 'Math', 'Literature', 'Painting', 'Analytics', 'Physics', 'Chemistry', 'Biology', 'History', 'Philosophy']

# Model load
with open('subject_classifier_rfc.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit 
st.title('Subject Recommendation System 1.0')
st.write('Score your proficiency in the following fields out of 10.')

# Inputs
eng = st.text_input('English: ')
mth = st.text_input('Mathematics: ')
lit = st.text_input('Literature: ')
pnt = st.text_input('Painting: ')
anl = st.text_input('Analytics: ')
phy = st.text_input('Physics: ')
chm = st.text_input('Chemistry: ')
bio = st.text_input('Biology: ')
hst = st.text_input('History: ')
phl = st.text_input('Philosophy: ')

# Buttons
if st.button('Get Recommendation'):
    try:
        
        input_list = [eng, mth, lit, pnt, anl, phy, chm, bio, hst, phl]
        input_list = list(map(float, input_list))  # Ensure inputs are floats

        
        prediction = model.predict([input_list])

        if prediction[0] == 0:
            recommended = 'Science'
        elif prediction[0] == 1:
            recommended = 'Commerce'
        elif prediction[0] == 2:
            recommended = 'Arts'

        st.success(f'Recommended for you: {recommended}')

    except Exception as e:
        st.error(f"Error: {e}")
        # User feedback

st.write("Click Comparison to see how you differ and match with others")


      
# Button for comparison
if st.button('Comparison'):
    try:
        input_list = [eng, mth, lit, pnt, anl, phy, chm, bio, hst, phl]

        fig = go.Figure()

        fig.add_trace(go.Scatter(x=columns, y=science_means, mode='lines+markers', name='Science', line=dict(color='blue',dash='dash')))
        fig.add_trace(go.Scatter(x=columns, y=com_means, mode='lines+markers', name='Commerce', line=dict(color='green',dash='dash')))
        fig.add_trace(go.Scatter(x=columns, y=arts_means, mode='lines+markers', name='Arts', line=dict(color='red',dash='dash')))
        fig.add_trace(go.Scatter(x=columns, y=input_list, mode='markers+lines', name='Your Score', line=dict(color='magenta')))

        fig.update_layout(
            title="Subject Comparison with Mean Scores",
            xaxis_title="Subjects",
            yaxis_title="Scores",
            showlegend=True,
            xaxis=dict(tickangle=90),
            template="plotly_dark"  
        )

        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Error: {e}")


if st.button('Compare with Science'):
    try:
        input_list = [eng, mth, lit, pnt, anl, phy, chm, bio, hst, phl]


        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=columns, y=science_means, 
            mode='lines+markers', 
            name='Mean Science Scores',
            line=dict(color='blue')
        ))
        fig.add_trace(go.Scatter(
            x=columns, y=input_list, 
            mode='lines+markers', 
            name='Your Score',
            line=dict(color='magenta')
        ))


        fig.update_layout(
            title='Comparison with Science',
            xaxis_title='Subjects',
            yaxis_title='Scores',
            xaxis_tickangle=90,
            legend_title='Legend',
            template='plotly_white'
        )
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Error: {e}")

if st.button('Compare with Arts'):
    try:
        input_list = [eng, mth, lit, pnt, anl, phy, chm, bio, hst, phl]


        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=columns, y=arts_means, 
            mode='lines+markers', 
            name='Mean Arts Scores',
            line=dict(color='red')
        ))
        fig.add_trace(go.Scatter(
            x=columns, y=input_list, 
            mode='lines+markers', 
            name='Your Score',
            line=dict(color='magenta')
        ))

      
        fig.update_layout(
            title='Comparison with Arts',
            xaxis_title='Subjects',
            yaxis_title='Scores',
            xaxis_tickangle=90,
            legend_title='Legend',
            template='plotly_white'
        )
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Error: {e}")


if st.button('Compare with Commerce'):
    try:
        input_list = [eng, mth, lit, pnt, anl, phy, chm, bio, hst, phl]


        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=columns, y=com_means, 
            mode='lines+markers', 
            name='Mean Commerce Scores',
            line=dict(color='green')
        ))
        fig.add_trace(go.Scatter(
            x=columns, y=input_list, 
            mode='lines+markers', 
            name='Your Score',
            line=dict(color='magenta')
        ))


        fig.update_layout(
            title='Comparison with Commerce',
            xaxis_title='Subjects',
            yaxis_title='Scores',
            xaxis_tickangle=90,
            legend_title='Legend',
            template='plotly_white'
        )
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Error: {e}")
