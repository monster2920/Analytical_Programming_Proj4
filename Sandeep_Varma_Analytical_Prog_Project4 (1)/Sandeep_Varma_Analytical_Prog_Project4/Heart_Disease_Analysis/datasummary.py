# pip install ucimlrepo
import ucimlrepo as ucimlrepo
#importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class dataSumamry:
    def __inti__(self):
        """
        Initialize the DataSummary class.
        """
        print("***************************")
        print("Data Summary Starts here...")
        print("***************************")
        print(""" Data Summary
        Data set is taken from UIC Data repository.\n
        
        I am considering the subset of the dataset that is needed to answer my research questions.Data set contains 303 records and 7 columns.
        
        \n1.age : Age
        \n2.sex : Sex
        \n3.trestbps : resting blood pressure (on admission to the hospital) mm/Hg
        \n4.chol : serum cholestoral mg/dl
        \n5.fbs : fasting blood sugar > 120 mg/dl
        \n6.ca : number of major vessels (0-3) colored by fluoroscopy
        \n7.num : diagnosis of heart disease. It is integer valued from 0 (no presence) to 4""")
    def fetch_data(self):
        """
        Fetch the heart disease dataset from the UCI repository and return it as a pandas DataFrame.

        Returns:
        - df (pd.DataFrame): The merged DataFrame containing both features and the target variable.
        """
        #fetching the data from the UCI repository database using their respective python modules and libraries
        print("Fetching the data from the UCI repository database using their respective python modules and libraries")
        from ucimlrepo import fetch_ucirepo
        # fetch dataset
        heart_disease = fetch_ucirepo(id=45)
        # data (as pandas dataframes)
        X = heart_disease.data.features
        y = heart_disease.data.targets
        # metadata
        print("Printing the metadata:")
        print(heart_disease.metadata)
        print("Printing the variable information")
        # variable information
        print(heart_disease.variables)
        print("lets merge the data into a single data frame which contains both features and the target variable")
        df = pd.concat([heart_disease.data.features, heart_disease.data.targets], axis=1)
        return df
    def display_data(self,df):
        """
        Display the data, data types of attributes, and the shape of the data.

        Parameters:
        - df (pd.DataFrame): The input DataFrame.

        Returns:
        - None
        """

        print("Displaying the data")
        print(df)
        print("Data types of attributes")
        print(df.dtypes)
        print("Checking the shape of the data")
        print(df.shape)





