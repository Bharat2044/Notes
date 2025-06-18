
1. Calculate the total debit and credit amount for each user
    db.transaction.aggregate([
        {
            $group:{
                _id:"$userId",
                totalDebit:{
                    $sum:{$cond:[{$eq:["$type","debit"]}, "$amount",0]}
                },
                totalCredit:{
                    $sum:{$cond:[{$eq:["$type","credit"]}, "$amount",0]}
                }
            }
        }
    ])

2. Find the user with the highest total credit amount
    db.transaction.aggregate([
        {
            $group:{
                _id:"$userId",
                totalCredit:{
                    $sum:{$cond:[{$eq:["$type","credit"]}, "$amount",0]}
                }
            }
        },
        {
            $sort:{totalCredit:-1}
        },
        {
            $limit:1
        }
    ])

3. Calculate the avg transaction amount for each month
db.transaction.aggregate([
    {
        $project:{
            _id:{$month:"$timestamp"},
            avgAmount:{$avg:"$amount"}
        }
    }
])
