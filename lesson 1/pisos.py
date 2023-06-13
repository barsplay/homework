def palindrome_check(string:str):
    # если строка == перевёрнутой строке (перевернул при помощи среза строки)
    if string == string[::-1]:
        return True
    else:
        return False

print(palindrome_check("лепсспел"))