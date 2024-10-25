import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `viajuntos`;")

cursor.execute("CREATE DATABASE `viajuntos`;")

cursor.execute("USE `viajuntos`;")

# criando tabelas
TABLES = {}
TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `username` varchar(25) NOT NULL,
      `name` varchar(50) NOT NULL, 
      `email` varchar(60) NOT NULL,
      `password_hash` varchar(100) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Postagens'] = ('''
      CREATE TABLE `postagens` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `user_id` int(11) NOT NULL,                
      `title` varchar(50) NOT NULL,
      `content` text NOT NULL, 
      `image_url` varchar(255) NOT NULL,
      `created_at` DATETIME,
      PRIMARY KEY (`id`)
      FOREIGN KEY (`user_id`) REFERENCES `usuarios`(`id`) ON DELETE CASCADE
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Avaliacoes'] = ('''
      CREATE TABLE `avaliacoes` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `post_id` int(100) NOT NULL,
      `user_id` int(11) NOT NULL,                
      `security_rating` int(1) NOT NULL,
      `solo_woman_rating` int(1) NOT NULL,
      `hospitality_rating` int(1) NOT NULL,
      `accessibility_rating` int(1) NOT NULL,                 
      `content` text NOT NULL, 
      `image_url` varchar(255) NOT NULL,
      `created_at` DATETIME,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`post_id`) REFERENCES `postagens`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`user_id`) REFERENCES `usuarios`(`id`) ON DELETE CASCADE
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Comentarios'] = ('''
      CREATE TABLE `comentarios` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `post_id` int(11) NOT NULL,
      `user_id` int(11) NOT NULL,
      `content` text NOT NULL,
      `image_url` varchar(255) NOT NULL,              
      `created_at` DATETIME,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`post_id`) REFERENCES `postagens`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`user_id`) REFERENCES `usuarios`(`id`) ON DELETE CASCADE
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Seguidores'] = ('''
      CREATE TABLE `seguidores` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `follower_id` int(100) NOT NULL,
      `followed_id` int(100) NOT NULL,          
      `created_at` DATETIME,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`follower_id`) REFERENCES `usuarios`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`followed_id`) REFERENCES `usuarios`(`id`) ON DELETE CASCADE
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (username, nome, email, password_hash) VALUES (%s, %s, %s, %s)'
usuarios = [
      ("vicotira", "Victória Rocha", "victoria_rocha_26@hotmail.com", "123456"),
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from viajuntos.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])



conn.commit()
cursor.close()
conn.close()