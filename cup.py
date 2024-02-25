import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# Load data
data = pd.read_csv('2022worldcup.csv', index_col=0)

st.title("Qatar World Cup")

# Function to display the dataframe
def display_data():
   
    st.write("The Qatar 2022, FIFA World Cup was the 22nd FIFA World Cup. It was hosted in Qatar from 20 November to 18 December 2022. It was the first World Cup hosted in the Arab world, and the second to be hosted fully in Asia. This was the last World Cup played with a 32 team format.")


st.image("11.PNG")
st.image("12.PNG")
st.image("13.PNG")


# Function to display a bar chart of goals scored
def goals_bar_chart():
    st.header("Goals Scored")
    goals = data['Gls']
    labels = data.index
    plt.figure(figsize=(10, 6))
    plt.bar(labels, goals)
    plt.xlabel('Teams')
    plt.ylabel('Goals')
    st.pyplot(plt)


# Function to display a scatter plot of goals and average age
def goals_vs_age_scatter_plot():
    st.header("Goals vs. Average Age")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(data['Age'], data['Gls'])
    ax.set_xlabel('Average Age')
    ax.set_ylabel('Goals')
    ax.set_title('Goals Scored vs. Average Age')
    st.pyplot(fig)


# Streamlit app
def main():
    st.title("Football World Cup - Team Statistics")

    st.sidebar.header("Navigation")
    nav = st.sidebar.selectbox("Select", ["Home", "Charts"])

    if nav == "Home":
        display_data()
        
    elif nav == "Charts":
        st.sidebar.subheader("Charts")
        chart_type = st.sidebar.selectbox("Select a chart", ["Goals Bar Chart", "Goals vs. Age Scatter Plot"])

        if chart_type == "Goals Bar Chart":
            goals_bar_chart()

        elif chart_type == "Goal Contributions":
            goal_contributions_chart()

        elif chart_type == "Goals vs. Age Scatter Plot":
            goals_vs_age_scatter_plot()

if __name__ == "__main__":
    main()


st.header("Goals and Assists Distribution")
labels = ['Goals', 'Assists']
sizes = [data['Gls'].sum(), data['Ast'].sum()]
colors = ['#ff9999', '#66b3ff']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
st.pyplot(plt)

# Display a 3D scatter plot of goals, assists, and average age
st.header("3D Scatter Plot: Goals, Assists, and Average Age")
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['Age'], data['Gls'], data['Ast'], c='r')
ax.set_xlabel('Average Age')
ax.set_ylabel('Goals')
ax.set_zlabel('Assists')
st.pyplot(fig)

st.header("Goals vs. Games Played")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data['MP'], data['Gls'])
ax.set_xlabel('Games Played')
ax.set_ylabel('Goals')
ax.set_title('Goals Scored vs. Games Played')
st.pyplot(fig)