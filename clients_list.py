def main():

    infile = open('clients.txt','r')

    i = 0
    
    for line in infile:
         line = line.rstrip('\n')
         i += 1
         print(str(i) + ". " + line)

    
    infile.close()

main()

        