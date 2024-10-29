import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin',
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
      `name` varchar(50) NOT NULL,
      PRIMARY KEY (`id`)   
      )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Subcontinents'] = ('''
      CREATE TABLE `subcontinents`(
      `id` int(2) NOT NULL AUTO_INCREMENT,
      `continent_id` int(2) NOT NULL,
      `name` varchar(50) NOT NULL,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`continent_id`) REFERENCES `continents`(`id`) ON DELETE CASCADE
      )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Country'] = ('''
      CREATE TABLE `country` (
      `id` int(4) NOT NULL AUTO_INCREMENT,
      `continent_id` int(2) NOT NULL,
      `subcontinent_id` int(2) NOT NULL,
      `name` varchar(100) NOT NULL,               
      `image_url` varchar(255) DEFAULT NULL,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`continent_id`) REFERENCES `continents`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`subcontinent_id`) REFERENCES `subcontinents`(`id`) ON DELETE CASCADE               
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['State/Province'] = ('''
      CREATE TABLE `states` (
      `id` int(8) NOT NULL AUTO_INCREMENT,
      `continent_id` int(2) NOT NULL,
      `subcontinent_id` int(2) NOT NULL,
      `country_id` int(4) NOT NULL,
      `name` varchar(50) NOT NULL,               
      PRIMARY KEY (`id`),
      FOREIGN KEY (`continent_id`) REFERENCES `continents`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`subcontinent_id`) REFERENCES `subcontinents`(`id`) ON DELETE CASCADE,
      FOREIGN KEY (`country_id`) REFERENCES `country`(`id`) ON DELETE CASCADE                            
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
      FOREIGN KEY (`country_id`) REFERENCES `country`(`id`) ON DELETE CASCADE                            
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
      FOREIGN KEY (`city_id`) REFERENCES `city`(`id`) ON DELETE CASCADE                            
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
      FOREIGN KEY (`place_id`) REFERENCES `place`(`id`) ON DELETE CASCADE                    
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
      FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE
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
continent_sql = 'INSERT INTO continents (name) VALUES (%s)'
continents = [
    ("Africa",), 
    ("America",),
    ("Asia",),
    ("Europe",),
    ("Oceania",)
]

try:
    for continent in continents:
        cursor.execute(continent_sql, continent)  # Inserção individual
    conn.commit()  # Confirmando a transação
    print("Continentes inseridos com sucesso.")
except mysql.connector.Error as err:
    print(f"Erro ao inserir continentes: {err}")

cursor.execute('select * from viajuntos.continents')
print(' -------------  Continents:  -------------')
for continent in cursor.fetchall():
    print(continents[1])

# inserindo subcontinentes
subcontinents_sql = 'INSERT INTO subcontinents (continent_id, name) VALUES (%s, %s)'
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
cursor.executemany(subcontinents_sql,subcontinents)

cursor.execute('select * from viajuntos.subcontinents')
print(' -------------  Subcontinents:  -------------')
for subcontinent in cursor.fetchall():
    print(subcontinents[1])

# Inserindo países
country_sql = 'INSERT INTO country (continent_id, subcontinent_id, name) VALUES (%s, %s, %s)'
countries = [
      # Northern Africa
      (1, 1, "Algeria"), 
      (1, 1, "Egypt"), 
      (1, 1, "Libya"), 
      (1, 1, "Mauritania"), 
      (1, 1, "Morocco"), 
      (1, 1, "Sahrawi Arab Democratic Republic"), 
      (1, 1, "Tunisia"),
      # West Africa
      (1, 2, "Benin"), 
      (1, 2, "Burkina Faso"), 
      (1, 2, "Cabo Verde"), 
      (1, 2, "Côte d'Ivoire"), 
      (1, 2, "Gambia"), 
      (1, 2, "Ghana"), 
      (1, 2, "Guinea-Bissal"), 
      (1, 2, "Guinea"), 
      (1, 2, "Liberia"), 
      (1, 2, "Mali"), 
      (1, 2, "Niger"), 
      (1, 2, "Nigeria"), 
      (1, 2, "Senegal"), 
      (1, 2, "Sierra Leone"), 
      (1, 2, "Togo"),
      # Central Africa
      (1, 3, "Burundi"),
      (1, 3, "Cameroon"),
      (1, 3, "Central African Republic"),
      (1, 3, "Chad"),
      (1, 3, "Congo"),
      (1, 3, "Democratic Republic of Congo"),
      (1, 3, "Equatorial Guinea"),
      (1, 3, "Gabon"),
      (1, 3, "São Tomé and Príncipe"),
      # East Africa
      (1, 4, "Comoros"),
      (1, 4, "Djibouti"),
      (1, 4, "Eritrea"),
      (1, 4, "Ethiopia"),
      (1, 4, "Kenya"),
      (1, 4, "Madagascar"),
      (1, 4, "Mauritius"),
      (1, 4, "Rwanda"),
      (1, 4, "Somalia"),
      (1, 4, "South Sudan"),
      (1, 4, "Sudan"),
      (1, 4, "Tanzania"),
      (1, 4, "Uganda"),
      # Southern Africa
      (1, 5, "Angola"),
      (1, 5, "Botswana"),
      (1, 5, "Lesotho"),
      (1, 5, "Malawi"),
      (1, 5, "Mozambique"),
      (1, 5, "Namibia"),
      (1, 5, "South Africa"),
      (1, 5, "Swaziland"),
      (1, 5, "Zambia"),
      (1, 5, "Zimbabwe"),
      # North America
      (2, 6, "Canada"),
      (2, 6, "United States of America"),
      (2, 6, "Mexico"),
      (2, 6, "Greenland"),
      (2, 6, "Bermuda"),
      (2, 6, "Saint Pierre and Miquelon"),
      # Central America
      (2, 7, "Anguilla"),
      (2, 7, "Antigua and Barbuda"),
      (2, 7, "Aruba"),
      (2, 7, "The Bahamas"),
      (2, 7, "Barbados"),
      (2, 7, "Bay Islands Department"),
      (2, 7, "Belize"),
      (2, 7, "Bonaire"),
      (2, 7, "British Virgin Islands"),
      (2, 7, "Cayman Islands"),
      (2, 7, "Costa Rica"),
      (2, 7, "Cuba"),
      (2, 7, "Curaçao"),
      (2, 7, "Dominica"),
      (2, 7, "Dominican Republic"),
      (2, 7, "El Salvador"),
      (2, 7, "Federal Dependencies of Venezuela"),
      (2, 7, "Grenada"),
      (2, 7, "Guadeloupe"),
      (2, 7, "Guatemala"),
      (2, 7, "Guyana"),
      (2, 7, "Haiti"),
      (2, 7, "Honduras"),
      (2, 7, "Jamaica"),
      (2, 7, "Martinique"),
      (2, 7, "Montserrat"),
      (2, 7, "Navassa Island"),
      (2, 7, "Nicaragua"),
      (2, 7, "Panama"),
      (2, 7, "Puerto Rico"),
      (2, 7, "Quintana Roo"),
      (2, 7, "Saba"),
      (2, 7, "San Andrés and Providencia"),
      (2, 7, "Saint Barthélemy"),
      (2, 7, "Saint Kitts and Nevis"),
      (2, 7, "Saint Lucia"),
      (2, 7, "Saint Martin"),
      (2, 7, "Saint Vincent and the Grenadines"),
      (2, 7, "Sint Eustatius"),
      (2, 7, "Sint Maarten"),
      (2, 7, "Suriname"),
      (2, 7, "Trinidad and Tobago"),
      (2, 7, "Turks and Caicos Islands"),
      (2, 7, "United States Virgin Islands"),
      # South America
      (2, 8, "Argentina"),
      (2, 8, "Bolivia"),
      (2, 8, "Brazil"), #107
      (2, 8, "Chile"),
      (2, 8, "Colombia"),
      (2, 8, "Ecuador"),
      (2, 8, "Falkland Islands"),
      (2, 8, "French Guiana"),
      (2, 8, "Guyana"),
      (2, 8, "Paraguay"),
      (2, 8, "Peru"),
      (2, 8, "South Georgia and the South Sandwich Islands"),
      (2, 8, "Suriname"),
      (2, 8, "Uruguay"),     
      (2, 8, "Venezuela"),   
      # Central Asia
      # Middle Asia
      # South Asia 
      # Southeast Asia
      # East Asia
      # Northern Europe
      # Southern Europe
      # Western Europe
      # Central-Eastern Europe
      # Australasia
      # Melanesia
      # Micronesia
      # Polynesia     

]
cursor.executemany(country_sql, countries)

cursor.execute('select * from viajuntos.country')
print(' -------------  Country:  -------------')
for country in cursor.fetchall():
    print(countries[2])

states_sql = 'INSERT INTO states (continent_id, subcontinent_id, country_id, name) VALUES (%s, %s, %s, %s)'
states = [
     #Brazil
    (2, 8, 107, "Acre"),
    (2, 8, 107, "Alagoas"),
    (2, 8, 107, "Amapá"),
    (2, 8, 107, "Amazonas"),
    (2, 8, 107, "Bahia"),
    (2, 8, 107, "Ceará"),
    (2, 8, 107, "Distrito Federal"),
    (2, 8, 107, "Espírito Santo"),
    (2, 8, 107, "Maranhão"),
    (2, 8, 107, "Mato Grosso"),
    (2, 8, 107, "Mato Grosso do Sul"),
    (2, 8, 107, "Minas Gerais"),
    (2, 8, 107, "Pará"),
    (2, 8, 107, "Paraíba"),
    (2, 8, 107, "Paraná"),
    (2, 8, 107, "Pernambuco"),
    (2, 8, 107, "Piauí"),
    (2, 8, 107, "Rio de Janeiro"),
    (2, 8, 107, "Rio Grande do Norte"),
    (2, 8, 107, "Rio Grande do Sul"),
    (2, 8, 107, "Rondônia"),
    (2, 8, 107, "Roraima"),
    (2, 8, 107, "Santa Catarina"),
    (2, 8, 107, "São Paulo"),
    (2, 8, 107, "Sergipe"),
    (2, 8, 107, "Tocantins"),
]
cursor.executemany(states_sql, states)

cursor.execute('SELECT * FROM states')
print(' -------------  States/Province:  -------------')
for state in cursor.fetchall():
    print(state)




conn.commit()
cursor.close()
conn.close()