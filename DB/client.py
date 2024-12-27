import sqlite3

connect = sqlite3.connect('clients.db')
cursor = connect.cursor()

def create_db():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
        )
    """)

connect.commit()
create_db()

def add_client(name, age, hobby=""):
    cursor.execute('INSERT INTO USERS(name, age, hobby ) VALUES (?,?,?)', (name, age, hobby))
    connect.commit()
    print(f'Пользователь {name} дабвлен')

def get_all_clients():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    if users:
        print(f"Список всех пользователей:")
        for user in users:
            print(f'Name: {user[1]}, age: {user[2]}')
    else:
        print(f'Список пользователей пуст')

def update_client_name(id, name):
    cursor.execute(
        'UPDATE users SET name = ? WHERE id = ?',
    (name, id)
    )
    connect.commit()

def delete_client(id):
    cursor.execute('DELETE FROM users WHERE id = ?', (id,))
    connect.commit()

# add_client('Джек Воробей', 48, 'Пиратство')
# add_client('Тор', 3000, 'Битвы')
# add_client('Брюс', 37, 'Бэтмэн')
# add_client('Локи', 2800, 'Фокусы')

# update_client_name(2, 'Тор Одинсон')

# delete_client(4)

get_all_clients()

connect.close()