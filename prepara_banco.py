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
TABLES['Users'] = ('''
      CREATE TABLE `users` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `username` varchar(25) NOT NULL,
      `name` varchar(50) NOT NULL, 
      `email` varchar(60) NOT NULL,
      `password_hash` varchar(100) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Continents'] = ('''
      CREATE TABLE `continents`(
      `id` int(2) NOT NULL AUTO_INCREMENT,
      `name` varchar(25) NOT NULL,
      PRIMARY KEY (`id`)   
      )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Subcontinents'] = ('''
      CREATE TABLE `subcontinents`(
      `id` int(2) NOT NULL AUTO_INCREMENT,
      `continent_id` int(2) NOT NULL,
      `name` varchar(25) NOT NULL,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`continent_id`) REFERENCES `continents`(`id`) ON DELETE CASCADE
      )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Country'] = ('''
      CREATE TABLE `country` (
      `id` int(4) NOT NULL AUTO_INCREMENT,
      `name` varchar(25) NOT NULL,               
      `continent_id` int(2) NOT NULL,
      `subcontinent_id` int(2) NOT NULL,
      `image_url` varchar(255) NOT NULL,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`continent_id`) REFERENCES `continents`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`subcontinent_id`) REFERENCES `subcontinents`(`id`) ON DELETE CASCADE               
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['State/Province'] = ('''
      CREATE TABLE `state` (
      `id` int(8) NOT NULL AUTO_INCREMENT,
      `name` varchar(25) NOT NULL,               
      `continent_id` int(2) NOT NULL,
      `subcontinent_id` int(2) NOT NULL,
      `country_id` int(4) NOT NULL,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`continent_id`) REFERENCES `continents`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`subcontinent_id`) REFERENCES `subcontinents`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`country_id`) REFERENCES `country`(`id`) ON DELETE CASCADE,                            
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['City/Village'] = ('''
      CREATE TABLE `city` (
      `id` int(12) NOT NULL AUTO_INCREMENT,
      `name` varchar(25) NOT NULL,               
      `continent_id` int(2) NOT NULL,
      `subcontinent_id` int(2) NOT NULL,
      `country_id` int(4) NOT NULL,
      `state_id`int(8) NOT NULL,                  
      PRIMARY KEY (`id`),
      FOREIGN KEY (`continent_id`) REFERENCES `continents`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`subcontinent_id`) REFERENCES `subcontinents`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`country_id`) REFERENCES `country`(`id`) ON DELETE CASCADE,                            
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Place'] = ('''
      CREATE TABLE `place` (
      `id` int(16) NOT NULL AUTO_INCREMENT,
      `name` varchar(25) NOT NULL,               
      `continent_id` int(2) NOT NULL,
      `subcontinent_id` int(2) NOT NULL,
      `country_id` int(4) NOT NULL,
      `state_id` int(8) NOT NULL,
      `city_id` int(12) NOT NULL,                 
      PRIMARY KEY (`id`),
      FOREIGN KEY (`continent_id`) REFERENCES `continents`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`subcontinent_id`) REFERENCES `subcontinents`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`country_id`) REFERENCES `country`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`state_id`) REFERENCES `state`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`city_id`) REFERENCES `city`(`id`) ON DELETE CASCADE,                            
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Avaliacoes'] = ('''
      CREATE TABLE `avaliacoes` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `continent_id` int(2) NOT NULL,
      `subcontinent_id` int(2) NOT NULL,
      `country_id` int(4) NOT NULL,
      `state_id` int(8) NOT NULL, 
      `city_id` int(12) NOT NULL,
      `place_id` int(16) NOT NULL,                                                
      `user_id` int(11) NOT NULL,                
      `security_rating` int(1) NOT NULL,
      `solo_woman_rating` int(1) NOT NULL,
      `hospitality_rating` int(1) NOT NULL,
      `accessibility_rating` int(1) NOT NULL,                 
      `content` text NOT NULL, 
      `created_at` DATETIME,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE
      FOREIGN KEY (`continent_id`) REFERENCES `continents`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`subcontinent_id`) REFERENCES `subcontinents`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`country_id`) REFERENCES `country`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`state_id`) REFERENCES `state`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`place_id`) REFERENCES `place`(`id`) ON DELETE CASCADE,                    
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Comentarios'] = ('''
      CREATE TABLE `comentarios` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `place_id` int(16) NOT NULL,
      `user_id` int(11) NOT NULL,
      `content` text NOT NULL,
      `image_url` varchar(255) NOT NULL,              
      `created_at` DATETIME,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`place_id`) REFERENCES `place`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`user_id`) REFERENCES `usuarios`(`id`) ON DELETE CASCADE
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
user_sql = 'INSERT INTO users (username, name, email, password_hash) VALUES (%s, %s, %s, %s)'
users = [
      ("vicotira", "Victória Rocha", "victoria_rocha_26@hotmail.com", "123456"),
]
cursor.executemany(user_sql, users)

cursor.execute('select * from viajuntos.users')
print(' -------------  Users:  -------------')
for user in cursor.fetchall():
    print(user[1])

#inserindo continentes
continent_sql = 'INSERT INTO continents (name) VALUES (%s, %s, %s, %s)'
continents = [
      ("Africa"),
      ("America"),
      ("Asia"),
      ("Europe"),
      ("Oceania"),
]
cursor.executemany(continent_sql,continents)

cursor.execute('select * from viajuntos.continents')
print(' -------------  Continents:  -------------')
for continent in cursor.fetchall():
    print(continents[1])

# inserindo subcontinentes
subcontinent_sql = 'INSERT INTO subcontinents (continent_id, name) VALUES (%d, %s)'
subcontinents = [
      (1, "Northern Africa"),
      (1, "West Africa"),
      (1, "Central Africa"),
      (1, "East Africa"),
      (1, "Southern Africa"),
      (2, "North America"),
      (2, "Central America"),
      (2, "South America"),
      (3, "Central Asia"),
      (3, "Middle Asia"),
      (3, "South Asia"),
      (3, "Southeast Asia"),
      (3, "East Asia"),
      (4, "Northern Europe"),
      (4, "Southern Europe"),
      (4, "Western Europe"),
      (4, "Central-Eastern Europe"),
      (5, "Australasia"),
      (5, "Melanesia"),
      (5, "Micronesia"),
      (5, "Polynesia"),
]
cursor.executemany(subcontinent_sql,subcontinents)

cursor.execute('select * from viajuntos.subcontinents')
print(' -------------  Subcontinents:  -------------')
for subcontinent in cursor.fetchall():
    print(subcontinents[1])

# Inserindo países





conn.commit()
cursor.close()
conn.close()