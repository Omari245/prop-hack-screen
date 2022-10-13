import time
import sys


def write(write):
    for i in write:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.05)


next = (input())
write("\033[32m")
write("Welcome to canal hacksoft.")
write("Please wait while we gain acces to your computer.")
write("This is an open-scource software developed by squad 303.")
write(
    "You are subject to have your computer scanned through all files and software to ensure you have no connection to international intelligence services."
)
write(
    "If you are found to have even a remote connection to CIA,FBI,NSA,MI6,MI5 or any other intelligence service your location will be tracked via your ip and will be raided and taken prisoner for interrogation."
)
write("understand this before you continue.")
write("to access commands use the command number C001.")
write("please enter C001 on the prompt.")
write("enter a command code.")
commandcode = input()
if commandcode == ("C001"):
    write("commands"
          "|IP FINDER=C002"
          "|BITCOIN MINER=C003"
          "|BITCOIN WALLET=C004"
          "|BACKDOOR SOFTWARE=C005"
          "|EMAIL INTERCEPTOR=C006"
          "|SERVER CRASH SOFTWARE=C007")
write("|please enter a commandcode")
if commandcode == (input()):
    sys.exit()

commandcodeC002 = input()
if commandcodeC002 == ("C002"):
    write("please enter a 9 digit social security number")

import random

softwares = ['ios', 'android', 'windows', 'macos', 'linux']
random_index = random.randint(0, len(softwares) - 1)

import random

devices = [
    'iphone', 'huwaei', 'windows laptop', 'macbook', 'linux device', 'samsung'
    'lg device'
]
random_index = random.randint(0, len(devices) - 1)

countries = [('US', 'United States'), ('AF', 'Afghanistan'), ('AL', 'Albania'),
             ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'),
             ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'),
             ('AG', 'Antigua And Barbuda'), ('AR', 'Argentina'),
             ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'),
             ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'),
             ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'),
             ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'),
             ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'),
             ('BO', 'Bolivia'), ('BA', 'Bosnia And Herzegowina'),
             ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'),
             ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'),
             ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodia'),
             ('CM', 'Cameroon'), ('CA', 'Canada'), ('CV', 'Cape Verde'),
             ('KY', 'Cayman Islands'), ('CF', 'Central African Rep'),
             ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'),
             ('CX', 'Christmas Island'), ('CC', 'Cocos Islands'),
             ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'),
             ('CK', 'Cook Islands'), ('CR', 'Costa Rica'),
             ('CI', 'Cote D`ivoire'), ('HR', 'Croatia'), ('CU', 'Cuba'),
             ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DK', 'Denmark'),
             ('DJ', 'Djibouti'), ('DM', 'Dominica'),
             ('DO', 'Dominican Republic'), ('TP', 'East Timor'),
             ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'),
             ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'),
             ('ET', 'Ethiopia'), ('FK', 'Falkland Islands (Malvinas)'),
             ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'),
             ('FR', 'France'), ('GF', 'French Guiana'),
             ('PF', 'French Polynesia'), ('TF', 'French S. Territories'),
             ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'),
             ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'),
             ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'),
             ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'),
             ('GN', 'Guinea'), ('GW', 'Guinea-bissau'), ('GY', 'Guyana'),
             ('HT', 'Haiti'), ('HN', 'Honduras'), ('HK', 'Hong Kong'),
             ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'),
             ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'),
             ('IE', 'Ireland'), ('IL', 'Israel'), ('IT', 'Italy'),
             ('JM', 'Jamaica'), ('JP', 'Japan'), ('JO', 'Jordan'),
             ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'),
             ('KP', 'Korea (North)'), ('KR', 'Korea (South)'),
             ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'),
             ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'),
             ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'),
             ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macau'),
             ('MK', 'Macedonia'), ('MG', 'Madagascar'), ('MW', 'Malawi'),
             ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'),
             ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'),
             ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'),
             ('MX', 'Mexico'), ('FM', 'Micronesia'), ('MD', 'Moldova'),
             ('MC', 'Monaco'), ('MN', 'Mongolia'), ('MS', 'Montserrat'),
             ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'),
             ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'),
             ('NL', 'Netherlands'), ('AN', 'Netherlands Antilles'),
             ('NC', 'New Caledonia'), ('NZ', 'New Zealand'),
             ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'),
             ('NU', 'Niue'), ('NF', 'Norfolk Island'),
             ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'),
             ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'),
             ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'),
             ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'),
             ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'),
             ('QA', 'Qatar'), ('RE', 'Reunion'), ('RO', 'Romania'),
             ('RU', 'Russian Federation'), ('RW', 'Rwanda'),
             ('KN', 'Saint Kitts And Nevis'), ('LC', 'Saint Lucia'),
             ('VC', 'St Vincent/Grenadines'), ('WS', 'Samoa'),
             ('SM', 'San Marino'), ('ST', 'Sao Tome'), ('SA', 'Saudi Arabia'),
             ('SN', 'Senegal'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'),
             ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'),
             ('SB', 'Solomon Islands'), ('SO', 'Somalia'),
             ('ZA', 'South Africa'), ('ES', 'Spain'), ('LK', 'Sri Lanka'),
             ('SH', 'St. Helena'), ('PM', 'St.Pierre'), ('SD', 'Sudan'),
             ('SR', 'Suriname'), ('SZ', 'Swaziland'), ('SE', 'Sweden'),
             ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'),
             ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'),
             ('TH', 'Thailand'), ('TG', 'Togo'), ('TK', 'Tokelau'),
             ('TO', 'Tonga'), ('TT', 'Trinidad And Tobago'), ('TN', 'Tunisia'),
             ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TV', 'Tuvalu'),
             ('UG', 'Uganda'), ('UA', 'Ukraine'),
             ('AE', 'United Arab Emirates'), ('UK', 'United Kingdom'),
             ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'),
             ('VA', 'Vatican City State'), ('VE', 'Venezuela'),
             ('VN', 'Viet Nam'), ('VG', 'Virgin Islands (British)'),
             ('VI', 'Virgin Islands (U.S.)'), ('YE', 'Yemen'),
             ('YU', 'Yugoslavia'), ('ZR', 'Zaire'), ('ZM', 'Zambia'),
             ('ZW', 'Zimbabwe')]
import random

#
random_country = random.choice(countries)

string = input()
if len(string) >= 10:
    write("please enter a nine digit social security number ")
string = input()

if len(string) <= 8:
    write("please enter a nine digit social security number ")
string = input()

if len(string) <= 9:

    def ip_generator():
        number = random.randint(0, 256)
        return number


write(
    f'IP is:{ip_generator()}.{ip_generator()}.{ip_generator()}.{ip_generator()} |  OS is: {softwares[random_index]}|   device is :{devices[random_index]}'
)
write("|Country's Name: " + random_country[1])
write("|Country's code: " + random_country[0])

if commandcodeC002 == (input()):
    sys.exit

commandcodeC003 = (input())
if commandcodeC003 == ("C003"):
    write("bitcoin mining is starting")

count = 1
while count <= 1000000.60000001308:
    print("btc 0.0< 00 bc", count)
    count = count + 0.1
count = 1
if count <= 1000000.60000001308:
    write(
        "you have mined the '1000000 bitcoins. this is the extend of mining that canal hacksoft can handle. to mine more please visit our specialised bitcoin mining software."
    )
if commandcodeC003 == (input()):
    sys.exit
commandcodeC004 = input()
if commandcodeC004 == ("C004"):
    write("")
