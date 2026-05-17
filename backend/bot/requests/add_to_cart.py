from cart.models import CartItem
from user.models import User

async def add_to_cart(product_id: int, user_id: int, quantity: int = 1):
    user = await User.objects.aget(id=user_id)

    cart_item = await CartItem.objects.filter(user=user, product_id=product_id).afirst()

    if cart_item:
        cart_item.quantity += quantity
        await cart_item.asave()
        return cart_item

    cart = await CartItem.objects.acreate(user=user, product_id=product_id, quantity=quantity,)
    return cart