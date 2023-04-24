import tkinter as tk

offset = 1

def encode(text, offset):
    encoded = []
    for char in text:
        if char.isalpha():
            new_char = chr(((ord(char.lower()) - ord('a') + offset) % 26) + ord('a'))
            encoded.append(new_char.upper() if char.isupper() else new_char)
        elif char.isdigit():
            encoded.append(chr(((ord(char) - ord('0') + offset) % 10) + ord('0')))
        else:
            encoded.append(char)
    return ''.join(encoded)

def decode(text, offset):
    return encode(text, -offset)

def encode_text():
    input_text = textbox1.get("1.0", tk.END).strip()
    encoded_text = encode(input_text, offset)
    textbox2.delete("1.0", tk.END)
    textbox2.insert(tk.END, encoded_text)

def decode_text():
    input_text = textbox2.get("1.0", tk.END).strip()
    decoded_text = decode(input_text, offset)
    textbox1.delete("1.0", tk.END)
    textbox1.insert(tk.END, decoded_text)

def increment_offset():
    global offset
    offset = (offset + 1) % 26
    update_offset_label()

def decrement_offset():
    global offset
    offset = (offset - 1) % 26
    update_offset_label()

def update_offset_label():
    offset_label.config(text=f"{offset}, {-26 + offset}")

app = tk.Tk()
app.title("Encoder/Decoder")

frame1 = tk.Frame(app)
frame1.grid(row=0, column=0)

frame2 = tk.Frame(app)
frame2.grid(row=1, column=0)

# Decoded Text
textbox1 = tk.Text(frame1, wrap=tk.WORD, width=30, height=10)
textbox1.grid(row=0, column=0, padx=(10, 5), pady=10)

# Encoded Text
textbox2 = tk.Text(frame1, wrap=tk.WORD, width=30, height=10)
textbox2.grid(row=0, column=1, padx=(5, 10), pady=10)

# Encode >>
encode_button = tk.Button(frame2, text="Encode >>", command=encode_text)
encode_button.grid(row=0, column=0, padx=(10, 50), pady=(0, 10), sticky=tk.N)

# Offset -
decrement_offset_button = tk.Button(frame2, text="-", command=decrement_offset)
decrement_offset_button.grid(row=0, column=1, padx=2, pady=(0, 10), sticky=tk.NE)

# Offset Value
offset_label = tk.Label(frame2, text=f"{offset}, {-26 + offset}")
offset_label.grid(row=0, column=2, pady=(0, 10), sticky=tk.N)

# Offset +
increment_offset_button = tk.Button(frame2, text="+", command=increment_offset)
increment_offset_button.grid(row=0, column=3, padx=2, pady=(0, 10), sticky=tk.NW)

# << Decode
decode_button = tk.Button(frame2, text="<< Decode", command=decode_text)
decode_button.grid(row=0, column=4, padx=(50, 10), pady=(0, 10), sticky=tk.N)

app.mainloop()
