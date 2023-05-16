//Ciclo WHILE
let contador = 0;
while(contador < 3) {
    console.log(contador);
    contador++;
}
console.log('Fin del ciclo WHILE');

//Ciclo DO WHILE
let conteo = 0;

do {
    console.log(conteo);
    conteo++
} while (conteo < 3);
console.log('Fin del ciclo DO WHILE');

//Ciclo FOR
for (let i = 0; i < 3; i++) {
    console.log(i);    
}
console.log('Fin del ciclo FOR');

//Palabra reservada BRAKE
for (let i = 0; i <= 10; i++) {
    if(i % 2 == 0) {
        console.log(i);
    } else {
        break;
    }
}
console.log('Termina el ciclo FOR');

//Palabra CONTINUE
for (let i = 0; i <= 10; i++) {
    if(i % 2 !== 0) {
        continue;
    } else {
        console.log(i);
    }  
}
console.log('Termina el ciclo FOR');