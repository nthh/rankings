
# coding: utf-8

# In[266]:

from urllib import request
from bs4 import BeautifulSoup

page = request.urlopen().read()
soup = BeautifulSoup(page)


# In[ ]:

for year in 


# In[368]:

#a= soup.find(id='Collegiate_Baseball')
#


df_baseball = pd.DataFrame()

for year in range(2002,2017+1):
    print(year)
    link = 'https://en.wikipedia.org/wiki/%s_NCAA_Division_I_baseball_rankings'%(year)
    soup = BeautifulSoup(request.urlopen(link).read())
 
    df = pd.read_html(str(soup.find(id=['Collegiate_Baseball','Collegiate_Baseball_Poll']).find_next('table')))[0]
    
    columns = ['RK']
    columns.extend(df.loc[0][1:])
    df.columns = columns
    df['SEASON'] = year

    df_baseball = df_baseball.append(pd.melt(df[df.RK.notnull()],id_vars=['RK','SEASON'], 
                                   value_vars = [row for row in df.columns if str(row) not in ('SEASON','nan','RK')], 
                                   var_name = 'WEEK', value_name = 'TEAM')).dropna()


# In[384]:

df_football['TEAM_PARSED'] = df_football.TEAM.map(lambda x: x.split('(')[0].strip())
df_baseball['TEAM_PARSED'] = df_baseball.TEAM.map(lambda x: x.split('(')[0].strip())

df_basketball.SEASON = df_basketball.SEASON.map(lambda x:x.split('-')[0])


# In[459]:

teams = []

rankings = pd.DataFrame(columns=('SEASON', 'TEAM', 'BASKETBALL','FOOTBALL','BASEBALL'))
for year in range(2006,2017):
    
    teams = df_baseball[(df_baseball.SEASON == year) &                   df_baseball.TEAM_PARSED.isin(df_basketball[(df_basketball.SEASON == year) &                   df_basketball.TEAM_PARSED.isin(df_football[df_football.SEASON==year].TEAM_PARSED)].TEAM_PARSED)]         .TEAM_PARSED.unique()
        
    for team in teams:
        rankings = rankings.append([{'SEASON':year,'TEAM':team, 
                          'BASKETBALL':df_basketball[(df_basketball.SEASON == year) &\
                                                     (df_basketball.TEAM_PARSED == team)].RK.mean(),
                          'FOOTBALL':df_football[(df_football.SEASON == year) & (df_football.TEAM_PARSED == team)].RK.mean(),
                          'BASEBALL': df_baseball[(df_baseball.SEASON == year) & (df_baseball.TEAM_PARSED == team)].RK.mean()
                         
                         }])
       
        
        
        
        


# In[473]:

rankings


# In[454]:

df_baseball[(df_baseball.SEASON == year) & (df_baseball.TEAM_PARSED == teams[1])].RK.mean()
df_football[(df_football.SEASON == year) & (df_football.TEAM_PARSED == teams[1])].RK.mean()
df_basketball[(df_basketball.SEASON == year) & (df_basketball.TEAM_PARSED == teams[1])].RK.mean()


# In[452]:

df_baseball[(df_baseball.SEASON == year)& (df_baseball.TEAM.str.startswith('Flor'))]


# In[412]:

df_basketball[      df_basketball.TEAM in (df_football[df_football.SEASON==2006].TEAM_PARSED.unique()]


# In[356]:

df_football = pd.DataFrame()

for year in range(2002,2017+1):
    print(year)
    link = 'https://en.wikipedia.org/wiki/%s_NCAA_Division_I_FBS_football_rankings'%(year)
    soup = BeautifulSoup(request.urlopen(link).read())
 
    df = pd.read_html(str(soup.find(id=['AP_Poll','AP_poll']).find_next('table')))[0]
    
    columns = ['RK']
    columns.extend(df.loc[0][1:])
    df.columns = columns
    df['SEASON'] = year

    df_football = df_football.append(pd.melt(df[df.RK.notnull()],id_vars=['RK','SEASON'], 
                                   value_vars = [row for row in df.columns if str(row) not in ('nan','RK','SEASON')], 
                                   var_name = 'WEEK', value_name = 'TEAM')).dropna()


# In[366]:

df_football


# In[347]:

df_baseball.dropna()


# In[326]:

import numpy as np
[(type(row),str(row)) for row in df.columns]


# In[307]:

nan


# In[146]:

#Basketball Rankings
from time import sleep

df_all = pd.DataFrame()


for year in range(2003,2017+1):
    
    for week in range(1,18+1):
        
        link = 'http://www.espn.com/mens-college-basketball/rankings/_/year/%s/week/%s/seasontype/2'%(year,week)
        soup = BeautifulSoup(request.urlopen(link).read())
 
        sleep(.2)
        try:
            print(year,week)
            for table in soup.findAll('table'):
                df = pd.read_html(str(table))[0]

                df.columns = df.iloc[1]
                df['POLL'] = df.iloc[0][0]
                df = df[2:]
                #Season
                df['SEASON'] = soup.find(id='dropdowns').findAll('option',selected=True)[0].text

                #Week
                df['WEEK'] = soup.find(id='dropdowns').findAll('option',selected=True)[1].text

                #title
                df['TITLE'] = soup.findAll('h1')[0].text
                if len(df) > 5:
                    df_all = df_all.append(df)
        except: 
            print(year,week,'EXCEPTION')
            next


# In[265]:

df_all.to_csv('NCAABrankings.csv')


# In[260]:

df_all[df_all.TEAM_PARSED.str.startswith('Alaba')].TEAM_PARSED.unique()


# In[230]:

df_all[(df_all.POLL == 'AP Top 25') & (df_all.TEAM_PARSED == 'Alabama')].RK.mean()


# In[259]:

df_all.TEAM_PARSED = df_all.TEAM_PARSED.str.strip()


# In[213]:

df_all.dtypes


# In[119]:

for year in dfDict:
    print(year,len(dfDict[year][0]))


# In[123]:

df_all = pd.DataFrame()


# In[125]:

df_all = df_all.append(dfDict[2011][0])


# In[126]:

df_all = df_all.append(dfDict[2012][0])


# In[129]:

df_all


# In[29]:

list(range(2003,2017+1))
list(range(1,19+1))


# In[30]:

import pandas as pd


# In[86]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen('http://68.71.212.186/mens-college-basketball/team/roster/_/id/2751').read()
soup = BeautifulSoup(page)
soup.prettify()


# In[ ]:




# In[41]:

import pandas as pd
#df = pd.read_csv('https://query.data.world/s/27q9lb4mw9d5ck96lhix48tj8')
kag = pd.read_csv('RegularSeasonDetailedResults.csv')
teams = pd.read_csv('Teams.csv')


# In[5]:

for letter in 'fang':
    print letter


# In[57]:

kag[(kag.Season == 2016)&(kag.Wteam == 1330)].Wfga3


# In[68]:

list(kag)


# In[93]:

x= kag.groupby(['Season','Wteam']).Wstl.mean().sort_values()
y = kag.groupby(['Season','Wteam']).Lstl.mean().sort_values()
#y = kag.groupby(['Season','Wteam']).size()

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns

plt.scatter(x,y)


# In[56]:

kag[kag.Season == 2016][['Wfga3','Wfgm3']].sort_values('Wfga3').head()
kag.iloc[71092,:]

kag.groupby(['Season','Wteam']).Wfga3.mean().sort_values()




# In[58]:

teams[(teams.Team_Id == 1330) | (teams.Team_Id == 1381)]


# In[ ]:

kag[kag.Season == 2016][['Wfga3','Wfgm3']].sort_values


# In[12]:

df[['Winning Seed','Losing Seed','Winning Score','Losing Score']]


# In[15]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns

df[ (df['Winning Seed'] - df['Losing Seed']) == 8]

colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(df[['Winning Seed','Losing Seed','Winning Score','Losing Score']].astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)


# In[ ]:

df[ (df['Winning Seed'] - df['Losing Seed']) == 4].groupby(['Winning Seed','Losing Seed']).size


# In[16]:


ncaa.sort_values('OPP_SCORE',ascending=False).head(5).to_clipboard()
ncaa.head(5)


# In[21]:

plt.scatter(x=ncaa.SEED,y=ncaa.OPP_SEED, c = 'Red')
#plt.scatter(x=ncaa.SCORE,y=ncaa.OPP_SCORE, c = 'Red')


# In[26]:

ncaa[(ncaa.SEED == 1) & (ncaa.OPP_SEED == 13)]


# In[32]:

ncaa.groupby(['SEED','OPP_SEED']).order_size().plot()


# In[3]:

import pandas as pd
from sqlalchemy import create_engine

alch_CONN_STR = 'SYSTEM:dbpassword@127.0.0.1:1521/XE'

engine = create_engine('oracle+cx_oracle://'+ alch_CONN_STR)

ncaa = pd.read_sql(con=engine, sql = 'SELECT * FROM NCAA_FINAL')
ncaa.columns = [col.strip().upper().replace(' ','_')  for col in ncaa.columns] 


# In[69]:

games = ncaa.groupby(['TEAM']).size().add(ncaa.groupby(['OPP_TEAM']).size(),fill_value=0)
wins = ncaa[ncaa.OPP_SCORE<ncaa.SCORE].groupby(['TEAM']).size().add(ncaa[ncaa.OPP_SCORE>ncaa.SCORE].groupby(['OPP_TEAM']).size(),fill_value=0)
(wins/games).sort_values(ascending=False)

ncaa[(ncaa.YEAR == 2013)]


# In[5]:

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
#ncaa.head(5).plot.scatter()


# In[929]:

elite_eight = ncaa[ncaa['round'] == 4]
sweet_16 = ncaa[ncaa['round'] == 3]


# In[931]:

(sweet_16.groupby(ncaa.seed).size().add(sweet_16.groupby(ncaa.opp_seed).size(),fill_value=0)).plot.bar()


# In[928]:

#(ncaa.groupby(ncaa.seed).size().add(ncaa.groupby(ncaa.opp_seed).size(),fill_value=0)).plot.bar()
(elite_eight.groupby(ncaa.seed).size().add(elite_eight.groupby(ncaa.opp_seed).size(),fill_value=0)).plot.bar()


# In[ ]:

(ncaa.groupby(ncaa.seed).size().add(ncaa.groupby(ncaa.opp_seed).size(),fill_value=0)).plot


# In[ ]:




# In[889]:




# In[894]:

df_final.columns = [col.strip().upper().replace(' ','_')  for col in df_final.columns]  

df_final.to_sql(name='NCAA',con=engine,index_label= 'RECORD_NUM',index=True)


# In[48]:

import time

for team in xrange(2750,2770):
    page = urllib2.urlopen('http://68.71.212.186/mens-college-basketball/team/roster/_/id/' + str(team)).read()
    soup = BeautifulSoup(page)
    time.sleep(.1)
    if len(soup.findAll('b')) > 0:
        print soup.findAll('b')[0]
    



# In[68]:

#year = str(2014)


# In[78]:


link = 'http://www.espn.com/mens-college-basketball/statistics/player/_/stat/blocks/sort/blocks/year/'
for year in xrange(2000,2016):
    page = urllib2.urlopen(link + str(year))
    soup = BeautifulSoup(page)
    print year,soup.findAll('td')[25]
    time.sleep(.5)                       
    


# In[386]:

link = 'http://www.databasesports.com/ncaab/tourney.htm?yr=' + str(year)

page = urllib2.urlopen(link)
soup = BeautifulSoup(page)


# In[182]:

import urllib2
from bs4 import BeautifulSoup
dir(soup.findAll('table')[3].findAll('a')[0])
midwest = soup.findAll('table')[3]

#.findAll('a')[0].find_previous_sibling()


# In[318]:

type(midwest.findAll("tr", { "class" : "tourney" })[0].findAll('td')[1].contents[1])


# In[864]:

list()


# In[882]:



bracket = 6
#year = 2010
df_final = pd.DataFrame()

for year in xrange(1985,2010+1):
    
    team_seed = {}

    data = []
    
    time.sleep(.5)
    link = 'http://www.databasesports.com/ncaab/tourney.htm?yr=' + str(year)

    page = urllib2.urlopen(link)
    soup = BeautifulSoup(page)

    for region_num in xrange(2,6):

        region_name = soup.findAll('table')[region_num].contents[0].contents[0].contents[0]

        region = soup.findAll('table')[region_num]


        for b_num, bracket in enumerate(region.findAll("tr", { "class" : "tourney" })):

            for k,tag in enumerate( bracket.findAll('td')):

        #for k,tag in enumerate(south.findAll("tr", { "class" : "tourney" })[bracket].findAll('td')):
            #print tag.contents

            #print 'tag' + str(k)

                for i,content in enumerate(tag.contents):

                    #print 'content' + str(i)

                    if k == 0:
                        rnd = 1
                        if i in (0,4):
                            seed = content
                        if i in (1,5):
                            team = content.text
                            if team not in team_seed:
                                team_seed[team] = seed
                        if i in (2,6):
                            score = int(content.strip())

                            data.append([year,region_name,rnd,b_num+1,team,score])

                    if k > 0 and k < 8:

                        rnd = k/2.0+1
                        if rnd == int(rnd):

                            if i == 0:
                                team = content.text
                                #print 'round : ' + str(rnd) + ',team: ' + team
                            if i == 1:
                                score = int(content.strip())
                                data.append([year,region_name,int(rnd),b_num+1,team,score])

                    #if  type(content) == type(bs4tag):
                    #    print content.text
                    #else:
                    #    print content
    df = pd.DataFrame(data, columns=['Year','Region','Round','Bracket','Team','Score'])
    df['Match'] = np.ceil(df.Bracket/(2.0**(df.Round-1)))

    for team in team_seed:
        team_seed[team] = int(str(team_seed[team]).strip().replace('(','').replace(')',''))
        df['Seed'] = df['Team'].map(team_seed)

    df_final = df_final.append(df,ignore_index=True)


# In[887]:



#alch_CONN_STR = 'SYSTEM:dbpassword@127.0.0.1:1521/XE'

engine = create_engine('oracle+cx_oracle://'+ alch_CONN_STR)
df_final.groupby(['Year','Region','Round','Bracket'])


# In[ ]:




# In[599]:

east = soup.findAll('table')[2]
midwest = soup.findAll('table')[3]
south = soup.findAll('table')[4]
west = soup.findAll('table')[5]


# In[479]:

soup.findAll('table')[2].contents[0].contents[0].contents[0]


# In[477]:

print list(xrange(2,6))


# In[492]:

import pandas as pd


# In[834]:

df2 = df[(df.Region == 'East') & (df.Round == 2)]
df2


# In[821]:




# In[861]:

df


# In[850]:

team_seed['Baylor'].apply(lambda x: )


# In[849]:

str(team_seed['Baylor'])


# In[859]:

df['Seed'] = df['Team'].map(team_seed)


# In[ ]:




# In[855]:




# In[756]:

1- 16 - 8
2- 8 - 4 
3- 4 - 2 
4- 2 - 1


16/1 16/2 16/4 16/8


b/r
b/r
b/(r+1)
b/(r*2)


1 1/1
2 1/2
3 1/4
4 1/8

2^(r-1)


# In[793]:

2.0**(3)/b


# In[785]:

2^0
2^1
2^2
(2)^(3)-1
(2)
2^(1^)


# In[777]:


r=4
for x in xrange(1,9):
    print np.ceil(((1.0)*x/r))


# In[695]:

r = 2
b = 8
(b)*((1.0/(r+1)))


# In[799]:




# In[359]:

for section in south.findAll("tr", { "class" : "tourney" }):

    for tag in section.findAll('td'):
        #print tag.contents
        for i,content in enumerate(tag.contents):

            if  type(content) == type(bs4tag):
                print content.text
            else:
                print content       


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[179]:

print soup.findAll('table')[3].prettify()


# In[237]:

soup


# In[3]:

a = raw_input('Guess number between 1 and 100')

print a


# In[28]:

import numpy as np
rand_int = np.random.randint(100)
print rand_int
guess = int(raw_input('Guess: '))
tries = 1
while guess <> rand_int:
    if guess < rand_int:
        print 'Go higher'
    if guess > rand_int:
        print 'Go lower'
    tries += 1
    guess = int(raw_input('Guess: '))
print 'num guesses: ' + str(tries)    


# In[92]:

import pandas as pd
df = pd.read_csv('https://query.data.world/s/bp6xjlw6tle6sir0g5xlsowr4')


# In[105]:

list(df)


# In[150]:

plt.scatter(df['Year'],df['Children'])


# In[119]:

df.groupby('Age').Sleeping.mean().plot()


# In[159]:

fig = plt.gcf()
fig.set_size_inches(20, 3)
df.groupby(['Gender'])['Housework'].mean().plot()


# In[141]:

df.groupby(['Education Level']).Golfing.mean().plot()


# In[102]:

volunt = df[(df['Weekly Earnings'] > 0 )& (df['Volunteering'] > 0 )]


# In[112]:

len(df)


# In[ ]:




# In[168]:

import pandas as pd
df = pd.read_csv('https://query.data.world/s/9bfgt92wyeywhm3sm45xuozhe')


# In[172]:

df[ df.State == 'RI']


# In[ ]:

import vincent
state_data = pd.read_csv(state_unemployment)
vis.tabular_data(state_data, columns=['State', 'Unemployment'])
vis.geo_data(bind_data='data.id', reset=True, states=state_geo)
vis.update_map(scale=1000, projection='albersUsa')
vis + (['#c9cedb', '#0b0d11'], 'scales', 0, 'range')
vis.to_json(path)


# In[164]:

import pandas as pd
df = pd.read_excel('https://query.data.world/s/6mgyyd4571w5jeaz5z7u331mt')


# In[165]:

df

