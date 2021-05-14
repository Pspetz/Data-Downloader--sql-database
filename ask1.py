from bs4 import BeautifulSoup
import requests
import os
#https://ec.europa.eu/eurostat/cache/metadata/en/tour_occ_esms.htm

def download_file(link,year):
    #eksagwgh  link kai katevasma arxeiou excel
    href = link.get("href")
    #apothhkeush excel me to onoma kai thn xronologia an den yparxoun hdh
    if os.path.isfile('spetzfiles/' + str(year) + '/' + link.get_text()+str(year)+'.xls'):
        print('spetzfiles/' + str(year) + '/' + link.get_text() + str(year) + '.xls uparxei hdh!')
    else:
        file = requests.get(str(href))
        print('spetzfiles/' + str(year) + '/' + link.get_text() + str(year) + '.xls welcome tomyprog !')
        open('spetzfiles/' + str(year) + '/' + link.get_text() + str(year) + '.xls', 'wb').write(
            file.content)



#vasiko link tis selidas gia ta statistika tou tourismou

baseUrl = 'https://www.statistics.gr/el/statistics/-/publication/STO12/'
fileUrl = []

#dhmiourgia fakelou gia thn apothikeush ton excel files
if not os.path.exists('spetzfiles'):
    os.makedirs('spetzfiles')

#gemisma tou fileUrl[] me ta urls gia kathe etos --> baseUrl+year
#dhmioyrgia fakelou gia kathe etos ksexwrista
for year in range(2015,2019):
    fileUrl.append(baseUrl+str(year))
    print(baseUrl+str(year))
    if not os.path.exists('spetzfiles/'+str(year)):
        os.makedirs('spetzfiles/'+str(year))

print('-----------------------\n-----------------------\n-----------------------')
#gia kathe url tou antistoixou etous katevazoume to html page gia ekswgwgi ton links me ta arxeia excel
#apothikeysi kathe excel ston swsto fakelo me tin xronologia tou
year = 2015 
for url in fileUrl:
    #apothikeysh html selidas gia kathe etos se kathe fakelo etous
    myfile = requests.get(url)
    open ('spetzfiles/'+str(year)+'/statistics'+str(year)+'.html','wb').write(myfile.content)
    #eksagwgh olwn ton url pou periexei h selida tou antistoixou etous
    with open('spetzfiles/'+str(year)+'/statistics'+str(year)+'.html','r',encoding='utf-8') as fp:
        contents = fp.read()
        soup = BeautifulSoup(contents,'lxml')
        all_links = (soup.find_all('a'))
        print('Try to Download next files from: '+url)
        #anazitisi kai anagnwrisi ton links pou periexoun ta excel files me to parakatw string
        for link in all_links:
            if("Διανυκτερεύσεις στα καταλύματα" and "Αφίξεις στα καταλύματα"in str(link)):
                download_file(link,year)

    year += 1
    print('-----------------------\n-----------------------\n-----------------------')
