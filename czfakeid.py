#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import datetime
import sys
import unicodedata

''' definice funkci '''

def get_pohlavi():
	nahoda = 0
	nahoda = random.randint(1,2)
	
	if nahoda == 1:
		pohlavi = 'M'
	elif nahoda == 2:
		pohlavi = 'F'
	
	return pohlavi


def get_rok_narozeni():
	
	now = datetime.datetime.now()
	rok_konec = int(now.year)
	rok_konec = rok_konec - 18
	rok_pocatek = int(now.year)
	rok_pocatek = rok_pocatek - 80
	
	rok_narozeni = random.randint(rok_pocatek,rok_konec)

	return rok_narozeni

def get_mesic_narozeni():

	mesic_narozeni = random.randint(01,12)
	return mesic_narozeni

def get_den_narozeni(mesic_narozeni):
	
	if (mesic_narozeni == "04" or mesic_narozeni == "06" or mesic_narozeni == "09" or mesic_narozeni == "11"):
		posledni_den = 30
	elif mesic_narozeni == "02":
		posledni_den = 28
	else:
		posledni_den = 31
	
	den_narozeni = random.randint(01,posledni_den)

	return den_narozeni


def get_rodne_cislo(rok_narozeni,mesic_narozeni,den_narozeni,pohlavi):
	
	poradi = random.randint(001,999)
	
	rok = str(rok_narozeni)
	rok = rok[-2] + rok[-1]


	if pohlavi == 'F':
		mesic_narozeni = mesic_narozeni + 50

	if rok_narozeni < 1954:
		kontrolni_soucet = ''
	else:
		kontrolni_soucet = '0'


	rc = str(rok) + str(mesic_narozeni).zfill(2) + str(den_narozeni).zfill(2) + str(poradi).zfill(3) + str(kontrolni_soucet)

	if rok_narozeni > 1954:
		soucet1 = int(rc[0]) + int(rc[2]) + int(rc[4]) + int(rc[6]) + int(rc[8])
		soucet2 = int(rc[1]) + int(rc[3]) + int(rc[5]) + int(rc[7]) + int(rc[9])
		soucet = soucet1 - soucet2
		soucet = soucet%11
		if soucet == 10:
			soucet = 0

		kontrolni_soucet = soucet
	
	rodne_cislo = str(rok) + str(mesic_narozeni).zfill(2) + str(den_narozeni).zfill(2) + '/' + str(poradi).zfill(3) + str(kontrolni_soucet)

	return rodne_cislo





def get_jmeno(pohlavi):
	
	jmena_muzi = ['Jiří','Jan','Petr','Josef','Pavel','Martin','Jaroslav','Tomáš','Miroslav','Zdeněk','František','Václav','Michal','Milan','Karel','Jakub','Lukáš','David','Vladimír','Ladislav','Ondřej','Roman','Stanislav','Marek','Radek','Daniel','Antonín','Vojtěch','Filip','Adam','Miloslav','Matěj','Aleš','Jaromír','Libor','Dominik','Patrik','Vlastimil','Jindřich','Miloš','Oldřich','Lubomír','Rudolf','Ivan','Luboš','Robert','Štěpán','Radim','Richard','Bohumil','Matyáš','Vít','Ivo','Rostislav','Luděk','Dušan','Kamil','Šimon','Vladislav','Zbyněk','Bohuslav','Michael','Alois','Viktor','Štefan','Vítězslav','René','Jozef','Ján','Kryštof','Eduard','Marcel','Emil','Dalibor','Ludvík','Radomír','Tadeáš','Otakar','Vilém','Bedřich','Alexandr','Denis','Vratislav','Leoš','Radovan','Břetislav','Marian','Přemysl','Erik']

	jmena_zeny = ['Marie','Jana','Eva','Hana','Anna','Lenka','Kateřina','Věra','Lucie','Alena','Petra','Jaroslava','Veronika','Martina','Jitka','Tereza','Ludmila','Helena','Michaela','Zdeňka','Ivana','Jarmila','Monika','Zuzana','Jiřina','Markéta','Eliška','Marcela','Barbora','Dagmar','Dana','Kristýna','Vlasta','Božena','Irena','Miroslava','Libuše','Pavla','Marta','Adéla','Andrea','Simona','Vendula','Květa','Renata','Olga','Šárka','Anežka','Nikola','Diana','Klára','Blanka','Iveta','Gabriela','Alžběta','Iva','Bohuslava','Miloslava','Lada','Lýdie','Soňa','Růžena','Silvie','Radka','Aneta','Ester' ]


	if pohlavi == 'M':
		nahoda = random.randint(0,88)
		jmeno = jmena_muzi[nahoda]
	elif pohlavi == 'F':
		nahoda = random.randint(0,65)
		jmeno = jmena_zeny[nahoda]

	return jmeno




def get_prijmeni(pohlavi):

	prijmeni_muzi = ['Novák','Svoboda','Novotný','Dvořák','Černý','Procházka','Kučera','Veselý','Horák','Němec','Pokorný','Marek','Pospíšil','Hájek','Jelínek','Král','Růžička','Beneš','Fiala','Sedláček','Doležal','Zeman','Kolář','Krejčí','Navrátil','Čermák','Urban','Vaněk','Blažek','Kříž','Kratochvíl','Kovář','Kopecký','Bartoš','Vlček','Musil','Šimek','Polák','Konečný','Malý','Čech','Kadlec','Štěpánek','Staněk','Holub','Dostál','Soukup','Šťastný','Mareš','Sýkora','Moravec','Tichý','Valenta','Vávra','Matoušek','Bláha','Říha','Ševčík','Bureš','Hruška','Mašek','Pavlík','Dušek','Hrubý','Havlíček','Janda','Mach','Müller','Liška']
	prijmeni_zeny = ['Nováková','Svobodová','Novotná','Dvořáková','Černá','Procházková','Kučerová','Veselá','Horáková','Němcová','Pokorná','Marková','Pospíšilová','Hájková','Jelínková','Králová','Růžičková','Benešová','Fialová','Sedláčková','Doležalová','Zemanová','Kolářová','Krejčová','Navrátilová','Čermáková','Urbanová','Vaňková','Blažková','Křížová','Kratochvílová','Kovářová','Kopecká','Bartošová','Vlčková','Musilová','Šimková','Poláková','Konečná','Malá','Čechová','Kadlecová','Štěpánková','Staňková','Holubová','Dostálová','Soukupová','Šťastná','Marešová','Sýkorová','Moravcová','Tichá','Valentová','Vávrová','Matoušková','Bláhová','Říhová','Ševčíková','Burešová','Hrušková','Mašková','Pavlíková','Dušková','Hrubá','Havlíčková','Jandová','Machová','Müllerová','Lišková']

	nahoda = random.randint(0,68)

	if pohlavi == 'M':
		prijmeni = prijmeni_muzi[nahoda]
	elif pohlavi == 'F':
		prijmeni = prijmeni_zeny[nahoda]

	return prijmeni

def get_misto_narozeni():
	# Praha, Brno, Ostrava a Plzen jsou v listu vicekrat, protoze se jedna o pravdepodobnejsi mista narozeni
	mesta = ['Benešov','Beroun','Blansko','Brno','Brno','Brno','Bruntál','Břeclav','Česká Lípa','České Budějovice','Český Krumlov','Děčín','Domažlice','Frýdek-Místek','Havlíčkův Brod','Hodonín','Hradec Králové','Cheb','Chomutov','Chrudim','Jablonec nad Nisou','Jeseník','Jičín','Jihlava','Jindřichův Hradec','Karlovy Vary','Karviná','Kladno','Klatovy','Kolín','Kroměříž','Kutná Hora','Liberec','Litoměřice','Louny','Mělník','Mladá Boleslav','Most','Náchod','Nový Jičín','Nymburk','Olomouc','Opava','Ostrava','Ostrava','Ostrava','Pardubice','Pelhřimov','Písek','Plzeň','Plzeň','Plzeň','Praha','Praha','Praha','Praha','Praha','Praha','Praha','Praha','Prachatice','Prostějov','Přerov','Příbram','Rakovník','Rokycany','Rychnov nad Kněžnou','Semily','Sokolov','Strakonice','Svitavy','Šumperk','Tábor','Tachov','Teplice','Trutnov','Třebíč','Uherské Hradiště','Ústí nad Labem','Ústí nad Orlicí','Vsetín','Vyškov','Zlín','Znojmo','Žďár nad Sázavou','Aš','Blatná','Boskovice','Broumov','Bučovice','Bystřice nad Pernštejnem','Čáslav','Český Brod','Dačice','Dubá','Dvůr Králové nad Labem','Frýdlant','Horšovský Týn','Hořovice','Hranice','Hustopeče','Chotěboř','Krnov','Kyjov','Litvínov','Mikulov','Moravská Třebová','Moravské Budějovice','Moravský Krumlov','Nové Město na Moravě','Rosice','Rýmařov','Říčany','Sedlec','Slavkov u Brna','Tišnov','Třeboň','Valašské Klobouky','Velká Bíteš','Velké Meziříčí','Veselí nad Moravou','Zábřeh','Židlochovice']
	nahoda = random.randint(0,122)
	misto_narozeni = mesta[nahoda]


	return misto_narozeni

def get_email(jmeno,prijmeni,rok):

	nahoda_domena = random.randint(0,4)
	domeny = ['seznam.cz','centrum.cz','seznam.cz','volny.cz','gmail.com']
	domena = domeny[nahoda_domena]
	
	jmeno = unicode(jmeno, "utf-8")	
	jmeno = unicodedata.normalize('NFKD', jmeno).encode('ascii','ignore')
	jmeno = jmeno.lower()
	
	prijmeni = unicode(prijmeni, "utf-8")
	prijmeni = unicodedata.normalize('NFKD', prijmeni).encode('ascii','ignore')
	prijmeni = prijmeni.lower()

	rok = str(rok)	
	rok = rok[2] + rok[3]
	
	nahoda_alias = random.randint(0,14)
	nahoda_suffix = random.randint(1,30)

	if nahoda_alias == 0:
		alias = jmeno + '.' + prijmeni
	elif nahoda_alias == 1:
		alias = jmeno + prijmeni
	elif nahoda_alias == 2:
		alias = jmeno + rok
	elif nahoda_alias == 3:
		alias = jmeno + '.' + rok
	elif nahoda_alias == 4:
		alias = prijmeni + rok
	elif nahoda_alias == 5:
		alias = prijmeni + '.' + rok
	elif nahoda_alias == 6:
		alias = jmeno + prijmeni[0]
	elif nahoda_alias == 7:
		alias = jmeno[0] + prijmeni
	elif nahoda_alias == 8:
		alias = jmeno + '.' + prijmeni[0]
	elif nahoda_alias == 9:
		alias = jmeno[0] + '.' + prijmeni
	elif nahoda_alias == 11:
		alias = jmeno + '.' + prijmeni + rok
	elif nahoda_alias == 12:
		alias = jmeno + '.' + prijmeni + '.' + rok
	else:
		alias = jmeno + '.' + prijmeni

	email =  alias + '@' + domena

	return email


def get_telefon():
	
	

	predcisli_mobil = ['601','602','606','607','603','604','605','608','702','720','721','722','723','724','725','726','727','728','729','730','731','732','733','734','735','736','737','738','739','770','771','772','773','774','775','776','778']

	nahoda_predcisli = random.randint(0,36)
	predcisli = predcisli_mobil[nahoda_predcisli]

	dvojcisli1 = random.randint(00,99)
	dvojcisli2 = random.randint(00,99)
	dvojcisli3 = random.randint(00,99)
	
	telefon = str(predcisli) + str(dvojcisli1).zfill(2) + str(dvojcisli2).zfill(2) + str(dvojcisli3).zfill(2)

	return telefon


''' program '''

if len(sys.argv) > 1:
	param = sys.argv[1]

	if param.isdigit():
		param = int(param)
		print 'jméno;příjmení;pohlaví;datum narození;místo narození;rodné číslo;email;telefon'
		for x in xrange(param):
			pohlavi = get_pohlavi()
		        rok = get_rok_narozeni()
		        mesic = get_mesic_narozeni()
		        den = get_den_narozeni(mesic)
		        rodne_cislo = get_rodne_cislo(rok,mesic,den,pohlavi)
		        jmeno = get_jmeno(pohlavi)
		        prijmeni = get_prijmeni(pohlavi)
		        misto_narozeni = get_misto_narozeni()
			email = get_email(jmeno,prijmeni,rok)
			telefon = get_telefon()
		
			print jmeno + ';' + prijmeni + ';' + pohlavi + ';' + str(den).zfill(2) + str(mesic).zfill(2) + str(rok) + ';' + misto_narozeni + ';' + rodne_cislo + ';' + email + ';' + str(telefon)
			
		sys.exit(0)

	else:
		print "error"
		sys.exit(1)
else:
	pohlavi = get_pohlavi()
	rok = get_rok_narozeni()
	mesic = get_mesic_narozeni()
	den = get_den_narozeni(mesic)
	rodne_cislo = get_rodne_cislo(rok,mesic,den,pohlavi)
	jmeno = get_jmeno(pohlavi)
	prijmeni = get_prijmeni(pohlavi)
	misto_narozeni = get_misto_narozeni()
	email = get_email(jmeno,prijmeni,rok)
	telefon = get_telefon()

	print ''
	print ' Jméno a příjmení: ' + jmeno + ' ' + prijmeni
	print ' Pohlaví: '+ pohlavi
	print ' Datum a místo narození: ' + str(den).zfill(2) + '.' + str(mesic).zfill(2) +'.' + str(rok) + ' ' + misto_narozeni
	print ' Rodné číslo: ' + rodne_cislo
	print ' E-mail: ' + email
	print ' Telefon: ' + str(telefon)
	print ''
	
	sys.exit(0)




