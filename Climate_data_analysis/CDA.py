#  importing 4 x libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# function to simulate loading temperature data
def load_temperature_data():
   data = pd.DataFrame({
      'Data':pd.date_range(start='1/1/2020',periods = 100),
      'Temperature':np.random.normal(20,5,100)
   })
   return data
#  main function where the app is run
def main():
   st.title("Climate Data Analysis")

#    Sidebar for user input: select variable to analyze
   st.sidebar.header("Settings")
# Extend This part with more variables or options 
   variable = st.sidebar.selectbox("Select Variables",['Temperature'])
# load and display data
   data = load_temperature_data()
# displaying the raw data as a table 
   st.write("#### Raw Data")
   st.write(data)

# plotting the data
   st.write(f"### {variable} Over Time")
   fig,ax = plt.subplots()
   ax.plot(data['Data'],data[variable],color='tab:red')
   plt.xlabel('Data')
   plt.ylabel(variable)
   plt.title(f"{variable} Over Time")
   st.pyplot(fig)



# Running the main function
if __name__ == "__main__":
   main()