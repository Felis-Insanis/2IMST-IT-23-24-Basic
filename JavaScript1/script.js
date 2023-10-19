//oppgave 1
let welcome = "Hello World!";
console.log(welcome);

//oppgave 2
let navn = "Attila";
console.log(`Halo, ${navn}!`);

//oppgave 3
let radius = 20;
let pi = 3.14;

let omkrets = 2 * radius * pi;

console.log(`For radius ${radius} er omkretsen ${omkrets}`);

export const data = {
    firstName: 'Attila',
    lastName: 'Csonka'
};

console.log(`Halo, ${data.firstName} ${data.lastName}!`);

//4.2
data.age = 17;
data.birthDay = "30. Oktober";
data.is18 = false;

let loggable = JSON.stringify(data);
console.log({loggable});

//oppgave 5
//a
let nameLength = navn.length;
console.log(`Halo, ${navn}! Ditt navn er ${nameLength} bokstaver.`);

//b
let fullName = data.firstName + '' + data.lastName;
nameLength = fullName.length;

console.log(`Halo, ${fullName}! Navnet ditt er ${nameLength} bokstaver.`);

// oppgave 6
console.log(`Hei, jeg heter ${fullName}!`)

//oppgave 7
let template = `Hei, mitt navn er ${data.firstName + ' ' + data.lastName}. Jeg er ${data.age} år gammel og har bursdag ${data.birthDay}.`;
console.log(template);

// oppgave 9
let [x, y] = prompt('Gi meg to tall.').split(' ');

let a = parseFloat(x);
let b = parseFloat(y);

if (a < b) {
    window.alert(`${a} < ${b}`)
} else if (a == b) {
    window.alert(`${a} < ${b}`)
} else if (a > b) {
    window.alert(`${a} < ${b}`)
} else {
    window.alert('You done f\'d up, man.')
}

// oppgave 10
window.alert('Halt! This is an age inspection!')
let alder = parseInt(prompt('Produce thy age!'))

window.alert('...')

if (alder >= 18) {
    window.alert('The Lady hath allowed thee to vote! You may continue.')
} else {
    window.alert('The Lady hath not allowed thee to vote! Be gone!')
    window.close()
}