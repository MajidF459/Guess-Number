import random
def get_vallid_int(prompt):#ورودی فقط عدد صحیح
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('invalid input! please enter a valid number ')
while True:
    low =get_vallid_int('number one ')
    high= get_vallid_int('number two ')
    if high > low:
            break
    print('number tow must be greeter than number one! please try again')
list_between_inputs= list(range(low,1+high))# لیست بین ورودی ها و خودشون
input_distances=high-low+1 #فاصله ورودی ها 
r=random.randint(low,high) 
#guess_count تعداد حدس
if input_distances> 10:
    guess_count=random.randint(5,7)
else:
    guess_count=random.randint(1,input_distances)
rotation=0 #چرخش
count=set()
while rotation<guess_count:
    try:
        if new_guess in count:
            list_between_inputs.remove(new_guess)
    except:
        pass
    print(list_between_inputs)
    print(count)
    try: 
        print("_"*20)   
        new_guess_str=input(f'remained guess: {guess_count-(rotation)} => enter your next guess: ')
        new_guess=int(new_guess_str)
        if new_guess in count:
            rotation-=1
            print("_"*20)
        if new_guess in list_between_inputs:
            if r == new_guess:
                print('great! your guess is correct!')
                print("_"*20)
                break
            elif r> new_guess:
                print('your guess is lower >> then selected number')
                print("_"*20)
                count.add(new_guess)
            else:
                print('your guess is higher << then selected number')
                print("_"*20)
                count.add(new_guess) 
            guess_count-=1
            if rotation==guess_count:
                print(f'The Right Answer is {r} ')
                print("_"*20)
                break
    except:
        print('plase enter a valid number')