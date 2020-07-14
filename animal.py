import  sys

#comment 

def cat():
    print ("meow!")

def default():
    print('What is up ????')

def main():
    if sys.argv[1] == 'cat':
        cat()
    else :
        default()

if __name__ == '__main__':
    main()