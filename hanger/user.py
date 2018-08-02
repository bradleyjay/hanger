import copy
import fake_lib
import random

'''

Contains classes and functions to create a user, populate their closet, 
and make modifications to both.

'''

class Admin:
    def __init__(self):
        self.user_list = []
        self.user_count = 0

    def user_list(self):
        if self.user_list:
            for user in user_list:
                print(user)


    def add_user(self, name):
        new = User(name,self.user_count)
        self.user_list.append(new)
        self.user_count += 1
        return new

    def del_user(self, user_id):
        for user in self.user_list:
            if user.id == user_id:
                user = None  # is this how delete works?


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

        self.outerwear = []
        self.top = []
        self.bottom = []
        self.shoe = []
        
        self.closet = [self.outerwear, self.top, self.bottom, self.shoe]

    def add_article(self, article):
        if article != None:
            if article.ctype == 'outerwear': self.closet[0].append(article)
            if article.ctype == 'top': self.closet[1].append(article)
            if article.ctype == 'bottom': self.closet[2].append(article)
            if article.ctype == 'shoe': self.closet[3].append(article)

    def disp_closet(self):
        if self.closet != None:
            for kind in self.closet:
                for article in kind:
                    if article.ctype != None:
                        print(article)
                    else:
                        print('Error.')


    def __str__(self):
        return self.name + '    ' + 'UserID: ' + str(self.user_id) + '\n'

    def recommend(self, occasion):
        '''
        Takes occassion, gets weather. Then runs through list of things in closet,
        per category, and grabs one appropriate answer for each.
        '''

        # deep copy closet once, then let algo pull items out of that. Keep
        # using that for each outfit made so there's no overlaps. (could be switchable
        # pretty easily, you'd just make a new deep copy for each outfit)
        # Assuming python's passing the pointer to the closet, this should work as
        # written, otherwise, gotta find a way to keep using same one...

        working_closet = copy.deepcopy(self.closet)
        #weather_today = fake_lib.weather_report()
        weather_today = fake_lib.weather_report()
        # call private recommender function for each outfit required.
        outfit1 = self._recommend(working_closet, occasion, weather_today)
        outfit2 = self._recommend(working_closet, occasion, weather_today)

      
        self.print_outfit(outfit1,1)  
        self.print_outfit(outfit2,2)
       
    def _recommend(self, closet, occasion, weather_today):

        # outfit will be a list with a slot for each clothing type
        outfit = [None, None, None, None]


        # choose_article call needs outfit so it can check for clashes later.

        outfit[0] = self.choose_article(closet, occasion, weather_today, outfit,'outerwear')
        outfit[1] = self.choose_article(closet, occasion, weather_today, outfit,'top')
        outfit[2] = self.choose_article(closet, occasion, weather_today, outfit,'bottom')
        outfit[3] = self.choose_article(closet, occasion, weather_today, outfit,'shoe')

        return outfit

        # ## start with shoes
        # for shoe in closet[3]:
        #     if occasion in shoe.occasion:              # proper occasion?
        #         if shoe.season[weather_today] == 1:     # season in dict = 1?
        #             outfit[3] = shoe.name
        #             closet[3].remove(shoe)
        ## this bit is janky, idk how to improve it. You have instance, 
        # so I guess, I'd return that instance in the real code, and do a
        # bunch of things. Add it to the outfit actually sent to user, but just
        # in staging (wouldn't actually change it's last-worn unless picked.)
        #
        '''
        Lots of things to do with it. For now, maybe just add name to list in outfit,
        but still gotta keep instance around to do the edits if picked.

        For first rev, assume they do pick, but i think you should still build in the 
        seperate choose n display part, then the update real closet and last-worn like they
        chose it.  
        '''

    def choose_article(self, closet, occasion, weather_today, outfit, article_ctype):
        '''
        Return an item (instance) of a requested type from whats left in the closet 
        (i.e. the working_closet) for the given occasion, appropriate for 
        the weather, that doesn't (optional) clash with anything selected 
        so far and (optional) matches.

        '''

        # match article ctype to slot in closet / outfit
        if article_ctype == 'outerwear': s = 0
        elif article_ctype == 'top': s = 1
        elif article_ctype == 'bottom': s = 2
        else: s = 3

        #placeholder for a "clashes" function call, checking each item picked vs.
        # those already selected. Likewise, "matches"

        clashes = None 
        matches = True

        selected_item = None  # default

        for item in closet[s]:
            if occasion in item.occasion:              # proper occasion?
                if item.season[weather_today] == 1:     # season in dict = 1?
                    if clashes == None:
                        if matches == True:
                            selected_item = item
                            closet[s].remove(item)

        return selected_item

    def print_outfit(self, outfit, outfit_number):
        if outfit != None:
            
            print('\n' + '---------------------')
            print('Outfit ' + str(outfit_number) + ': \n')

            for article in outfit:
                if article != None:      # default is None, if nothing got picked
                    print(article.name)
                else:
                    print(None)

            print('---------------------' + '\n')
        else:
            print('\n Error: Outfit not found. \n')