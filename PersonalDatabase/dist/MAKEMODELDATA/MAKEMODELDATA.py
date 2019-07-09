from pickle import *
import os


class some_class:

    def input(self, a="I"):
        if a == "I":
            self.name = input('Enter Name (char_limit = 20): ')
            self.make = input('Enter Make (char_limit = 15): ')
            self.date = input('Enter Date Of Receipt [MM/DD/YYYY]: ')
            while datevali(self.date) == False:
                self.date = input('Enter Date Of Receipt [MM/DD/YYYY]: ')
            self.sent = input("Enter Model: ")
            l = str(load(open("ref.dat", "rb")))
            self.serial = input('Enter Serial (char_limit = 20): ')
            dump(int(l) + 1, open("ref.dat", "wb"))
        elif a == "E":
            self.name = input('Enter Name (char_limit = 20): ')
            self.make = input('Enter Make (char_limit = 15): ')
            self.date = input('Enter Date Of Receipt [MM/DD/YYYY]: ')
            while datevali(self.date) == False:
                self.date = input('Enter Date Of Receipt [MM/DD/YYYY]: ')
            self.sent = input("Enter Model: ")

    def disp(self):
        print(self.name + " " * (20 - len(self.name)),
              "|\t",
              self.make + " " * (20 - len(self.make)),
              "\t|",
              self.sent + ' ' * (20 - len(self.sent)) + '\t|',
              self.serial + " " * (8 - len(self.serial)),
              "|\t",
              self.date,
              sep=" ")


def datevali(x):
    d = x.split("/")
    if int(d[1]) in [1, 3, 5, 7, 8, 10, 12]:
        if int(d[0]) <= 31:
            return True
        else:
            return False
    elif int(d[1]) in [4, 6, 9, 11]:
        if int(d[0]) <= 30:
            return True
        else:
            return False
    elif int(d[1]) == 2:
        if int(d[2]) % 400 == 0:
            if int(d[0]) <= 29:
                return True
            else:
                return False
        elif int(d[2]) % 100!= 0:
            if int(d[2]) % 4 == 0:
                if int(d[0]) <= 29:
                    return True
                else:
                    return False
            elif int(d[2]) % 4!= 0:
                if int(d[0]) <= 28:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False


def formatter():
    print("""
_________________________________________________________________________________________________
_________________________________________________________________________________________________
""")
    print("NAME" + " " * (20 - len("name")),
          "|\t",
          "MAKE" + " " * (20 - len('make')),
          "\t|",
          "MODEL" + ' ' * (20 - len('MODEL')) + '\t|',
          "SERIAL" + " " * 2,
          "|\t",
          "DATE")
    print("""-------------------------------------------------------------------------------------------------
""")


def create(a="wb"):
    if a == "wb":
        input('Are you sure?')
        ref = open("ref.dat", a)
        dump(0, ref)
        ref.close()
    f = open("data.dat", a)
    o1 = some_class()
    while True:
        o1.input()
        dump(o1, f)

        prompt = input('New Entry? (Y/N) :')
        if prompt.lower() == 'n':
            break
    f.close()


def disp():
    if not os.path.isfile('data.dat'):
        print ("""
File not found
Please recheck the root directory""")
    else:
        f = open("data.dat", "rb")
        try:
            formatter()
            while True:
                s1 = load(f)
                s1.disp()

        except EOFError:
            print("""
_________________________________________________________________________________________________
_________________________________________________________________________________________________

Data Loaded Successfully
""")
        except:
            print("Unknown Error")
        finally:
            f.close()


def search():
    if not os.path.isfile('data.dat'):
        print("""
File not found
Please recheck the root directory""")
    else:
        f = open("data.dat", "rb")
        o1 = some_class()
        k = 0
        ask = input("""search by?
1) Serial no.
2) Name
3) Make
4) Year of Birth
""")
        if ask == "1":
            st = input("Enter Serial No.: ")
        elif ask == "2":
            st = input("Enter Name: ")
        elif ask == "3":
            st = input("Enter Make: ")
        elif ask == "4":
            st = input("Enter Year Of Birth: ")
        try:
            formatter()
            while True:
                o1 = load(f)
                if ask == "1":
                    if o1.serial.lower() == st.lower():
                        o1.disp()
                        k += 1
                elif ask == "2":
                    if o1.name.lower() == st.lower():
                        o1.disp()
                        k += 1
                elif ask == "3":
                    if o1.make.lower() == st.lower():
                        o1.disp()
                        k += 1
                elif ask == "4":
                    if o1.date[-4:] == st:
                        o1.disp()
                        k += 1
        except EOFError:
            if k == 0:
                print("No Data Found")
            else:
                print("""
_________________________________________________________________________________________________
_________________________________________________________________________________________________

Entry Found
""")
        except:
            print("Unknown Error")
        finally:
            f.close()


def modify():
    if not os.path.isfile('data.dat'):
        print("""
File not found
Please recheck the root directory""")
    else:
        f = open("data.dat", "rb")
        t = open("temp.dat", "wb")
        o1 = some_class()
        k = 0
        st = input("Enter Serial no.: ")
        try:
            while True:
                o1 = load(f)
                if o1.serial.lower()!= st.lower():
                    dump(o1, t)
                else:
                    k += 1
                    o1.input("E")
                    dump(o1, t)
        except EOFError:
            if k == 0:
                print("Serial no. not found..")
            else:
                print("Record Modified Successfully")
        except:
            print("Unknown Error")
        finally:
            f.close()
            t.close()
        os.remove("data.dat")
        os.rename("temp.dat", "data.dat")


def delete():
    if not os.path.isfile('data.dat'):
        print ("""
File not found
Please recheck the root directory""")
    else:
        f = open("data.dat", "rb")
        t = open("temp.dat", "wb")
        o1 = some_class()
        k = 0
        st = input("Enter Serial no.: ")
        try:
            while True:
                o1 = load(f)
                if o1.serial.lower()!= st.lower():
                    dump(o1, t)
                else:
                    k += 1
        except EOFError:
            if k == 0:
                print("Serial no. not found..")
            else:
                print("Record deleted")
        except:
            print("Unknown Error")
        finally:
            f.close()
            t.close()
        os.remove("data.dat")
        os.rename("temp.dat", "data.dat")


while True:
    print("""
1) Delete All And Create New
2) Add
3) Display
4) Modify
5) Search
6) Delete
7) Exit

Enter Your Choice:
""")

    ch = input()
    if ch == '1':
        create()
    elif ch == '2':
        create("ab")
    elif ch == '3':
        disp()
    elif ch == '4':
        modify()
    elif ch == '5':
        search()
    elif ch == '6':
        delete()
    elif ch == '7':
        break
