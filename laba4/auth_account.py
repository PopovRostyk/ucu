import hashlib
import time


class Property:
    '''
    Is showing details of properties.
    '''
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        '''
        Printing information about property.
        Returning None
        '''
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        '''
        Returning dictionary of main property characteristic which where printed.
        '''
        return dict(square_feet=input("Enter the square feet: "),
         beds=input("Enter number of bedrooms: "),
         baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    '''
    Is creating valid input arguments and returning input.
    '''
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Apartment(Property):
    '''
    This class is updating information about property.
    '''
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        '''
        Is showing details of property
        Returning None
        '''
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)
        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in \
                Apartment.valid_laundries:
            laundry = input("What laundry facilities does "
                            "the property have? ({})".format(
                ", ".join(Apartment.valid_laundries)))
        balcony = ''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input("Does the property have a balcony? " "({})".format(", ".join(Apartment.valid_balconies)))
            parent_init.update({"laundry": laundry, "balcony": balcony})
        return parent_init

    def prompt_init():
        '''
        Is updating dictionary with new information and returning it.
        '''
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have? ",
            Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class House(Property):
    '''
    Is getting information about house.
    '''
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
        garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        '''
        This function is printing information about house.
        Returning None
        '''
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        '''
        Is updating dictionary with new information about house and returning it.
        '''
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
        House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
        House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({"fenced": fenced, "garage": garage, "num_stories": num_stories})
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    '''
    Is giving information about house for purchase.
    '''
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        '''
        Printing information about house for purchase.
        Returning None
        '''
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        '''
        Updating dictionary with new information about purchasing and returning it.
        '''
        return dict(
        price=input("What is the selling price? "),
        taxes=input("What are the estimated taxes? "))
    prompt_init = staticmethod(prompt_init)


class Rental:
    '''
    Is giving information about house for rental.
    '''
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        '''
        Is printing information about house for rental.
        Returning None
        '''
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        '''
        Is updating dictionary with new information about house for rental and returning it.
        '''
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))
    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    '''
    Is giving information about house.
    '''
    def prompt_init():
        '''
        Is combining basic information about house with information about house for rental.
        '''
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    def prompt_init():
        '''
        Is combining basic information about apartment with information about apartment for rental.
        '''
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    def prompt_init():
        '''
        Is combining basic information about apartment with information about apartment for purchasing.
        '''
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    def prompt_init():
        '''
        Is combining basic information about apartment with information about house for purchasing.
        '''
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()
        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))


class User:
    def __init__(self, username, password):
        '''Create a new user object. The password
        will be encrypted before storing.'''
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        '''Encrypt the password with the username and return
        the sha digest.'''
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        '''Return True if the password is valid for this
        user, false otherwise.
        '''
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


class Authenticator:
    def __init__(self):
        '''Construct an authenticator to manage
        users logging in and out.'''
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            print('This username is already taken')
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            print('Password must consist of more than 5 symbols.')
            raise PasswordTooShort(username)
        user = User(username, password)
        self.users.update([(username, user)])

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            print('This username does not exist.')
            raise InvalidUsername(username)
        if not user.check_password(password):
            print('Incorrect password.')
            raise InvalidPassword(username, user)
        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False


class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


def adding():
    agent = Agent()
    add = True
    user_list = Authenticator()
    while add:
        b = input('Do you want to add property(yes, no, later): ')
        if b == 'yes':
            a = input('Do you want to log in/sign up: ')
            if a == 'log in':
                user_list.login(username=input('write username: '), password=input('Write password: '))
                agent.add_property()
            if a == 'sign up':
                user_list.add_user(username=input('write username: '), password=input('Write password: '))
                print('Now you need to log in.')
                user_list.login(username=input('write username: '), password=input('Write password: '))
                agent.add_property()
            else:
                add = False
        if b == 'later':
            time.sleep(5)
            adding()
        else:
            add = False
        if input('Do you want to see all properties?(yes, no): ') == 'yes':
            agent.display_properties()
        else:
            continue
adding()
