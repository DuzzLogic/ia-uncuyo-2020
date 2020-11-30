import pandas as pd
import numpy as np

def calcular_entropy(df_label):
    clases,n = np.unique(df_label,return_counts = True)
    entropy = np.sum([(-n[i]/np.sum(n))*np.log2(n[i]/np.sum(n)) for i in range(len(clases))])
    return entropy

def calcular_ganancia(dataset,atributo,label): 
    entropia_original = calcular_entropy(dataset[label])   
    values,a_count= np.unique(dataset[atributo],return_counts=True)
    
    entropia_esperada = np.sum([(a_count[i]/np.sum(a_count))*calcular_entropy(dataset.where(dataset[atributo] == values[i]).dropna()[label]) for i in range(len(values))])    
    
    ganancia = entropia_original - entropia_esperada
    return ganancia

def aprendizaje_AD(dataset, df, atributos, label, parent = None):
    dt = np.unique(df[label], return_counts=True)
    unique_data = np.unique(dataset[label])

    if len(unique_data) <= 1:
        return unique_data[0]

    elif len(dataset) == 0:
        return unique_data[np.argmax(dt[1])]

    elif len(atributos) == 0:
        return parent

    else:
        parent = unique_data[np.argmax(dt[1])]

        item_values = [calcular_ganancia(dataset,atributo,label) for atributo in atributos]

        atributo_optimo_index = np.argmax(item_values)
        atributo_optimo = atributos[atributo_optimo_index]
        decision_tree = {atributo_optimo:{}}
        atributos = [i for i in atributos if i != atributo_optimo]

        for value in np.unique(dataset[atributo_optimo]):
            min_data = dataset.where(dataset[atributo_optimo] == value).dropna()

            min_tree = aprendizaje_AD(min_data, df, atributos, label, parent)

            decision_tree[atributo_optimo][value] = min_tree

    return decision_tree
