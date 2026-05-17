from cart.models import CartItem
from products.models import Product

async def add_to_cart(product_id: int, user_id: int, quantity: int = 1):
    cart_item = await CartItem.objects.filter(user_id = user_id, product_id = product_id).afirst()

    if cart_item:
        cart_item.quantity += quantity
        await cart_item.asave()
        return cart_item

    cart = await CartItem.objects.acreate(
        user=user_id,
        product_id=product_id,
        quantity=quantity,
    )
    return cart
