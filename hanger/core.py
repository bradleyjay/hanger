'''

Closeted: Main Prog


'''
from random import *
import clothing_classes as cc

from user import *
from fake_lib import *

# Initialize
me = Admin()
fake_mode(me)


me.user_list[0].recommend('casual')

# def recommender_engine(user):
#     pass

#     ## needs to provide one outfit for a given weather report
#     #### requires priority queue of each item type
#     #### you'd then move through that queue for the oldest-worn item with season profile, skip outerwear if its hot for now.

#     ## iterate that over 

#     ## each of those items should be updated as worn today
#     ###pqueue should update its order automatically, dump them at back
