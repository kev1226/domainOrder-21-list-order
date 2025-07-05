from ariadne import QueryType, make_executable_schema
from app.graphql.resolver import resolve_list_orders_by_user

type_defs = """
    type User {
        email: String!
    }

    type ProductLine {
        product_id: String!
        name: String!
        price_unit: Float!
        quantity: Int!
        line: String!
        subtotal: Float!
    }

    type Total {
        amount: Float!
        currency: String!
        label: String!
    }

    type Order {
        id: ID!
        user: User!
        products: [ProductLine!]!
        total: Total!
        status: String!
    }

    type Query {
        listOrdersByUser: [Order!]!
    }
"""

query = QueryType()
query.set_field("listOrdersByUser", resolve_list_orders_by_user)
schema = make_executable_schema(type_defs, [query])
