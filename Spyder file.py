import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df_treeloss_drivers=pd.read_csv('C:/Users/prave/OneDrive - University of Hertfordshire/Applied DS 1/Tree loss due to fire/Tree cover loss due to fires in United Kingdom/treecover_loss__ha 1.csv',index_col='Tree cover loss year')
df_treeloss_drivers.head()

def plot_treeloss_drivers_pie(df_treeloss_drivers):
    #Pie chart to show tree cover loss % by different drivers over the years from 2001 to 2023#

    drivers_loss_sum=df_treeloss_drivers.groupby('Tree cover loss drivers')['Tree cover loss (ha)'].sum()
    plt.figure(dpi=144)
    plt.pie(drivers_loss_sum,labels=drivers_loss_sum.index,autopct='%1.1f%%',colors=sns.color_palette('Set2'),startangle=15,shadow=False, explode=[0.5, 0.5, 0.5, 0.5, 0.5])
    plt.title('Tree loss drivers (2001 to 2023)')
    plt.legend(loc='upper right',fontsize=6)
    plt.show()
    
plot_treeloss_drivers_pie(df_treeloss_drivers)
    
def plot_treeloss_drivers_by_eachyear(df_treeloss_drivers):

    #Year wise tree loss (hectares) bar chart from 2001 to 2023#
    
    plt.figure(dpi=144)
    plt.bar(df_treeloss_drivers.index, df_treeloss_drivers['Tree cover loss (ha)'],color='teal')
    plt.xticks(df_treeloss_drivers.index, rotation=90, ha='right')
    plt.title('Tree loss (ha) over the Years (2001-2023)')
    plt.xlabel('Years')
    plt.ylabel('Tree cover Loss (ha)')
    plt.show()
    
    
plot_treeloss_drivers_by_eachyear(df_treeloss_drivers)


def plot_tree_cover_loss_vs_emissions(df_treeloss_drivers):
    
    #Scatterplot show Treecover loss relationship with CO2 emission with its drivers#
    
    plt.figure(dpi=144)
    sns.scatterplot(x=df_treeloss_drivers['Tree cover loss (ha)'], y=df_treeloss_drivers['Co2 emissions (mg)'], hue=df_treeloss_drivers['Tree cover loss drivers'], palette='viridis')
    plt.title('Tree Cover Loss (ha) vs CO2 Emissions (mg)')
    plt.xlabel('Tree Cover Loss (ha)')
    plt.ylabel('CO2 Emissions (Mg)')
    plt.legend(title='Driver',bbox_to_anchor=(1,1),loc='upper left')
    plt.grid(True, color='lightgray',alpha=0.4, linestyle='-', linewidth=0.4)
    plt.show()
    
plot_tree_cover_loss_vs_emissions(df_treeloss_drivers)
    
def plot_relation_between_treecoverloss_and_CO2emission(df_treeloss_drivers):
    
    #Heatmap to show linear relationship between Tree cover loss vs CO2 Emissions#

    plt.figure(dpi=144)
    df_corr= df_treeloss_drivers[['Tree cover loss (ha)', 'Co2 emissions (mg)']].corr()
    sns.heatmap(df_corr, annot=True, cmap='RdBu', vmin=-1, vmax=1,linewidth=1,linecolor='red',yticklabels=True)
    plt.title('Correlation Heatmap between Tree Cover Loss (ha) vs CO2 Emissions (mg) (2001-2023)')
    plt.show()
    
plot_relation_between_treecoverloss_and_CO2emission(df_treeloss_drivers)
    
    #Tree cover loss (ha) describe (2001-2023)
print('Tree cover loss (ha) describe (2001-2023)\n\n',df_treeloss_drivers['Tree cover loss (ha)'].describe())
    
    #Tree loss between from 2001 to 2023_Mean
print('Tree cover loss (ha) (2001-2023) Statistics\n\n','mean:',df_treeloss_drivers['Tree cover loss (ha)'].mean())

#Tree loss between from 2001 to 2023_Median
print('median:',df_treeloss_drivers['Tree cover loss (ha)'].median())

#Tree loss between from 2001 to 2023_Standard Deviation
print('Standard Deviation:',df_treeloss_drivers['Tree cover loss (ha)'].std())

#Total tree loss between from 2001 to 2023
print('Total tree loss between from 2001 to 2023:',df_treeloss_drivers['Tree cover loss (ha)'].sum())

#Tree loss between from 2001 to 2023_Skewness
print('Skewness:',df_treeloss_drivers['Tree cover loss (ha)'].skew())

#Tree loss between from 2001 to 2023_Kurtosis
print('Kurtosis:',df_treeloss_drivers['Tree cover loss (ha)'].kurt())

# Tree loss CO2 Emission describe (2001-2023)
print('Tree loss CO2 Emission describe (2001-2023)\n\n', df_treeloss_drivers['Co2 emissions (mg)'].describe())


#Tree loss CO2 Emission_mean between from 2001 to 2023
print('Co2 emissions (mg) Statistics\n\n','Mean:',df_treeloss_drivers['Co2 emissions (mg)'].mean())

#Tree loss CO2 Emission_median between from 2001 to 2023
print('Median:',df_treeloss_drivers['Co2 emissions (mg)'].median())

#Tree loss CO2 Emission_Standard Deviation between from 2001 to 2023
print('Standard Deviation:',df_treeloss_drivers['Co2 emissions (mg)'].std())

#Total Tree loss CO2 Emission between from 2001 to 2023
print('Total CO2 Emission(2001 to 2023):',df_treeloss_drivers['Co2 emissions (mg)'].sum())

#Tree loss CO2 Emission_Skewness between from 2001 to 2023
print('Skewness',df_treeloss_drivers['Co2 emissions (mg)'].skew())

#Tree loss CO2 Emission_Kurtosis between from 2001 to 2023
print('Kurtosis',df_treeloss_drivers['Co2 emissions (mg)'].kurt())

Corr=df_treeloss_drivers[['Tree cover loss (ha)', 'Co2 emissions (mg)']].corr()
print('Tree cover loss (ha) vs Co2 emissions (mg) correlation (2001-2023):\n',Corr)