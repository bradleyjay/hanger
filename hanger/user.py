import copy
import fake_lib
import random
import hanger_priority_queue
import datetime

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
                user = None  # is this how delete works? (In python, not sql probs.)


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.outfit_count = None

        self.outerwear = hanger_priority_queue.Queue()
        self.top = hanger_priority_queue.Queue()
        self.bottom = hanger_priority_queue.Queue()
        self.shoe = hanger_priority_queue.Queue()

        self.closet = [self.outerwear, self.top, self.bottom, self.shoe]

    def user_login_initialize(self):
        '''
        This will end up housing all the functions that run when a user logs
        in. Closet should time sort itself, so you're not running that sort
        when you request outfits (or, for safety, both places).
    
        Weather report.

        '''
        self.closet_sort()
        self.weather_today = fake_lib.weather_report()

    def add_article(self, article):
        if article != None:
            # each closet slot is a priority queue - calls insert() method 
            # to add to the queue
            if article.ctype == 'outerwear': self.closet[0].enqueue(article)
            if article.ctype == 'top': self.closet[1].enqueue(article)
            if article.ctype == 'bottom': self.closet[2].enqueue(article)
            if article.ctype == 'shoe': self.closet[3].enqueue(article)

    def disp_closet(self):
        if self.closet != None:
            for kind in self.closet:
                for article in kind.items:
                    if article.ctype != None:
                        print(article)
                        print('\n')
                    else:
                        print('Error: Missing entry.')

    def disp_closet_queue(self):
        if self.closet != None:
            for kind in self.closet:
                print('\n' + 'CATEGORY')
                for article in kind.items:
                    if article.ctype != None:
                        print(article.name)
                        
                    else:
                        print('Error: Missing entry.')


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

        #working_closet = copy.deepcopy(self.closet) #no need with queue
        #weather_today = fake_lib.weather_report()
        
       

        # call private recommender function for each outfit required.
        # this should split now - 
        #V 1 - update queues to make sure they're in order (not optimal, just for now...should be done at a less in-the-way time)
        # prep for outfit building
        
        self.closet_sort()
        self.picked_list = []
        self.outfit_list = []
        self.outfit_count = 2

        # 2 - Pick outfits, while building a "picked list" that marks what's
        # been chosen in a previous outfit already, so no repeats occur.
        
        for i in range(0,int(self.outfit_count)):
            outfit = self._recommend(occasion, self.weather_today)
            self.outfit_list.append(outfit)
        
       
    def user_outfit_choice(self):
        '''
        Iterate through outfit_list, report outfit name and the name of each 
        item in the outfit.
        '''
        print(len(self.outfit_list))
        print('\n CHOOSE AN OUTFIT')
        for outfit in self.outfit_list:
            if outfit != None:
            
                print('\n' + '---------------------')
                print('Outfit ' + str(self.outfit_list.index(outfit)+1) + ': \n')

                for article in outfit:
                    if article != None:      # default is None, if nothing got picked
                        print(article.name)
                    else:
                        print(None)

                print('---------------------' + '\n')
            else:
                print('\n Error: Outfit not found. \n')
        
        i = input('Enter the number of the outfit you want to wear today')

        if int(i) in range(1,len(self.outfit_list)):
            for article in self.outfit_list[int(i)-1]:
                if article != None:
                    print("You're wearing " + article.name)
                    article.last_worn = datetime.date.today()

        else: 
            print(str(i)+":" + 'Invalid Entry.')
        
        self.closet_sort() # lil heavy handed, but sort closet queues after selection
        # resets queues to correct state, which moves position of chosen items.

        

    def closet_sort(self):
        '''
        Sort each category in the closet in time order.
        '''

        for kind in self.closet:
            if kind != None:
                kind.time_sort()

    def _recommend(self, occasion, weather_today):

        # outfit will be a list with a slot for each clothing type
        outfit = [None, None, None, None]


        # choose_article call needs outfit so it can check for clashes later.

        outfit[0] = self.choose_article(self.closet, occasion, weather_today, outfit,'outerwear')
        outfit[1] = self.choose_article(self.closet, occasion, weather_today, outfit,'top')
        outfit[2] = self.choose_article(self.closet, occasion, weather_today, outfit,'bottom')
        outfit[3] = self.choose_article(self.closet, occasion, weather_today, outfit,'shoe')

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

        clashes = False 
        matches = True

        selected_item = None  # default


        # list is last_worn sorted: so iterate through it til you find a match.
        # if you dont, returns None, adds nothing to picked_list
        for item in closet[s].items:
            if item not in self.picked_list:
                if occasion in item.occasion:              # proper occasion?
                    if item.season[weather_today] == 1:     # season in dict = 1?
                        if clashes == False:
                            if matches == True:
                                # add pointer to that item to outfit
                                selected_item = item

                                # add pointer to that item to picked_list
                                self.picked_list.append(item)
                                break

        return selected_item # for now, if this ends up being None, that's ok. 
        # later, needs some mechanism to not just pick the first good one, 
        # and also not to just take it straight away.


    def print_picked_list(self):
        for article in self.picked_list:
            print(article.name)

    