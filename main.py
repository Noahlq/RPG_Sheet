def insertAccount(user, password):
    arquivo = open('database.txt', 'a')
    arquivo.write(f'{password} {user}\n')

    return {"user": user, "password": password}
