# Instrucciones

> ejecutar el index.py para probar el scrip


## ejemplo : 

```
py .\index.py
```


## clase => Parse():

Se encarga de tranfomar la información a Json 

###### Metodos


* handle_get_nim => esta funcion nos regresa el nim del estudio
* separa_cadena => esta funcion saca todos los resultados de las cadenas y genera el json  


##  settings > settings.py

Archivo con las con el ejemplo de la cadena

## ejemplo del json: 

```

{
   "nim":" 10122021001865",
   "resultados":[
      {
         "app_code":"WBC 1",
         "resultado":"4.07",
         "unidad":"10*3/uL"
      },
      {
         "app_code":"RBC 1",
         "resultado":"5.29",
         "unidad":"10*6/uL"
      },
      {
         "app_code":"HGB 1",
         "resultado":"15.9",
         "unidad":"g/dL"
      },
      {
         "app_code":"HCT 1",
         "resultado":"45.8",
         "unidad":"%"
      },
      {
         "app_code":"MCV 1",
         "resultado":"86.6",
         "unidad":"fL"
      },
      {
         "app_code":"MCH 1",
         "resultado":"30.1",
         "unidad":"pg"
      },
      {
         "app_code":"MCHC 1",
         "resultado":"34.7",
         "unidad":"g/dL"
      },
      {
         "app_code":"PLT 1",
         "resultado":"258",
         "unidad":"10*3/uL"
      },
      {
         "app_code":"NEUT  1",
         "resultado":"66.3",
         "unidad":"%"
      },
      {
         "app_code":"LYMPH  1",
         "resultado":"25.6",
         "unidad":"%"
      },
      {
         "app_code":"MONO  1",
         "resultado":"7.4",
         "unidad":"%"
      },
      {
         "app_code":"EO  1",
         "resultado":"0.5",
         "unidad":"%"
      },
      {
         "app_code":"BASO  1",
         "resultado":"0.2",
         "unidad":"%"
      },
      {
         "app_code":"NEUT  1",
         "resultado":"2.70",
         "unidad":"10*3/uL"
      },
      {
         "app_code":"LYMPH  1",
         "resultado":"1.04",
         "unidad":"10*3/uL"
      },
      {
         "app_code":"MONO  1",
         "resultado":"0.30",
         "unidad":"10*3/uL"
      },
      {
         "app_code":"EO  1",
         "resultado":"0.02",
         "unidad":"10*3/uL"
      },
      {
         "app_code":"BASO  1",
         "resultado":"0.01",
         "unidad":"10*3/uL"
      },
      {
         "app_code":"RDW SD 1",
         "resultado":"41.7",
         "unidad":"fL"
      },
      {
         "app_code":"RDW CV 1",
         "resultado":"13.3",
         "unidad":"%"
      },
      {
         "app_code":"MPV 1",
         "resultado":"10.1",
         "unidad":"fL"
      },
      {
         "app_code":"Blasts",
         "resultado":"0",
         "unidad":""
      },
      {
         "app_code":"Immature Gran",
         "resultado":"20",
         "unidad":""
      },
      {
         "app_code":"Left Shift",
         "resultado":"0",
         "unidad":""
      },
      {
         "app_code":"NRBC",
         "resultado":"10",
         "unidad":""
      },
      {
         "app_code":"Atypical Lympho",
         "resultado":"0",
         "unidad":""
      },
      {
         "app_code":"Abn Lympho Blasts",
         "resultado":"0",
         "unidad":""
      },
      {
         "app_code":"RBC Agglutination",
         "resultado":"60",
         "unidad":""
      },
      {
         "app_code":"Turbidity HGB Interference",
         "resultado":"90",
         "unidad":""
      },
      {
         "app_code":"Iron Deficiency",
         "resultado":"80",
         "unidad":""
      },
      {
         "app_code":"HGB Defect",
         "resultado":"80",
         "unidad":""
      },
      {
         "app_code":"Fragments",
         "resultado":"0",
         "unidad":""
      },
      {
         "app_code":"PLT Clumps",
         "resultado":"10",
         "unidad":""
      },
      {
         "app_code":"PLT Clumps S",
         "resultado":"40",
         "unidad":""
      },
      {
         "app_code":"SCAT DIFF",
         "resultado":"PNG&R&20220521&R&2022_02_10_12_44_10122021001865_DIFF.PNG",
         "unidad":""
      },
      {
         "app_code":"DIST RBC",
         "resultado":"PNG&R&20220521&R&2022_02_10_12_44_10122021001865_RBC.PNG",
         "unidad":""
      },
      {
         "app_code":"DIST PLT",
         "resultado":"PNG&R&20220521&R&2022_02_10_12_44_10122021001865_PLT.PNG",
         "unidad":""
      }
   ]
}

```
