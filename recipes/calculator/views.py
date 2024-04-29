from django.shortcuts import render, reverse
from django.http import HttpResponse

from calculator.forms import MyForm

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
    # можете добавить свои рецепты ;)
}

def home_view(request):
    dishes = {}
    for key in DATA.keys():
        # dishes[key] = f"http://127.0.0.1:8000/recipe/{key}"
        dishes[key] = f"http://127.0.0.1:8000/recipe/?dish={key}&servings=1"
        
    context = {'dishes': dishes}
    print(f'{context=}')
    
    return render(request, 'calculator/home.html', context)
    
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def recipe(request):
    dish = request.GET.get("dish")
    servings = int(request.GET.get("servings", 1))
    recipe_for_out = {dish: DATA[dish]}
    print(f'2{recipe_for_out=}')
    
    context = {'recipe': {}}
    for key, value in recipe_for_out[dish].items():
        context['recipe'][key] = value * servings
    print(f'{context=}')
    
    return render(request, 'calculator/index.html', context)
    