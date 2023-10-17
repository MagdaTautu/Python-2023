
#2
#result = " ".join(hex(n)[2:] for n in range(ord('A'),ord('A')+26))
#print(result)

#ALTA METODA

#----------------(0-9)
start_char = '0'  # Caracterul de start
num_elements = 10  # Numărul de elemente din range
ascii_hex_list = [f'{ord(start_char) + i:02x}' for i in range(num_elements)]
# Adaugam spații 
ascii_hex_string = ' '.join(ascii_hex_list)
print("de la 0 la 9: " + ascii_hex_string)

#----------------(a-z)
start_char = 'a'
num_elements = 26 

ascii_hex_list = [f'{ord(start_char) + i:02x}' for i in range(num_elements)]
ascii_hex_string = ' '.join(ascii_hex_list)
print("de la a la z: " + ascii_hex_string)

#----------------(A-Z)
start_char = 'A'
num_elements = 26 

ascii_hex_list = [f'{ord(start_char) + i:02x}' for i in range(num_elements)]
ascii_hex_string = ' '.join(ascii_hex_list)
print("de la A la Z: " + ascii_hex_string)
