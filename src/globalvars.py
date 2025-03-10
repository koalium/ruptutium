
Global_plane=[]
Global_planeviewnum = 0
import FreeSimpleGUI as sg

Global_Materials=[]
Global_Reverse= []
Global_Forward=[]
Global_Flat=[]
Global_Result=[]
Global_Size=[]
Global_Mto=[]
Global_testqty=[]

filpathdef = '../my_data/001.xlsx'
file_path = '../my_data/my_file.txt'
filenamedef = '1'
fileexepdef ='xlsx'

##
mtotitle = ["MTO","IR254","kimiadaran kavir","Rupture Disk 20 inch Burst pressure = 0.4 Barg , Berst Temprature = 50 C , QTY = 2"," Vaccum Support"]
mtoheader = ["index","element","properties","qty","unit","mass of unit","price of ech","Price"]
default_dbfilename = 'mainDB_.xlsx'
dbfileparh = ''
dbfilename = dbfileparh + default_dbfilename
writefilepathdefault = './'
writefilename = 'outetfile.xlsx'
writefileexcelpath= writefilepathdefault
writefileexcel = writefileexcelpath+writefilename
dbburstpressure = 'bp'
dbbursttemprature = 'bt'
rupstr = 'rupture'
rupqtystr = 'rptrqty'
elementtypestr ='type'
reverserupturesheetname = 'reverse'
forwardrupturesheetname = 'forward'
flatrupturesheetname = 'flat'
materialsheetname = 'material'
worksheetname = 'work'
holdersheetname = 'holder'
holderelementstr = 'holder'
rawsizesheet = 'size'
testsheetname='test'
mtosheet = 'mto'
sheetnameresault='results'
sheetnameinserts='inserts'
thicknessstrhedear='thickness'
sheetnameofdatabase=[]
sheetnameofdatabase.append(materialsheetname)
sheetnameofdatabase.append(sheetnameinserts)
sheetnameofdatabase.append(sheetnameresault)
sheetnameofdatabase.append(testsheetname)
sheetnameofdatabase.append(mtosheet)
sheetnameofdatabase.append(rawsizesheet)

ruplasermargin=5
rupturerawplatewidthmm=1000
rupturerawplateheightmm=2000
 
rupturelasermetalsheetedgemargins=15
rupturelasermetalsheetcutwidth=3
rupturelasermetalsheetcutmargins=3

rupturesealrolewidthmm=1200
rupturesealroleheightmm=12000

rupturelasermargin=5
findres =[]
findsize=[]
feetres=[]
mto = []
mainto=[]
rupturemakeerrorpercentage=8

##

mtoitemlist=[]
ruplayer_1=['s316',0.5]
ruplayer_2=['s316',0.1]
ruplayerseal=['ptfe',0.4]
ruplayers=[ruplayer_1,ruplayer_2,ruplayerseal]
rupturelayers=[]
ruptureprojectelementformto={
    'type':'reverse',
    'size':2,
    'bp':5,
    'bt':50,
    'layers':ruplayers,
    'qty':5,
    'sensor':False,'wirecut':False , 'analysmaterial':False, 'ship':False ,'box':False ,'tag':False, 'waterjet_layser':False
    }

SETTINGS_PATH = '.'


mlstr=""
mainmaterialheader = 'mainmat'

# Create a UserSettings object. The JSON file will be saved in the same folder as this .py file
window_contents = sg.UserSettings(path='.', filename='mysettings.json')

keys_to_save = ('-COMBOTYPER-', '-INPUTRNS-', '-SPINRQTY-','-SPINHQTY-', '-COMBOMAINMATERIALR-', '-COMBOSEALMATERIALR-', '-COMBOSUBATERIALR-', '-CBSENR-','-CBBXGR-', '-COMBOTYPEH-', '-INPUTHNS-','-COMBOMAINMATERIALH-','-CBSHPR-','-CBWJLR-', '-CBWRCR-', '-CBANMR-','-CBTAGR-','-SPINMAQTY-','-SPINRSNSQTY-',  '-INPUTRBT-', '-INPUTRBP-', '-CBGKTH-','-COMBOMAINMATERIALRH-','-SPINRHQTY-','-CBBHLDR-','-CBGKTRH-','-CBSENR-',
                '-INPUTPRICESS304SHEET-','-INPUTPRICENICKELSHEET-','-INPUTPRICESS316SHEET-','-INPUTPRICEMONELSHEET-', '-INPUTPRICEINCONELSHEET-','-INPUTPRICEHASTELLOYSHEET-','-INPUTPRICEALUMINIUMSHEET-','-INPUTPRICETITANIUMSHEET-','-INPUTPRICECOPERSHEET-','-INPUTPRICEHYDROFORM-','-INPUTPRICEBOXING-','-INPUTPRICEGASKETS-', '-INPUTPRICESHIPPING-','-INPUTPRICESHAFTMO60-','-INPUTPRICESHAFTCHROM-', '-INPUTPRICESHAFTNICKEL-', '-INPUTPRICEPTFESHEET-','-INPUTPRICEPVCSHEET-',
           '-INPUTPRICECSSHEET-','-INPUTPRICEPTFESHEET-', '-INPUTPRICEPVCSHEET-', '-INPUTPRICESHEETSILVER-', '-INPUTPRICESHAFT304-','-INPUTPRICESHAFT316-','-INPUTPRICESHAFTMONEL-','-INPUTPRICESHAFTINCONEL-','-INPUTPRICEPAINT-', '-INPUTPRICESWATERJET-','-INPUTPRICEWIRECUT-', '-INPUTPRICEBOXING-', '-INPUTPRICEHEATFORM-','-INPUTPRICEHEATTREATMENT-',
           '-INPUTPRICESHAFTHASTELLOY-','-INPUTPRICESHAFTALUMINIUM-','-INPUTPRICESHAFTCOPPER-','-INPUTPRICESHAFTTITANIUM-', '-INPUTPRICESHAFTMO40-','-INPUTPRICESHAFTSILVER-', '-INPUTPRICESTESTING-','-INPUTPRICESENSOR-','-INPUTPRICESANALYSMAT-', '-INPUTPRICESTESTING-','-INPUTPRICESTAG-', '-INPUTPRICEMILLING-','-INPUTPRICEMACHINERY-','-INPUTPRICEWELDING-', 
           '-INPUTPRICESTAG-', '-INPUTPRICEMILLING-','-INPUTPRICEMACHINERY-', '-INPUTPRICEWELDING-','-INPUTPRICEPAINT-', '-INPUTPRICESWATERJET-','-INPUTPRICEWIRECUT-','-INPUTPRICEBOXING-','-INPUTPRICESHIPPING-')

key_to_database=('material','reverse','forward','flat','size','mto','test')

ruplayermaterialsdef=['s316','s316','ptfe']
ruptomtodef=['reverse',2,5,50,ruplayermaterialsdef,5,False,False,False,False,False,False,False]   
rawsheetwidemainlayers=2000
rawsheetwideseallayer=1200
rawsheetheightmainlayers=1000
rawsheetheightseallayer=4000
