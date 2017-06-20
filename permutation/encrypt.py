import sys
import util as u

def main():
    filename = sys.argv[1]
    pw = u.str2num(sys.argv[2])
    with open(filename, 'r') as myfile:
        plaintext = myfile.read()
    with open('cyphertext.txt','wb') as outfile:
        outfile.write(u.encrypt(plaintext,pw))
           
if __name__ == '__main__':
    main()