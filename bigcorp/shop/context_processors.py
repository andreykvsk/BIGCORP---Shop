from .models import Category


def categories(request):
    cats = Category.objects.filter(parent=None)
    return {'categories': cats}
