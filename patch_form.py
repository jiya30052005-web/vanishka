from bs4 import BeautifulSoup

file_path = r'c:\Users\KISHORI CHARPE\Downloads\vanishka-main\vanishka-main\computerbaba-redesign\contact.html'
with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

form = soup.find('form')
if form:
    form['id'] = 'contactInquiryForm'
    inputs = form.find_all('input')
    if len(inputs) >= 3:
        inputs[0]['id'] = 'contactName'
        inputs[1]['id'] = 'contactPhone'
        # inputs[2] is Email
    
    select = form.find('select')
    if select:
        select['id'] = 'contactCategory'
        
    textarea = form.find('textarea')
    if textarea:
        textarea['id'] = 'contactMessage'

    # The button needs to be type submit
    button = form.find('button')
    if button:
        button['type'] = 'submit'

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Form IDs patched successfully!")
else:
    print("Form not found in contact.html")
