# Keeps track of what key is down (a set is unique so its good for keeping keys)
keys_down = set()

def is_key_pressed(key):
    return key in keys_down