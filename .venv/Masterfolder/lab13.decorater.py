# decorater

def add_kuchu_items(cat):

    def billufood():
        print("treats")
        print("waterfountain")
        cat()
        print("biscuits")

    return billufood()




@add_kuchu_items
def bagheera_food_list():
    print("wet food")
    print("dry food")