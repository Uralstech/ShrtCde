"""
    Author: Uralstech (Udayshankar Ravikumar)\n
    GitHub: https://github.com/Uralstech/ShrtCde

    An IO module for reading and writing files.
"""

from typing import Literal, Union

def readf(path: str, settings: Literal['r', 'rl', 'rls']='r', encoding='utf8') -> Union[str, list]:
    """
        Reads file at path and returns data according to setting.

        Parameters
        ----------

        - ``path``: (string) Path to the file.
        - ``settings``: (string) Read settings for the file.
                - ``'r'``: (string) Reads and returns the file content as string.
                - ``'rl'``: (string) Reads and returns first line of the file as string.
                - ``'rls'``: (string) Reads and returns the file content as list.
        - ``encoding``: (string) Encoding to use when opening the file.
    """

    read = []

    with open(path, 'r', encoding=encoding) as file:
        if settings == 'r': read = file.read()
        elif settings == 'rl': read = file.readline()
        elif settings == 'rls': read = list(file.readlines())

    return read

def writef(path: str, data: Union[list, tuple], settings: Literal['w', 'a', 'x']='w', encoding='utf8') -> None:
    """
        Writes to file at path according to settings.
        
        Parameters
        ----------

        - ``path``: (string) Path to the file.\n
        - ``settings``:
                - ``'w'``: (string) Overrides the whole file and writes data.
                - ``'a'``: (string) Adds data to the file, without changing existing data.
                - ``'x'``: (string) Creates a new file and writes data. Only works if no file with the same name exists at path.\n
        - ``encoding``: (string) Encoding to use when opening the file.
    """

    with open(path, settings, encoding=encoding) as file:
        for i in data:
            file.write(i + '\n')

def findf(path: str) -> bool:
    """
        Checks if file at path exists.
        Returns True if it does; otherwise False.

        Parameters
        ----------

        - ``path``: (string) Path to the file.
    """

    try:
        file = open(path, "r")
        file.close()
        return True
    except:
        return False