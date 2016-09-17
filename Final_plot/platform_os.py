import csv
from pylab import *
import matplotlib.pyplot as plt
count1=[]
req_data=[]
req_newdata=[]
p_os=[]
p_os=['Yahoo!','MSIE','Windows','Exabot/3.0;','Googlebot/2.1;','Powermarks/3.5;']

def get_request (str):

        f=open('weblog.txt','r')
        pdata=[]
        req_data1=[]

        data=csv.reader(f,delimiter=' ')

        for row in data:
                row[3]=row[3][1:]
                row[3]=row[3].split(':')
                row[3][1:4]=[':'.join(row[3][1:4])]

                row[5]=row[5].split('/')
                row[5][0]=row[5][0].split(' ')
                #print(row[5][0][1])
                row[4]=row[4][:5]
                row[9]=row[9].split(' ')
                row[9][0]=row[9][0].split(':')

                if row[5][0][1][:4].lower() == 'www.':
                    row[5][0][1]=row[5][0][1][4:]
                #if  len(row[9])>2 and row[9][2][0] is '(' :
                 #   row[9][2]=row[3][1:]

                #row[9][1:15]=[':'.join(row[9][1:15])]

                pdata.append(row)


        #for term in pdata:
            #print(term)

        for row in pdata:
                if len(row[9]) >2:
                    item=row[9][2]

                if row[5][0][1]==str:
                    req_data1.append(item)
                if item in req_data:
                    continue
                else:
                    if (row[5][0][1]==str) and len(row[9])>2:
                       req_data.append(row[9][2])


        #print(ipdata1)
        os=['Yahoo!','MSIE','(Windows','Exabot/3.0;','Googlebot/2.1;','Powermarks/3.5;']

        p_os=['Yahoo!','MSIE','Windows','Exabot/3.0;','Googlebot/2.1;','Powermarks/3.5;']

        print(req_data)
        for term in req_data:
            if term in os:
                 req_newdata.append(term)

        for row in req_newdata:
               count1.append(req_data1.count(row))


        #print(count1)
        f.close()
        return count1;

def main():
    count=[]
    count=get_request('www.kinneryandrajan.com')


    import pylab as p
    fig = p.figure()
    ax = fig.add_subplot(1,1,1)

    N=len(count)
    ind=range(len(count))

    ax.bar(ind, count, facecolor='#009900', ecolor='black')

    ax.set_ylabel('No of Hits')

    ax.set_title("Platforms Used to Access www.kinneryandrajan.com.",fontstyle='italic')

    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    majorLocator   = MultipleLocator(1)

    ax.xaxis.set_major_locator(majorLocator)
    ax.set_xticklabels(p_os,rotation='vertical')
    #ax.xaxis.set_linespacing(4)
    fig.autofmt_xdate()

    p.show()

    '''plt.bar(range(len(count)),count,align="center",width=0.5,alpha=0.5)
    plt.ylabel('WWW.TWIBUZZ.COM')
    plt.xlabel('No of Hits')
    plt.set_xticklabels(count)
    def autolabel(rects):
     for rect in rects:
        height = rect
        plt.text(1.05*height, '%d'%int(height),
                ha='center', va='bottom')



    plt.show()

    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])

    #explode=(1, 0.05, 1)
    pie(count, labels=req_newdata,autopct='%1.1f%%', shadow=True, startangle=90)
    title('Type of Request to www.kinneryandrajan.com', bbox={'facecolor':'0.8', 'pad':5})

    show()'''

    pass

if __name__ == '__main__':
    main()
