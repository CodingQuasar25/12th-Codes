d,f={},['Seniors','Sub-Juniors','Juniors']

def nestd(d):
    print('\nThe leading scores are')
    for i in f:
        ct=d[i]['Shivaji']
        for j in d[i]:
            if d[i][j]>ct:
                ct,h=d[i][j],j
                cd=1
            elif d[i][j]==ct:
                h1=j
                cd=2
        if cd==1:
            print(i,':-',h,':',ct)
        elif cd==2:
            print(i,':-',h,'&',h1,':',ct)

for i in f:
    c={}
    print('Scores of',i)
    c['Shivaji']=int(input('Enter Score of Shivaji: '))
    c['Tagore']=int(input('Enter Score of Tagore: '))
    c['Pratap']=int(input('Enter Score of Pratap: '))
    c['Bharathi']=int(input('Enter Score of Bharathi: '))
    d[i]=c    
nestd(d)
