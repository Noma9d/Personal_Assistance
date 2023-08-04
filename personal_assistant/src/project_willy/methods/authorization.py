import hashlib
import os
import json
import getpass
from pathlib import Path
from abc import ABC, abstractmethod


class ClassAuthorization(ABC):

    @abstractmethod
    def load_users(self):
        pass

    @abstractmethod
    def login(self):
        pass


class Authorization:

    def __init__(self):
        self.users = dict
        self.key = None
        self.password = None
        self.identifier = None
        self.salt = None
        self.max_attempts = 5

    def load_users(self):

        try:
            data_folder = Path(__file__).resolve().parent.parent / 'data'
            file = data_folder.joinpath('users.json')

            with open(file, "r") as fh:
                self.users = json.load(fh)
                if not isinstance(self.users, dict):
                    self.users = dict
                    
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = dict
            return False

    def login(self):

        self.identifier = input('Input your login (name, email, phone number or username): ')

        for user_data in self.users.values():
            if (
                self.identifier.lower() == user_data['username'].lower()
                or self.identifier.lower() == user_data['email'].lower()
                or self.identifier == user_data['phone']
            ):
                self.user_data = user_data

                for attempt in range(self.max_attempts):
                    print(f'Hello {self.identifier}! Enter your password')
                    self.password = getpass.getpass('Password: ')

                    self.salt = os.urandom(32)
                    self.salt = bytes.fromhex(self.user_data['salt'])
                    self.key = bytes.fromhex(self.user_data['key'])
                    new_key = hashlib.pbkdf2_hmac(
                        'sha256', self.password.encode('utf-8'), self.salt, 100000
                    )

                    if self.key == new_key:
                        print(f'{self.user_data["username"]}, your personal assistant "Willy" welcomes you')
                        break
                    else:
                        print('Invalid password.')
                else:
                    print('Exceeded maximum number of login attempts.')
                break
        else:
            print('User not found')


if __name__ == '__main__':

    authorization = Authorization()
    if authorization.load_user():
        authorization.login()
    else:
        print('User data is not load check the data file.')
