# CZfakeID
Czech fake identity generator

CZfakeID is a small console utility, which can provide desired amount of fake Czech names and related personal data to fill in your forms, databases etc.
It could be helpful if you need to verify that your application can correctly handle Czech latin characters (ě,š,č,ř and so on) or you need to test
the verification of national identification number validity, validity of phone number which belongs to real Czech phone operator and so on.

Currently, the following attributes are being generated:
* jméno (name) - one of 88 Czech male names and 65 female ones
* příjmení (surname) - one of 68 most common Czech surnames (both male and female forms, therefore 136 at all)
* pohlaví (gender) - male / female
* datum narození (date of birth)
* rodné číslo (national identification number)
* rodinný stav (civil status) - svobodný, svobodná (single) / ženatý, vdaná (married) / rozvedený, rozvedený (divorced) / ovdovělý, ovdovělá (widowed)
* email - alias generated from name and surname or from the year of birth + one of common Czech freemail domains (and Gmail.com, which is also popular in CZ)
* telefon (phone number) - nine digit mobile phone number, first three digits are one of czech mobile operators prefixes

## Usage:

```
./czfakeid.py 10
```

Output will be the requested amount of identities with values separated by semicolons (CSV), for instance 10 in this example:
```
jméno;příjmení;pohlaví;datum narození;místo narození;rodné číslo;rodinný stav;email;telefon
Helena;Holubová;F;26071959;Děčín;595726/XXXX;vdaná;helena.XX@seznam.Xz;733936XXX
Lýdie;Pavlíková;F;29051963;Praha;635529/XXXX;vdaná;lydiepavlikova@gmail.Xom;727640XXX
Kateřina;Staňková;F;19041961;Liberec;615419/XXXX;rozvedená;k.stankova@volny.Xz;733273XXX
Jaroslava;Sedláčková;F;23111946;Uherské Hradiště;466123/XXX;vdaná;jaroslava.46@seznam.Xz;775444XXX
Jozef;Bartoš;M;10071943;Praha;430710/XXXX;ovdovělý;bartos.43@centrum.Xz;729684XXX
Dalibor;Janda;M;17011974;Praha;740117/XXXX;rozvedený;d.janda@seznam.Xz;778830XXX
Lukáš;Ševčík;M;15021983;Most;830215/XXXX;ženatý;lukassevcik@seznam.Xz;772618XXX
Diana;Fialová;F;07051999;Příbram;995507/XXXX;svobodná;fialova.99@seznam.Xz;702393XXX
Otakar;Bartoš;M;11041947;Kladno;470411/XXX;rozvedený;otakar47@gmail.Xom;772042XXX
Tadeáš;Šťastný;M;10101976;Frýdek-Místek;761010/XXXX;ženatý;tadeas.stastny@seznam.Xz;739877XXX

```

In the example above, the real output of the program was altered, some values were replaced by character X,
because some of them were most probably personal data of really existing persons (just to be sure - GDPR, you know :)

If you execute the program without any parameter, only one identity will be generated and following result will be shown:

```
 Jméno a příjmení: Antonín Zeman
 Pohlaví: M
 Datum a místo narození: 05.04.1945 Jablonec nad Nisou
 Rodné číslo: 450405/XXX
 Rodinný stav: ovdovělý


 E-mail: zeman.XX@seznam.Xz
 Telefon: 604988XXX

```

## WARNING! 
**Use with caution! The output of CZfakeID program can be considered as personal private data, which are protected by law.
Altough the result is completely random, some use-cases of the generated output can be illegal.
Responsibility goes to you, use at your own risk! **



