

const myInput = document.getElementById("myInput");
const hasTrafikGrunn = document.getElementById("hasTrafikGrunn");
const output = document.getElementById("output");

// oppgave 0
let inputNumber = 0
myInput.value = inputNumber;

let inputBool = false
hasTrafikGrunn.value = inputBool;

function subMit(){
    let age = parseInt(myInput.value);
    if (age < 16) {
        output.innerHTML = "Du er ikke gammel nok.";
    } else if (16 <= age && age < 25 && hasTrafikGrunn.checked == false) {
        output.innerHTML = "Du må fullføre trafikalt grunnkurs først.";
    } else {
        output.innerHTML = "Du kan øvelseskjøre.";
    }
}
// oppgave 1
function loopless(){
    console.log('1')
    console.log('2')
    console.log('3')
    console.log('4')
    console.log('5')
    console.log('6')
    console.log('7')
    console.log('8')
    console.log('9')
    console.log('10')
}

function forLoop(){
    for (let i = 1; i <= 10; i++) {
        console.log(i)
    }
}

function whileLoop(){
    let lapNr = 1;
    while (lapNr <= 10) {
        console.log(lapNr)
        lapNr += 1
    }
}
// oppgave 3
function revealPerson(){
    console.log(data.firstName)
}
// oppgave 4

// oppgave 5

// oppgave 6

// oppgave 7
