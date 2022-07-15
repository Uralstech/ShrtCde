def fread(path, setting='r', encoding='utf8'):
    '''
        Author: Udayshankar R
    
        Reads file at path and returns data according to setting.
    '''

    read = []

    with open(path, 'r', encoding=encoding) as file:
        if setting == 'r': read = file.read()
        elif setting == 'rl': read = list(file.readlines())[0]
        elif setting == 'rls': read = list(file.readlines())

    return read

def fwrite(path, data, setting='w', encoding='utf8'):
    '''
        Author: Udayshankar R
    
        Write to file at path according to setting.
    '''

    with open(path, setting, encoding=encoding) as file:
        for i in data:
            file.write(i + '\n')

def fexists(path: str):
    '''
        Author: Udayshankar R
    
        Checks if file at "full_path" exists.
        Returns True if it does, otherwise False.
    '''

    try:
        file = open(path, "r")
        file.close()
        return True
    except:
        return False