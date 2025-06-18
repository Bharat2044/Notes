let user = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}
/* console.log(user.address.city)
console.log(user.address.zipcode)
console.log(user.address.street) */

let {city,zipcode,street,geo:{lat,lng}} = user.address;
console.log(city,zipcode,street,lat,lng)

