import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def inferences(df):

    """
    Generate and display inferences based on the given DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.

    Returns:
    - None
    """
    print("******************************************")
    print("Inference - 1 : What is the distribution of age and gender in the dataset, and are there any noticeable trends or differences in heart disease prevalence within these groups?")
    print("******************************************")
    # Group the data by 'age_group' and 'gender' and count the number of individuals with heart diseases for each group
    heart_disease_df = df[df['num'] != 0]
    heart_disease_count = heart_disease_df.groupby(['age_group', 'sex'])['num'].count().reset_index()
    # Renaming columns for readability
    print(heart_disease_count.rename(columns={'num': 'count'}))
    plt.figure(figsize=(10, 6))
    sns.barplot(data=heart_disease_df, x='age_group', y='num', hue='sex', ci=None)
    plt.title('Seaborn - Number of Individuals with Heart Disease by Age Group and Gender')
    plt.xlabel('Age Group')
    plt.ylabel('Count')
    plt.legend(title='Sex')
    plt.show()

    # Set the figure size
    plt.figure(figsize=(10, 6))
    # Create a bar plot using Matplotlib
    for sex in heart_disease_df['sex'].unique():
        subset = heart_disease_df[heart_disease_df['sex'] == sex]
        age_counts = subset.groupby('age_group')['num'].sum()
        plt.bar(age_counts.index, age_counts, label=sex)
    # Set plot title and labels
    plt.title('Matplotlib - Number of Individuals with Heart Disease by Age Group and Gender')
    plt.xlabel('Age Group')
    plt.ylabel('Count')
    # Add legend
    plt.legend(title='Sex')
    # Show the plot
    plt.show()
    print("""Observations : From the above result can say that more number of people with heart diseases are falling in age group of 65 and over both males and females""")
    print("******************************************")
    print("Inference - 2 :What is the distribution of the number of major vessels colored by fluoroscopy, and is there a clear association between this variable and the presence of heart disease?")
    print("******************************************")
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='ca', hue='num', palette='Set1', hue_order=[0, 1])
    plt.title('Seaborn - Distribution of Major Vessels Colored by Fluoroscopy by Heart Disease Status')
    plt.xlabel('Number of Major Vessels (ca)')
    plt.ylabel('Count')
    plt.legend(title='Heart Disease', labels=['No', 'Yes'])

    #using matplotlib
    # Assuming df is your DataFrame
    plt.figure(figsize=(8, 6))
    # Grouped bar chart using Matplotlib
    categories = df['ca'].unique()
    bar_width = 0.35  # Width of each bar

    # Get counts for each category and hue
    counts_no = df[df['num'] == 0].groupby('ca').size().reindex(categories, fill_value=0).tolist()
    counts_yes = df[df['num'] == 1].groupby('ca').size().reindex(categories, fill_value=0).tolist()

    # Calculate the positions for the bars
    positions_no = range(len(categories))
    positions_yes = [pos + bar_width for pos in positions_no]
    # Plot the bars
    plt.bar(positions_no, counts_no, width=bar_width, color='blue', label='No')
    plt.bar(positions_yes, counts_yes, width=bar_width, color='orange', label='Yes')
    # Set x-axis labels
    plt.xticks([pos + bar_width / 2 for pos in positions_no], categories)
    # Set labels and title
    plt.title('Matplotlib - Distribution of Major Vessels Colored by Fluoroscopy by Heart Disease Status')
    plt.xlabel('Number of Major Vessels (ca)')
    plt.ylabel('Count')
    plt.legend(title='Heart Disease', labels=['No', 'Yes'])
    plt.show()
    print("""Observations : From the above results it shows that more people has vessels not colored by fluoroscopy in case of heart disease""")
    print("******************************************")
    print("Inference - 3 :     Does having blood pressure greater than 120 have any observable impact on the curability of heart disease, and how common is this condition among individuals?")
    print("******************************************")
    # Create a countplot to visualize the impact of blood pressure on heart disease presence
    df['fbs']=df['fbs'].astype(int)
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='fbs', hue='num', palette='Set1', hue_order=[0, 1])
    plt.title('Impact of Blood Pressure on Heart Disease Presence')
    plt.xlabel('Fasting Blood Sugar (fbs) >120 (1) or <=120 (0)')
    plt.ylabel('Count')
    plt.legend(title='Heart Disease', labels=['No', 'Yes'])
    plt.show()
    # Calculate the percentage of individuals with high blood pressure (>120)
    total_high_bp = df['fbs'].sum()
    total_individuals = len(df)
    percentage_high_bp = (total_high_bp / total_individuals) * 100
    print(f"Percentage of individuals with high blood pressure (>120): {percentage_high_bp}%")
    print("""Observations : From the above data it is evident that a person with blood pressure > 120 has high likely to get heart diseases.""")
    print("******************************************")
    print("Inference - 4 : Can we identify any significant correlations or associations between ca(no of vessels colored by fluoroscopy) and the variable indicating the curability of heart disease?")
    print("******************************************")
    # Create a correlation matrix for all columns in the DataFrame df
    correlation_matrix = df.corr()
    # Create a heatmap
    plt.figure(figsize=(7,4))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap ")
    plt.show()
    print("""From the above correlation matrix visualized using heatmap, Age and Num has very less correlation so curing of heart disease might  depend on the age.

    But num is correlated with the ca which is number of vessels colored by fluoroscopy which means that this treatment can be a good treatment to the heart disease.""")
