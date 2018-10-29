'''

Hanger: Main Prog


'''


# local imports - my code modules 
# (don't use from ___ import *, its impossible to follow later)

import clothing_classes as cc
import user
import fake_lib

#general imports
import random
import os

# Initialize
os.system('clear')
me = user.Admin()     # create the Admin (in fake_lib.py: has user_list, 
                      # functions to add/del/list users

fake_lib.fake_mode(me)    # create dummy user, give her a name, 
                          # fill her closet, add to admin's user_list, echo when done

# *Fake function*: do all the things a user would need at log-in time, on our one 
# fake user
# rn: time sort their closet, "check" weather
me.user_list[0].user_login_initialize()
input('Initialization complete')

print('Starting state of queues:')
me.user_list[0].disp_closet_queue()

me.user_list[0].recommend('casual')    #run recommend, occasion: 'casual'

#me.user_list[0].print_picked_list()
me.user_list[0].user_outfit_choice()   # ask user to choose outfit from choices

print('End State of Queues:')
me.user_list[0].disp_closet_queue()    # print out state of queues after choice,
                                       # to show they were picked, and last_worn
                                       # was updated


# def recommender_engine(user):
#     pass

#     ## needs to provide one outfit for a given weather report
#     #### requires priority queue of each item type
#     #### you'd then move through that queue for the oldest-worn item with season profile, skip outerwear if its hot for now.

#     ## iterate that over 

#     ## each of those items should be updated as worn today
#     ###pqueue should update its order automatically, dump them at back
