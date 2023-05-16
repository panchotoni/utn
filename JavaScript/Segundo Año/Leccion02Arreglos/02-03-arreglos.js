
//Creacion de Array o Arreglos
//SINTAXIS VIEJA
let autos = new Array('Ferrari', 'Renault', 'BMW' )
//SINTAXIS NUEVA 
let autos1 = ['Porsche', 'Ford', 'Lambo']
console.log(autos1);

//Recorremos los elementos de un arreglo

console.log(autos[0]);
console.log(autos[2]);

for(let i = 0; i < autos.length; i++) {
    let contador= i+1;
    console.log(contador+": "+autos[i]);
}


//Modificamos los elementos del arreglo
autos[1] = 'Volvo'
console.log(autos[1]);

//Agregamos nuevos valores al arreglo
autos.push('Audi')
console.log(autos);

//Otras forma de agregar
autos[autos.length] = 'Porsche'
console.log(autos);

autos[6] = 'Renault' //En este caso hay que tener cuidado xq podemos dejar espacios vacios
console.log(autos);


//Como preguntar si lo que estamos usando es un Array
console.log(Array.isArray(autos))

console.log(autos instanceof Array);
