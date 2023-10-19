const unit_to_symbol = {
    "kelvin": "K",
    "celsius": "°C",
};

const to_celsius = {
}

// oppgave 5-7 + Kelvin
function unitChange() {
    const unit = document.getElementById('enhet').value;
    const displayUnit = document.getElementById('unitFrom');
    const resultBox = document.getElementById('output');
    const inputValue = parseFloat(document.getElementById('inputValue').value);
    switch(unit) { // changes the unit of the input and the output to the correct ones.
        case 'celsiusToKelvin':
            console.log('1')
            displayUnit.innerHTML = '°C'
            resultBox.innerHTML = `${inputValue + 273.15} K`;
            break;
        case 'kelvinToCelsius':
            displayUnit.innerHTML = 'K'
            resultBox.innerHTML = `${inputValue - 273.15} °C`;
            console.log('2')
            break;
        case 'fahrenheitToKelvin':
            displayUnit.innerHTML = '°F'
            resultBox.innerHTML = `${(inputValue - 32) / 1.8 + 273.15} K`;
            console.log('3')
            break;
        case 'fahrenheitToCelsius':
            displayUnit.innerHTML = '°F'
            resultBox.innerHTML = `${(inputValue - 32) / 1.8} °C`;
            console.log('4')
            break;
        case 'celsiusToFahrenheit':
            displayUnit.innerHTML = '°C'
            resultBox.innerHTML = `${inputValue * 1.8 + 32} °F`;
            console.log('5')
            break;
        case 'kelvinToFahrenheit':
            displayUnit.innerHTML = 'K'
            resultBox.innerHTML = `${(inputValue - 273.15) * 1.8 + 32} °F`;
            console.log('6')
            break;
        default:
            console.log('How did you select this!?')
    }
}
unitChange()

// oppgave 8/utfordring
function colorChange(){
    const red = document.getElementById('red').value;
    const green = document.getElementById('green').value;
    const blue = document.getElementById('blue').value;
    console.log(red)
    console.log(green)
    console.log(blue)
    console.log(`rgb(${red}, ${green}, ${blue})`);
    document.body.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`
}
colorChange()

function colorSet(color){
    document.body.style.backgroundColor = color
    switch (color) {
        case 'red':
            document.getElementById('red').value = 255;
            document.getElementById('green').value = 0;
            document.getElementById('blue').value = 0;
            break;
        case 'green':
            document.getElementById('red').value = 0;
            document.getElementById('green').value = 255;
            document.getElementById('blue').value = 0;
            break;
        case 'blue':
            document.getElementById('red').value = 0;
            document.getElementById('green').value = 0;
            document.getElementById('blue').value = 255;
            break;
    }
}