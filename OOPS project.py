class Library:
    def __init__(self,listofbooks):
        self.books = listofbooks

    def ListofBooks(self): # 1st method
        print(f'\n{len(self.books)} Books are available :')
        for book in (self.books):

            print('♦--',book)

    def BorrowBooks(self): # 2nd method
        print('SO, YOU WANT TO BORROW THE BOOK')
        name = input('Enter student Name :')
        bookname = input('Enter the Book Name that you want to Borrow :')
        if bookname not in self.books:
            print('SORRY!!!...THIS BOOK IS NOT AVAILABLE IN LIBRARY OR TAKEN BY SOMEONE ELSE \n')
        else :# means book is available
            print(f'{bookname} BOOK IS ISSUED TO {name}: THANK YOU... KEEP IT WITH CARE AND RETURN ON TIME\n')
            self.books.remove(bookname)
            Track.append({name:bookname})


    def ReturnBooks(self): # 3rd method
        print('SO, YOU WANT TO RETURN THE BOOK')
        name = input('Enter student Name :')
        bookname = input('Enter the Book Name that you want to Return :')
        if {name:bookname} in Track:
            Track.remove({name:bookname})
            self.books.append(bookname)
            print('THANKS FOR RETURNING THE BOOK...HAVE A GOOD DAY')
        else:
            print(f'{name} you didn\'t Borrow any Book')

    def DonateBooks(self): # 4th method
        print('SO, WANT TO DONATE THE BOOK')
        name = input('Enter student Name :')
        bookname = input('Enter the Book Name that you want to DONATE :')
        self.books.append(bookname)
        Track.append({name:bookname})
        print('THANKS OF DONATING THIS BOOK...HAVE A GOOD DAY :) ')

    def TransactionofBooks(self): # 5th method
        print(f'{len(Track)} TRANSACTIONS ARE AS FOLLOWS')

        for i in range(1,len(Track)+1):
            for trans in Track:
                for key,value in trans.items():
                    print(i,'.',f'{value} book is taken/issued by {key}')

    def Exit(self):
        print('\nTHANKS FOR VISITING THE LIBRARY...')
        print('......HOPE YOU will COME AGAIN......\n')
        exit()



if __name__ == '__main__':

    indiaslibrary = Library(['marathi','hindi','english','physics','chemistry','mathamatics','biology'])
    Track = []

    print('\n\t\t\t\t\t\t\t\t\t\t\t\t\t♦♦♦♦♦♦♦♦ WELCOME TO THE LIBRARY ♦♦♦♦♦♦♦♦\n')

    while (True):
        print('\nCHOOSE WHAT YOU WANT TO DO\n')
        print('1. List of Books')
        print('2. Borrow Book')
        print('3. Return Book')
        print('4. Donate Book')
        print('5. Transaction of Books')
        print('6. Exit the Library')

        usr_response = input("\nEnter your choice : ")
        if usr_response.isnumeric():
            if usr_response == "1":
                    print(indiaslibrary.ListofBooks())
            elif usr_response == "2":
                    print(indiaslibrary.BorrowBooks())
            elif usr_response == "3":
                    print(indiaslibrary.ReturnBooks())
            elif usr_response == "4":
                    print(indiaslibrary.DonateBooks())
            elif usr_response == "5":
                    print(indiaslibrary.TransactionofBooks())
            elif usr_response == "6":
                    print(indiaslibrary.Exit())
            else:
                print("\nPLEASE ENTER VALID INPUT\n")



        # print("\nPRESS 'Q' TO QUIT AND 'C' TO CONTINUE\n")
        # while(True):
        #         ui = input('Enter your choice :')
        #         if ui == "Q":
        #             print('\nTHANKS FOR VISITING THE LIBRARY\n')
        #             exit()
        #         elif ui == "C":
        #             continue
        #         else:
        #             print("\nENTER VALID INPUT\n")







# track = [{'apple':'red'},{'banana':'yellow'},{'jackfruit':'green'}]
# track = {'apple':'red','banana':'yellow','jackfruit':'green'}
# new = {}
# # print(track.items())
#
# for i in track:
#     for key,value in i.items():
#         new.update({key:value})
# print(new)




