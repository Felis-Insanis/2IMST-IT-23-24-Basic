// oppgave 6
let sizeW = parseInt(Math.random()*6 + 3);
let sizeH = parseInt(Math.random()*6 + 3);

console.log(sizeW, sizeH)
//generate map
function mapGen(width, height) {
    const newMatrix = [];
    for (let h = 0; h < height+1; h++) {
        newMatrix.push([]);
        for (let w = 0; w < width+1; w++) {
            newMatrix[h].push([h, w]);
        }
    }
    //generate location
    let treasureX = parseInt(Math.random()*width);
    let treasureY = parseInt(Math.random()*height);
    console.log(newMatrix)
    console.log(treasureX, treasureY)
    newMatrix[treasureY][treasureX].push('X');
    return newMatrix
}
const treasureMap = mapGen(sizeW, sizeH);
console.log(treasureMap)

//find treasure
function findTreasure(map) {
    for (const height of map) {
        for (const width of height) {
            if (width.includes('X')) {
                console.log(`Treasure found at (${width[0]}, ${width[1]})`)
            }
        }
    }
}
findTreasure(treasureMap)

// oppgave 4
function addStudent() {
    const list = document.getElementById('students');
    const name = document.getElementById('nameInput').value;
    const age = document.getElementById('ageInput').value;
    const route = document.getElementById('classInput').value;
    const success = document.getElementById('success');

    console.log(list)
    
    if (list.innerHTML.includes(name) == false) {
        const li = document.createElement('li');
        li.appendChild(document.createTextNode(`${name}:\nAlder: ${age} år\nKlasse: ${route}`));
        list.appendChild(li);
        success.textContent = 'En elev har blitt lagt til!';
    } else if (list.innerHTML.includes(name) == true) {
        success.textContent = 'Feil kode 666:\nElev allerede eksisterer.';
    }
    console.log(list)
}

// oppgave 7
const names = ['Lucifer', 'Belzebub', 'Satan', 'Abaddon', 'Mammon', 'Belgephor', 'Asmodeus', 'Faust', 'Erik', 'Dante', 'Vergil', 'Nero', 'Nyancat']


function getInitiale(name) {
    const initiale = name.substr(0, 1)
    return initiale
}

const initialer = names.map(getInitiale)

console.log(initialer)