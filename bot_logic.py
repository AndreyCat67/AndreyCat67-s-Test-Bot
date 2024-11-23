import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
    

def emoji_pass(pass_length):
    elements = "😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😗😙🥲😚"
    emoji = ""
    for i in range(pass_length):
        emoji += random.choice(elements)
    return emoji
    