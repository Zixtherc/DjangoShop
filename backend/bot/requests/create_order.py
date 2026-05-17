from order.models import Order, OrderItem
from products.models import Product

async def create_order(products_id: list, user, quantity: int, unique_code: str):
    order = await Order.objects.acreate(
        user=user,
        status='pending',
        payment_code=unique_code
    )
    for product_id in products_id:
        try:
            product = await Product.objects.aget(id=product_id)
        except Product.DoesNotExist:
            continue
        await OrderItem.objects.acreate(
            order=order,
            product=product,
            quantity=quantity
        )
    return order