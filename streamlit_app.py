import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Define sample data as a dictionary with days of the week as keys and lists of temperatures as values.
# Each key-value pair corresponds to a city and its temperature readings across a week.
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'New York': [22, 23, 19, 21, 24, 20, 22],
    'London': [15, 16, 14, 15, 13, 14, 15],
    'Tokyo': [26, 25, 27, 28, 26, 27, 25]
}

# Convert the dictionary into a pandas DataFrame to facilitate data manipulation and visualization.
df = pd.DataFrame(data)

# Set the title of the Streamlit application. This will appear as a header in the web application.
st.title('Weekly Temperature Trends')

# Create a select box widget in the Streamlit app interface.
# This allows the user to choose a city from the list, affecting which city's data is displayed.
city = st.selectbox('Choose a city:', ['New York', 'London', 'Tokyo'])

# Create a radio button widget to choose the type of plot: Line Chart or Bar Chart.
# This user input determines how the data will be visualized.
plot_type = st.radio("Choose the type of plot:", ['Line Chart', 'Bar Chart'])

# Define a function to plot data based on the selected city and plot type.
def plot_data(city, plot_type):
    # Create a figure and a set of subplots.
    fig, ax = plt.subplots()
    
    # Check if the plot type is 'Line Chart'.
    if plot_type == 'Line Chart':
        # Plot a line graph of the selected city's temperatures over the week.
        ax.plot(df['Day'], df[city], marker='o')  # 'o' marker style
        plt.xlabel('Day of the Week')  # Label for the x-axis
        plt.ylabel('Temperature (°C)')  # Label for the y-axis
        plt.title(f'Temperature Trend in {city}')  # Title of the plot
    
    # Check if the plot type is 'Bar Chart'.
    elif plot_type == 'Bar Chart':
        # Plot a bar chart of the selected city's temperatures over the week.
        ax.bar(df['Day'], df[city], color='skyblue')  # Blue color for bars
        plt.xlabel('Day of the Week')  # Label for the x-axis
        plt.ylabel('Temperature (°C)')  # Label for the y-axis
        plt.title(f'Temperature Trend in {city}')  # Title of the plot
    
    # Display the plot in the Streamlit app.
    st.pyplot(fig)

# Call the plot_data function with the selected city and plot type to display the plot in the app.
plot_data(city, plot_type)
