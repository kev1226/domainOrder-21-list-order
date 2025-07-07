from fastapi import Request
from app.auth.jwt_utils import decode_token
from app.repository.order_repository import find_orders_by_email


async def resolve_list_orders_by_user(_, info):
    request: Request = info.context["request"]
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user_data = decode_token(token)

    if not user_data:
        raise Exception("Token inválido")

    email = user_data["email"]
    orders = await find_orders_by_email(email)

    for order in orders:
        order["id"] = str(order["_id"])

    return orders
