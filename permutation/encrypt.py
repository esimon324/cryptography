import sys
import algos as al

def main():
    filename = str(sys.argv[1])
    pw = int(sys.argv[2])
    with open(filename, 'r') as myfile:
        plaintext = myfile.read()
    with open('cyphertext.txt','wb') as outfile:
        outfile.write(al.encrypt(plaintext,pw))
           
if __name__ == '__main__':
    main()