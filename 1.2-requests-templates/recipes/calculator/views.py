from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}

def start(request):
    template_name = 'calculator/start.html'
    return render(request, template_name)


def recipe_list(request):
    template_name = 'calculator/recipe_list.html'
    context = DATA
    return render(request, template_name, {'context': context})


def recipe(request, recipe_name):
    template_name = 'calculator/recipe.html'
    try:
        context = {
            'recipe': DATA[recipe_name]

            }
    except: KeyError
    context = {
        'recipe': ''

    }
    return render(request, template_name, context)


