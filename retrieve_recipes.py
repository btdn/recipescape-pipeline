# recipe/<id>: get recipe using id
# recipes/<dishname>: get all the recipes of dish
# clusters/<dishname>: get all clustering result of dish

import json

server = "http://recipe.hyeungshikjung.com/recipe/"
datadir = "./example_recipes/"

def get_json_from_file(query):
    with open(datadir+query+".json") as json_file:
        return json.load(json_file)

def get_json_from_server(query):
    try:
        r = requests.get(servername+query)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)

def get_json(query):
    return get_json_from_file(query)

def get_recipes_json(dishname):
    #getting annotated text instructions for all recipes for dishname
    return get_json("recipes/"+dishname)


def get_all_recipes(dishname):
    #getting annotated text instructions for all recipes for dishname
    return get_json("trees/"+dishname)
    
def get_single_recipe(recipeid):
    #getting a single recipe
    return get_json("recipe/"+recipeid)

def get_clusters(dishname):
    return get_json("clusters"+dishname)
