from django.shortcuts import render, redirect
import requests
from api_key import key

# Create your views here.
def index(request):
    app_id = key['app_id']
    api_keys = key['api_key']
    url_root = 'http://api.yummly.com/v1/api/recipes?_app_id='
    url_middle = '&_app_key='
    food_search = 'garlic'
    url = str(url_root) + str(app_id) + str(url_middle) + str(api_keys) + "&q=" + str(food_search)
    print("Url: {}".format(url))
    response = requests.get(url)
    recipes = response.json()
    matches = recipes['matches']
    match_list = []
    i = 0
    for i in range(0, len(matches)):
        match = matches[i]
        # print("Matches: {}".format(match))
        match_list.append(matches)
    recipe_list = []
    flavor_list = []
    # for j in range(0, len(match_list)):
    #     recipe_match = match_list[j]
    #     print("Recipe: {}".format(recipe_match))
    #     recipe_list.append(recipe_match)
    #     flavor = recipe_match[j]['flavors']
    #     flavor_list.append(flavor)
    j = 0
    for j in range(0, len(match_list)):
        recipe = match_list[j]
        # print("Recipe: {}".format(match_list[j]))
        # recipe_list.append(match_list[j])
        flavor = match_list[j][j]
        print("Flavor:\n {}".format(flavor))
        flavor_list.append(flavor)
        j += 1
    context = {
        'flavor_list': flavor_list,
        'match_list': match_list,
        'matches': matches,
        'recipe_list': recipe_list,
        'recipes': recipes,
    }
    return render(request, 'yummly_api/index.html', context)