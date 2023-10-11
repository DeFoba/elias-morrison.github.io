from bs4 import BeautifulSoup
from random import choice

import string

with open('index.html', 'r', encoding='utf-8') as file:
    file = file.read()

html = BeautifulSoup(file, 'html.parser')
sections = html.find_all('section')

# html.find_all(string=str)

const_list = []

main_dict = {}

for section in sections:
    main_class = section.get('class')[-1].split('-')[-1]
    main_dict[main_class] = []

    section['id'] = 'js_text_prevent_override_' + main_class

    count = 0 
    for span in section.find_all('span'):
        main_dict[main_class].append(span.text.strip())
        span['id'] = str('js_text_prevent_override_' + main_class + '_' + ''.join([choice(string.ascii_letters) for x in range(5)]))
        const_list.append(f'const {main_class}_{count} = document.getElementById("{span["id"]}").textContent; // {span.text.strip()}')
        count += 1
        # print(span['id'])

# print(str(html))
with open('new.html', 'w', encoding='utf-8') as nf:
    nf.write(html.prettify())

print(*const_list, sep='\n')

# print(main_dict)