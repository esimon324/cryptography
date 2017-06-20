import sys
import util as u

def main():
    filename = str(sys.argv[1])
    pw = u.str2num(sys.argv[2])
    with open(filename, 'r') as myfile:
        cyphertext = myfile.read()
    with open('plaintext.txt','wb') as outfile: 
        outfile.write(u.decrypt(cyphertext,pw))
           
if __name__ == '__main__':
    main()