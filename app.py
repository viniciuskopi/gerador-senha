import tkinter as tk
import random
import string

# Definindo variáveis globais
length_entry = None
numbers_var = None
lowercase_var = None
uppercase_var = None
special_chars_var = None
error_label = None
password_entry = None

def generate_password():
    global length_entry, numbers_var, lowercase_var, uppercase_var, special_chars_var, error_label, password_entry
    
    length_str = length_entry.get()
    error_label.config(text="")

    if not length_str:
        error_label.config(text="Informe um tamanho válido para a senha.")
        return

    length = int(length_str)
    use_numbers = numbers_var.get()
    use_lowercase = lowercase_var.get()
    use_uppercase = uppercase_var.get()
    use_special_chars = special_chars_var.get()

    valid_characters = ''
    if use_numbers:
        valid_characters += string.digits
    if use_lowercase:
        valid_characters += string.ascii_lowercase
    if use_uppercase:
        valid_characters += string.ascii_uppercase
    if use_special_chars:
        valid_characters += string.punctuation

    if not valid_characters:
        error_label.config(text="Selecione pelo menos um conjunto de caracteres.")
        return

    if length < (use_numbers + use_lowercase + use_uppercase + use_special_chars):
        error_label.config(text="Tamanho insuficiente para os requisitos selecionados.")
        return

    password = generate_valid_password(length, valid_characters)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def generate_valid_password(length, valid_characters):
    if not valid_characters:
        return ""

    password = ''
    if numbers_var.get():
        password += random.choice(string.digits)
        length -= 1

    if lowercase_var.get():
        password += random.choice(string.ascii_lowercase)
        length -= 1

    if uppercase_var.get():
        password += random.choice(string.ascii_uppercase)
        length -= 1

    for _ in range(length):
        password += random.choice(valid_characters)

    password = ''.join(random.sample(password, len(password)))  # Embaralhe a senha
    return password

def on_enter_pressed(event):
    generate_password()

app = tk.Tk()
app.title("Gerador de Senhas")
app.geometry("400x400")  # Tamanho da janela

# Tamanho da senha
length_label = tk.Label(app, text="Tamanho da Senha:", anchor="w", padx=10)
length_label.pack(fill="x")

length_entry = tk.Entry(app, font=("Courier", 12))
length_entry.bind("<Return>", on_enter_pressed)  # Adicione a ligação ao evento "Enter"
length_entry.pack(fill="x", padx=10)

# Opções para caracteres
options_frame = tk.Frame(app, bg="white")
options_frame.pack(fill="both", padx=10)

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(options_frame, text="Números", variable=numbers_var, anchor="w")
numbers_checkbox.pack(fill="x")

lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(options_frame, text="Letras minúsculas", variable=lowercase_var, anchor="w")
lowercase_checkbox.pack(fill="x")

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(options_frame, text="Letras maiúsculas", variable=uppercase_var, anchor="w")
uppercase_checkbox.pack(fill="x")

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(options_frame, text="Caracteres Especiais", variable=special_chars_var, anchor="w")
special_chars_checkbox.pack(fill="x")

# Botão de geração de senha
generate_button = tk.Button(app, text="Gerar Senha", command=generate_password, font=("Courier", 14))
generate_button.pack(pady=10)

# Campo de senha centralizado com fonte monoespaçada
password_entry = tk.Entry(app, font=("Courier", 14))
password_entry.pack(fill="x", padx=10)

# Rótulo para mensagens de erro
error_label = tk.Label(app, text="", fg="red")
error_label.pack()

app.mainloop()
