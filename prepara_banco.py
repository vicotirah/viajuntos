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
      `subcontinent_id` int(2) NOT NULL,
      `name` varchar(100) NOT NULL,               
      `image_url` varchar(255) DEFAULT NULL,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`subcontinent_id`) REFERENCES `subcontinents`(`id`) ON DELETE CASCADE               
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['State/Province'] = ('''
      CREATE TABLE `states` (
      `id` int(8) NOT NULL AUTO_INCREMENT,
      `country_id` int(4) NOT NULL,
      `name` varchar(50) NOT NULL,               
      PRIMARY KEY (`id`),
      FOREIGN KEY (`country_id`) REFERENCES `country`(`id`) ON DELETE CASCADE                            
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['City/Village'] = ('''
      CREATE TABLE `city` (
      `id` int(12) NOT NULL AUTO_INCREMENT,
      `state_id`int(8) NOT NULL, 
      `name` varchar(25) NOT NULL,                   
      PRIMARY KEY (`id`),
      FOREIGN KEY (`state_id`) REFERENCES `country`(`id`) ON DELETE CASCADE                            
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Place'] = ('''
      CREATE TABLE `place` (
      `id` int(16) NOT NULL AUTO_INCREMENT,
      `name` varchar(25) NOT NULL,               
      `city_id` int(12) NOT NULL,                 
      PRIMARY KEY (`id`),
      FOREIGN KEY (`city_id`) REFERENCES `city`(`id`) ON DELETE CASCADE                            
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Avaliacoes'] = ('''
      CREATE TABLE `avaliacoes` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `place_id` int(16) NOT NULL,                                                
      `user_id` int(11) NOT NULL,                
      `security_rating` int(1) NOT NULL,
      `solo_woman_rating` int(1) NOT NULL,
      `hospitality_rating` int(1) NOT NULL,
      `accessibility_rating` int(1) NOT NULL,
      `cuisine_rating` int(1) NOT NULL,                                   
      `content` text NOT NULL, 
      PRIMARY KEY (`id`),
      FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE
      FOREIGN KEY (`place_id`) REFERENCES `place`(`id`) ON DELETE CASCADE                    
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Comentarios'] = ('''
      CREATE TABLE `comentarios` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `place_id` int(16) NOT NULL,                                                
      `user_id` int(11) NOT NULL,                
      `comment` varchar(150) NOT NULL,
      PRIMARY KEY (`id`),
      FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE
      FOREIGN KEY (`place_id`) REFERENCES `place`(`id`) ON DELETE CASCADE                    
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
country_sql = 'INSERT INTO country (continent_id, subcontinent_id, name) VALUES (%s, %s)'
countries = [
      # Northern Africa
      (1, "Algeria"), 
      (1, "Egypt"), 
      (1, "Libya"), 
      (1, "Mauritania"), 
      (1, "Morocco"), 
      (1, "Sahrawi Arab Democratic Republic"), 
      (1, "Tunisia"),
      # West Africa
      (2, "Benin"), 
      (2, "Burkina Faso"), 
      (2, "Cabo Verde"), 
      (2, "Côte d'Ivoire"), 
      (2, "Gambia"), 
      (2, "Ghana"), 
      (2, "Guinea-Bissal"), 
      (2, "Guinea"), 
      (2, "Liberia"), 
      (2, "Mali"), 
      (2, "Niger"), 
      (2, "Nigeria"), 
      (2, "Senegal"), 
      (2, "Sierra Leone"), 
      (2, "Togo"),
      # Central Africa
      (3, "Burundi"),
      (3, "Cameroon"),
      (3, "Central African Republic"),
      (3, "Chad"),
      (3, "Congo"),
      (3, "Democratic Republic of Congo"),
      (3, "Equatorial Guinea"),
      (3, "Gabon"),
      (3, "São Tomé and Príncipe"),
      # East Africa
      (4, "Comoros"),
      (4, "Djibouti"),
      (4, "Eritrea"),
      (4, "Ethiopia"),
      (4, "Kenya"),
      (4, "Madagascar"),
      (4, "Mauritius"),
      (4, "Rwanda"),
      (4, "Somalia"),
      (4, "South Sudan"),
      (4, "Sudan"),
      (4, "Tanzania"),
      (4, "Uganda"),
      # Southern Africa
      (5, "Angola"),
      (5, "Botswana"),
      (5, "Lesotho"),
      (5, "Malawi"),
      (5, "Mozambique"),
      (5, "Namibia"),
      (5, "South Africa"),
      (5, "Swaziland"),
      (5, "Zambia"),
      (5, "Zimbabwe"),
      # North America
      (6, "Canada"),
      (6, "United States of America"),
      (6, "Mexico"),
      (6, "Greenland"),
      (6, "Bermuda"),
      (6, "Saint Pierre and Miquelon"),
      # Central America
      (7, "Anguilla"),
      (7, "Antigua and Barbuda"),
      (7, "Aruba"),
      (7, "The Bahamas"),
      (7, "Barbados"),
      (7, "Bay Islands Department"),
      (7, "Belize"),
      (7, "Bonaire"),
      (7, "British Virgin Islands"),
      (7, "Cayman Islands"),
      (7, "Costa Rica"),
      (7, "Cuba"),
      (7, "Curaçao"),
      (7, "Dominica"),
      (7, "Dominican Republic"),
      (7, "El Salvador"),
      (7, "Federal Dependencies of Venezuela"),
      (7, "Grenada"),
      (7, "Guadeloupe"),
      (7, "Guatemala"),
      (7, "Guyana"),
      (7, "Haiti"),
      (7, "Honduras"),
      (7, "Jamaica"),
      (7, "Martinique"),
      (7, "Montserrat"),
      (7, "Navassa Island"),
      (7, "Nicaragua"),
      (7, "Panama"),
      (7, "Puerto Rico"),
      (7, "Quintana Roo"),
      (7, "Saba"),
      (7, "San Andrés and Providencia"),
      (7, "Saint Barthélemy"),
      (7, "Saint Kitts and Nevis"),
      (7, "Saint Lucia"),
      (7, "Saint Martin"),
      (7, "Saint Vincent and the Grenadines"),
      (7, "Sint Eustatius"),
      (7, "Sint Maarten"),
      (7, "Suriname"),
      (7, "Trinidad and Tobago"),
      (7, "Turks and Caicos Islands"),
      (7, "United States Virgin Islands"),
      # South America
      (8, "Argentina"),
      (8, "Bolivia"),
      (8, "Brazil"), #107
      (8, "Chile"),
      (8, "Colombia"),
      (8, "Ecuador"),
      (8, "Falkland Islands"),
      (8, "French Guiana"),
      (8, "Guyana"),
      (8, "Paraguay"),
      (8, "Peru"),
      (8, "South Georgia and the South Sandwich Islands"),
      (8, "Suriname"),
      (8, "Uruguay"),     
      (8, "Venezuela"),   
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

states_sql = 'INSERT INTO states (continent_id, subcontinent_id, country_id, name) VALUES (%s, %s)'
states = [
     #Brazil
    (107, "Acre"),
    (107, "Alagoas"),
    (107, "Amapá"),
    (107, "Amazonas"),
    (107, "Bahia"),
    (107, "Ceará"),
    (107, "Distrito Federal"),
    (107, "Espírito Santo"),
    (107, "Goiás")
    (107, "Maranhão"),
    (107, "Mato Grosso"),
    (107, "Mato Grosso do Sul"),
    (107, "Minas Gerais"),
    (107, "Pará"),
    (107, "Paraíba"),
    (107, "Paraná"),
    (107, "Pernambuco"),
    (107, "Piauí"),
    (107, "Rio de Janeiro"),
    (107, "Rio Grande do Norte"),
    (107, "Rio Grande do Sul"),
    (107, "Rondônia"),
    (107, "Roraima"),
    (107, "Santa Catarina"),
    (107, "São Paulo"),
    (107, "Sergipe"),
    (107, "Tocantins"),
]
cursor.executemany(states_sql, states)

cursor.execute('SELECT * FROM states')
print(' -------------  States/Province:  -------------')
for state in cursor.fetchall():
    print(states)

cities_sql = 'INSERT INTO states (state_id, name) VALUES (%s, %s)'
cities = [
     # --- BRASIL ---
     (1, "Rio Branco"), # Acre
     (2, "Maceió"), # Alagoas
     (3, "Macapá"), # Amapá
     (4, "Manaus"), # Amazonas
     (5, "Salvador"), # Bahia
     (5, "Porto Seguro"),
     (5, "Recife de Fora"),
     (5, "Trancoso"),
     (5, "Arraial D'Ajuda"),
     (5, "Vila de Caraíva"),
     (5, "Santa Cruz de Cabrália")
     (6, "Fortaleza"), # Ceará
     (6, "Paracuru"),
     (6, "Beberibe"),
     (6, "Aracati"),
     (7, "Brasília"), # DF
     (8, "Vitória"), # Espirito Santo
     (9, "Goiânia"), # Goiás
     (9, "Caldas Novas")
     (10, "São Luís"), # Maranhão
     (11, "Cuiabá"), # Mato Grosso
     (12, "Campo Grande"), # Mato Grosso do Sul
     (13, "Belo Horizonte"), # Minas Gerais
     (13, "Extrema"),
     (13, "Bueno Brandão"),
     (13, "São Thomé das Letras"),
     (13, "Três Corações")
     (14, "Belém"), #Pará
     (15, "João Pessoa"), #Paraíba
     (15, "Cabedelo")
     (16, "Curitiba"), #Paraná
     (17, "Recife"), #Pernambuco
     (17, "Porto de Galinhas"),
     (17, "Olinda"),
     (17, "Saloá")
     (18, "Teresina"), #Piauí
     (19, "Rio de Janeiro"), #Rio de Janeiro
     (20, "Natal"), #Rio Grande do Norte
     (20, "São Miguel do Gostoso"),
     (21, "Porto Alegre"), # Rio Grande do Sul
     (22, "Porto Velho"), # Rondônia
     (23, "Boa Vista"), # Roraima
     (24, "Florianópolis"), # Santa Catarina
     (25, "São Paulo"), # Sao Paulo
     (25, "Atibaia"),
     (25, "Bragança Paulista"),
     (25, "Campinas"),
     (26, "Aracaju"), # Sergipe
     (27, "Palmas"), # Tocantins
]

cursor.executemany(cities_sql, cities)

cursor.execute('SELECT * FROM cities')
print(' -------------  Cities:  -------------')
for city in cursor.fetchall():
    print(cities)

conn.commit()
cursor.close()
conn.close()
