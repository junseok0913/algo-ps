num_list = []
while True:
    num_list.append(list(map(str, input())))
    if num_list[-1] == ['0']:
        num_list.pop()
        break

for n_s in num_list:
    half = len(n_s)//2
    if len(n_s)%2 == 0:
        if n_s[:half] == list(reversed(n_s[half:])):
            print('yes')
        else:
            print('no')
    else:
        if n_s[:half] == list(reversed(n_s[half+1:])):
            print('yes')
        else:
            print('no')
