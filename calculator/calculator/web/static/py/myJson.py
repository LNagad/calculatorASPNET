import json, requests

def sendingCalc(data):
    s = json.dumps(data)

    with open('../js/data2.json', 'w') as f:
        f.write(s)


f = open('../js/data2.json', 'r')
a = f.read()
myFile = json.loads(a)

print(myFile)
print(myFile['operacion'])

json_str = '{"nombre":"Maycol","edad":18,"pais":"rd","telefono":809456878}'

jsonCalculated = {
    'operacion': '50+50',
    'resultado': 100
}

