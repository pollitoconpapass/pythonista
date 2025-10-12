# Pandas methods to handle Dataframes 🐼📊

## Load and explore data
### Read CSV
```py
df = pd.read_csv("archivo.csv")
```

### See first rows
```py
df.head(5)
```

### See last rows
```py
df.tail(5)
```

### General Info
```py
df.info()
```

### Statistical Summary
```py
df.describe()
```

### See columns
```py
df.columns()
```

### See dimensions
```py
df.shape()
```

## Seleccionar Datos
### Seleccionar una columna
```py
df["columna"]
```

### Seleccionar varias columnas
```py
df["col1", "col2"]
```

### Seleccionar por indice
```py
df.iloc[filas, columnas]
# Ej: 
df.iloc[0:5, 1:3]
```

### Seleccionar por nombre
```py
df.loc[filas, columnas]

# Ej:
df.loc[0:5, ["col1", "col2"]]
```

## Filtrado de datos
### Filtrar por condición
```py
df[df["columna"] > 10]
```

### Multiples condiciones
```py
# AND
df[(df["a"] > 5) & (df["b"] < 10)]

# OR
df[(df["a"] > 5) (df["b"] < 10)]
```

### Filtrar filas que contienen cierto texto
```py
df[df["columna"].str.contains("texto", case=False)]
```

### Eliminar duplicados
```py
df.drop_duplicates()
```

### Eliminar valores nulos
```py
df.dropna()
```

### Contar nulos
```py
df.isnull().sum()
```

### Valores unicos
```py
df["columna"].unique()
```


## Modificación y Limpieza
### Renombrar columnas
```py
df.rename(columns={"old": "new"}, inplace=True)
```

### Reemplazar valores
```py
df["col"].replace({"A": "X", "B": "Y"})
```

### Llenar valores nulos
```py
df.fillna(0)
```

### Agregar nueva columna a partir de otras
```py
df["nueva"] = df["a"] + df["b"]
```

### Eliminar columna
```py
df.drop("columna", axis=1, inplace=True)
```


## Agrupar y resumir datos
### Agrupar datos
Calcula estadísticas por grupo.
```py
df.groupby("columna")["otra_col"].mean()
```

### Contar valores
Cuenta la frecuencia de cada valor único.
```py
df["columna"].value_counts()
```

### Ordenar valores
Ordena por una columna.
```py
df.sort_values(by="columna", ascending=False)
```

### Calcular media, suma, etc.
```py
df["columna"].mean() # ->  .sum() | .max() | .min()
```

## Exportar Resultados
### Guardar en archivos CSV o Excel
```py
df.to_csv("salida.csv", index=False) # -> CSV
df.to_excel("salida.xlsx", index=False) # -> Excel
```