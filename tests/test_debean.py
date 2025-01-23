def debean(encoded_text):
    beanDict = {
        "A": "beans",
        "B": "Beans",
        "C": "BEans",
        "D": "BeAns",
        "E": "BeaNs",
        "F": "BeanS",
        "G": "bEans",
        "H": "bEAns",
        "I": "bEaNs",
        "J": "bEanS",
        "K": "beAns",
        "L": "beANs",
        "M": "beAnS",
        "N": "beaNs",
        "O": "beaNS",
        "P": "beanS",
        "Q": "BEAns",
        "R": "BEaNs",
        "S": "BEanS",
        "T": "BeANs",
        "U": "BeAnS",
        "V": "BeaNS",
        "W": "BeANS",
        "X": "BEANs",
        "Y": "BEAnS",
        "Z": "BEANS",
        "a": "𝓫𝓮𝓪𝓷𝓼",
        "b": "𝓑𝓮𝓪𝓷𝓼",
        "c": "𝓑𝓔𝓪𝓷𝓼",
        "d": "𝓑𝓮𝓐𝓷𝓼",
        "e": "𝓑𝓮𝓪𝓝𝓼",
        "f": "𝓑𝓮𝓪𝓷𝓢",
        "g": "𝓫𝓔𝓪𝓷𝓼",
        "h": "𝓫𝓔𝓐𝓷𝓼",
        "i": "𝓫𝓔𝓪𝓝𝓼",
        "j": "𝓫𝓔𝓪𝓷𝓢",
        "k": "𝓫𝓮𝓐𝓷𝓼",
        "l": "𝓫𝓮𝓐𝓝𝓼",
        "m": "𝓫𝓮𝓐𝓷𝓢",
        "n": "𝓫𝓮𝓪𝓝𝓼",
        "o": "𝓫𝓮𝓪𝓝𝓢",
        "p": "𝓫𝓮𝓪𝓷𝓢",
        "q": "𝓑𝓔𝓐𝓷𝓼",
        "r": "𝓑𝓔𝓪𝓝𝓼",
        "s": "𝓑𝓔𝓪𝓷𝓢",
        "t": "𝓑𝓮𝓐𝓝𝓼",
        "u": "𝓑𝓮𝓐𝓷𝓢",
        "v": "𝓑𝓮𝓪𝓝𝓢",
        "w": "𝓑𝓮𝓐𝓝𝓢",
        "x": "𝓑𝓔𝓐𝓝𝓼",
        "y": "𝓑𝓔𝓐𝓷𝓢",
        "z": "𝓑𝓔𝓐𝓝𝓢",
        "1": "𝕓𝕖𝕒𝕟𝕤",
        "2": "𝔹𝕖𝕒𝕟𝕤",
        "3": "𝔹𝔼𝕒𝕟𝕤",
        "4": "𝔹𝕖𝔸𝕟𝕤",
        "5": "𝔹𝕖𝕒ℕ𝕤",
        "6": "𝔹𝕖𝕒𝕟𝕊",
        "7": "𝕓𝔼𝕒𝕟𝕤",
        "8": "𝕓𝔼𝔸𝕟𝕤",
        "9": "𝕓𝔼𝕒ℕ𝕤",
        "0": "𝕓𝔼𝕒𝕟𝕊",
        "!": "𝚋𝚎𝚊𝚗𝚜",
        "@": "𝙱𝚎𝚊𝚗𝚜",
        "#": "𝙱𝙴𝚊𝚗𝚜",
        "$": "𝙱𝚎𝙰𝚗𝚜",
        "%": "𝙱𝚎𝚊𝙽𝚜",
        "^": "𝙱𝚎𝚊𝚗𝚂",
        "&": "𝚋𝙴𝚊𝚗𝚜",
        "*": "𝚋𝙴𝙰𝚗𝚜",
        "(": "𝚋𝙴𝚊𝙽𝚜",
        ")": "𝚋𝙴𝚊𝚗𝚂",
        ",": "𝚋𝚎𝙰𝚗𝚜",
        ".": "𝚋𝚎𝙰𝙽𝚜",
        "/": "𝚋𝚎𝙰𝚗𝚂",
        "?": "𝚋𝚎𝚊𝙽𝚜",
        " ": "𝚋𝚎𝚊𝚗𝚂",
        ":": "𝙱𝙴𝚊𝙽𝚜",
        "<": "𝙱𝚎𝙰𝙽𝚜",
        ">": "𝙱𝚎𝙰𝚗𝚂",
        "~": "𝙱𝚎𝚊𝙽𝚂",
        "+": "𝙱𝚎𝙰𝙽𝚂",
        "-": "𝙱𝙴𝙰𝙽𝚜", 
        "_": "𝙱𝙴𝙰𝚗𝚂",
        "=": "𝙱𝙴𝙰𝙽𝚂"
    }
    inv_beanDict = {v: k for k, v in beanDict.items()}
    result  = ''
    encoded_array = encoded_text.split()
    try:
        for i in encoded_array:
            result = result + inv_beanDict[i]
    except KeyError:
        print("Your message contains a character not recognized by p-ybEaNs. Character has been removed from result")

    return result

print('the quick brown fox jumps over the lazy dog:')
print(debean("𝓑𝓮𝓐𝓝𝓼 𝓫𝓔𝓐𝓷𝓼 𝓑𝓮𝓪𝓝𝓼 𝚋𝚎𝚊𝚗𝚂 𝓑𝓔𝓐𝓷𝓼 𝓑𝓮𝓐𝓷𝓢 𝓫𝓔𝓪𝓝𝓼 𝓑𝓔𝓪𝓷𝓼 𝓫𝓮𝓐𝓷𝓼 𝚋𝚎𝚊𝚗𝚂 𝓑𝓮𝓪𝓷𝓼 𝓑𝓔𝓪𝓝𝓼 𝓫𝓮𝓪𝓝𝓢 𝓑𝓮𝓐𝓝𝓢 𝓫𝓮𝓪𝓝𝓼 𝚋𝚎𝚊𝚗𝚂 𝓑𝓮𝓪𝓷𝓢 𝓫𝓮𝓪𝓝𝓢 𝓑𝓔𝓐𝓝𝓼 𝚋𝚎𝚊𝚗𝚂 𝓫𝓔𝓪𝓷𝓢 𝓑𝓮𝓐𝓷𝓢 𝓫𝓮𝓐𝓷𝓢 𝓫𝓮𝓪𝓷𝓢 𝓑𝓔𝓪𝓷𝓢 𝚋𝚎𝚊𝚗𝚂 𝓫𝓮𝓪𝓝𝓢 𝓑𝓮𝓪𝓝𝓢 𝓑𝓮𝓪𝓝𝓼 𝓑𝓔𝓪𝓝𝓼 𝚋𝚎𝚊𝚗𝚂 𝓑𝓮𝓐𝓝𝓼 𝓫𝓔𝓐𝓷𝓼 𝓑𝓮𝓪𝓝𝓼 𝚋𝚎𝚊𝚗𝚂 𝓫𝓮𝓐𝓝𝓼 𝓫𝓮𝓪𝓷𝓼 𝓑𝓔𝓐𝓝𝓢 𝓑𝓔𝓐𝓷𝓢 𝚋𝚎𝚊𝚗𝚂 𝓑𝓮𝓐𝓷𝓼 𝓫𝓮𝓪𝓝𝓢 𝓫𝓔𝓪𝓷𝓼"
))

print('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG:')
print(debean("BeANs bEAns BeaNs 𝚋𝚎𝚊𝚗𝚂 BEAns BeAnS bEaNs BEans beAns 𝚋𝚎𝚊𝚗𝚂 Beans BEaNs beaNS BeANS beaNs 𝚋𝚎𝚊𝚗𝚂 BeanS beaNS BEANs 𝚋𝚎𝚊𝚗𝚂 bEanS BeAnS beAnS beanS BEanS 𝚋𝚎𝚊𝚗𝚂 beaNS BeaNS BeaNs BEaNs 𝚋𝚎𝚊𝚗𝚂 BeANs bEAns BeaNs 𝚋𝚎𝚊𝚗𝚂 beANs beans BEANS BEAnS 𝚋𝚎𝚊𝚗𝚂 BeAns beaNS bEans"))

print('1234567890:')
print(debean('𝕓𝕖𝕒𝕟𝕤 𝔹𝕖𝕒𝕟𝕤 𝔹𝔼𝕒𝕟𝕤 𝔹𝕖𝔸𝕟𝕤 𝔹𝕖𝕒ℕ𝕤 𝔹𝕖𝕒𝕟𝕊 𝕓𝔼𝕒𝕟𝕤 𝕓𝔼𝔸𝕟𝕤 𝕓𝔼𝕒ℕ𝕤 𝕓𝔼𝕒𝕟𝕊'))

print('!@#$%^&*(),./? :<>~+-_=:')
print(debean('𝚋𝚎𝚊𝚗𝚜 𝙱𝚎𝚊𝚗𝚜 𝙱𝙴𝚊𝚗𝚜 𝙱𝚎𝙰𝚗𝚜 𝙱𝚎𝚊𝙽𝚜 𝙱𝚎𝚊𝚗𝚂 𝚋𝙴𝚊𝚗𝚜 𝚋𝙴𝙰𝚗𝚜 𝚋𝙴𝚊𝙽𝚜 𝚋𝙴𝚊𝚗𝚂 𝚋𝚎𝙰𝚗𝚜 𝚋𝚎𝙰𝙽𝚜 𝚋𝚎𝙰𝚗𝚂 𝚋𝚎𝚊𝙽𝚜 𝚋𝚎𝚊𝚗𝚂 𝙱𝙴𝚊𝙽𝚜 𝙱𝚎𝙰𝙽𝚜 𝙱𝚎𝙰𝚗𝚂 𝙱𝚎𝚊𝙽𝚂 𝙱𝚎𝙰𝙽𝚂 𝙱𝙴𝙰𝙽𝚜 𝙱𝙴𝙰𝚗𝚂 𝙱𝙴𝙰𝙽𝚂'))