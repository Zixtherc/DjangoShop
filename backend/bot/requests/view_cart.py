from cart.models import CartItem

async def view_cart(user_id: int):
    queryset = CartItem.objects.filter(user_id= user_id).select_related('product')

    cart_items = [item async for item in queryset]
    return cart_items