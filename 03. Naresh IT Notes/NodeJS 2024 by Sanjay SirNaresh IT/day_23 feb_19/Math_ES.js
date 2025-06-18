export default function add(a, b) {   // default export
    return a + b;
}
export function sub(a, b) {       // named export
    return a - b;
}

export let a = 10;


// 1. A module cannot have multiple default exports
// 2. varaibales cann't be exported using default export
// 3. 