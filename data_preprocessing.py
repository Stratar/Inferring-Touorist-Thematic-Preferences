import pandas as pd
from sklearn.model_selection import train_test_split
from collections import Counter
from data_visualisation import bar_charts

def import_data_from_xlsx(filename='data/customers/Touristic Concept_May 23, 2023_07.31.xlsx'):
    data = pd.read_excel(filename)

    return data

def remove_verbose_columns(data):

    list_columns = [item for item in data.columns.values if '_' in item]
    prefix_list = [item.split('_')[0] for item in list_columns]
    item_counts = Counter(prefix_list)
    duplicates = [item for item, count in item_counts.items() 
                  if (count > 1 and 'groupping' not in item)]
    # We now have all the column names which are re-occurring.
    # We should now be  able to find only the columns in the data which contain an item
    # from the list and change the column name to the suffix from the corresponding dictionary
    # data.columns = [data[col].iloc[0].rsplit('_')[0].split() if any(item in col 
    #                 for item in duplicates) else col for col in data.columns]
    data.rename(columns=lambda x: x.split('_')[0] + " " + data[x].iloc[0].split(' - ')[-1] 
                if any(item in x for item in duplicates) else x, inplace=True)
    return data

def filter_columns(data):
    selected_columns = ['D Sex', 'D Age', 'D Living_1', 'D Nationality_1', 'T Greece', 
                         'T Travel companion', 'P themes pos Agricultural', 
                         'P themes pos Cultural', 
                         'P themes pos Religious', 'P themes pos Architecture', 
                         'P themes pos Sports', 'P themes pos Winter sports', 
                         'P themes pos Wellness', 'P themes pos Natural']
    data = data[data['Finished'] == 'True']
    data = data[selected_columns]
    data = data.dropna()
    return data

def organise(data):
    text_data = data[['D Nationality_1', 'D Marital Status', '']].values
    numerical_data = data[['numerical_feature1', 'numerical_feature2']].values
    labels = data['target_variable'].values

    return text_data, numerical_data, labels

def split(text_data, numerical_data, labels):
    text_train, text_test, numerical_train, numerical_test, labels_train, labels_test = train_test_split(
    text_data, numerical_data, labels, test_size=0.2, random_state=42)

    return text_train, text_test, numerical_train, numerical_test, labels_train, labels_test

data = import_data_from_xlsx()
data = remove_verbose_columns(data)
data = filter_columns(data)

print(data)

# Groupped age data for theme preference visualization
groupped_data = data.groupby('D Age').mean()
bar_charts(groupped_data)
# Groupped sex data for theme preference visualization
groupped_data = data.groupby('D Sex').mean()
bar_charts(groupped_data)
# Groupped living data for theme preference visualization
groupped_data = data.groupby('D Living_1').mean()
bar_charts(groupped_data)
# Groupped nationality data for theme preference visualization
groupped_data = data.groupby('D Nationality_1').mean()
bar_charts(groupped_data)


