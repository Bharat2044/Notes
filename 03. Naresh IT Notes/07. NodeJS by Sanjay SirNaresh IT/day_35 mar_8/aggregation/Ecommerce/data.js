db.products.insertMany([
    {
        name:"SmartPhone",
        category:"Electronics",
        price:850,
        quantity:10,
        rating:[4,5,4,3,5]
    },
    {
        name:"Laptop",
        category:"Electronics",
        price:1000,
        quantity:5,
        rating:[5,5,4,5,4]
    },
    {
        name:"Headphones",
        category:"Electronics",
        price:100,
        quantity:20,
        rating:[4,3,4,4,5]
    },
    {
        name:"Shirt",
        category:"Clothing",
        price:190,
        quantity:50,
        rating:[5,4,5,4,3]
    },
    {
        name:"Running Shoes",
        category:"Footwear",
        price:80,
        quantity:15,
        rating:[4,4,3,5,5]
    },
    {
        name:"Watch",
        category:"Accessories",
        price:200,
        quantity:8,
        rating:[5,5,5,4,4]
    },
    {
        name:"Camera",
        category:"Electronics",
        price:800,
        quantity:3,
        rating:[4,4,3,5,5]
    },
    {
        name:"BookShelf",
        category:"Furniture",
        price:150,
        quantity:10,
        rating:[4,4,5,5,3]
    },
    {
        name:"Gaming Console",
        category:"Electronics",
        price:400,
        quantity:6,
        rating:[5,5,4,4,3]
    }
])

//////////
db.customers.insertMany([
    {
        name:"John Doe",
        email:"johndoe@example.com",
        address:"123, Main Street"
    },
    {
        name:"Jane Samith",
        email:"janesamith@example.com",
        address:"456, Main Street"
    },
    ,{
        name:"Mike Johnson",
        email:"mikejohnson@example.com",
        address:"789, Main Street"
    }
])

///orders
db.order.insertMany([
    {
        customerId:"",
        products:[
            { productId:ObjectId("product_id"),quantity:2},
            { productId:ObjectId("product_id"),quantity:1}
        ],
        totalAmount:1000
    },
    {
        customerId:"",
        products:[
            { productId:ObjectId("product_id"),quantity:3},
            { productId:ObjectId("product_id"),quantity:2}
        ],
        totalAmount:210
    },
    {
        customerId:"",
        products:[
            { productId:ObjectId("product_id"),quantity:1},
            { productId:ObjectId("product_id"),quantity:1}
        ],
        totalAmount:200
    },
    {
        customerId:"",
        products:[
            { productId:ObjectId("product_id"),quantity:1}
        ],
        totalAmount:280
    },
    {
        customerId:"",
        products:[
            { productId:ObjectId("product_id"),quantity:4},
        ],
        totalAmount:200
    }
])

////////////////////////////
db.products.insertMany([
    {
        _id:ObjectId("658b9c4ac2b85f2b2d837a36"),
        name:"SmartPhone",
        category:"Electronics",
        price:850,
        quantity:10,
        rating:[4,5,4,3,5]
    },
    {
        _id:ObjectId("658b9c4ac2b85f2b2d837a37"),
        name:"Laptop",
        category:"Electronics",
        price:1000,
        quantity:5,
        rating:[5,5,4,5,4]
    },
    {
        _id:ObjectId("658b9c4ac2b85f2b2d837a38"),
        name:"Headphones",
        category:"Electronics",
        price:100,
        quantity:20,
        rating:[4,3,4,4,5]
    },
    {
        _id:ObjectId("658b9c66c2b85f2b2d837a39"),
        name:"Shirt",
        category:"Clothing",
        price:190,
        quantity:50,
        rating:[5,4,5,4,3]
    },
    {
        _id:ObjectId("658b9c66c2b85f2b2d837a3a"),
        name:"Running Shoes",
        category:"Footwear",
        price:80,
        quantity:15,
        rating:[4,4,3,5,5]
    },
    {
        _id:ObjectId("658b9c66c2b85f2b2d837a3b"),
        name:"Watch",
        category:"Accessories",
        price:200,
        quantity:8,
        rating:[5,5,5,4,4]
    },
    {
        _id:ObjectId("658b9c66c2b85f2b2d837a3c"),
        name:"Camera",
        category:"Electronics",
        price:800,
        quantity:3,
        rating:[4,4,3,5,5]
    },
    {
        _id:ObjectId("658b9c66c2b85f2b2d837a3d"),
        name:"BookShelf",
        category:"Furniture",
        price:150,
        quantity:10,
        rating:[4,4,5,5,3]
    },
    {
        _id:ObjectId("658b9c66c2b85f2b2d837a3e"),
        name:"Gaming Console",
        category:"Electronics",
        price:400,
        quantity:6,
        rating:[5,5,4,4,3]
    }
])

//////////
db.customers.insertMany([
    {
        _id:ObjectId("658b9ccbc2b85f2b2d837a3f"),
        name:"John Doe",
        email:"johndoe@example.com",
        address:"123, Main Street"
    },
    {
        _id:ObjectId("658b9ccbc2b85f2b2d837a40"),
        name:"Jane Samith",
        email:"janesamith@example.com",
        address:"456, Main Street"
    },
    {
        _id:ObjectId("658b9ccbc2b85f2b2d837a41"),
        name:"Mike Johnson",
        email:"mikejohnson@example.com",
        address:"789, Main Street"
    }
])

///orders
db.order.insertMany([
    {
        customerId:ObjectId("658b9ccbc2b85f2b2d837a3f"),
        products:[
            { productId:ObjectId("658b9c4ac2b85f2b2d837a36"),quantity:2},
            { productId:ObjectId("658b9c66c2b85f2b2d837a3a"),quantity:1}
        ],
        totalAmount:1000
    },
    {
        customerId:ObjectId("658b9ccbc2b85f2b2d837a40"),
        products:[
            { productId:ObjectId("658b9c4ac2b85f2b2d837a38"),quantity:3},
            { productId:ObjectId("658b9c66c2b85f2b2d837a39"),quantity:2}
        ],
        totalAmount:210
    },
    {
        customerId:ObjectId("658b9ccbc2b85f2b2d837a3f"),
        products:[
            { productId:ObjectId("658b9c66c2b85f2b2d837a3d"),quantity:1},
            { productId:ObjectId("658b9c66c2b85f2b2d837a3c"),quantity:1}
        ],
        totalAmount:200
    },
    {
        customerId: ObjectId("658b9ccbc2b85f2b2d837a41"),
        products:[
            { productId:ObjectId("658b9c4ac2b85f2b2d837a36"),quantity:1}
        ],
        totalAmount:280
    },
    {
        customerId: ObjectId("658b9ccbc2b85f2b2d837a41"),
        products:[
            { productId:ObjectId("658b9c66c2b85f2b2d837a3c"),quantity:4},
            { productId:ObjectId("658b9c4ac2b85f2b2d837a38"),quantity:1}
        ],
        totalAmount:200
    }
])
