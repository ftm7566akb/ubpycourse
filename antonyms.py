
antonym = dict()
while (1):
    print('enter a word :')
    str = input()
    if str in antonym.keys():
            print('the antonym of', str, 'is', antonym[str])

    else:

            print('I dont know the antonym of', str, 'do you know?...yes/no?')
            result = input()
            if result == 'yes':
                print('what is it?')
                answer = input()
                antonym[str] = answer
                antonym[answer] = str

            else:

                 continue
