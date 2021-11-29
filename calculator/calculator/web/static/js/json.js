
 
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
        calculo: operacion,
        resultado: ''
    }
    // ---------------- convert dict to json

    fs.writeFile('./data2.json', JSON.stringify(calculateJson, null, 2), err => {
        if (err) {
            console.log(err);
        } else {
            console.log('File successfully written')
        }
    })
}

function hacerOperacion(){
    const operacion = document.getElementById('FunctionForm').value
    // console.log(typeof(operacion))
    // console.log(operacion)

    writeJson(operacion)
}





