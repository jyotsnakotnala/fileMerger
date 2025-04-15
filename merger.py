files = ['textfile1', 'textfile2','textfile3'] #input files

with open('merged.txt', 'w') as outfile: #automatically closes as with keyword is used after the work is done
    for fname in files:
        try:
            with open(fname, 'r') as infile:
                content = infile.read() # function to read the content of the infile
                outfile.write(content + '\n') #pasting the content into the outfile merged.text
        except FileNotFoundError:
            print(f"{fname} not found.")
