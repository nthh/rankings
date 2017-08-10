from urllib import request
from bs4 import BeautifulSoup
import pandas as pd
import re

#dfs = {'baseball':pd.DataFrame(),'football':pd.DataFrame(),'basketball':pd.DataFrame()}

df_all = pd.DataFrame()

for year in range(2007,2016+1):

    for sport in ['baseball','football','basketball']:
        print(sport,year)
        links = {
            'baseball': 'https://en.wikipedia.org/wiki/{}_NCAA_Division_I_baseball_rankings'.format(str(year+1)),
            'football': 'https://en.wikipedia.org/wiki/{}_NCAA_Division_I_FBS_football_rankings'.format(str(year)),
            'basketball': 'https://en.wikipedia.org/wiki/{}%E2%80%93{}_NCAA_Division_I_men%27s_basketball_rankings'.format(str(year),str(year+1)[-2:].zfill(2))
            }


        soup = BeautifulSoup(request.urlopen(url=links[sport]).read())

        df = pd.read_html(str(soup.find(id=['AP_Poll','AP_poll','Collegiate_Baseball','Collegiate_Baseball_Poll']).find_next('table')))[0]

        columns = ['RK']
        columns.extend(df.loc[0][1:])
        df.columns = columns
        df['SEASON'] = year
        df['SPORT'] = sport

        df_all = df_all.append(pd.melt(df[df.RK.notnull()],id_vars=['RK','SEASON','SPORT'],
                                       value_vars = [row for row in df.columns if str(row) not in ('SPORT','SEASON','nan','RK')],
                                       var_name = 'WEEK', value_name = 'TEAM')).dropna()

df_all['WEEK_PARSED'] = df_all.WEEK.map(lambda x: x.split('[')[0].split())
df_all['WEEK_NUM'] = df_all.WEEK_PARSED.map(lambda x: x[0] if len(x) == 3 else x[1] )
df_all['TEAM_PARSED'] = df_all.TEAM.map(lambda x: x.replace('–','').replace('State','St').replace('.','').replace('ʻ','').replace('’',"'").replace('т','').split('(')[0].split('(')[0].split('(')[0].strip())
df_all.TEAM_PARSED = df_all.TEAM_PARSED.map(lambda x: x[0:re.search("\d", x).start()].strip() if re.search("\d", x) != None else x )
df_all.TEAM_PARSED = df_all.TEAM_PARSED.map(lambda x: x.replace('Cal state Fullerton','Cal St Fullerton').replace('Southern California','USC').replace('Louisvlle','Louisville').replace('Lousiville','Louisville').replace('louisville','Louisville'))

rr  = df_all[ (df_all.WEEK_NUM != 'Preseason')].set_index(['SPORT','SEASON', 'TEAM_PARSED', 'WEEK_NUM'])

class NestedDict(dict):
    def __missing__(self, key):
        self[key] = NestedDict()
        return self[key]

d = NestedDict()
# Loop to store all elements of the dataframe in
# the instance of NestedDict
for k in rr.iterrows():
    d[k[0][0]][k[0][1]][k[0][2]][k[0][3]] = k[1].values[0]

f = open('./data/data2.json', "w")
f.write(json.dumps(d,default=str,indent = 4))
f.close()

##END OF DATA SCRAPING


##LOGO SCRAPING
import requests
from time import sleep

def getLogo(school,schoolKey=None):
    sleep(.5)
    school_p = school.lower().replace(' ','-')

    if schoolKey:
        school = schoolKey

    img = 'http://i.turner.ncaa.com/dr/ncaa/ncaa7/release/sites/default/files/images/logos/schools/{}/{}.40.png'.format(school_p[0],school_p)

    session = requests.Session()
    response = session.get(img, headers={'User-Agent': 'Mozilla/5.0'})

    if response.status_code == 200:
        logos[school] = img
        with open('./data/logos/' + school + '.png', 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False

logos = {}
schools = sorted(list(df_all.TEAM_PARSED.unique()))

for school in schools:
    getLogo(school)

provider = 'bing'
for school in [team for team in schools if team not in logos]:
    sleep(5)
    lnk = 'https://www.' + provider + '.com/search?q=site:ncaa.com/schools+{}&gbv=1&sei=YwHNVpHLOYiWmQHk3K24Cw'.format(school.replace("'",'').replace(' ','+'))

    r = requests.get(lnk, headers={'User-Agent': 'Mozilla/5.0'})
    school_ids = BeautifulSoup(r.text, "html.parser").findAll('cite')

    for _id in school_ids:
        if 'ncaa.com/schools/' in _id.text:
            if getLogo(_id.text.split('/schools/')[1].split('/')[0],school):
                break

print('logo not found for:',[team for team in schools if team not in logos])
