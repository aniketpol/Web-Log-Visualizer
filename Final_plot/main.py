import wx

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Weblog Visualiser", pos = wx.DefaultPosition, size = wx.Size( 474,232 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		fgSizer2 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Select a weblog file to load ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		fgSizer1.Add( self.m_filePicker1, 0, wx.ALL, 5 )

		fgSizer2.Add( fgSizer1, 1, wx.EXPAND, 5 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Select a website", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		m_weblistbox1Choices = []
		self.m_weblistbox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_weblistbox1Choices, wx.LB_ALWAYS_SB|wx.LB_SINGLE|wx.LB_SORT )
		bSizer1.Add( self.m_weblistbox1, 1, wx.ALL|wx.EXPAND, 5 )

		fgSizer2.Add( bSizer1, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Hits per Website", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button7, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 3, 2, 0, 0 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Hits Count vs IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Hits vs Request (Bar)", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button2, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Hits Count By Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button3, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Hits vs Request (Pie)", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button4, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Hits Count vs Browsers", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button5, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Hits by Platform", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button6, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )

		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.event_fileselected )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onclick_hwebsite )
		self.m_button1.Bind( wx.EVT_BUTTON, self.onclick_hip )
		self.m_button2.Bind( wx.EVT_BUTTON, self.onclick_hreqbar )
		self.m_button3.Bind( wx.EVT_BUTTON, self.onclick_hdate )
		self.m_button4.Bind( wx.EVT_BUTTON, self.onclick_hreqpie )
		self.m_button5.Bind( wx.EVT_BUTTON, self.onclick_hbrowser )
		self.m_button6.Bind( wx.EVT_BUTTON, self.onclick_hplatform )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def event_fileselected( self, event ):
		event.Skip()

	def onclick_hwebsite( self, event ):
		event.Skip()

	def onclick_hip( self, event ):
		event.Skip()

	def onclick_hreqbar( self, event ):
		event.Skip()

	def onclick_hdate( self, event ):
		event.Skip()

	def onclick_hreqpie( self, event ):
		event.Skip()

	def onclick_hbrowser( self, event ):
		event.Skip()

	def onclick_hplatform( self, event ):
		event.Skip()



import csv
from pylab import *
import matplotlib.pyplot as plt
from pylab import *

weblist=[]
f = file
pdata=[]


def get_daterequest (filename,itemname,count1,req_data):

        f=open(filename,'r')
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
                #print(row[5][0][1])

                pdata.append(row)


        #for term in pdata:
               # print(term)

        for row in pdata:
                #(row[3][0])
                item=row[3][0]

                if row[5][0][1]==itemname:
                    req_data1.append(item)
                if item in req_data:
                    continue
                else:
                    if (row[5][0][1]==itemname):
                       req_data.append(row[3][0])


        #print(ipdata1)
        for row in req_data:
               count1.append(req_data1.count(row))


        #print(count1)
        f.close()
        return count1;

def hbydate(filename,itemname):
    count1=[]
    req_data=[]

    count=[]
    count=get_daterequest(filename,itemname,count1,req_data)


    import pylab as p
    fig = p.figure()
    ax = fig.add_subplot(1,1,1)

    N=len(count)
    ind=range(len(count))

    ax.bar(ind, count, facecolor='#980000', ecolor='black')

    ax.set_ylabel('No of Hits')

    ax.set_title("Hit count According to Dates On "+itemname,fontstyle='italic')

    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    majorLocator   = MultipleLocator(1)

    ax.xaxis.set_major_locator(majorLocator)
    ax.set_xticklabels(req_data,rotation='vertical')
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
    pie(count, labels=req_data,autopct='%1.1f%%', shadow=True, startangle=90)
    title('Type of Request to www.kinneryandrajan.com', bbox={'facecolor':'0.8', 'pad':5})'''

    show()
    pass


def get_websitecount (filename,count1,req_data):

        f=open(filename,'r')
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
               # print(term)

        for row in pdata:
                #print(row[5][0][1])
                item=row[5][0][1]
                req_data1.append(row[5][0][1])
                if item in req_data:
                    continue
                else:
                   req_data.append(row[5][0][1])


        #print(req_data)
        for row in req_data:
               count1.append(req_data1.count(row))


        #print(count1)
        f.close()
        return count1;

def hitsperwebsite(filename):
    count1=[]
    req_data=[]
    count=[]
    count=get_websitecount(filename,count1,req_data)

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

    ax.bar(ind, count, facecolor='blue', ecolor='black',width=0.3)

    ax.set_ylabel('No of Hits')

    ax.set_title("Total Hits Count Per Website",fontstyle='italic')

    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    majorLocator   = MultipleLocator(1)

    ax.xaxis.set_major_locator(majorLocator)
    ax.set_xticklabels(req_data,rotation='vertical')
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
    pie(count, labels=req_data,autopct='%1.1f%%', shadow=True, startangle=90)
    title('Overall No of Hits', bbox={'facecolor':'0.8', 'pad':5})

    show()'''
    pass


def get_request (filename,str,count1,req_data,req_newdata):

        f=open(filename,'r')
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
                #print(row[5][0][1])

                #row[9][1:15]=[':'.join(row[9][1:15])]

                pdata.append(row)


        #for term in pdata:
         #       print(term)

        for row in pdata:
                if len(row[9][0][0]) < 13:
                    item=row[9][0][0]

                if row[5][0][1]==str:
                    req_data1.append(item)
                if item in req_data:
                    continue
                else:
                    if (row[5][0][1]==str):
                       req_data.append(row[9][0][0])


        #print(ipdata1)

        for row in req_data:
               count1.append(req_data1.count(row))


        #print(count1)
        f.close()
        return count1;

def browserhits(filename,itemname):
    count1=[]
    req_data=[]
    req_newdata=[]

    count=[]
    count=get_request(filename,itemname,count1,req_data,req_newdata)


    import pylab as p
    fig = p.figure()
    ax = fig.add_subplot(1,1,1)

    N=len(count)
    ind=range(len(count))

    ax.bar(ind, count, facecolor='#980000', ecolor='black')

    ax.set_ylabel('No of Hits')

    ax.set_title("Browsers used by User Agent On " + itemname,fontstyle='italic')

    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    majorLocator   = MultipleLocator(1)

    ax.xaxis.set_major_locator(majorLocator)
    ax.set_xticklabels(req_data,rotation='vertical')
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


p_os=[]
p_os=['Yahoo!','MSIE','Windows','Exabot/3.0;','Googlebot/2.1;','Powermarks/3.5;']

def get_ip (filename,itemname,count1,ipdata):

        f=open(filename,'r')
        pdata=[]
        ipdata1=[]

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
                pdata.append(row)



        for row in pdata:
                #print(row[0])
                item=row[0]
                #print(row[5][0][1])
                if row[5][0][1]==itemname:
                    ipdata1.append(item)
                if item in ipdata:
                    continue
                else:
                    if (row[5][0][1]==itemname):
                       ipdata.append(row[0])

        #print(ipdata)
        #print(ipdata1)
        for row in ipdata:
               count1.append(ipdata1.count(row))


        #print(count1)
        f.close()
        return count1;

def iphits(filename,websitename):
    count1=[]
    ipdata=[]
    count=[]
    count=get_ip(filename,websitename,count1,ipdata)

    '''#this is for non bar plot
    plt.ylabel('WWW.TWIBUZZ.COM')
    #plt.xlabel("No of Hits by Different IP's")
    #plt.xticks(count,ipdata)
    plt.plot(count,'g*-',label='Hit Count', linewidth=2)'''

    #this is bar graph
    #plt.xticks(count,ipdata,rotation='vertical')

    import pylab as p
    fig = p.figure()
    ax = fig.add_subplot(1,1,1)

    N=len(count)
    ind=range(len(count))

    ax.bar(ind, count, facecolor='blue', ecolor='black')

    ax.set_ylabel('No of Hits')

    ax.set_title("Hit count of Different IPs on "+websitename,fontstyle='italic')

    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    majorLocator   = MultipleLocator(1)
    ax.xaxis.set_major_locator(majorLocator)
    ax.set_xticklabels(ipdata,rotation='vertical')
    print ("Total ipdata:"+str(len(ipdata)))
    ax.set_xlim(0,len(ipdata))
    ax.set_ylim(0,max(ind)+1)
    fig.subplots_adjust(bottom=0.27)
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
                ha='center', va='bottom')


    #autolabel(count)
    #plt.legend()
    plt.show()'''

    '''this is for pie chart
    #labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    #fracs = [15, 30, 45, 10]
    explode=(1, 0.05, 1, 1)
    pie(count, explode=explode, labels=ipdata,
     autopct='%1.1f%%', shadow=True, startangle=90)
    #title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5}

    show()'''
    pass


def get_plat_request (filename,str,count1,req_data,req_newdata):

        f=open(filename,'r')
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

        #print(req_data)
        for term in req_data:
            if term in os:
                 req_newdata.append(term)

        for row in req_newdata:
               count1.append(req_data1.count(row))


        #print(count1)
        f.close()
        return count1;

def platform(filename,itemname):
    count1=[]
    req_data=[]
    req_newdata=[]

    count=[]
    count=get_plat_request(filename,itemname,count1,req_data,req_newdata)


    import pylab as p
    fig = p.figure()
    ax = fig.add_subplot(1,1,1)

    N=len(count)
    ind=range(len(count))

    ax.bar(ind, count, facecolor='#009900', ecolor='black')

    ax.set_ylabel('No of Hits')

    ax.set_title("Platforms Used to Access " + itemname,fontstyle='italic')

    from matplotlib.ticker import MultipleLocator, FormatStrFormatter
    majorLocator   = MultipleLocator(1)

    ax.xaxis.set_major_locator(majorLocator)
    ax.set_xticklabels(p_os,rotation='vertical')
    #ax.xaxis.set_linespacing(4)
    fig.autofmt_xdate()

    p.show()

class InstanceFrame(MyFrame1):
    filename=""

    def display_graph(self,count,req_data,title,ystring):
        import pylab as p
        fig = p.figure()
        ax = fig.add_subplot(1,1,1)

        N=len(count)
        ind=range(len(count))

        ax.bar(ind, count, facecolor='blue', ecolor='black')

        ax.set_ylabel(ystring)

        ax.set_title(title,fontstyle='italic')

        from matplotlib.ticker import MultipleLocator, FormatStrFormatter
        majorLocator   = MultipleLocator(1)

        ax.xaxis.set_major_locator(majorLocator)
        ax.set_xticklabels(req_data,rotation='vertical')
        ax.set_xlim(0,len(req_data))
        ax.set_ylim(0,len(count))

        p.show()

    def __init__(self):
        MyFrame1.__init__(self,None)

    def event_fileselected( self, event ):
        filename=self.m_filePicker1.GetPath()
        f=open(filename,'r')


        data=csv.reader(f,delimiter=' ')

        for row in data:
                row[3]=row[3][1:]
                row[3]=row[3].split(':')
                row[3][1:4]=[':'.join(row[3][1:4])]

                row[5]=row[5].split('/')
                row[5][0]=row[5][0].split(' ')

                row[4]=row[4][:5]
                row[9]=row[9].split(' ')
                row[9][1:15]=[':'.join(row[9][1:15])]
                if row[5][0][1][:4].lower() == 'www.':
                    row[5][0][1]=row[5][0][1][4:]
                if(row[5][0][1] not in weblist):
                    weblist.append(row[5][0][1])
                pdata.append(row)
        self.m_weblistbox1.Clear()
        for x in weblist:
            self.m_weblistbox1.Append(str(x))

    def onclick_hwebsite( self, event ):
        hitsperwebsite(self.m_filePicker1.GetPath())

    def onclick_hip( self, event ):
        iphits(self.m_filePicker1.GetPath(),self.m_weblistbox1.GetStringSelection())

    def onclick_hreqbar( self, event ):
        itemname=self.m_weblistbox1.GetStringSelection()
        count1=[]
        req_data1=[]
        req_data=[]
        for row in pdata:
                item=row[6]

                if row[5][0][1]==itemname:
                    req_data1.append(item)
                if item in req_data:
                    continue
                else:
                    if (row[5][0][1]==itemname):
                       req_data.append(row[6])


        for row in req_data:
               count1.append(req_data1.count(row))
        self.display_graph(count1,req_data,"Hits according to Request Type on " + itemname,"Number of hits")


    def onclick_hdate( self, event ):
        hbydate(self.m_filePicker1.GetPath(),self.m_weblistbox1.GetStringSelection())


    def onclick_hreqpie( self, event ):
        itemname=self.m_weblistbox1.GetStringSelection()
        count1=[]
        req_data1=[]
        req_data=[]
        for row in pdata:

                item=row[6]

                if row[5][0][1]==itemname:
                    req_data1.append(item)
                if item in req_data:
                    continue
                else:
                    if (row[5][0][1]==itemname):
                       req_data.append(row[6])


        for row in req_data:
               count1.append(req_data1.count(row))

        figure(1, figsize=(6,6))
        ax = axes([0.1, 0.1, 0.8, 0.8])


        pie(count1, labels=req_data,autopct='%1.1f%%', shadow=True, startangle=90)
        title('Type of Request to '+itemname, bbox={'facecolor':'0.8', 'pad':5})

        show()


    def onclick_hbrowser( self, event ):
        browserhits(self.m_filePicker1.GetPath(),self.m_weblistbox1.GetStringSelection())


    def onclick_hplatform( self, event ):
        platform(self.m_filePicker1.GetPath(),self.m_weblistbox1.GetStringSelection())

    def __del__(self):
        f.close()
        pass

class MyApp(wx.App):

    def OnInit(self):

        frame = InstanceFrame()
        frame.Show(True)

        self.SetTopWindow(frame)

        return True

if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()

