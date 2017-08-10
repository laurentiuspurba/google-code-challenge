from Crypto.Cipher import AES
import base64

'''
To get function definition for this solution, you need to decypt the encoded string.
Once you have that decoded string, use that one in your anser(data, n) function.
You do not need the 'from Crypto... and import' statement once you have the result
of decoded string.
Good luck!!!
'''

def answer(data, n):
    encoded = 'yKbRsL7zaVYuArNT752zt38VO8hYiByt+dS+6uuBk7gj9Ywj/PTvyXg2OsqX+3q3e8IzmIqtik4pi40ajEaaLsqQOe7OzIfgBZUOS34iyjQ= '
    decoded = cipher.decrypt(base64.b64decode(encoded))
