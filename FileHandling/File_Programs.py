# write a python program to get all the email from given files

def get_all_emails(filename):
    email = []
    with open(filename, "r") as file:
        file_lines = file.readlines()
        print(file_lines)
        for line in file_lines:
            word_list = line.split(" ")
            for word in word_list:
                if "@" in word:
                    email.append(word)
                else:
                    continue

    return email

output = get_all_emails('read_data_email.txt')
print(output)

def replace_words_in_the_file(filename, word1, word2):
    with open(filename, "r") as file:
       filedata = file.read()
       modify_data = filedata.replace(word1, word2)

    with open(filename, "w") as file:
        file.write(modify_data)


replace_words_in_the_file("read_data_email.txt", "JAVA", "Python")