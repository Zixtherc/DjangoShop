from products.models import Product

async def get_product(filter: str = None):
    queryset = Product.objects.all()
    products = []
    async for product in queryset:
        products.append(product)
    return products