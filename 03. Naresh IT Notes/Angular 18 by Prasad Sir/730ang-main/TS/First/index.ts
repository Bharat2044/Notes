let p: string = "hdfgh";
// TS is used for static data typing
console.log(p, typeof p)
    // TS provides static data typing
    // number,boolean,string,undefined,null
    // TS can understand datatype by two ways
    //1. type inference , 2. type annotation
    // Type inference means it will guess the datatype by value
// Type annotation means we specify datatypes explicitly
let a: number = 25;
console.log(typeof a)
let b: boolean = true;
let c: undefined = undefined;
let d: null = null;
// union - what if you want to give multiple datatypes to single variable
let e: number | string = "prasad"
// declare a variable which accepts string or boolean or number
let f: number | string | boolean = true;
// arrays
let g: number[] = [ 25, 78, -2, 0 ];
let h: (number | string)[] = [ 55, "raj", 91 ];
// what if i want each element different type -- tuple
let i: [ number, string, number ] = [ 25, "dghgsd", 78 ];
// any -- any will remove ts static typing
let j: any = 25;

// enum
// enum is used for constants
enum k{
    sunday,
    monday,
    tuesday,
    wednesday,
    thursday,
    friday,
    saturday,
}
console.log(k.sunday) //0
interface obj1{
    name: string,
    mob: number,
    email?:string
}
// interfaces are used for object definitions
let obj:obj1 = {
    name: "prasad",
    email:'a@a.com',
    mob:232323
}

// create an object which can contain 
// username, age and salary
interface myObj{
    username: string,
    age: number,
    salary?:number
}
interface myObj2 extends myObj{
    email:string
}
let obj2: myObj2 = {
     username: "fghj",
    age: 8888,
   email:'a@a.com'
}
class fun implements myObj2{
    username!: string;
    age!: number;
    email!: string;
}
let y= new fun()

//functions
// function sum(a:number, b:number):never
// {
//     throw new Error("this is error")
// }
// sum(2,3)

// type alias
type prasad = number | string | boolean;
function add(a:number,b:number):number
{
    return a + b;
}








