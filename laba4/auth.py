import hashlib


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
