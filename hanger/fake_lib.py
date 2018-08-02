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
    a = cc.Jacket(name = 'Denim Jacket', color = 'blue', material = 'denim', occasion = ['casual'])
    b = cc.Blazer(name = 'Fancy Blazer', color = 'black', material = 'suede', 
        waterproof = -1, occasion=['party','work'])
    

    ## top

    c = cc.Shirt(name = 'Radiohead Tee', color = 'gray', occasion=['casual','workout'])

    d = cc.Blouse(name = 'Light Blouse', color = 'peach', material = 'cotton', 
        season= {'Spring/Fall': 0, 'Summer': 1, 'Winter': 0}, occasion = ['casual','party'])
    e = cc.Shirt(name = 'Heavy Sweater', color = 'white', material = 'wool', 
        season= {'Spring/Fall': 0, 'Summer': 0, 'Winter': 1}, occasion = ['casual','work','party'])

    ## bottom
    f = cc.Tights(name = 'Yoga Pants', color = 'black', occasion = ['casual', 'workout','party'])
    g = cc.Skirt(name = 'Frilly Skirt', color = 'white', season= {'Spring/Fall': 0, 'Summer': 1, 'Winter': 0}, occasion = ['casual','party'])
    h = cc.Pants(name = 'Skinny Jeans', color = 'black', occasion = ['casual','party'])

    ## shoes
    i = cc.Sneaker(name = 'Converse', color = 'blue', season = {'Spring/Fall': 1, 'Summer': 1, 'Winter': 0}, occasion= ['casual','workout'])
    j = cc.Boot(name = 'Rain Boots', color = 'green', material = 'rubber', season = {'Spring/Fall': 1, 'Summer': 1, 'Winter': 1}, waterproof = 1, occasion =['casual'])
    k = cc.Boot(name = 'Chukka Boot', color = 'black', material = 'suede', season =  {'Spring/Fall': 1, 'Summer': 1, 'Winter': 1}, waterproof = -1, occasion = ['casual','party','work'])
    l = cc.Flat(name = 'Flats', color = 'white', season = {'Spring/Fall': 1, 'Summer': 1, 'Winter': 0}, occasion=['casual','work','party'])

    to_closet = [a,b,c,d,e,f,g,h,i,j,h,l]

    for article in to_closet:
        user.add_article(article)

    print(user)
    user.disp_closet()
    return print('Closet loaded')

def weather_report():
    
    # returns phony season to narrow clothes choice
    '''
    temp = random.randint(30,100)
    if temp < 45: season = 'Winter'
    elif temp < 65: season = 'Spring/Fall'
    else: season = 'Summer'
    '''
    roll = random.randint(1,3)
    if roll == 1: season = 'Spring/Fall'
    elif roll == 2: season = 'Summer'
    else: season = 'Winter'
    
    print('Season = ' + season)
    return season
