binary_file=open("binaty_file.bin", mode="wb+")
text="hello 123"
encoded=text.encode("utf-8")
binary_file.write(encoded)
binary_file.seek(0)
binary_data=binary_file.read()
print("binary:", binary_data)
text=binary_data.decode("utf-8")
print("Decoded data:", text)

for byte in binary_data:
    print(byte)