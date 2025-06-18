const { db } = require("../../restaurantApi/model/User")

db.users.insertMany([
    {
        name:"John Doe",
        email:"johndoe@example.com",
        address:"123 Main Street"
    },
    {
        name:"Jane Smith",
        email:"janesmith@example.com",
        address:"456 Main Street"
    },
    {
        name:"Mike Johnson",
        email:"mikejohnson@example.com",
        address:"789, Main Street"
    },
    {
        name:"Emily Davis",
        email:"emilydavis@example.com",
        address:"112, Main Street"
    },
    {
        name:"David Wilson",
        email:"davidwilson@example.com",
        address:"342, Main Street"
    }
])

// transaction

db.transaction.insertMany([
    {
        userId:"ObjectId user",
        type:"debit",
        amount:500,
        description:"Grocery Shopping"
    },
    {
        userId:"ObjectId user",
        type:"credit",
        amount:1000,
        description:"Salary Deposit"
    },
    {
        userId:"ObjectId user",
        type:"debit",
        amount:200,
        description:"Online Purchase"
    },
    {
        userId:"ObjectId user",
        type:"credit",
        amount:300,
        description:"Refund"
    },
    {
        userId:"ObjectId user",
        type:"debit",
        amount:50,
        description:"Coffee Shop"
    },
    {
        userId:"ObjectId user",
        type:"credit",
        amount:1500,
        description:"Investment Dividend"
    },
    {
        userId:"ObjectId user",
        type:"debit",
        amount:100,
        description:"Transportation"
    },
    {
        userId:"ObjectId user",
        type:"credit",
        amount:500,
        description:"Bonus"
    },
    {
        userId:"ObjectId user",
        type:"debit",
        amount:300,
        description:"Dinner at Restaurant"
    },
    {
        userId:"ObjectId user",
        type:"credit",s
        amount:2000,
        description:"Loan Repayment"
    }
])