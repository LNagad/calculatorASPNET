import json

#Descifrar un json

'''
json_str = '{"nombre":"Maycol","edad":18,"pais":"rd","telefono":809456878}'


print(json_str)
print(type(json_str))

python_dict = json.loads(json_str)

print(python_dict['nombre'])

'''

#---------------- Crear un json

data = {
    "nombre": "Maycol",
    "edad": 19,
    "pais": "republica dom",
    "telefono": 809458555,
    "cursos": ["PHP", "Python", "JavaScript", "C#", "Node.js"]
}

# json_data = json.dumps(data)
# print(json_data)
# print(type(json_data))

# ------------ subdividir el json o fragmentarlo o cortarlo por pedasitos

"""
mis_datos = json.loads(json_data)

datos_php = mis_datos['cursos'][0]
datos_python = mis_datos['cursos'][1]
datos_js = mis_datos['cursos'][2]
datos_csharp = mis_datos['cursos'][3]
datos_node = mis_datos['cursos'][4]

print(f'''Cursos:
1. {datos_node} 
2. {datos_python}
3. {datos_js}''') 

"""


#--------------- nuevos metodos crear json
'''
json_data = json.JSONEncoder().encode({"resultado":500, "status":"ok"})
print(json_data)
print(type(json_data))
print('\n')
'''
#--------------- nuevos metodos crear diccionario o dict
'''
python_dict = json.JSONDecoder().decode(json_data)
print(python_dict)
print(type(python_dict))
'''



