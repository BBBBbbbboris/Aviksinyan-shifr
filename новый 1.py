import tkinter as tk

# Функция перевода текста на авиксинский шифр
def translate_to_aviksin():
    aviksin_alphabet = {
        'А': '#67467#', 'Б': '#42325#', 'В': '#39862#', 'Г': '#98165#', 'Д': '#21398#', 'Е': '#56984#', 'Ё': '#92584#',
        'Ж': '#78356#', 'З': '#21456#', 'И': '#39568#', 'Й': '#69325#', 'К': '#52314#', 'Л': '#98532#', 'М': '#25689#',
        'Н': '#17465#', 'О': '#43678#', 'П': '#75698#', 'Р': '#31254#', 'С': '#36947#', 'Т': '#47856#', 'У': '#63257#',
        'Ф': '#94758#', 'Х': '#14567#', 'Ц': '#78439#', 'Ч': '#24568#', 'Ш': '#74893#', 'Щ': '#23548#', 'Ъ': '#64875#',
        'Ы': '#91324#', 'Ь': '#56982#', 'Э': '#82379#', 'Ю': '#17925#', 'Я': '#98564#'
    }
    
    text = input_field.get().upper()
    translated_text = ''
    
    for letter in text:
        if letter in aviksin_alphabet:
            translated_text += aviksin_alphabet[letter]
        else:
            translated_text += letter
    
    output_field.configure(state='normal')
    output_field.delete('1.0', tk.END)
    output_field.insert(tk.END, translated_text)
    output_field.configure(state='disabled')
    
# Создание окна
window = tk.Tk()
window.title('Переводчик на авиксинский шифр')
window.geometry('400x300')

# Создание элементов интерфейса
input_label = tk.Label(text='Введите текст на русском языке:')
input_label.pack()

input_field = tk.Entry(width=40)
input_field.pack()

translate_button = tk.Button(text='Перевести', command=translate_to_aviksin)
translate_button.pack()

output_label = tk.Label(text='Текст на авиксинском шифре:')
output_label.pack()

output_field = tk.Text(width=40, height=10)
output_field.pack()
output_field.configure(state='disabled')

# Запуск главного цикла окна
window.mainloop()
