# pwdgen - a password generator

This repository contains a password generator with a command line interface for quickly generating a new password that consists of all the letters, digits, and punctuation characters in the ASCII character set.

The command line interface is provided through [Python Fire](https://github.com/google/python-fire).
___
### A list of available flags for the command line interface

 * min_length: The minimum password length, which defaults to 10 characters.
 * max_length: The maximum password length, which defaults to 76 characters.
 * exclude: An optional parameter to exclude specific characters.
 * unique: An option to allow for generating unique instead of repeating characters, which is set to 'True' by default.

To view the available flags on a terminal:
```shell
python3 pwdgen.py -- --help
```

If *min_length* and *max_length* are unequal, the password length will be randomly choosen between *min_length* and *max_length* number of characters.

_Note_: For reasons of password strength, each generated password contains at least one letter, one digit, and one punctuation character.
___
### Usage examples
#### Generate a password with a length of 12 characters
```shell
python3 pwdgen.py --min_length=12 --max_length=12
```

#### In addition to a password length of 12 characters, allow for repeating characters
```shell
python3 pwdgen.py --min_length=12 --max_length=12 --unique=False
```

#### Generate a password with a length of 12 characters, and exclude the following punctuation characters: ?!;:_,.-()[]{}
```shell
python3 pwdgen.py --min_length=12 --max_length=12 --exclude='?!;:_,.-()[]{}'
```
