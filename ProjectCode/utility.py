import random

import repository

def random_line(filePath):
    return random.choice(list(open(filePath)))

def generate_random_record(tablename, id):

    data = ''

    if tablename == 'STUDENCI_PR':
        with open('./DataForGenerator/nr_indeksu.txt') as f:
            ind = f.readlines()[id]
        with open('./DataForGenerator/PESELs.txt') as f:
            pesel = f.readlines()[id]
        data = random_record_student(ind, pesel)
    elif tablename == 'PRAC_UCZELNI':
        with open('./DataForGenerator/PESELs.txt') as f:
            pesel = f.readlines()[id + 100]
        data = random_record_employee(id, pesel)
    elif tablename == 'OCENY_PR':
        data = random_record_ocena(id)
    elif tablename == 'PRZEDMIOTY_PR':
        data = random_record_przedmiot(id)
    elif tablename == 'SEMESTRY':
        data = random_record_sem(id)
    elif tablename == 'ROKI':
        data = random_record_rok(id)

    return data

def generate_data_for_table(tablename, num):
    repository.remove_all_data(tablename)
    for i in range(num):
        repository.insert_data(tablename, generate_random_record(tablename, i))

def random_record_rok(id):
    data_rozp = random_line('./DataForGenerator/date_recrutation.txt'); stopien = random.choice(['I stopnia','II stopnia', 'III stopnia'])
    forma = random.choice(['Stacjonarnie','Zdalnie','Hybrydowo'])
    data_zak = '{}-{}-{}'.format(int(data_rozp.split('-')[0]) + 4, data_rozp.split('-')[1], data_rozp.split('-')[2])
    data = '{id},\'{data_rozp}\', \'{stopien}\',\'{forma}\',\'{data_zak}\''\
        .format(id=id, data_rozp=data_rozp, stopien=stopien, forma=forma, data_zak = data_zak)
    return data

def random_record_sem(id):
    numer_sem = random.choice([i for i in range(1,10)]); ects = 30; do_przekr = random.choice([19,24])
    data = '{id},{sem},{ects},{do_przekr}'.format(id=id, sem=numer_sem, ects=ects, do_przekr=do_przekr)
    return data

def random_record_przedmiot(id):
    record = random_line('./DataForGenerator/Przedmioty.txt')
    id_kierunku = random.choice([0, 1, 2])
    nazwa = record.split(':')[0]; ects = int(record.split(':')[1])
    id_semestru = random.choice([i for i in range(10)])

    data = '{id_kierunku},{id},\'{nazwa}\',{ects},{id_semestru}'.format(id=id, id_kierunku=id_kierunku, nazwa=nazwa, ects=ects, id_semestru=id_semestru)
    return data

def random_record_student(ind, pesel):
    #ind = random_line('./DataForGenerator/nr_indeksu.txt'); pesel = random_line('./DataForGenerator/PESELs.txt')
    imie = random_line('./DataForGenerator/names.txt'); nazwisko = random_line('./DataForGenerator/surnames.txt')
    plec = random.choice(['Mezczyzna', 'Kobieta']); adres = random_line('./DataForGenerator/Addresses.txt')
    data_ur = random_line('./DataForGenerator/date_births.txt'); tel =random_line('./DataForGenerator/phone.txt')
    data_rekr=random_line('./DataForGenerator/date_recrutation.txt'); status=random_line('./DataForGenerator/status_study.txt')
    grupa_dz=random_line('./DataForGenerator/Dziekanska_grupa.txt'); ECTS=random_line('./DataForGenerator/ECTS_punkty_stud.txt')
    srednia=random_line('./DataForGenerator/srednia.txt'); id_sem=random.choice([i for i in range(10)])
    narod=random_line('./DataForGenerator/nationality.txt')
    data = '{ind},{pesel},\'{imie}\',\'{nazwisko}\',\'{plec}\',' \
           '\'{adres}\',\'{data_ur}\',\'{tel}\',\'{data_rekr}\',' \
           '\'{status}\',\'{grupa_dz}\',{ECTS},{srednia},{id_sem},\'{narod}\''.format(
                    ind=int(ind), pesel=int(pesel), imie=imie, nazwisko=nazwisko, plec=plec, adres=adres, data_ur=data_ur,
                    tel=tel, data_rekr=data_rekr, status=status, grupa_dz=grupa_dz,ECTS=int(ECTS), srednia=float(srednia),
                    id_sem=int(id_sem), narod=narod)
    return data

def random_record_employee(id, pesel):
    #pesel = random_line('./DataForGenerator/PESELs.txt')
    imie = random_line('./DataForGenerator/names.txt')
    nazwisko = random_line('./DataForGenerator/surnames.txt')
    plec = random.choice(['Mezczyzna', 'Kobieta'])
    adres = random_line('./DataForGenerator/Addresses.txt')
    data_ur = random_line('./DataForGenerator/date_births.txt')
    tel = random_line('./DataForGenerator/phone.txt')
    narod = random_line('./DataForGenerator/nationality.txt')

    tytul = random_line('./DataForGenerator/tytuly.txt')
    stanowisko_line = random_line('./DataForGenerator/stanowiska.txt')
    stanowisko = stanowisko_line.split(' ')[0]; od = int(stanowisko_line.split(' ')[1]); do = int(stanowisko_line.split(' ')[2])
    wynagrod = random.randint(od, do)
    data_zat = random_line('./DataForGenerator/date_births.txt')
    wymiar = random_line('./DataForGenerator/godziny_pracy.txt')

    data = '{prac_id},{id},{PESEL},\'{imie}\',\'{nazwisko}\',' \
           '\'{plec}\',\'{adres}\',\'{data_ur}\',\'{narod}\',' \
           '\'{tel}\',\'{tytul}\',\'{stanowisko}\',{wynagrod},\'{data_zat}\',{wymiar}'.format(
        prac_id=int(id), id=int(id),PESEL=int(pesel), imie=imie, nazwisko=nazwisko, plec=plec, adres=adres, data_ur=data_ur,
        narod=narod, tel=tel, tytul=tytul, stanowisko=stanowisko, wynagrod=wynagrod, data_zat=data_zat, wymiar=int(wymiar))
    return data

def random_record_ocena(id):
    id_przed = random.choice([i for i in range(35)])
    nr_indek = random_line('./DataForGenerator/nr_indeksu.txt')
    prac_id = random.choice([i for i in range(25)])
    wart_oceny = float(random_line('./DataForGenerator/skala_ocen.txt'))
    termin_wyst = random_line('./DataForGenerator/date_births.txt')
    czy_popr = random.choice(['Y', 'N'])

    data = '{id},{przedm_id},{student_nr_ind},{prac_id_prac},{ocena},' \
           '\'{termin}\',\'{czy}\',{prac_ucz_prac_ID}'.format(
        id=int(id), przedm_id=(id_przed), student_nr_ind=nr_indek, prac_id_prac=prac_id,
        ocena=wart_oceny, termin=termin_wyst, czy=czy_popr, prac_ucz_prac_ID=prac_id)
    return data

def insert_const_data():
    # Fill 'wydzialy table'
    with open('./DataForGenerator/wydzialy.txt', 'r') as file:
        lines = file.readlines()

    repository.remove_all_data('wydzialy')
    index = 0
    for line in lines:
        record = '{},\'{}\''.format(index, line)
        repository.insert_data('wydzialy', record)
        index += 1

    # Fill 'kierunki table'
    with open('./DataForGenerator/kierunki.txt', 'r') as file:
        lines = file.readlines()

    repository.remove_all_data('kierunki')
    index = 0
    for line in lines:
        record = '{},{},\'{}\''.format(index, index, line)
        repository.insert_data('kierunki', record)
        index+=1

    # Insert przedmioty

# Repository, pre-runned function
def insert_data_for_dictionaries():
    # Fill 'stanowiska' table
    with open('./DataForGenerator/stanowiska.txt', 'r') as file:
        lines = file.readlines()

    repository.remove_all_data('stanowiska')
    for line in lines:
        splitted_line = line.split(' ')
        stanowisko_name = splitted_line[0]
        od = splitted_line[1]
        do = splitted_line[2]
        record = '\'{}\',{},{}'.format(stanowisko_name, od, do)
        repository.insert_data('stanowiska', record)

    # Fill 'tytuly table'
    with open('./DataForGenerator/tytuly.txt', 'r') as file:
        lines = file.readlines()

    repository.remove_all_data('tytuly')
    for line in lines:
        record = '\'{}\''.format(line)
        repository.insert_data('tytuly', record)

    # Fill 'statusy table'
    with open('./DataForGenerator/status_study.txt', 'r') as file:
        lines = file.readlines()

    repository.remove_all_data('statusy')
    for line in lines:
        record = '\'{}\''.format(line)
        repository.insert_data('statusy', record)