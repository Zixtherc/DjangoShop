from products.models import Category 

async def get_categories():
    queryset = Category.objects.all()
    categories = []
    async for category in queryset:
        categories.append(category)
    return categories