let account = { accNo: 12345, accBal: 5000 }; // Not -encapsulated

console.log(account.accNo, account.accBal); //Read
account.accBal = -50000; // write
console.log(account.accNo, account.accBal); //Read


function openAccount(initialBal) {
    console.log(`Your account is opened with ${initialBal}`);

    let accNo = 12345;
    let accBal = initialBal;

    return { // Exposing functions, not the data
        displayInfo: function () {
            console.log(accNo, accBal)
        },
        deposit: function (amt) {
            if(amt<0){
                console.log('Boss!, Idont want your money, Plz go back ')
            }else{
                accBal = accBal + amt;
                console.log(`You deposited ${amt} , current bal is ${accBal}`)
            }
        }
    }
}
let encapsulatedAccount = openAccount(3000);
console.log(encapsulatedAccount.accBal, encapsulatedAccount.accNo);
encapsulatedAccount.displayInfo();
encapsulatedAccount.deposit(-4000);
encapsulatedAccount.deposit(4000);
encapsulatedAccount.displayInfo();
console.dir(encapsulatedAccount.deposit)