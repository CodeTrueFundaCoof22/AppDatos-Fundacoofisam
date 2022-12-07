##Importar librerias
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
import plotly.express as px
##Funcion para revisar datos categóricos o texto
def revCategoricos(dataframe, nomCol):
    rev = dataframe[nomCol].value_counts()
    print("Hola estoy aqui")
    return rev
## Mostrar grafica de barras
def graficabar(dataframe, text_input2):
    colors = ['#2ecc71', '#9b59b6', '#34495e','#f1c40f']
    text_input2 = str(text_input2)
    total = (dataframe[text_input2].value_counts())
    fig, ax = plt.subplots()
    plt.bar(total.index, total, color=colors)
    plt.show()
    return fig
## Añadidura de torta
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} C)".format(pct, absolute)

## Mostrar grafica de torta
def graficatorta(dataframe, text_input2):
    text_input2 = str(text_input2)
    total = (dataframe[text_input2].value_counts())
    fig, ax = plt.subplots()
    plt.pie(total, labels=total.index, autopct = lambda pct: func(pct, total))
    plt.show()
    return fig

## Funcion para eliminar columnas
def eliminarCol(dataframe, text_input3):
    columns_names = dataframe.columns.values
    for i in [text_input3]:
        for a in columns_names:
                if a == i:
                    dataframe = dataframe.drop(a, axis=1)
                else:
                    dataframe = dataframe
    return dataframe

## --------------------------------------Funcion principal-----------------------------------------  
def main():
    st.title("App Datos")
    ## Cargar archivo
    uploaded_file = st.file_uploader("Bienvenido, sube tu archivo")
    if uploaded_file is not None:
        # To read file as bytes
        bytes_data = uploaded_file.getvalue()
        dataframe = pd.read_excel(uploaded_file)
        
    if uploaded_file is not None:
        nombres_Columnas = dataframe.columns.values
        lista_nombres_columnas = list(nombres_Columnas)
        for i in lista_nombres_columnas:
            if i == 'Agencia':
                st.sidebar.header("Selecciona tu filtro")
                agencia = st.sidebar.multiselect(
                    "Selecciona la agencia",
                    options=dataframe['Agencia'].unique(),
                    default=dataframe['Agencia'].unique()
                )
                
                tipoIdentificacion = st.sidebar.multiselect(
                    "Selecciona el tipo de identificacion",
                    options=dataframe['TipoIdentificacion'].unique(),
                    default=dataframe['TipoIdentificacion'].unique()
                )
                
                aportes = st.sidebar.multiselect(
                    "Selecciona el aporte",
                    options=dataframe['Aportes'].unique(),
                    default=dataframe['Aportes'].unique()
                )
                
                dataframe_seleccionado = dataframe.query(
                    "Agencia == @agencia & TipoIdentificacion == @tipoIdentificacion & Aportes == @aportes")
                st.header("Tabla con filtro")
                st.dataframe(dataframe_seleccionado)
        else:
            st.header("Tabla")
            st.write(dataframe)
        
        st.header("Lista de las columnas")  
        nombres_Columnas = dataframe.columns.values
        lista_nombres_columnas = list(nombres_Columnas)
        st.write(nombres_Columnas)
        ## Revisar cantidad de datos
        st.header("Campo para revisar los datos de las columnas")
        text_input = st.text_input(
            "Ingresa el nombre de la columna 👇",
            label_visibility="visible",
            disabled=False,
            key='10'
            )
        if text_input:
            st.write(revCategoricos(dataframe, text_input))
            
        ## Graficas
        st.header("Campo para revisar los datos en graficas")
        text_input2 = st.text_input(
            "Ingresa el nombre de la columna 👇",
            label_visibility="visible",
            disabled=False,
            key="2"
            )
        if text_input2:
            st.pyplot(graficabar(dataframe, text_input2))
            st.pyplot(graficatorta(dataframe, text_input2))
                        
        
    ## ------- Botones -------------
    ## Revisar datos
    #revisarDatos = st.button("Vizualiza la cantidad de datos en una columna")
    #revisarDatosGrafica = st.button(label="Vizualiza la cantidad de datos en una grafica")
    #cambiarDatosNa = st.button(label="Cambia los valores en blanco")
    #st.write(revisarDatos)
    #nomCol = st.text_input(label="Ingresa el nombre de la columna")
    #if revisarDatos:
    #    nombres_Columnas = dataframe.columns.values
    #    lista_nombres_columnas = list(nombres_Columnas)
    #    st.write(nombres_Columnas)
    #    st.caption("Ingresa el nombre de la columna que quieres revisar")
    #st.write(revCategoricos(dataframe, nomCol))
    #if nomCol is None:
     #   st.write("You entered: ", nomCol)
    ## Grafica barras
    #if revisarDatosGrafica == True:
    #    st.write(graficabar(dataframe))
    ## Cambiar valores en blanco
    #if cambiarDatosNa == True:
    #    nombres_Columnas = dataframe.columns.values
    #    lista_nombres_columnas = list(nombres_Columnas)
    #    st.write(nombres_Columnas)
    #    nomReem = st.text_input("Ingresa el valor que quieres colocar por los espacios en blanco")
    #    nomCol = st.text_input(label="Ingresa el nombre de la columna")
    #    dataframe[nomCol] = reemNa(dataframe, nomCol)

if __name__ == '__main__':
    main()
    
    