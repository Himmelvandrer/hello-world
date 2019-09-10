import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]


            dictFile = open ('dictionary.txt', 'r')  # Aapner for lesing
            for word in dictFile.readlines:
                word = word.strip ('\n')
                cryptWord = crypt.crypt(word.salt)
                if (cryptWord == cryptPass):
                    print ("[+] Fant passordet! Det er: " + word + "\n")
                    return
            print ("[-] Fant ikke passordet... \n")
            return

    def main():
        passFile = open ('passwords.txt', 'r')
        for line in passFile.readlines():
            if ":" in line:
                user = line.split(':')[0]
                cryptPass = line.split(':')[1].strip(' ')
                print ("Leter etter passordet for " + user)
                testPass (cryptPass)
    if __name__ == "__main__":
        main()