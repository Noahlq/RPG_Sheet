def insertAccount(user, password):
    arquivo = open('database.txt', 'a')
    arquivo.write(f'{user} {password}\n')

    return {"user": user, "password": password}
