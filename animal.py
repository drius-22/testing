import  sys




def dog():
    print ("hua  !  ")


def default():
    print('What is up ????')

def main():
    if sys.argv[1]== 'dog':
        dog()
    else:
        default()

if __name__ == '__main__':
    main()