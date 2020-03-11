import requests
import re
from bs4 import BeautifulSoup

for i in range(1495,2400):
    try:
        get_str = 'http://www.howstat.com/cricket/Statistics/Matches/MatchScorecard.asp?MatchCode='+str(i).zfill(4)
        page = requests.get(get_str)
        soup = BeautifulSoup(page.text, 'html.parser')
        td_list = soup.find_all('td')
        no_of_days = ''
        date_of_test = ''
        result_flg = ''
        for elem in td_list:
            regstr = elem.text
            if regstr.strip() == 'Match Date:':
                date_of_test = elem.findNextSiblings()[0].text
            if regstr.strip() == 'Result:':
                if elem.findNextSiblings()[0].text.strip() == 'Match drawn':
                    result_flg = 'Match Drawn'
                else:
                    result_flg = 'Result'
            r1 = re.findall("Day [0-9]",regstr)
            if r1 != []:
                no_of_days = r1[0]
        print (str(i) + '\t' + date_of_test.strip() + '\t' + no_of_days.split(' ')[1] + '\t' + result_flg.strip())
    except:
        pass