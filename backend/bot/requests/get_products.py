from products.models import Product

async def get_product(category_id: str = None):
    if category_id:
        queryset = Product.objects.filter(category_id=category_id)
    else:
        queryset = Product.objects.all()
    products = [product async for product in queryset]
    return products