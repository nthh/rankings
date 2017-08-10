
# coding: utf-8

# In[1]:

from urllib import request
from bs4 import BeautifulSoup

page = request.urlopen().read()
soup = BeautifulSoup(page)

dfs = {'baseball':pd.DataFrame(),'football':pd.DataFrame(),'basketball':pd.DataFrame()}


for year in range(2016,2016+1):
       
    for sport in ['baseball','football','basketball']:
        print(year)
        links = {
            'baseball': 'https://en.wikipedia.org/wiki/{}_NCAA_Division_I_baseball_rankings'.format(str(year+1)),
            'football': 'https://en.wikipedia.org/wiki/{}_NCAA_Division_I_FBS_football_rankings'.format(str(year)),
            'basketball': 'https://en.wikipedia.org/wiki/{}%E2%80%93{}_NCAA_Division_I_men%27s_basketball_rankings'.format(str(year),str(year+1)[-2:].zfill(2))
            }


        soup = BeautifulSoup(request.urlopen(link).read())

        df = pd.read_html(str(soup.find(id=['AP_Poll','AP_poll','Collegiate_Baseball','Collegiate_Baseball_Poll']).find_next('table')))[0]

        columns = ['RK']
        columns.extend(df.loc[0][1:])
        df.columns = columns
        df['SEASON'] = year

        dfs[sport] = dfs[sport].append(pd.melt(df[df.RK.notnull()],id_vars=['RK','SEASON'], 
                                       value_vars = [row for row in df.columns if str(row) not in ('SEASON','nan','RK')], 
                                       var_name = 'WEEK', value_name = 'TEAM')).dropna()

