let x = 10
console.log(x.length);
console.log("Tipos primitivos");
//Creamos un objeto

let persona =  {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad: 28,
    idioma: 'es',

    nombreCompleto: function(params) {
        return this.nombre+" "+this.apellido
    },

    get nombreEdad(){
        return this.nombre + ', edad: ' + this.edad
    },

    get lang(){
        return this.idioma.toUpperCase()
    },

    set lang(language){
        this.idioma = language.toUpperCase()
    }
}


console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.edad);
console.log(persona.email);
console.log(persona);
console.log(persona.nombreCompleto());
console.log("Ejecutando con un objeto");

let persona2 = new Object();//Debe crear un nuevo objeto en memoria
persona2.nombre = "Juan"
persona2.direccion = "Salada 14"
persona2.telefono = "21312314"
console.log(persona2.nombre);
console.log(persona["apellido"]); //Forma de recorrer prop como un arreglo

console.log("Creamos un nuevo objeto");
//FOR IN
for (prop in persona) {
    console.log(prop);
    console.log(persona[prop]);
}
persona.apellida = "Tonidandel"
delete persona.apellida //ACA ELIMINAMOS LA PROPIEDAD APELLIDA
console.log(persona);
console.log("Creamos y eliminamos un error");

//DISTINTA FORMAS DE EIMPRIMIR UN OBJETO
//Numero 1: concatenar cada valor de las propiedades

console.log(persona.nombre+', '+persona.apellido);

//Numero2: A traves del ciclo for in

for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero 3: La funcion Object.values()
let personaArray = Object.values(persona)
console.log(personaArray);

//Numero 4: Utilizaremos el metodo JSON.stringify
let personaString = JSON.stringify(persona)
console.log(personaString);


//USAMOS EL METODO GET Y SET
console.log('Utilizamos el get');
console.log(persona.nombreEdad);

console.log(persona.lang);
persona.lang = 'en'
console.log(persona.lang);

//Constructor 
function Persona3(nombre, apellido, email){
    this.nombre = nombre
    this.apellido = apellido
    this.email = email
    this.nombreCompleto = function(){
        return this.nombre + ' ' + this.apellido
    }
}

let padre = new Persona3('Leo', 'Lopez', 'lopez1@gmail.com')
padre.nombre = 'Luis'
padre.telefono = '123148129341'
console.log(padre);
console.log(padre.nombreCompleto());
let madre = new Persona3('Laura', 'Contrera', 'contreral@gmail.com')
console.log(madre);
console.log(madre.telefono);
console.log(madre.nombreCompleto());

//Difgerentes formas de crear objetos
//Caaso numero 1
let miObjeto = new Object()
//Caso numero 2
let miObjeto2 = {}

//Caso String 1
let miCadena1 = new String('Hola')
//Caso String 2
let miCadena2 = 'Hola' //ESTA ES LA RECOMENDAD

//Caso con numeros 1
let num = new Number(1)
//Caso con numeros 2
let nnum2 = 1; //RECOMENDADA

//Caso boolean 1
let miBolean = new Boolean(false)
//Caso boolean 2
let miBolean2 = false //RECOMENDADA

//Caso arreglos 1
let miArreglo = new Array()
//Caso arreglos 2
let miArreglo2 = [] //RECOMENDADA

//Caso function 1
let miFuncion = new function(){}
//Caso function 2
let miFuncion2 = function(){} //RECOMENDADA

//USO DE PROTOTYPE
Persona3.prototype.telefono = '123123123123';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '123123'
console.log(madre.telefono);

//USO DE CALL SE PASAN LOS ARGUMENTOS CUANDO SE USA EL CALL
let persona4 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto2: function(titulo, telefono) {
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono
        //return this.nombre+' '+this.apellido
    }
}

let persona5 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona4.nombreCompleto2('Dr', '13123'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing', '6878786'));

//METODO APPLY SE PASAN LOS ARGUMENTOS CON UN ARREGLO
let arreglo = ['Abogado', '43643656']
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));