from bs4 import BeautifulSoup
import requests
import os


def download_file(link,year):
    #eksagwgh  link kai katevasma arxeiou excel
    href = link.get("href")
    #orizw path gia apothhkeush excel k html me to onoma kai thn xronologia an den yparxoun hdh
    if os.path.isfile('spetzfiles/' + str(year) + '/' + link.get_text()+str(year)+'.xls'): 
        print('spetzfiles/' + str(year) + '/' + link.get_text() + str(year) + '.xls uparxei hdh!') #
    else:
        file = requests.get(str(href))
        print('spetzfiles/' + str(year) + '/' + link.get_text() + str(year) + '.xls welcome tomyprog !')
        open('spetzfiles/' + str(year) + '/' + link.get_text() + str(year) + '.xls', 'wb').write(file.content)



#link tis istoselidas gia ta statistika 

baseUrl = 'https://www.statistics.gr/el/statistics/-/publication/STO12/'
fileUrl = []

#dhmiourgia fakelou gia thn apothikeush ton excel files
if not os.path.exists('spetzfiles'):
    os.makedirs('spetzfiles')

#gemisma tou fileUrl[] me ta urls gia kathe etos --> baseUrl+year
#dhmioyrgia fakelou gia kathe etos ksexwrista apo to 2015 ews to 2018
for year in range(2015,2019):
    #prosthetw ta dedomena ston folder
    fileUrl.append(baseUrl+str(year))
    print(baseUrl+str(year))
    if not os.path.exists('spetzfiles/'+str(year)): #ean den uparxei o folder mazi me tin antistoixei xronologia ftiakse enan 
        os.makedirs('spetzfiles/'+str(year))

print('-----------------------\n-----------------------\n-----------------------')
#gia kathe url tou antistoixou etous katevazoume to html page gia ekswgwgi ton links me ta arxeia excel
#apothikeysi kathe excel ston swsto fakelo me tin xronologia tou
year = 2015 
for url in fileUrl:
    #apothikeysh html selidas gia kathe etos se kathe fakelo etous
    myfile = requests.get(url)
    open ('spetzfiles/'+str(year)+'/statistics'+str(year)+'.html','wb').write(myfile.content)
    #eksagwgh olwn ton url pou periexei h selida tou antistoixou etous kai dimourgia deikti arxeiou fp
    with open('spetzfiles/'+str(year)+'/statistics'+str(year)+'.html','r',encoding='utf-8') as fp: 
        periexomena = fp.read()
        soup = BeautifulSoup(periexomena,'lxml')
        all_links = (soup.find_all('a'))
        print('Try to Download next files from: '+url)
        #anazitisi kai anagnwrisi ton links pou periexoun ta excel files me to parakatw string
        for link in all_links:
            if("Αφίξεις στα καταλύματα"in str(link)):
                download_file(link,year)
           


    year += 1
    print('-----------------------\n-----------------------\n-----------------------')



