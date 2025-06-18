// print all the cities
db.cities.aggregate([
    { $match: { } }
]);

// print the cities from from North America continet
db.cities.aggregate([
    { $match: { "continent": "North America" } }
])

// print the cities from from NorthAmerica/Asia continet
db.cities.aggregate([
    { $match: { "continent": { $in: ["North America", "Asia"] } } }
])

// sort the cities by population(desc)
db.cities.aggregate([
    { $sort: { "population": -1 } }
])


db.cities.aggregate([
    {
        $group: {
            "_id": {
                "continent": "$continent",
                "country": "$country"
            }
        }
    }
])

db.cities.aggregate([
    {
        $group: {
            "_id": {
                "continent": "$continent",
                "country": "$country"
            },
            "highest_population": { $max: "$population" },
            "first_city": { $first: "$name" },
            "cities_in_top_20": { $sum: 1 }
        }
    }
])

db.cities.aggregate([
    {
        $match: {
            "continent": { $in: ["North America", "Asia"] }
        }
    },
    {
        $sort: { "population": -1 }
    },
    {
        $group: {
            "_id": {
                "continent": "$continent",
                "country": "$country"
            },
            "first_city": { $first: "$name" },
            "highest_population": { $max: "$population" }
        }
    }
])