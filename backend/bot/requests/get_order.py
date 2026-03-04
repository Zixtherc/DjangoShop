from order.models import Order

async def get_orders(user_id: int):
    queryset = Order.objects.filter(user_id=user_id).values('id', 'status')
    orders = []
    async for order in queryset:
        orders.append(order)
    return orders