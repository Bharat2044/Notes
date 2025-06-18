//total order quantity of medium size pizzas grouped by pizza name
db.orders.aggregate([
  { $match: { size: "medium" } },
  { $group: { _id: "$medium", totalQuantity: { $sum: "$quantity" } } }
]);

