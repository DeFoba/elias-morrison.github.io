start_text = open('enter.txt', 'r').read()
var_keys = input('Enter var key with ",": ').replace('(', '').replace(')', '').replace(' ', '').split(',')
values = input('Enter values: ').replace('(', '').replace(')', '').replace(' ', '').split(',')

with open('output.js', 'w') as file:
    start_text = 'let result = ' + start_text
    count = 0
    for var in var_keys:
        start_text = start_text.replace(f': {var}', f': {values[count]}').replace(f' {var},', f' {values[count]},')
        count += 1

    file.write(start_text)