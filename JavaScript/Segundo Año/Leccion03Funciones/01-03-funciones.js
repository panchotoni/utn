miFuncion(5, 3) //Esto es el hosting

function miFuncion(a, b) {
    //console.log("Sumamos: "+ (a + b));
    return a + b; 
}

//LLAMADO A LA FUNCION
miFuncion(1, 2)

let resultado = miFuncion(10, 10)
console.log(resultado);

//FUNCION TIPO EXPRESION

let x = function(a, b) {return a + b};
resultado = x(1, 4)
console.log(resultado);

//FUNCIONES DE TIPO SELF Y INVOCKING

(function(a, b){
    console.log('Ejecutando la funcion: '+ (a + b));
})(9, 6)


console.log(typeof miFuncion);

function miFuncion2(a, b) {
    console.log(arguments.length);
}

miFuncion2(5, 7)

var miFuncionTexto = miFuncion2.toString()
console.log(miFuncionTexto);


//ARROW FUNCTION
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(100, 1)
console.log(resultado);

let sumar = function(a, b){
    return (arguments[0]);
}

resultado = sumar(3)
console.log(resultado);

let respuesta = sumarTodo(5, 4, 13, 10, 9)
console.log(respuesta);

function sumarTodo(){
    let suma = 0
    for(let i = 0; i < arguments.length; i++) {
        suma += arguments[i] //ARGUMENTS ES PARA ARREGLOS
    }
    return suma;
}

//TIPOS PRIMITIVOS 
let z = 10;
function cambiarValor(a){
    a = 20;
}

cambiarValor(z)
console.log(z);


//PASO POR REFERENCIA
const persona = {
    nombre: "Juan",
    apellido: "Lepez"
}

console.log(persona);

function cambiarValorObjeto(p1) {
    p1.nombre = "Ignacio"
    p1.apellido = "Perez"
}

cambiarValorObjeto(persona)
console.log(persona);