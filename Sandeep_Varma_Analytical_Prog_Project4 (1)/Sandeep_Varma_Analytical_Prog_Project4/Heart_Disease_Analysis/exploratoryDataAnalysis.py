import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class exploratoryDataAnalysis:
    
    def _inti__(self):
        """
        Initialize the ExploratoryDataAnalysis class.
        """
        print("***************************")
        print("EDA Starts here...")
        print("***************************")
    def drop_columns(self,df,columns):
        """
        Drop specified columns from the DataFrame.

        Parameters:
        - df (pd.DataFrame): The input DataFrame.
        - columns (list): List of column names to be dropped.

        Returns:
        - df (pd.DataFrame): The DataFrame after dropping specified columns.
        """
        df.drop(columns,axis=1,inplace=True)
        print("Printing the columns after dropping the columns")
        print(df.columns)
        return df
    def data_information_boxplots(self,df):
        """
        Display data information, check for null values, and generate boxplots for numerical attributes.

        Parameters:
        - df (pd.DataFrame): The input DataFrame.

        Returns:
        - None
        """
        print("Checking for null values")
        print(df.isnull().sum())
        print("Checking the statistical summary of the dataset")
        print(df.describe())
        print("""describe() method gives the all summary statistics like mean, max, min standard deviation,frequency and the four quartile range data distribution which helps to understand the data distribution of the dataset
        \nNow I will deep diving into analysis with each and every attribute""")
        print("Analysing the age distribution")
        print(df['age'].describe())
        print("The average age in the data set is 54 years and minimum age is 29 and the maximum age is 77years.")
        #boxplot using the matplotlib
        plt.figure(figsize=(8, 6))
        plt.boxplot(df['age'])
        plt.title('Matplotlib - Boxplot for ' + 'Age')
        plt.ylabel('Values')
        plt.show()
        print("From the boxplot we can observe how the data is distributed and can come to know the different quartile ranges from the boxplot for a data.")
        #boxplot using the seaborn
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df['age'])
        plt.title('Boxplot for Age - Seaborn')
        plt.ylabel('Values')
        plt.show()
        print("Replacing the 1 with male and 0 with female")
        df['sex'] = df['sex'].replace({1: 'male', 0: 'female'})
        print(df['sex'].describe())
        print("Data contains total 303 records with two uique genders namely male and female.")
        print(df['trestbps'].describe())
        print("For resting blood pressure on admission to the hospital the average blood pressure is 131 mm/Hg. Maximum and Minimum blood pressure are 200 mm/Hg and 94 mm/Hg respectively")
        print("From the above boxplot I can see that there were few outliers in the data of this attribute")
        print(df['chol'].describe())
        print("The average cholesterol of a persons here is around 246.69 mg/dl and the maximum being the 564 mg/dl and minimum is 126 mg/dl")
        #boxplot using the matplotlib
        plt.figure(figsize=(8, 6))
        plt.boxplot(df['chol'])
        plt.title('Boxplot for ' + 'cholesterol - Matplotlib')
        plt.ylabel('Values')
        plt.show()
        #boxplot using the seaborn
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df['chol'])
        plt.title('Boxplot for cholesterol - Seaborn')
        plt.ylabel('Values')
        plt.show()
        print("In this column also there are few outliers in the data that is around 5 outlier can be found as per the boxplot")
        print(df['fbs'].astype(str).describe())
        print("fbs represents the fasting blood sugar. 1 represent the that fasting blood sugar level is >120 mg/dl and 0 represent less than 120 mg/dl")
        print(df['ca'].describe())
        print("ca attribute represents the number of major vessels (0-3) colored by fluoroscopy. Here the maximum vessels can be only upto 3 and the on average we can consider it as 1 vessel being colored by fluoroscopy.")
        print(df['num'].astype(str).describe())
        print("num is target variable indicating disease presence (values 1,2,3,4) from absence (value 0).")
        print("There are 5 unique different types of values but as per the data dictionary given by the UCI 0 represents the absence and other value represents the present of the disease")
    def analysis(self,df):
        """
        Conduct exploratory analysis on the dataset, including visualization of age distribution, gender distribution,
        fasting blood sugar, cholesterol, and more.

        Parameters:
        - df (pd.DataFrame): The input DataFrame.

        Returns:
        - None
        """
        print("**********************************")
        print("Age")
        print("**********************************")
        # Lets draw the distribution of the age attribute
        print("Distribution of the age attribute")
        plt.hist(df['age'], bins=10, color='skyblue', edgecolor='black')
        plt.title('Histogram of Age')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.show()
        print("Most of the people fall between the age approximately around 53 and 63 years old.")
        # Defining the age group boundaries
        age_bins = [0, 17, 44, 64, float('inf')]  # age ranges for each group
        print("Defining the corresponding age group labels")
        # Defining the corresponding age group labels
        age_labels = ['Under 18 years', '18–44 years', '45–64 years', '65 and over']
        print("Creating a new column 'age_group' based on age values")
        # Creating a new column 'age_group' based on age values
        df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
        print("Creating a new column 'age_group' based on age values")
        # Filter the data to include only individuals with heart disease
        heart_disease_df = df[df['num'] != 0]

        # Define the age group labels
        age_group_labels = ['Under 18 years', '18–44 years', '45–64 years', '65 and over']

        # Create subplots for Matplotlib and Seaborn side by side
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        # Using Matplotlib
        ax1.bar(age_group_labels, heart_disease_df.groupby('age_group').size())
        ax1.set_title('Matplotlib: Number of Individuals with Heart Disease by Age Group')
        ax1.set_xlabel('Age Group')
        ax1.set_ylabel('Count')

        # Using Seaborn
        sns.countplot(data=heart_disease_df, x='age_group', order=age_group_labels, palette='Set1', ax=ax2)
        ax2.set_title('Seaborn: Number of Individuals with Heart Disease by Age Group')
        ax2.set_xlabel('Age Group')
        ax2.set_ylabel('Count')
        ax2.tick_params(axis='x', labelrotation=45)  # Rotate x-axis labels for Seaborn plot

        plt.tight_layout()
        plt.show()
        print("""Observations : As per the barplot, it shows that there more population falls in age group of 45 - 64 years followed by 65 years and above.
                We can observe that even without bins also results are matching nearly.Here if we consider the age bins close to 55 and 65 we can see the much matching between the distribution of age and the no of people fall under age bin 45 to 64 as shown above""")
        print("****************************************")
        print("Sex")
        print("****************************************")
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        # Using Matplotlib
        ax1.bar(['Male', 'Female'], heart_disease_df['sex'].value_counts())
        ax1.set_title('Matplotlib: Number of Individuals with Heart Disease by Gender-Matplotlib')
        ax1.set_ylabel('Count')

        # Using Seaborn
        sns.countplot(data=heart_disease_df, x='sex', palette='Set1', ax=ax2)
        ax2.set_title('Seaborn: Number of Individuals with Heart Disease by Gender-Seaborn')
        ax2.set_ylabel('Count')
        plt.tight_layout()
        plt.show()
        print("Observations : Surprisingly the heart diseases were more prevalent among the Males compared to the Females.")
        print("********************************************")
        print("fbs : Fasting blood sugar > 120 mg/dl")
        print("********************************************")
        #here also we will replace 1 with fbs >120 and 0 with fbs<0
        heart_disease_df['fbs']=heart_disease_df['fbs'].replace({1:"fbs>120",0:"fbs<120"})
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        # Using Matplotlib
        ax1.bar(['fbs<120 mg/dl', 'fbs>120 mg/dl'], heart_disease_df['fbs'].value_counts())
        ax1.set_title('Matplotlib: Number of Individuals with fbs > 120 mg/dl and fbs < 120 mg/dl')
        ax1.set_ylabel('Count')

        # Using Seaborn
        sns.countplot(data=heart_disease_df, x='fbs', palette='Set1', ax=ax2)
        ax2.set_title('Seaborn: Number of Individuals with fbs > 120 mg/dl and fbs < 120 mg/dl')
        ax2.set_ylabel('Count')
        plt.tight_layout()
        plt.show()
        print("Observations : From the above plots it shows that more people has fbs <120 mg/dl")
        print("*******************************************")
        print("Average cholesterol by each group with heart disease")
        print("*******************************************")
        print(df.groupby('age_group').agg({'chol': ['mean', 'count']}).reset_index())
        print("""Observations : from the above data, cholesterol is more in the age group of 5 and above and also the average cholesterol for that age group is around 263.82 mg/dl""")
        print("*******************************************")
        print("Average Blood Pressure by age group")
        print("*******************************************")
        print(df.groupby('age_group').agg({'trestbps': ['mean', 'count']}).reset_index())
        print("Observations : The blood pressure is high in age group of 65 and over with an average blood pressure of 137 mm Hg")
        print("*******************************************")
        print("Average Blood pressure and cholesterol by sex")
        print("*******************************************")
        print(df.groupby('sex').agg({'trestbps': ['mean'],'chol':['mean','count']}).reset_index())
        print("""Observations : In males the persons with average cholesterol  of around 239 mg/dl and blood pressure of around 131 mm Hg are likely to het heart diseases and similarly in Females with blood pressure around 133 mm Hg and cholesterol  of around 262 mg/dl are more likely to get heart diseases""")
    print("Exploratory Data Analysis Ends here...")



