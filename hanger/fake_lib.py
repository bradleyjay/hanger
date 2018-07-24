'''

This has all the fake tie ins that will later be systems

'''
import clothing_classes as cc
import random
import datetime

def fake_mode(admin):

    # sets up program with fake user, fake closet

    name_list = ['Samantha', 'Patrice', 'Barb', 'Lily', 'Betty', 'Ann', 'Bernadette']
    #random.randint(0,len(name_list)-1) ????
    new = admin.add_user(name_list[random.randint(0,len(name_list)-1)])  # roll a name, create a user
    fill_closet(new)
    return print('New user: ' + new.name)

def fill_closet(user):
    ## fills fake closet for fake user

    ## outerwear
    a = cc.Jacket(name = 'Denim Jacket', color = 'blue', material = 'denim', prof_cas = 3)
    b = cc.Blazer(name = 'Fancy Blazer', color = 'black', material = 'suede', 
        waterproof = -1, prof_cas = -10)
    

    ## top

    c = cc.Shirt(name = 'Radiohead Tee', color = 'gray', prof_cas = 10)

    d = cc.Blouse(name = 'Light Blouse', color = 'peach', material = 'cotton', 
        season= {'Spring/Fall': 0, 'Summer': 1, 'Winter': 0})
    e = cc.Shirt(name = 'Heavy Sweater', color = 'white', material = 'wool', 
        season= {'Spring/Fall': 0, 'Summer': 0, 'Winter': 1})

    ## bottom
    f = cc.Tights(name = 'Yoga Pants', color = 'black')
    g = cc.Skirt(name = 'Frilly Skirt', color = 'white', prof_cas = 3, season= {'Spring/Fall': 0, 'Summer': 1, 'Winter': 0})
    h = cc.Pants(name = 'Skinny Jeans', color = 'black')

    ## shoes
    i = cc.Sneaker(name = 'Converse', color = 'blue')
    j = cc.Boot(name = 'Rain Boots', color = 'green', material = 'rubber', waterproof = 1)
    k = cc.Boot(name = 'Chukka Boot', color = 'black', material = 'suede', waterproof = -1)
    l = cc.Flat(name = 'Flats', color = 'white')

    to_closet = [a,b,c,d,e,f,g,h,i,j,h,l]

    for article in to_closet:
        user.add_article(article)

    print(user)
    user.disp_closet()
    return print('Closet loaded')

def weather_report():
    
    # returns phony season to narrow clothes choice

    temp = random.randint(30,100)
    if temp < 45: season = 'Winter'
    elif temp < 65: season = 'Spring/Fall'
    else: season = 'Summer'

    return season

