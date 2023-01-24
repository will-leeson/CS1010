import argparse
import sys

parser = argparse.ArgumentParser(description="A Caesar Cipher Program")
parser.add_argument('--code', required=True, help="The code to encode or decode", type=str)
parser.add_argument('--action', required=True, choices=["encode", "decode"])
parser.add_argument('--offset', required='encode' in sys.argv, type=int)

args = parser.parse_args()

def cipher(code: str, alphabet: dict[str, int], offset: int):
    cipheredAlphabet = {((alphabet[x]-offset)%26):x for x in alphabet}
    print(cipheredAlphabet)
    
    newCode = ""
    for letter in code.lower():
        if letter not in alphabet:
            newCode+=letter
        else:
            newCode+=cipheredAlphabet[alphabet[letter]]
    return newCode

def decipher(code: str, alphabet: dict[str, int]):
    for i in range(len(alphabet)):
        print(cipher(code, alphabet, i))
    

alphabet = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}


if args.action == "encode":
    encodedWord = cipher(args.code, alphabet=alphabet, offset=args.offset)
    print(encodedWord)
elif args.action == "decode":
    decipher(args.code, alphabet)
else:
    assert False, "I'm not sure how you got here. Congrats"