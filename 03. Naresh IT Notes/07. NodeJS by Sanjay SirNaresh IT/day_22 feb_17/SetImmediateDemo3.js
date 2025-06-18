const baz = () => console.log('baz');
const foo = () => console.log("foo");
const zoo = () => console.log("zoo");

const start = () => {
    console.log("Function starts");
    setImmediate(baz);
    new Promise((resolve, reject) => {
        resolve("bar");
    }).then((resolve) => {
        console.log(resolve);
        process.nextTick(zoo);
    });
    process.nextTick(foo);
    console.log("Function ends")
};
start();