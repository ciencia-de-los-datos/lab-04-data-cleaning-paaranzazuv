"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    df = df.copy()
    #df= df.dropna()
    df["sexo"] = df["sexo"]
    df["sexo"] = df["sexo"].str.strip()
    df["sexo"] = df["sexo"].str.lower()
    df["sexo"] = df["sexo"].str.replace("-", "")
    #df["sexo"] = df["sexo"].str.translate(
     #   str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")    )
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"]
    #df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.strip()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.replace("-", " ")
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.replace("_", " ")
    #df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.translate(
    #    str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")    )

    df["idea_negocio"] = df["idea_negocio"]
    #df["idea_negocio"] = df["idea_negocio"].str.strip()
    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.replace("-", " ")
    df["idea_negocio"] = df["idea_negocio"].str.replace("_", " ")
    #df["idea_negocio"] = df["idea_negocio"].str.translate(
    #    str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    #        )
    
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst= True, format='mixed')

    df['estrato'] = df['estrato'].astype("category")

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype("int")
    
    df["barrio"] = df["barrio"]
    #df["barrio"] = df["barrio"].str.strip()
    df["barrio"] = df["barrio"].str.lower()
    df["barrio"] = df["barrio"].str.replace("-", " ")
    df["barrio"] = df["barrio"].str.replace("_", " ")
    #df["barrio"] = df["barrio"].str.translate(
    #    str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    #       )
    
    df["monto_del_credito"] = df["monto_del_credito"]
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(",", "")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(".00", "")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(" ", "")
    df["monto_del_credito"] = df["monto_del_credito"].str.strip("$")
    #df["monto_del_credito"] = df["monto_del_credito"].str.translate(
    #    str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")            )
    
    df["línea_credito"] = df["línea_credito"]
    #df["línea_credito"] = df["línea_credito"].str.strip()
    df["línea_credito"] = df["línea_credito"].str.lower()
    df["línea_credito"] = df["línea_credito"].str.replace("-", " ")
    df["línea_credito"] = df["línea_credito"].str.replace("_", " ")
    #df["línea_credito"] = df["línea_credito"].str.translate(
    #    str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    #        )
    #df["línea_credito"] = df["línea_credito"].astype("category")

    df = df.drop_duplicates()
    df=df.dropna()
    
#         # Convertir la columna 'Fecha' al tipo datetime, especificando los formatos
#     df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format='%Y/%m/d%', errors='coerce')  # Formato: 'YYYY-MM-DD'
#     df['fecha_de_beneficio'] = df['fecha_de_beneficio'].combine_first(pd.to_datetime(df['fecha_de_beneficio'], format='%m/d%/%Y', errors='coerce'))  # Formato: 'AbbreviatedMonth DD, YYYY'
#     df['fecha_de_beneficio'] = df['fecha_de_beneficio'].combine_first(pd.to_datetime(df['fecha_de_beneficio'], format='%Y-%m-%d %H:%M:%S', errors='coerce'))  # Formato: 'YYYY-MM-DD HH:MM:SS'
    

# # Imprimir DataFrame con fechas limpias
    
    p

     #
    # Inserte su código aquí
    #

    return df


