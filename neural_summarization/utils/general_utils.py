import hashlib


def print_block(string_):
    """Prints the string inside a block of #
    Args:
        string_ (str): The string to be printed inside the block     
    """
    print '#' * 80
    print string_
    print '#' * 80


def form_hash(string_):
    """Forms the sha1 hash of the string 
    Args:
        string_ (str): The string to be hashed
    Returns:
       (str): The sha1 hashed string 
    
    """
    sha1 = hashlib.sha1()
    sha1.update(string_)
    hashed_string = sha1.hexdigest()
    return hashed_string

