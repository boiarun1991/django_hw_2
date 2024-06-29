from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}


def get_recipe(request, dish):
    if request.GET.get('servings'):
        servings = int(request.GET.get('servings'))
        if servings < 0:
            servings *= -1
        context = {'recipe': DATA.get(dish)}
        for ing, amount in context['recipe'].items():
            context['recipe'][ing] = amount * servings
        return render(request, 'calculator/index.html', context)

    context = {'recipe': DATA.get(dish)}
    return render(request, 'calculator/index.html', context)
