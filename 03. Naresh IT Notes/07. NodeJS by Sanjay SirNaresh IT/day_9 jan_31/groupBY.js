let employees = [
    { eId: 101, name: 'sanjay', sal: 5000, gender: 'male' },
    { eId: 104, name: 'geeta', sal: 8000, gender: 'female' },
    { eId: 103, name: 'sameer', sal: 7000, gender: 'male' },
    { eId: 102, name: 'sita', sal: 9000, gender: 'female' },
    { eId: 105, name: 'deepak', sal: 8000, gender: 'male' },
];
function groupBy( arr , field ){
    let result = {};

    for(let emp of employees){
        let value = emp[field]; // value = 5000

        if( result[value] ){
            result[value].push(emp);
        }else{
            result[value] = [];
            result[value].push(emp);
        }
    }
    return result;
}
let res = groupBy( employees , 'gender' );
console.log(res)


/*  expected output = {
    5000 : [ {}],
    7000 : [ {}],
    8000 : [ {},{}],
    9000 : [ {}],
} */