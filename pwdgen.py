"""pwdgen is password generator with a command line interface.

It supports generating passwords with unique or repeating characters. In
addition, specific characters can be excluded from the character set used for
generating a password.

The available flags for the CLI are:
  --min_length: The minimum password length. Defaults to 10 characters.
  --max_length: The maximum password length. Defaults to 76 characters.
  --exclude: An optional parameter to exclude specific characters.
  --unique: An option to allow for unique instead of repeating characters.
        Defaults to True.
"""

from random import randint, sample, shuffle
from string import ascii_letters, digits, punctuation

import fire


class Password:
    """ A class for generating a password."""

    def __init__(self, min_length, max_length):
        """Inits Password class with minimum and maximum password length."""
        self._password = str()
        self._length = 0
        if min_length != max_length:
            self._length = randint(min_length, max_length)
        else:
            self._length = min_length
        self._char_set = ascii_letters + digits + punctuation

    def exclude_chars(self, chars):
        """Removes the specified characters from the character set from which
        the password will be generated.

        Args:
            chars (str): A string with all the characters to exclude from the
                character set.

        """
        self._char_set = self._char_set.translate({ord(x): None for x in chars})

    def _draw(self):
        """Draws a number of characters.

        The number of drawn characters is the length of the password. At least
        one letter, one digit, and one punctuation character are drawn, and all
        characters are drawn from a uniform distribution of the characters in
        the character set.

        Returns:
            chars (list): A list of characters that can contain multiples.

        """
        # Ensures that the password contains at least one letter, one digit, and
        # one punctuation character.
        chars = [sample(ascii_letters, k=1), sample(digits, k=1),
                 sample(punctuation, k=1)]
        # Draws the remaining number of characters.
        chars.extend(sample(self._char_set, self._length - 3))
        chars = [item[0] for item in chars]
        return chars

    def _draw_unique(self):
        """Draws a number of unique characters.

        The number of drawn characters is the length of the password. At least
        one letter, one digit, and one punctuation character are drawn, and all
        characters are drawn from a uniform distribution of the characters in
        the character set.

        Returns:
            chars (list): A list of unique characters.

        """
        # Ensures that the password contains at least one letter, one digit, and
        # one punctuation character.
        chars = [sample(ascii_letters, k=1), sample(digits, k=1),
                 sample(punctuation, k=1)]
        # Draws the remaining number of unique characters.
        size = 3
        while size < self._length:
            n = sample(self._char_set, k=1)
            if n not in chars:
                chars.append(n)
                size += 1
        chars = [item[0] for item in chars]
        return chars

    def set_password(self, chars):
        """ Setter method.

        Args:
            chars (str): The password string.

        """
        self._password = chars

    def get_password(self):
        """ Getter method.

        Returns:
            str: The password string.

        """
        return self._password

    def generate(self, unique):
        """Generates a password with unique characters, if the character set
        contains enough unique characters regarding the password length.

        Args:
            unique (bool):

        """
        if unique:
            try:
                assert len(self._char_set) >= self._length
            except AssertionError:
                print(f'Cannot choose {self._length} unique characters, if the '
                      f'available set of characters has only'
                      f' {len(self._char_set)} unique characters!')
                exit(1)
            chars = self._draw_unique()
        else:
            chars = self._draw()
        shuffle(chars)
        pwd = ''.join(chars)
        self.set_password(pwd)


def password(min_length=10, max_length=76, exclude=None, unique=True):
    """Generates and prints a password.

    If the parameters 'min_length' and 'max_length' are unequal, a random
    password with a length between 'min_length' and 'max_length' number of
    characters will be generated.

    Args:
        min_length (int): The minimum password length. Default is 10 characters.
        max_length (int): The maximum password length. Default is 76 characters.
        exclude (str): An optional parameter to exclude specific characters.
        unique (bool): An option to allow for unique instead of repeating
            characters. Defaults to True.

    """
    pwd = Password(min_length, max_length)
    if exclude is not None:
        pwd.exclude_chars(exclude)

    pwd.generate(unique)
    print(f'Password: {pwd.get_password()}')


def main():
    fire.Fire(password)


if __name__ == '__main__':
    main()
