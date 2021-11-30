let operacion = document.getElementById('FunctionForm').value

let inputDisplay = document.getElementById('FunctionForm');

let buttons = Array.from(document.getElementsByClassName('button'));

function check(e) {
  if (e == '√☐') {
    return '√'
    // } else if (  (e+'').includes('x^2') ) {
    //   let value = inputDisplay.value;
    //   let value2 = inputDisplay.value;

    //   value = value.substr(-1);
    //   value = parseInt(value);

    //   // console.log(value2);
    //   return value * value;

  } else {
    return e;
  }
}

buttons.map(button => {

  button.addEventListener('click', e => {

    switch (e.target.innerText) {
      case 'x^2':

        value = inputDisplay.value;
        valueX = value;

        // first, delete the last input to replace it for its elevation

        value = value.substring(0, value.length - 1);
        inputDisplay.value = value;

        inputDisplay.value = valueX + '**'
        break;

      case 'C':

        inputDisplay.value = '';
        document.getElementById('resultado').innerText = ''
        break;
      case '←':
        value = inputDisplay.value;
        value = value.substring(0, value.length - 1);

        inputDisplay.value = value;
        break;
      default:
        inputDisplay.value += check(e.target.innerText);
    }
  })

});