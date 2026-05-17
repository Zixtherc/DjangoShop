from products.models import Product

async def get_product(category_id: str = None, product_id: int = None):
    if product_id:
        try:
            return await Product.objects.aget(id=product_id)
        except Product.DoesNotExist:
            return None
    if category_id:
        queryset = Product.objects.filter(category_id=category_id)
    else:
        queryset = Product.objects.all()
    products = [product async for product in queryset]
    return products