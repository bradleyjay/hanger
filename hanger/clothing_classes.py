import datetime

class Article:

    def __init__(

        self,
        name =None,
        color = None, 
        material=None,
        season= {'Spring/Fall': 1, 'Summer': 0, 'Winter': 0}, #might want to do this like occasion
        occasion =[None],
        last_worn= datetime.date.today() - datetime.timedelta(days = 21), # initialize all clothes as worn 3 weeks back (ready for wear)
        waterproof=0,

        ):

        '''
        Template for all articles of clothing
        '''

        # classification (subtypes set these) 
        self.name = name
        self.ctype = None # clothing type (shoe)
        self.cctype = None # subtype (flat, boot, heel, sneaker)

        # client facing stats
        self.color = color
        self.material = material
        self.waterproof = waterproof # 0: no/doesn't matter. -1: vulnerable to water 1: waterproof
        self.occasion = occasion
        self.last_worn = last_worn
        
        # algo stats
        self.season = season

        # always none to start
        self.dangerflag = None # always starts as none, otherwise why enter it


    def __str__(self):
        info = ["Name: " + str(self.name) + '\n',
            "Clothing Type: " + str(self.ctype) + '\n',
            "Subtype: " + str(self.cctype) + '\n',
            "Color: " + str(self.color) + '\n',
            "Material: " + str(self.material) + '\n',
            "Waterproof: " + str(self.waterproof) + '\n',
            "Last Worn: " + str(self.last_worn) + '\n',
            "Occasion: " + str(self.occasion),
            ]
        return ''.join(info)
        
    


################################################################
################# Main Clothing TYPE ##########################
################################################################

class Outerwear(Article):
    def __init__(self, **kwargs):
        '''
        super() calls Article's init. Otherwise, class just uses this init, and never calls Article.__init__
        Also allows sending arguments to Article's init. 
        Anything you want superceded can be changed after super()

        '''
        super().__init__(**kwargs)
        self.ctype = 'outerwear'


class Top(Article):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ctype = 'top'

class Bottom(Article):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ctype = 'bottom'

class Shoe(Article):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ctype = 'shoe'

'''
class Accent(Article):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ctype = 'Accent'

'''



################################
######## Outerwear  ############
################################


class Jacket(Outerwear):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cctype = 'jacket'

class Blazer(Outerwear):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cctype = 'blazer'

class Sweatshirt(Outerwear):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cctype = 'sweatshirt'


################################
############## Top  ############
################################


class Dress(Top):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cctype = 'dress'

class Shirt(Top):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cctype = 'shirt'

class Blouse(Top):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cctype = 'blouse'

################################
########### Bottom  ############
################################

class Skirt(Bottom):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cctype = 'Skirt'

class Pants(Bottom):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cctype = 'pants'

class Tights(Bottom):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cctype = 'tights'

################################
########### Shoes  #############
################################

class Flat(Shoe):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cctype = 'flats'

class Heel(Shoe):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cctype = 'heels'

class Sneaker(Shoe):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cctype = 'sneaker'

class Boot(Shoe):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cctype = 'boot'

