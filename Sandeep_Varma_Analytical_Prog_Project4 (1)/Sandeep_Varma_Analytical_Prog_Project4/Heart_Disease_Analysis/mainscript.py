import datasummary as ds
import pandas as pd
import exploratoryDataAnalysis as eda
import matplotlib.pyplot as plt
import seaborn as sns
import inferences as infe
pd.set_option('display.max_columns',None)
print("***************************")
print("Introduction")
print("***************************")
print("""The dataset of Heart Disease is taken from UCI Data repository which contains both numerical and categorical features, allowing for a comprehensive exploration of potential correlations and patterns related to heart disease. Age and sex provide demographic information, while blood pressure and cholesterol levels are crucial indicators of heart health. The presence of blood pressure exceeding 120 and the number of major vessels colored by fluoroscopy offer additional medical insights, and the target variable serves as the primary outcome of interest, indicating whether heart disease can be cured.""")
print("***************************")
print("Research Questions")
print("***************************")
print("""
1. What is the distribution of age and gender in the dataset, and are there any noticeable trends or differences in heart disease prevalence within these groups?

\n2. What is the distribution of the number of major vessels colored by fluoroscopy, and is there a clear association between this variable and the presence of heart disease?

\n3. Does having blood pressure greater than 120 have any observable impact on the curability of heart disease, and how common is this condition among individuals?

\n4. Can we identify any significant correlations or associations between variables (e.g., age, cholesterol, blood pressure) and the variable indicating the curability of heart disease?""")

ds_obj=ds.dataSumamry()
df=ds_obj.fetch_data()
ds_obj.display_data(df)
eda_obj=eda.exploratoryDataAnalysis()
df=eda_obj.drop_columns(df,['cp','restecg','thalach','slope','thal'])
eda_obj.data_information_boxplots(df)
eda_obj.analysis(df)
infe.inferences(df)
# correlation_matrix=df.corr()
# plt.figure(figsize=(7,4))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title("Correlation Heatmap ")
# plt.show()
print("*********************************************")
print("Conclusion")
print("*********************************************")
print("""I conclude that the population within the dataset, all of whom have heart disease, exhibits a predominant distribution in the age group of 45-64 years, followed by those aged 65 and above. Notably, heart diseases appear to be more prevalent among males than females, emphasizing the role of gender as a potential risk factor for heart disease within this specific group. Moreover, the majority of individuals in the dataset have fasting blood sugar levels below 120 mg/dL, indicating a lower incidence of high blood sugar. Cholesterol levels tend to be higher among those aged 65 and above, with an average cholesterol level of approximately 263.82 mg/dL in this age group. The dataset also suggests that high blood pressure is more common among individuals aged 65 and over, with an average blood pressure of 137 mm Hg in this group. Additionally, males with an average cholesterol level of around 239 mg/dL and blood pressure of about 131 mm Hg, as well as females with blood pressure around 133 mm Hg and cholesterol of approximately 262 mg/dL, appear to be more likely to develop heart diseases within this specific heart disease population. The data further highlights that individuals with uncolored vessels by fluoroscopy are more commonly associated with heart disease. These insights underscore the importance of age, gender, blood sugar levels, cholesterol, and blood pressure as influential factors in the occurrence of heart diseases within this dataset of individuals already diagnosed with heart disease.
""")
print("*********************************************")
print("References")
print("*********************************************")
print("""
1. https://archive.ics.uci.edu/dataset/45/heart+disease

\n2. https://pandas.pydata.org/docs/user_guide/groupby.html#aggregation

\n3. https://sparkbyexamples.com/pandas/pandas-aggregate-functions-with-examples/

\n4. https://www.digitalocean.com/community/tutorials/exploratory-data-analysis-python

\n5. https://www.datacamp.com/courses/exploratory-data-analysis-in-python

\n6. https://www.kite.com/blog/python/data-analysis-visualization-python/

\n7. https://medium.com/5-minute-eda/5-minute-eda-correlation-heatmap-b57bbb7bae14""")
