
##############################
# Strings - Text analysis 
##############################


import random # Just to create the enigma

##############################
# Activity 5 - Statistical analysis of a text
##############################



## Question 1 ##


def occurrences_letter(letter,sentence):
    """ Coutn the number of appearance of the given letter in the sentence
    Input: a letter, a sentence in uppercase
    Output: the number of this letter """

    nb = 0
    for charac in sentence:
        if charac == letter:
            nb = nb + 1

    return nb


# Test 
sentence = "IS THERE ANYBODY OUT THERE"
print("The sentence",sentence,"contains",occurrences_letter("E",sentence),"times the letters E")



## Question 2 ##

def number_letters(sentence):
    """ Count the total number of letters
    Input: a sentence in uppercase
    Output: the total number of letters from "A" to "Z" """

    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    nb = 0
    for charac in sentence:
        if charac in alphabet:
            nb = nb + 1

    return nb


# Test 
sentence = "IS THERE ANYBODY OUT THERE"
print("The sentence",sentence,"contains",number_letters(sentence),"letters")



## Question 3 ##

def percentage_letter(letter,sentence):
    """ Calcule le ratio d'une letter donnée dans sentence
    Input: une letter et une sentence en majuscule
    Output: le percentage d'apparition de la letter """

    nb_letters = occurrences_letter(letter,sentence)
    nb_total = number_letters(sentence)
    percentage = nb_letters/nb_total*100
    
    return percentage


# Test 
sentence = "IS THERE ANYBODY OUT THERE"
percentage = percentage_letter("E",sentence)
print("The sentence",sentence,"contains",percentage,"% of letter E")
print("Round percentage:","{0:.2f}".format(percentage))


## Question 4 ##

def display_frequency(sentence):
    """ Count and display the ration of all letters in the sentence
    Input: a sentence in uppercase
    Output: the display of percentage of letters appearance """

    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for letter in alphabet:
        percentage = percentage_letter(letter,sentence)
        print(letter," : ","{0:.2f}".format(percentage))

    return


# SECRET ------------------
# Creation of the enigma

def myshuffle(x):
    x = list(x)
    random.shuffle(x)
    return x

#for word in sentence.split():
#  print(list(word))
#  print(myshuffle(list(word)))

# Le corbeau et le renard - Jean de la Fontaine
sentence1 = "MAITRE CORBEAU SUR UN ARBRE PERCHE TENAIT EN SON BEC UN FROMAGE MAITRE RENARD PAR L ODEUR ALLECHE LUI TINT A PEU PRES CE LANGAGE ET BONJOUR MONSIEUR DU CORBEAU QUE VOUS ETES JOLI QUE VOUS ME SEMBLEZ BEAU SANS MENTIR SI VOTRE RAMAGE SE RAPPORTE A VOTRE PLUMAGE VOUS ETES LE PHENIX DES HOTES DE CES BOIS A CES MOTS LE CORBEAU NE SE SENT PAS DE JOIE ET POUR MONTRER SA BELLE VOIX IL OUVRE UN LARGE BEC LAISSE TOMBER SA PROIE LE RENARD S EN SAISIT ET DIT MON BON MONSIEUR APPRENEZ QUE TOUT FLATTEUR VIT AUX DEPENS DE CELUI QUI L ECOUTE CETTE LECON VAUT BIEN UN FROMAGE SANS DOUTE LE CORBEAU HONTEUX ET CONFUS JURA MAIS UN PEU TARD QU ON NE L Y PRENDRAIT PLUS"

#sentence_mystere1 = ' '.join([''.join(myshuffle(list(word))) for word in sentence1.split() ])

# Le roi de aulnes - Goethe
sentence2 = "WER REITET SO SPAT DURCH NACHT UND WIND ES IST DER VATER MIT SEINEM KIND ER HAT DEN KNABEN WOHL IN DEM ARM ER FASST IHN SICHER ER HALT IHN WARM MEIN SOHN WAS BIRGST DU SO BANG DEIN GESICHT SIEHST VATER DU DEN ERLKONIG NICHT DEN ERLENKONIG MIT KRON UND SCHWEIF  MEIN SOHN ES IST EIN NEBELSTREIF DU LIEBES KIND KOMM GEH MIT MIR GAR SCHONE SPIELE SPIEL ICH MIT DIR MANCH BUNTE BLUMEN SIND AN DEM STRAND MEINE MUTTER HAT MANCH GULDEN GEWAND MEIN VATER MEIN VATER UND HOREST DU NICHT WAS ERLENKONIG MIR LEISE VERSPRICHT SEI RUHIG BLEIBE RUHIG MEIN KIND IN DURREN BLATTERN SAUSELT DER WIND" 

#sentence_mystere2 = ' '.join([''.join(myshuffle(list(word))) for word in sentence2.split() ])

# Cent ans de solitude - Gabriel Garcia Marquez
sentence3 = "FASCINADO POR UNA REALIDAD INMEDIATA QUE ENTONCES LE RESULTO MAS FANTASTICA QUE EL VASTO UNIVERSO DE SU IMAGINACION PERDIO TODO INTERES POR EL LABORATORIO DE ALQUIMIA PUSO A DESCANSAR LA MATERIA EXTENUADA POR LARGOS MESES DE MANIPULACION Y VOLVIO A SER EL HOMBRE EMPRENDEDOR DE LOS PRIMEROS TIEMPOS QUE DECIDIA EL TRAZADO DE LAS CALLES Y LA POSICION DE LAS NUEVAS CASAS Y SE DETERMINO QUE FUERA EL QUIEN DIRIGIERA LA REPARTICION DE LA TIERRA"

sentence_mystere3 = ' '.join([''.join(myshuffle(list(word))) for word in sentence3.split() ])

# Sumertimes - Elle Fitzgerald
sentence4 = "SUMMERTIME AND THE LIVING IS EASY FISH ARE JUMPING AND THE COTTON IS HIGH OH YOUR DADDY IS RICH AND YOUR MA IS GOOD LOOKING SO HUSH LITTLE BABY DONT YOU CRY ONE OF THESE MORNINGS YOU RE GONNA RISE UP SINGING AND YOULL SPREAD YOUR WINGS AND YOULL TAKE TO THE SKY BUT TILL THAT MORNING THERE AINT NOTHING CAN HARM YOU WITH DADDY AND MAMMY STANDING BY"

sentence_mystere4 = ' '.join([''.join(myshuffle(list(word))) for word in sentence4.split() ])


# FIN SECRET ------------------

# Mystery sentences

sentence_mystery1 = "TMAIER BERACUO RSU NU REBRA PRCEEH EIANTT NE ONS EBC NU GAOFREM EIMATR RERNAD APR L RDUOE LAHECLE UIL TTNI A EUP SREP EC LGNGAEA TE RBONUJO ERMNOUSI DU UBRACEO QUE OVSU EEST LIJO UQE OUVS EM MSZELBE BAEU ASNS MIERNT IS RVETO AGRAME ES PRARPTOE A OEVTR AMGUPLE VUOS SEET EL PNIHXE DSE OSHET ED CSE BIOS A ESC MSOT LE OUBRCEA NE ES ESTN ASP DE IEJO TE OUPR ERRNOTM AS BELEL XOVI IL OREVU NU RGLEA ECB ILESSA EBOMTR AS PIOER EL NRDAER S EN ISIAST TE ITD MNO NOB EUSRMNOI NRPEEAZP QEU UTOT EUTLRFTA IVT XUA SPNEDE DE UECIL UQI L TECEOU TECET NEOCL VATU BNEI UN GMAEORF SNAS TUOED LE EOABURC OHENTXU TE NSCOFU UJRA SMIA UN EPU TRDA UQ NO EN L Y ARRPEIDNT ULSP"

print(sentence_mystery1)

display_frequency(sentence_mystery1)

sentence_mystery2 = "WRE TREITE SO TSPA CUDHR AHNCT UND WIND SE STI RED AEVRT MTI ESEIMN IDNK RE ATH END NEABNK WLOH IN EMD AMR ER AFTSS HIN IHSERC RE AHTL HIN MRWA EINM SHNO SAW SRTIBG UD SO NGBA DNEI EIHSGTC ESISTH RAETV UD DEN LERNIOKG NITHC NDE LOENINKGRE TIM OKRN UDN CHWFSEI NEIM NSOH ES STI IEN BIFTRLSEEEN DU BILESE IKDN OMKM EHG MIT MIR RAG ECHNOS EPELSI EIPSL IHC ITM RDI HNCMA BEUTN MBLUNE DINS NA DEM TNDRAS NMIEE UTETMR AHT CAMHN UDNGEL GDAWEN MIEN EATRV MENI VEART DUN OSTHER DU CINTH SAW KNNOEIREGL RIM ILEES PRSTVRCIEH ISE IHGRU BEEILB RIGUH MNEI KNDI NI RDNEUR NATBRLET STAESUL EDR WNID"

print(sentence_mystery2)

display_frequency(sentence_mystery2)

sentence_mystery3 = "DSNOACAIF ORP ANU DAEDALRI DNAAEIMTI EQU NNCOSETE EL RSTEOUL SMA AACTFAITNS UQE EL TSVAO OINSRVUE DE US ANIGIICANOM EIORDP TOOD RTEIENS RPO LE ITOABOLRROA ED QIUAMALI USOP A NSSRCAEAD LA TMREAAI NXTADAUEE ROP GOARLS EMESS DE NNAMICLUIAPO Y LOVOIV A RES LE RHMEOB EOMDNEERPRD DE LOS RSOPMRIE OMTSIPE UEQ CIIDADE LE RTDAAOZ ED LSA CELSAL Y LA NICOIOPS ED LAS UESVNA SSACA Y ES ITRMNEEOD QEU AERFU EL UEQIN IIIRDEGAR LA NAIORTREICP DE AL RRTEIA"

print(sentence_mystery3)

display_frequency(sentence_mystery3)

sentence_mystery4 = "IMTRUESMME DNA TEH LNGIIV SI EYAS SIFH REA GJPNUIM DNA HET TTNOCO IS GHIH OH OUYR DDADY SI IRHC DAN ROUY MA SI DOGO GKOILON OS USHH LTLIET BBYA NDOT OUY CYR NEO OF HESET GNSRONIM YUO RE NANGO SIER PU SNIGING NAD OULLY EPADRS YUOR GINSW DAN LYOLU KATE OT HET KSY TUB ITLL TATH MGNIRNO EREHT NATI INTGOHN ACN AHMR OYU TWIH DADYD NDA MYMMA NSTIDGAN YB"

print(sentence_mystery4)

display_frequency(sentence_mystere4)