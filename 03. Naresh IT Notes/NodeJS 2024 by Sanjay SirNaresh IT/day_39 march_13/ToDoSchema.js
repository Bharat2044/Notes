const { GraphQLSchema, GraphQLObjectType, GraphQLID, GraphQLString, GraphQLBoolean, GraphQLList } = require("graphql");

let allTodos = [
    { id: 1, title: 'ToDo-1', completed: true },
    { id: 2, title: 'ToDo-2', completed: false },
    { id: 3, title: 'ToDo-3', completed: true },
]

let TodoType = new GraphQLObjectType({
    name: 'todo',
    fields: function () {
        return {
            id: { type: GraphQLID },
            title: { type: GraphQLString },
            completed: { type: GraphQLBoolean },
        }
    }
});
let queryType = new GraphQLObjectType({
    name: 'Query',
    fields: function () {
        return {
            todos: {
                type: new GraphQLList(TodoType),
                resolve: function () {
                    return allTodos;
                }
            }
        }
    }
})

module.exports = new GraphQLSchema({ query: queryType })