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