import socket

def is_sha1(maybe_sha):
    if len(maybe_sha) != 40:
        return False
    try:
        sha_int = int(maybe_sha, 16)
    except ValueError:
        return False
    return True

def get_list_from_string(list_string):
    return list_string.split(',')

def is_ip(maybe_ip):
    try:
        socket.inet_aton(maybe_ip)
        return True
    except socket.error:
        return False

CONTAINS_VALIDATORS={}