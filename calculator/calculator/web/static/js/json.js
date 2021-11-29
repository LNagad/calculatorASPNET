// ----------- reading the json
function readJson() {
    const data = require('./data.json')

    let resultado = data.resultado
    console.log(resultado)
    
    // return resultado
}

// -------------- writing and creating a json file
function writeJson(operacion) {
    const fs = require('fs')

    const calculateJson = {
        calculo: '150+150',
        resultado: 300
    }
    // ---------------- convert dict to json

    // const jsonString = JSON.stringify(newObject);
    // console.log(jsonString)

    fs.writeFile('./data2.json', JSON.stringify(calculateJson, null, 2), err => {
        if (err) {
            console.log(err);
        } else {
            console.log('File successfully written')
        }
    })
}

readJson()