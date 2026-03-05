from order.models import Order, OrderItem
from products.models import Product

async def create_order(products_id: list, user: object, quantity: int):
    order = Order.objects.create(user=user)
    for product_id in products_id:
        
        try:
            product = Product.objects.get(id = product_id)
        except Product.DoesNotExist:
            continue
        order_item = OrderItem.objects.create(order=order, product=product,quantity=quantity)
    return order