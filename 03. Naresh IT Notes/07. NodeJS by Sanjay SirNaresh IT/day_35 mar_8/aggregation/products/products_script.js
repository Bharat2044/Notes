// print the count of each category
db.products.aggregate([
    {"$group" : {_id:"$category",count:{$sum:1}}}
])

// Print name,price for the products of category-electronics
db.products.aggregate([
    {$match:{category:'Electronics'}},
    {$project:{name:1,price:1}}
])
  

// Find name , price of  Top 2 'electronics' products by price
db.products.aggregate([
    {$match:{category:'Electronics'}},
    {$sort:{"price":-1}},
    {$project:{name:1,price:1}},
    {$limit:2}
]);


  