import sys
import algos as al

def main():
    filename = str(sys.argv[1])
    pw = int(sys.argv[2])
    with open(filename, 'r') as myfile:
        cyphertext = myfile.read()
    with open('plaintext.txt','wb') as outfile: 
        outfile.write(al.decrypt(cyphertext,pw))
           
if __name__ == '__main__':
    main()