#!/usr/bin/env python
# coding: utf-8

# REGEX - wyrażenia regularne
# --------------------

# Funkcja match()zwraca znaleziony napis, jeśli od początku pasuje do patternu. W innym przypadku zwróci None.

# In[2]:


import re


# In[4]:


pattern = r"napis"#r zapisujemy bo taka jest składnia
sequence = "napis moj super"
print(re.match(pattern, sequence))
#przestawiony napis moj super i znajdzie napis


# In[4]:


pattern = r"napis"
sequence = "napis"
print(re.match(pattern, sequence))


# In[ ]:


pattern = r"napis"
sequence = "napis"
print(re.match(pattern, sequence).group())


# search() w przeciwieństwie do match szuka patternu w całym stringu

# In[ ]:


pattern = r"napis"
sequence = "To taki napis"
print(re.search(pattern, sequence).group())


# In[ ]:


pattern = "n."
zwykly_napis_1 = "napis"
zwykly_napis_2 = "n."
print(re.search(pattern, zwykly_napis_1))
print(re.search(pattern, zwykly_napis_2))


# Kropka oznacza dowolny znak, oprócz znaku nowej linii

# In[9]:


re.search(r'N.p.s', 'to jest N5pis N6pis').group()#kropka oznacza jeden znak


# ^ oznacza początek napisu

# In[72]:


re.search(r'^Na.', 'Napis').group()#kropka znaczy jakiekolwiek inny znak


# $ oznacza koniec napisu

# In[10]:


print(re.search(r'Na.$', 'isNap'))


# \* powtarza ostatni znak zero lub wiele razy

# In[18]:


print(re.search(r'^Na.*', 'Napis to napar').group())
print(re.search(r'^Na.*6', 'Napis to napar'))
print(re.search(r'Na.*$', 'toaleta to Napis').group())
print(re.search(r'Na.*$', 'hasło krzyżowki : Napis to koniec').group())


# \+ powtarza ostatni znak przynajmniej raz

# In[19]:


print(re.search(r'^Na.*', 'Na'))
print(re.search(r'Na.*$', 'Na'))

print(re.search(r'Na.+$', 'Na'))#plus mial szukac coś więcej, ale nie znalazł i przez to jest problem


# Czasem możemy chcieć zawęzić zakres np w przypadku szukania takiego wzorca:
# (.*) w takim stringu
# 
# "(a) b (c)"
# 
#  zostanie znalezione 
#  
#  "(a) b (c)" 
#  
#  zamiast jedynie 
#  
#  (a)
# 
# ? w skrócie ogranicza zakres do jak najmniejszego, czyli szuka zero lub jedno wystąpień znaku po lewej w przeszukiwanym stringu

# In[21]:


print(re.search(r'Na*?', 'Naaaaa'))#? najkrótszy string
print(re.search(r'a*?', 'Naaaaa'))#masz zero razy bo ?
print(re.search(r'a+?', 'Naaaaa'))#a wiele razy, ae najkrótszy string


# In[22]:


print(re.search(r'Na*', 'Naaaaa'))#? najkrótszy string
print(re.search(r'a*', 'Naaaaa'))
print(re.search(r'a+', 'Naaaaa'))#a wiele razy, ae najkrótszy string/plus wiele i jeden


# In[23]:


print(re.search(r'ma?n', 'mn'))
print(re.search(r'ma?n', 'man'))
print(re.search(r'ma?n', 'maaan'))
print(re.search(r'ma?n', 'main'))
print(re.search(r'ma?n', 'woman'))


# {m} oznacza ile powtórzeń danego znaku chcemy

# In[24]:


print(re.search(r'\d{2}-\d{3}', '02-081').group())#jakas cyfra dwa raz i myślnik i 3 cyfry
print(re.search(r'\d{2}-\d{3}', '022-081').group())


# In[26]:


print(re.search(r'\d{2}-\d{3}', '02-081').group())#jakas cyfra dwa raz i myślnik i 3 cyfry
print(re.search(r'\d{2}-\d{3}', '044422-081444').group())


# {m,n} określa dokładny zakres ilości powtórzeń

# In[28]:


print(re.search(r'\d{3,4}-\d{3}', '02-081'))
print(re.search(r'\d{2,3}-\d{3}', '022-081'))
print(re.search(r'.\d{2,3}-\d{3}', 'w2-3nd'))


# In[30]:


print(re.search(r'.d{3}','aaaddd'))


# i znowu dodanie znaku zapytania ogranicza znaleziony string do minimum

# In[31]:


print(re.search(r'\d{2,3}?-\d{3}', '02200000000-081'))


# A co jeśli chcemy znaleźć napisy z ukośnikami, kropkami lub plusami? Może posłużyć się znakiem 'ucieczki': \

# In[34]:


print(re.search(r'\d+\+\d', '2+2'))# slesh d - znak ucieczki, czyli interpretuj w specjalny sposób /jakas cyfra,zwykly +,cyfre wile razy
print(re.search(r'\d+\*\d', '2*2'))

print(re.search(r'\d+\+\d+', '222+222'))
print(re.search(r'\d+\+\d', '+2'))
print(re.search(r'\d*\+\d', '+2'))


# Jeśli natomiast chcemy wykorzystać poznane powyżej symbole dla większej grupy znaków to możemy zgrupować je w [ ] i następnie użyć któregoś z symbolu lub symboli

# W nawiasach kwadratowych możemy określać również zakres np od a do z: [a-z] oraz od 0 do 9 [0-9], czyli w praktyce wszystkie litery lub cyfry

# In[37]:


print(re.search(r'[a-z]', 'falafel'))#jeśli znajdziesz jaką literę wiele razy to zwróć mi
print(re.search(r'[a-b]', 'falafel'))#jeśli znajdziesz jaką literę wiele razy to zwróć mi

print(re.search(r'[a-z]+', 'falafel    '))#nie weźmie spacji

print(re.search(r'[0-9]', '9573528'))
print(re.search(r'[0-9]+', '9573528'))

print(re.search(r'[0-9]+[a-z]+', '9573528hafdyusk94635'))
print(re.search(r'[0-9][a-z]+', '9573528hafdyusk94635'))

print(re.search(r'\w+','9573528hafdyusk94635'))


# In[39]:


print(re.search(r'[abc]+', 'abcccccabcabcabc'))
print(re.search(r'[abc]+', 'abccccc_abc_abc_abc'))
print(re.search(r'[abc_]+', 'abccccc_abc_abc_abc'))
print(re.search(r'[c-d]+', 'abccccc_abc_abc_abc'))
print(re.search(r'[c-d]+?', 'abccccc_abc_abc_abc'))


# Znaki specjalne tracą swoje specjalne znaczenie w nawiasach kwadratowych np [(+*)] oznacza znajdź mi otwarcie okrągłego nawiasu, plus, gwiazdkę lub zamknięcie okrągłego nawiasu

# In[40]:


print(re.search(r'[(+*)]', 'ababa + ababa'))
print(re.search(r'[(+*)]+', 'ababa ((++ ababa '))#[]zakres którego szukam


# W nawiasach kwadratowych zastosowanie ^ oznacza znak wykluczenia, a więc będziemy szukać wszystkiego poza tym znakiem

# In[42]:


print(re.search(r'[^5]+', '123456789'))#wszystko tylko nie


# In[50]:


print(re.search(r'[^45]+', '123456789'))#wszystko tylko nie ////szukaj ciągu znaków a przy findall
print(re.findall(r'[^45]+', '123456789'))#wszystko tylko nie ////szukaj ciągu znaków a przy findall wszystkie ciągi


# In[ ]:


print(re.search(r'Warszawa|Krakow', 'Warszawa to piekne miasto'))# | lub


# Istnieją także skróty :
#     * \d - cyfry
#     * \D - nie cyfry
#     * \s - spacje, taby, nowe linie itp
#     * \S - stringi, włączając w to znaki specjalne oraz cyfry
#     * \w - słowa, czyli j.w. bez znaków specjalnych [a-zA-Z0-9_]
#     * \W - zaprzeczenie w.w.

# In[44]:


print(re.search(r'\s+', 'Warszawa        to piekne miasto'))


# In[45]:


print(re.search(r'\S+', 'Warszawa to piekne miasto'))#znajdzie do spacji


# In[46]:


print(re.search(r'\w+', 'Warszawa to piekne miasto'))#w wyszukuje litery albo cyfry


# In[47]:


print(re.search(r'\W+', 'Warszawa++?*)%^&) to piekne miasto'))


# Aby znaleźć wszystkie dopasowania stosujemy findall() zamiast search()

# In[48]:


print(re.findall(r'\w+', 'Warszawa to piekne miasto'))


# Możemy też wykorzystać wyrażenia regularne do zamiany na inny string dzięki wykorzystaniu sub()

# In[49]:


print(re.sub(r'\w+', 'zmieniony','Warszawa to piekne miasto'))#zmieniamy wszystko na jedną wartość


# -------------
# https://regex101.com/

# ------------------
# Ok, przejdźmy teraz do ćwiczeń:

# 1. Znajdźmy w poniższym stringu numery telefonów

# In[126]:


string_to_clean = 'BTgMrF0npR665-5544-63BTgMrF0npR735-5520-51BTgMrF0npR885-5543-07BTgMrF0npR795-5583-74BTgMrF0npR505-5574-48BTgMrF0npR735-5514-34BTgMrF0npR455-5578-66BTgMrF0npR575-5596-20BTgMrF0npR605-5581-78BTgMrF0npR695-5575-18BTgMrF0npR885-5525-86BTgMrF0npR455-5535-05BTgMrF0npR785-5577-67BTgMrF0npR665-5533-11BTgMrF0npR695-5594-32BTgMrF0npR535-5540-51BTgMrF0npR785-5568-32BTgMrF0npR575-5592-96BTgMrF0npR455-5563-01BTgMrF0npR605-5537-21BTgMrF0npR455-5531-45BTgMrF0npR725-5534-83BTgMrF0npR885-5542-59BTgMrF0npR795-5516-02BTgMrF0npR695-5585-66BTgMrF0npR505-5572-18BTgMrF0npR735-5590-00BTgMrF0npR505-5543-71BTgMrF0npR735-5542-93BTgMrF0npR535-5563-43BTgMrF0npR665-5518-66BTgMrF0npR665-5538-23BTgMrF0npR605-5568-72BTgMrF0npR885-5549-15BTgMrF0npR455-5566-28BTgMrF0npR785-5580-92BTgMrF0npR695-5583-90BTgMrF0npR535-5561-47BTgMrF0npR505-5586-43BTgMrF0npR455-5550-78 '
string_to_clean
print(re.findall(r'\d{3}-\d{4}-\d{2}', string_to_clean))


# In[ ]:





# 2. Znajdź jedynie imiona żeńskie, wyczyść je z innych znaków, jeśli będzie taka potrzeba

# In[130]:


imiona = 'Balbina, Barbara, Beata, Berenika, Bernadeta, Bianka, Blanka, Bogda, Bogna, Bogumiła, Bogusława, Edyta, Bartłomiej, Bartosz, Bastian, Beniamin, Benjamin, Bernard, Błażej, Bogumił, Bolesław, Borys, Bożydar, Brajan, Eftalia, Elena, Eleonora, Eliza, Elwira, Jadwiga, Jagna, Jagoda, Jana, Janina, Jaśmina, Leokadia, Jessica, Joanna, Jola, Jacek, Jacob, Jakub, Jan, Janusz, Jarosław, Jeremi, Jeremiasz, Jerzy, Jędrzej, Joachim'
imiona
print(re.findall(r'.[a-z]+a,','Balbina, Barbara, Beata, Berenika, Bernadeta, Bianka, Blanka, Bogda, Bogna, Bogumiła, Bogusława, Edyta, Bartłomiej, Bartosz, Bastian, Beniamin, Benjamin, Bernard, Błażej, Bogumił, Bolesław, Borys, Bożydar, Brajan, Eftalia, Elena, Eleonora, Eliza, Elwira, Jadwiga, Jagna, Jagoda, Jana, Janina, Jaśmina, Leokadia, Jessica, Joanna, Jola, Jacek, Jacob, Jakub, Jan, Janusz, Jarosław, Jeremi, Jeremiasz, Jerzy, Jędrzej, Joachim'))


# In[127]:


imiona_2 = imiona.split(' ')
imiona_2


# In[129]:


imiona = re.findall(r'\w+a,',imiona)
imiona = [x.replace(',','') for x in imiona]
imiona


# 3. Policz ile liter 'i' znajduje się w super napisie

# In[88]:


super_napis = 'piigiiiihiiiiiiiihihihihiffffffiiiiiiiiiiikikikikikikiloiiiiiiiiiiiiiaaaaaaappppppppppppppppyyyyyyyyyyyyiiiiiiiiiiiii'
super_napis
print(re.findall(r'i*\d', super_napis))


# In[131]:


len(re.findall('i',super_napis))


# 4. Znajdź adresy mailowe

# In[104]:


napis = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher super_user@gmail.com'
napis
print(re.findall(r'.[a-z]+@[a-z]*.[a-z]*',napis))


# In[134]:


print(re.findall('\w+@\w+\.\w+', napis))


# 5. Zamień domene z adresów mailowych na onet.pl

# In[115]:


napis = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher super_user@gmail.com'
napis
print(re.sub(r'@[a-z]*.[a-z]*','@onet.pl', napis))


# In[137]:


re.sub(r'@\S+','@onet.pl',napis)


# 6. Napisz zapytanie wyszukujące, czy w stringu znajduje się 'q' lub 'Q'

# In[138]:


super_string = 'kwa kwa qua'
print(re.search(r'q|Q', super_string))


# In[ ]:





# 7. Napisz zapytanie wyszukujące, czy w stringu znajduje się '*'

# In[139]:


super_string = 'moj super string z gwiazdka *'
print(re.search(r'\*',super_string))
print(re.search(r'[*]',super_string'))


# In[ ]:





# 8. Stwórz słownik danych osobowych z poniższego stringa

# In[124]:


string_z_danymi = 'Karol Kowalski, ul.Prosta 5/10, 675-835-578, 04-445'
print(re.findall(r'\w+',string_z_danymi))


# In[141]:


kod_pocztowy = re.search(r'\d{2}-\d{3}',string_z_danymi).group()
telefon = re.search(r'\d{3}-\d{3}-\d{3}',string_z_danymi).group()
print(kod_pocztowy, telefon)


# In[144]:


adres = re.search(r'ul\..+?,',string_z_danymi).group()
print(adres)


# In[147]:


imie_nazwisko = re.search(r'\w+ {1}\w+,?',string_z_danymi).group()
print(imie_nazwisko)


# 9. Napisz zapytanie wyszukujące, czy w stringu znajdują się dwie samogłoski pod rząd (a,e,i,o,u)

# In[150]:


super_string = 'moaj supear string z gwiazdka *'
super_string_bez = 'moj supr string z gwazdka *'


# In[153]:


print(re.search(r'[aeiou][2]', super_string'))
print(re.search(r'[aeiou][2]',super_string_bez'))


# 10. Napisz zapytanie wyszukujące, czy w stringu znajduje się przynajmniej 6 znaków

# In[154]:


dlugi_string = '* 345 ja'
krotki_string = '12 ja'


# In[156]:


print(re.search(r'.[6]', dlugi_string))
print(re.search(r'.[6]', krotki_napis))


# 11. Napisz pętlę określającą, czy w stringu znajduje się słowo 'obiad'

# In[159]:


moja_obiadowa_lista = [
    'ale super obiad',
    'tu nie maobiadu',
    'chce do domu',
    'zima idzie',
    'bedzie obiad?'
    'obiad     '
]


# In[160]:


for string in moja_obiadowa_lista:
    print(re.search(r'( obiad)|(obiad )',string))


# In[ ]:




