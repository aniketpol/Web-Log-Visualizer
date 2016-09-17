import csv
from pylab import *
import matplotlib.pyplot as plt
count1=[]
req_data=[]
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
                row[9][1:15]=[':'.join(row[9][1:15])]

                if row[5][0][1][:4].lower() == 'www.':
                    row[5][0][1]=row[5][0][1][4:]
                pdata.append(row)


        #for term in pdata:
         #       print(term)

        for row in pdata:
                #print(row[6])
                item=row[6]

                if row[5][0][1]==str:
                    req_data1.append(item)
                if item in req_data:
                    continue
                else:
                    if (row[5][0][1]==str):
                       req_data.append(row[6])


        #print(ipdata1)
        for row in req_data:
               count1.append(req_data1.count(row))


        print(count1)
        f.close()
        return count1;

def main():
    count=[]
    count=get_request('www.twibuzz.com')

    '''#this is for non bar plot
    plt.ylabel('WWW.TWIBUZZ.COM')
    #plt.xlabel("No of Hits by Different IP's")
    #plt.xticks(count,ipdata)
    plt.plot(count,'g*-',label='Hit Count', linewidth=2)''

    #this is bar graph
    #plt.xticks(count,ipdata,rotation='vertical')'''

    import pylab as p
    fig = p.figure()
    ax = fig.add_subplot(1,1,1)

    N=len(count)
    ind=range(len(count))

    ax.bar(ind, count, facecolor='blue', ecolor='black')

    ax.set_ylabel('No of Hits')

    ax.set_title("Hit count of Different IP's on www.twibuzz.com",fontstyle='italic')

    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    majorLocator   = MultipleLocator(1)

    ax.xaxis.set_major_locator(majorLocator)
    ax.set_xticklabels(req_data,rotation='vertical')
    #ax.xaxis.set_linespacing(4)
    #fig.autofmt_xdate()

    p.show()

    '''plt.bar(range(len(count)),count,align="center",width=0.5,alpha=0.5)
    plt.ylabel('WWW.TWIBUZZ.COM')
    plt.xlabel('No of Hits')
    plt.set_xticklabels(count)
    def autolabel(rects):
     for rect in rects:
        height = rect
        plt.text(1.05*height, '%d'%int(height),
                ha='center', va='bottom')'''



    plt.show()

    #this is for pie chart
    #labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    #fracs = [15, 30, 45, 10]
    #explode=(1, 0.05, 1, 1)
    #pie(count, explode=explode, labels=ipdata,
    #autopct='%1.1f%%', shadow=True, startangle=90)
    #title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5}

    #show()
    pass

if __name__ == '__main__':
    main()
