```python
import tp6dt as ti
import pandas as pd
import numpy as np
import json
```


```python
df = pd.read_csv('tennis.csv')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>outlook</th>
      <th>temp</th>
      <th>humidity</th>
      <th>windy</th>
      <th>play</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>sunny</td>
      <td>hot</td>
      <td>high</td>
      <td>False</td>
      <td>no</td>
    </tr>
    <tr>
      <th>1</th>
      <td>sunny</td>
      <td>hot</td>
      <td>high</td>
      <td>True</td>
      <td>no</td>
    </tr>
    <tr>
      <th>2</th>
      <td>overcast</td>
      <td>hot</td>
      <td>high</td>
      <td>False</td>
      <td>yes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>rainy</td>
      <td>mild</td>
      <td>high</td>
      <td>False</td>
      <td>yes</td>
    </tr>
    <tr>
      <th>4</th>
      <td>rainy</td>
      <td>cool</td>
      <td>normal</td>
      <td>False</td>
      <td>yes</td>
    </tr>
  </tbody>
</table>
</div>




```python
atributos = df.columns[:-1]
label = 'play'
```


```python
arbol_D = ti.aprendizaje_AD(df,df,atributos,label)
```


```python
print(arbol_D)
```

    {'outlook': {'overcast': 'yes', 'rainy': {'windy': {0.0: 'yes', 1.0: 'no'}}, 'sunny': {'humidity': {'high': 'no', 'normal': 'yes'}}}}
    


```python
tree_str = json.dumps(arbol_D, indent=4)
tree_str = tree_str.replace("\n    ", "\n")
tree_str = tree_str.replace('"', "")
tree_str = tree_str.replace(',', "")
tree_str = tree_str.replace("{", "")
tree_str = tree_str.replace("}", "")
tree_str = tree_str.replace("    ", " | ")
tree_str = tree_str.replace("  ", " ")
```


```python
print(tree_str)
```

    
    outlook: 
     | overcast: yes
     | rainy: 
     | | windy: 
     | | | 0.0: yes
     | | | 1.0: no
     | | 
     | 
     | sunny: 
     | | humidity: 
     | | | high: no
     | | | normal: yes
     | | 
     | 
    
    
    
