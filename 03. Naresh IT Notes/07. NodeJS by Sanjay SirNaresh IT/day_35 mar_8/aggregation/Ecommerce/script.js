1. Get the avergae price of products in "Electronics" category.

   db.products.aggregate([
       {
           $match:{category:"Electronics"}
       },
       {
           $group:{
               _id:null,
               avgPrice:{$avg:"$price"},
           }
       }
   ])


> [ { _id: null, avgPrice: 630 } ]

2. Count total number of orders
db.order.aggregate([
    {
        $count:"totalOrders"
    }
])

> [ { totalOrders: 5 } ]

3. Get the top 3 customers with the highest total order amount
db.order.aggregate([
    {
        $group:{
            _id:"$customerId",
            totalAmount:{$sum:"$totalAmount"}
        }
    },
    {
        $sort:{totalAmount: 1}
    },
    {
        $limit:3
    }
])

4. calculate the averge rating of each products

db.products.aggregate([
    {
        $project:{
            name:1,
            avgRating:{$avg:"$rating"}
        }
    }
])

5. Get the total revenue for each category

db.order.aggregate([
    {
        $lookup:{
            from:"products",
            localField:"products.productId",
            foreignField:"_id",
            as:"productDetails"
        }
    },
    {
        $unwind:"$productDetails"
    },
    {
        $group:{
            _id:"$productDetails.category",
            totalRevenue:{
                $sum:{$multiply:["$productDetails.price","$productDetails.quantity"]}
            }
        }
    }
])
