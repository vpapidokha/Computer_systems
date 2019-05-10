# python
# -*- coding: utf-8 -*-
import math
import sys
import os


def size_of_file_with_different_extension(file_name, extension):
    return os.stat(file_name.split(".")[0] + extension).st_size


def size_comparison(file_name, amount_of_information, extension):
    file_size = size_of_file_with_different_extension(file_name, extension)
    print("In case of using " + extension + ", we have next results:")
    if int(amount_of_information / 8) < int(file_size):
        print(" amount of information is less than file size for: " + str(file_size - amount_of_information / 8))
    else:
        if int(amount_of_information / 8) > int(fileSize):
            print(" amount of information is bigger than file size for: " + str(amount_of_information / 8 - file_size))
        else:
            print(" amount of information is the same as file size: " + str(amount_of_information))

#Testing lines

def to_bits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result


def base64_converter(line, temp_file, base64_alphabet):
    bytes = to_bits(line)
    counter = 0
    number = ''
    if len(bytes) % 6 == 2:
        bytes.extend([0, 0, 0, 0])
    elif len(bytes) % 6 == 4:
        bytes.extend([0, 0])
    else:
        pass
    for i in bytes:
        number = number + str(i)
        counter = counter + 1
        if counter == 6:
            index = int(number, 2)
            temp_file.write(base64_alphabet[index-1])
            number = ''
            counter = 0
    temp_file.write("\n")


def base64_text_info(file_name, base64_alphabet):
    base64_occurrence =[0]*(len(base64_alphabet) + 1)
    base64_frequency =[0]*(len(base64_alphabet) + 1)
    base64_amount_of_chars = 0
    base64_entropy = 0
    temp_file_name = "D:/temp/temp.txt"
    temp_file = open(temp_file_name, mode='r', encoding='utf-8')
    text = list(temp_file)

    for i in text:
        line = list(i)
        base64_amount_of_chars = base64_amount_of_chars + len(line)
        for c in range(len(base64_alphabet)):
            base64_occurrence[c] = base64_occurrence[c] + line.count(base64_alphabet[c])

    temp_file.close()

    for i in range(len(base64_alphabet)):
        base64_frequency[i] = base64_occurrence[i] / base64_amount_of_chars
        print(base64_alphabet[i] + " occurrence in the base64 coded text is: " + str(base64_occurrence[i]) +
              " and its frequency is: " + str(base64_frequency[i]))
        if base64_occurrence[i] != 0:
            base64_entropy = base64_entropy - (base64_frequency[i] * math.log2(base64_frequency[i]))
    print("The entropy of base64 coded text is: " + str(base64_entropy))
    base64_amount_of_info = base64_amount_of_chars * base64_entropy
    print("Amount of information in base64 coded text is: " + str(base64_amount_of_info) + " bit\n")
    size_comparison(file_name, base64_amount_of_info, ".txt")
    size_comparison(file_name, base64_amount_of_info, ".zip")
    size_comparison(file_name, base64_amount_of_info, ".tar")
    size_comparison(file_name, base64_amount_of_info, ".rar")
    size_comparison(file_name, base64_amount_of_info, ".xz")
    size_comparison(file_name, base64_amount_of_info, ".bz2")


########################################################################################################################
# Var definitions


base64_alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                   'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                   'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/', '=')
alphabet = ('а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я',
            ',', '.', '!', '?', '-', ':', ';')
occurrence = [0] * len(alphabet)
frequency = [0] * len(alphabet)
entropy = 0
amountOfChars = 0
amount_of_info = 0
fileName = sys.argv[1]
base = fileName.split(".")[0]
fileSize = os.stat(fileName).st_size
zipArchiveSize = size_of_file_with_different_extension(fileName, ".zip")
rarArchiveSize = size_of_file_with_different_extension(fileName, ".rar")
tarArchiveSize = size_of_file_with_different_extension(fileName, ".tar")
bz2ArchiveSize = size_of_file_with_different_extension(fileName, ".bz2")
xzArchiveSize = size_of_file_with_different_extension(fileName, ".xz")
file = open(sys.argv[1], mode='r', encoding='utf-8')
temp_file = open("D:/temp/temp.txt", mode='w', encoding='utf-8')
text = list(file)

########################################################################################################################
# Calculating occurrence, frequency and entropy

print(sys.argv[1] + "\n")
for i in text:
    base64_converter(i, temp_file, base64_alphabet)
    line = list(i)
    line = [e for e in line if e not in ("\n", "\ufeff")]
    amountOfChars = amountOfChars + len(line)
    for c in range(len(alphabet)):
        occurrence[c] = occurrence[c] + line.count(alphabet[c])
file.close()
temp_file.close()

for i in range(len(alphabet)):
    frequency[i] = occurrence[i]/amountOfChars
    print(alphabet[i] + " occurrence in the text is: " + str(occurrence[i]) + " and it frequency is: " +
          str(frequency[i]))
    if occurrence[i] != 0:
        entropy = entropy - (frequency[i] * math.log2(frequency[i]))
print("The entropy of text is: " + str(entropy))
amount_of_info = amountOfChars * entropy
print("Amount of information in text is: " + str(amount_of_info) + "\n")

########################################################################################################################
# Comparison of sizes

size_comparison(fileName, amount_of_info, ".txt")
size_comparison(fileName, amount_of_info, ".zip")
size_comparison(fileName, amount_of_info, ".tar")
size_comparison(fileName, amount_of_info, ".rar")
size_comparison(fileName, amount_of_info, ".xz")
size_comparison(fileName, amount_of_info, ".bz2")
print()
base64_text_info(fileName, base64_alphabet)
