from order.models import Order, OrderItem
from products.models import Product

async def create_order(product_id: str, user: object, time: str):
    queryset = Order.objects.create(user= user, created_at=time)



# from order.models import Order

# async def get_orders(user_id: int):
#     queryset = Order.objects.filter(user_id=user_id).values('id', 'status')
#     orders = []
#     async for order in queryset:
#         orders.append(order)
#     return orders
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # status = models.CharField(max_length=20,default='new')