import ui
import snd
import systemSetting
import net
import chat
import app
import locale
import chrmgr
import player
import chr
import game
import background
import uiPhaseCurtain
import interfaceModule
import shop
import uiSwitchBonus

class OptionDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__Load()
		self.curtain = uiPhaseCurtain.PhaseCurtain()
		self.curtain.speed = 0.01
		self.curtain.Hide()
		race = net.GetMainActorRace()
		if race != 1000:
			self.bonus0.InsertItem(1, "Max HP")
			self.bonus0.InsertItem(2, "Kýlýç Savunmasý")
			self.bonus0.InsertItem(3, "Çift-El Savunma")
			self.bonus0.InsertItem(4, "Býçak Savunmasý")
			self.bonus0.InsertItem(5, "Çan Savunmasý")
			self.bonus0.InsertItem(6, "Yelpaze Savunmasý")
			self.bonus0.InsertItem(7, "Oka karþý dayanaklýlýk")
			self.bonus0.InsertItem(8, "Büyüye karþý dayanýklýlýk")
			self.bonus0.InsertItem(9, "Yaþam Enerjisi")
			self.bonus0.InsertItem(10, "Zeka")
			self.bonus0.InsertItem(11, "Güç")
			self.bonus0.InsertItem(12, "Çeviklik")
			self.bonus0.InsertItem(13, "Saldýrý deðeri")
			self.bonus0.InsertItem(14, "Ortalama Zarar")
			self.bonus0.InsertItem(15, "Beceri Hasarý")
			self.bonus0.InsertItem(16, "Saldýrý Hýzý")
			self.bonus0.InsertItem(17, "Hareket Hýzý")
			self.bonus0.InsertItem(18, "Büyü Hýzý")
			self.bonus0.InsertItem(19, "HP Üretimi")
			self.bonus0.InsertItem(20, "Zehirlenme Deðiþimi")
			self.bonus0.InsertItem(21, "Sersemletme Þansý")
			self.bonus0.InsertItem(22, "Kritik Vuruþ Þansý")
			self.bonus0.InsertItem(23, "Delici Vuruþ Þansý")
			self.bonus0.InsertItem(24, "Yarý insanlara karþý güçlü")
			self.bonus0.InsertItem(25, "Ölümsüzlere karþý güçlü")
			self.bonus0.InsertItem(26, "Þeytanlara karþý güçlü")
			self.bonus0.InsertItem(27, "Sersemlik karþýsýnda baðýþýklýk")
			self.bonus0.InsertItem(28, "Yavaþlama karþýsýnda baðýþýklýk")
			self.bonus0.InsertItem(29, "Beden karþýsýnda ataklarýn bloklanmasý")
			self.bonus0.InsertItem(30, "Oklardan korunma þansý")
			self.bonus0.InsertItem(31, "Vücut darbelerini yansýtma þansý")
			self.bonus0.InsertItem(32, "Zehire Karþý Koyma")
			self.bonus0.InsertItem(33, "EXP Bonus Þansý")
			self.bonus0.InsertItem(34, "Ýki kat yang düþme þansý")
			self.bonus0.InsertItem(35, "Ýki kat eþya düþme þansý")
		else:		
			self.chooseBonus0.SetText("Niciun Bonus Disponibil.")

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " -------------------------------------- DELETE GAME OPTION DIALOG"

	def __Initialize(self):
		self.titleBar = 0

	def Destroy(self):
		self.ClearDictionary()

		self.__Initialize()
		print " -------------------------------------- DESTROY GAME OPTION DIALOG"
	
	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("OptionDialog.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")
			self.setbonus0			= GetObject("Ok_button")
			self.bonus0			= GetObject("Bonus0_List")
			self.chooseBonus0			= GetObject("ChooseBonus0")
			self.cancel			= GetObject("stop_button")
		except:
			import exception
			exception.Abort("OptionDialog.__Load_BindObject")

	def __Load(self):
		self.__Load_LoadScript("UIscript/boniliste.py")

		self.__Load_BindObject()

		self.SetCenterPosition()

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

		self.setbonus0.SetEvent(ui.__mem_func__(self.__Setbonus0))
		self.cancel.SetEvent(ui.__mem_func__(self.__Cancelbonus0))
		
	def __Cancelbonus0(self):
		self.Hide()
		
	def __Setbonus0(self):
		race = net.GetMainActorRace()
		group = net.GetMainActorSkillGroup()
		getIndex = self.bonus0.GetSelectedItem()
		if getIndex == 1 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 1
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Max. HP")
		elif getIndex == 1 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 1
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Max. HP")
		elif getIndex == 1 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 1
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Max. HP")
		elif getIndex == 1 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 1
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Max. HP")
		elif getIndex == 1 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 1
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Max. HP")
		elif getIndex == 1 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 1
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Max. HP")
		elif getIndex == 1 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Max. HP")
		elif getIndex == 1 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Max. HP")
		elif getIndex == 1 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Max. HP")
		elif getIndex == 1 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Max. HP")
		elif getIndex == 2 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 29
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Kýlýç Savunmasý")
		elif getIndex == 2 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 29
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Kýlýç Savunmasý")
		elif getIndex == 2 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 29
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Kýlýç Savunmasý")
		elif getIndex == 2 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 29
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Kýlýç Savunmasý")
		elif getIndex == 2 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 29
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Kýlýç Savunmasý")
		elif getIndex == 2 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 29
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Kýlýç Savunmasý")
		elif getIndex == 2 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 29
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Kýlýç Savunmasý")
		elif getIndex == 2 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 29
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Kýlýç Savunmasý")
		elif getIndex == 2 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 29
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Kýlýç Savunmasý")
		elif getIndex == 2 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 29
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Kýlýç Savunmasý")
		elif getIndex == 3 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 30
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Çift-El Savunma")
		elif getIndex == 3 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 30
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Çift-El Savunma")
		elif getIndex == 3 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 30
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Çift-El Savunma")
		elif getIndex == 3 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 30
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Çift-El Savunma")
		elif getIndex == 3 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 30
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Çift-El Savunma")
		elif getIndex == 3 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 30
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Çift-El Savunma")
		elif getIndex == 3 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 30
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Çift-El Savunma")
		elif getIndex == 3 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 30
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Çift-El Savunma")
		elif getIndex == 3 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 30
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Çift-El Savunma")
		elif getIndex == 3 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 30
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Çift-El Savunma")
		elif getIndex == 4 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 31
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Býçak Savunmasý")
		elif getIndex == 4 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 31
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Býçak Savunmasý")
		elif getIndex == 4 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 31
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Býçak Savunmasý")
		elif getIndex == 4 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 31
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Býçak Savunmasý")
		elif getIndex == 4 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 31
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Býçak Savunmasý")
		elif getIndex == 4 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 31
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Býçak Savunmasý")
		elif getIndex == 4 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 31
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Býçak Savunmasý")
		elif getIndex == 4 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 31
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Býçak Savunmasý")
		elif getIndex == 4 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 31
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Býçak Savunmasý")
		elif getIndex == 4 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 31
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Býçak Savunmasý")
		elif getIndex == 5 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 32
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Çan Savunmasý")
		elif getIndex == 5 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 32
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Çan Savunmasý")
		elif getIndex == 5 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 32
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Çan Savunmasý")
		elif getIndex == 5 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 32
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Çan Savunmasý")
		elif getIndex == 5 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 32
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Çan Savunmasý")
		elif getIndex == 5 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 32
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Çan Savunmasý")
		elif getIndex == 5 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 32
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Çan Savunmasý")
		elif getIndex == 5 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 32
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Çan Savunmasý")
		elif getIndex == 5 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 32
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Çan Savunmasý")
		elif getIndex == 5 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 32
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Çan Savunmasý")
		elif getIndex == 6 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 33
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Yelpaze Savunmasý")
		elif getIndex == 6 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 33
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Yelpaze Savunmasý")
		elif getIndex == 6 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 33
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Yelpaze Savunmasý")
		elif getIndex == 6 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 33
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Yelpaze Savunmasý")
		elif getIndex == 6 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 33
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Yelpaze Savunmasý")
		elif getIndex == 6 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 33
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Yelpaze Savunmasý")
		elif getIndex == 6 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 33
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Yelpaze Savunmasý")
		elif getIndex == 6 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 33
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Yelpaze Savunmasý")
		elif getIndex == 6 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 33
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Yelpaze Savunmasý")
		elif getIndex == 6 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 33
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Yelpaze Savunmasý")
		elif getIndex == 7 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 34
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Oka karþý dayanaklýlýk")
		elif getIndex == 7 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 34
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Oka karþý dayanaklýlýk")
		elif getIndex == 7 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 34
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Oka karþý dayanaklýlýk")
		elif getIndex == 7 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 34
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Oka karþý dayanaklýlýk")
		elif getIndex == 7 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 34
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Oka karþý dayanaklýlýk")
		elif getIndex == 7 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 34
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Oka karþý dayanaklýlýk")
		elif getIndex == 7 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 34
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Oka karþý dayanaklýlýk")
		elif getIndex == 7 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 34
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Oka karþý dayanaklýlýk")
		elif getIndex == 7 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 34
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Oka karþý dayanaklýlýk")
		elif getIndex == 7 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 34
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Oka karþý dayanaklýlýk")
		elif getIndex == 8 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 37
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Büyüye karþý dayanýklýlýk")
		elif getIndex == 8 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 37
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Büyüye karþý dayanýklýlýk")
		elif getIndex == 8 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 37
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Büyüye karþý dayanýklýlýk")
		elif getIndex == 8 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 37
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Büyüye karþý dayanýklýlýk")
		elif getIndex == 8 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 37
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Büyüye karþý dayanýklýlýk")
		elif getIndex == 8 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 37
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Büyüye karþý dayanýklýlýk")
		elif getIndex == 8 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 37
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Büyüye karþý dayanýklýlýk")
		elif getIndex == 8 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 37
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Büyüye karþý dayanýklýlýk")
		elif getIndex == 8 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 37
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Büyüye karþý dayanýklýlýk")
		elif getIndex == 8 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 37
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Büyüye karþý dayanýklýlýk")
		elif getIndex == 9 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 3
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Yaþam Enerjisi")
		elif getIndex == 9 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 3
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Yaþam Enerjisi")
		elif getIndex == 9 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 3
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Yaþam Enerjisi")
		elif getIndex == 9 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 3
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Yaþam Enerjisi")
		elif getIndex == 9 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 3
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Yaþam Enerjisi")
		elif getIndex == 9 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 3
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Yaþam Enerjisi")
		elif getIndex == 9 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 3
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Yaþam Enerjisi")
		elif getIndex == 9 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 3
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Yaþam Enerjisi")
		elif getIndex == 9 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 3
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Yaþam Enerjisi")
		elif getIndex == 9 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 3
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Yaþam Enerjisi")
		elif getIndex == 10 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 4
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Zeka")
		elif getIndex == 10 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 4
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Zeka")
		elif getIndex == 10 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 4
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Zeka")
		elif getIndex == 10 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 4
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Zeka")
		elif getIndex == 10 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 4
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Zeka")
		elif getIndex == 10 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 4
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Zeka")
		elif getIndex == 10 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 4
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Zeka")
		elif getIndex == 10 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 4
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Zeka")
		elif getIndex == 10 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 4
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Zeka")
		elif getIndex == 10 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 4
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Zeka")
		elif getIndex == 11 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 5
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Güç")
		elif getIndex == 11 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 5
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Güç")
		elif getIndex == 11 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 5
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Güç")
		elif getIndex == 11 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 5
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Güç")
		elif getIndex == 11 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 5
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Güç")
		elif getIndex == 11 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 5
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Güç")
		elif getIndex == 11 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 5
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Güç")
		elif getIndex == 11 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 5
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Güç")
		elif getIndex == 11 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 5
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Güç")
		elif getIndex == 11 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 5
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Güç")
		elif getIndex == 12 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 6
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Çeviklik")
		elif getIndex == 12 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 6
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Çeviklik")
		elif getIndex == 12 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 6
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Çeviklik")
		elif getIndex == 12 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 6
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Çeviklik")
		elif getIndex == 12 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 6
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Çeviklik")
		elif getIndex == 12 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 6
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Çeviklik")
		elif getIndex == 12 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 6
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Çeviklik")
		elif getIndex == 12 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 6
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Çeviklik")
		elif getIndex == 12 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 6
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Çeviklik")
		elif getIndex == 12 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 6
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Çeviklik")
		elif getIndex == 13 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 53
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Saldýrý deðeri")
		elif getIndex == 13 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 53
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Saldýrý deðeri")
		elif getIndex == 13 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 53
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Saldýrý deðeri")
		elif getIndex == 13 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 53
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Saldýrý deðeri")
		elif getIndex == 13 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 53
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Saldýrý deðeri")
		elif getIndex == 13 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 53
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Saldýrý deðeri")
		elif getIndex == 13 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 53
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Saldýrý deðeri")
		elif getIndex == 13 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 53
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Saldýrý deðeri")
		elif getIndex == 13 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 53
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Saldýrý deðeri")
		elif getIndex == 13 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 53
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Saldýrý deðeri")
		elif getIndex == 14 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 72
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Ortalama Zarar")
		elif getIndex == 14 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 72
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Ortalama Zarar")
		elif getIndex == 14 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 72
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Ortalama Zarar")
		elif getIndex == 14 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 72
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Ortalama Zarar")
		elif getIndex == 14 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 72
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Ortalama Zarar")
		elif getIndex == 14 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 72
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Ortalama Zarar")
		elif getIndex == 14 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 72
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Ortalama Zarar")
		elif getIndex == 14 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 72
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Ortalama Zarar")
		elif getIndex == 14 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 72
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Ortalama Zarar")
		elif getIndex == 14 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 72
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Ortalama Zarar")
		elif getIndex == 15 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 71
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Beceri Hasarý")
		elif getIndex == 15 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 71
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Beceri Hasarý")
		elif getIndex == 15 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 71
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Beceri Hasarý")
		elif getIndex == 15 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 71
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Beceri Hasarý")
		elif getIndex == 15 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 71
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Beceri Hasarý")
		elif getIndex == 15 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 71
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Beceri Hasarý")
		elif getIndex == 15 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 71
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Beceri Hasarý")
		elif getIndex == 15 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 71
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Beceri Hasarý")
		elif getIndex == 15 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 71
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Beceri Hasarý")
		elif getIndex == 15 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 71
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Beceri Hasarý")
		elif getIndex == 16 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 7
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Saldýrý Hýzý")
		elif getIndex == 16 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 7
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Saldýrý Hýzý")
		elif getIndex == 16 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 7
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Saldýrý Hýzý")
		elif getIndex == 16 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 7
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Saldýrý Hýzý")
		elif getIndex == 16 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 7
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Saldýrý Hýzý")
		elif getIndex == 16 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 7
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Saldýrý Hýzý")
		elif getIndex == 16 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 7
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Saldýrý Hýzý")
		elif getIndex == 16 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 7
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Saldýrý Hýzý")
		elif getIndex == 16 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 7
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Saldýrý Hýzý")
		elif getIndex == 16 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 7
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Saldýrý Hýzý")
		elif getIndex == 17 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 8
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Hareket Hýzý")
		elif getIndex == 17 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 8
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Hareket Hýzý")
		elif getIndex == 17 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 8
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Hareket Hýzý")
		elif getIndex == 17 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 8
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Hareket Hýzý")
		elif getIndex == 17 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 8
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Hareket Hýzý")
		elif getIndex == 17 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 8
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Hareket Hýzý")
		elif getIndex == 17 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 8
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Hareket Hýzý")
		elif getIndex == 17 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 8
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Hareket Hýzý")
		elif getIndex == 17 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 8
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Hareket Hýzý")
		elif getIndex == 17 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 8
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Hareket Hýzý")
		elif getIndex == 18 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 9
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Büyü Hýzý")
		elif getIndex == 18 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 9
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Büyü Hýzý")
		elif getIndex == 18 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 9
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Büyü Hýzý")
		elif getIndex == 18 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 9
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Büyü Hýzý")
		elif getIndex == 18 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 9
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Büyü Hýzý")
		elif getIndex == 18 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 9
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Büyü Hýzý")
		elif getIndex == 18 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 9
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Büyü Hýzý")
		elif getIndex == 18 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 9
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Büyü Hýzý")
		elif getIndex == 18 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 9
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Büyü Hýzý")
		elif getIndex == 18 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 9
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Büyü Hýzý")
		elif getIndex == 19 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 10
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus HP Üretimi")
		elif getIndex == 19 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 10
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus HP Üretimi")
		elif getIndex == 19 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 10
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus HP Üretimi")
		elif getIndex == 19 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 10
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus HP Üretimi")
		elif getIndex == 19 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 10
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus HP Üretimi")
		elif getIndex == 19 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 10
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus HP Üretimi")
		elif getIndex == 19 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 10
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus HP Üretimi")
		elif getIndex == 19 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 10
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus HP Üretimi")
		elif getIndex == 19 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 10
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus HP Üretimi")
		elif getIndex == 19 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 10
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus HP Üretimi")
		elif getIndex == 20 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 12
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Zehirlenme Deðiþimi")
		elif getIndex == 20 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 12
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Zehirlenme Deðiþimi")
		elif getIndex == 20 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 12
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Zehirlenme Deðiþimi")
		elif getIndex == 20 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 12
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Zehirlenme Deðiþimi")
		elif getIndex == 20 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 12
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Zehirlenme Deðiþimi")
		elif getIndex == 20 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 12
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Zehirlenme Deðiþimi")
		elif getIndex == 20 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 12
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Zehirlenme Deðiþimi")
		elif getIndex == 20 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 12
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Zehirlenme Deðiþimi")
		elif getIndex == 20 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 12
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Zehirlenme Deðiþimi")
		elif getIndex == 20 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 12
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Zehirlenme Deðiþimi")
		elif getIndex == 21 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 13
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Sersemletme Þansý")
		elif getIndex == 21 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 13
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Sersemletme Þansý")
		elif getIndex == 21 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 13
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Sersemletme Þansý")
		elif getIndex == 21 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 13
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Sersemletme Þansý")
		elif getIndex == 21 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 13
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Sersemletme Þansý")
		elif getIndex == 21 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 13
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Sersemletme Þansý")
		elif getIndex == 21 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 13
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Sersemletme Þansý")
		elif getIndex == 21 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 13
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Sersemletme Þansý")
		elif getIndex == 21 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 13
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Sersemletme Þansý")
		elif getIndex == 21 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 13
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Sersemletme Þansý")
		elif getIndex == 22 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 15
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Kritik Vuruþ Þansý")
		elif getIndex == 22 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 15
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Kritik Vuruþ Þansý")
		elif getIndex == 22 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 15
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Kritik Vuruþ Þansý")
		elif getIndex == 22 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 15
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Kritik Vuruþ Þansý")
		elif getIndex == 22 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 15
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Kritik Vuruþ Þansý")
		elif getIndex == 22 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 15
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Kritik Vuruþ Þansý")
		elif getIndex == 22 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 15
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Kritik Vuruþ Þansý")
		elif getIndex == 22 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 15
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Kritik Vuruþ Þansý")
		elif getIndex == 22 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 15
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Kritik Vuruþ Þansý")
		elif getIndex == 22 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 15
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Kritik Vuruþ Þansý")
		elif getIndex == 23 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 16
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Delici Vuruþ Þansý")
		elif getIndex == 23 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 16
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Delici Vuruþ Þansý")
		elif getIndex == 23 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 16
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Delici Vuruþ Þansý")
		elif getIndex == 23 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 16
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Delici Vuruþ Þansý")
		elif getIndex == 23 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 16
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Delici Vuruþ Þansý")
		elif getIndex == 23 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 16
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Delici Vuruþ Þansý")
		elif getIndex == 23 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 16
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Delici Vuruþ Þansý")
		elif getIndex == 23 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 16
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Delici Vuruþ Þansý")
		elif getIndex == 23 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 16
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Delici Vuruþ Þansý")
		elif getIndex == 23 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 16
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Delici Vuruþ Þansý")
		elif getIndex == 24 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 17
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Yarý insanlara karþý güçlü")
		elif getIndex == 24 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 17
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Yarý insanlara karþý güçlü")
		elif getIndex == 24 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 17
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Yarý insanlara karþý güçlü")
		elif getIndex == 24 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 17
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Yarý insanlara karþý güçlü")
		elif getIndex == 24 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 17
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Yarý insanlara karþý güçlü")
		elif getIndex == 24 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 17
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Yarý insanlara karþý güçlü")
		elif getIndex == 24 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 17
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Yarý insanlara karþý güçlü")
		elif getIndex == 24 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 17
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Yarý insanlara karþý güçlü")
		elif getIndex == 24 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 17
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Yarý insanlara karþý güçlü")
		elif getIndex == 24 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 17
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Yarý insanlara karþý güçlü")
		elif getIndex == 25 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 21
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Ölümsüzlere karþý güçlü")
		elif getIndex == 25 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 21
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Ölümsüzlere karþý güçlü")
		elif getIndex == 25 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 21
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Ölümsüzlere karþý güçlü")
		elif getIndex == 25 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 21
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Ölümsüzlere karþý güçlü")
		elif getIndex == 25 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 21
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Ölümsüzlere karþý güçlü")
		elif getIndex == 25 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 21
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Ölümsüzlere karþý güçlü")
		elif getIndex == 25 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 21
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Ölümsüzlere karþý güçlü")
		elif getIndex == 25 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 21
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Ölümsüzlere karþý güçlü")
		elif getIndex == 25 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 21
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Ölümsüzlere karþý güçlü")
		elif getIndex == 25 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 21
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Ölümsüzlere karþý güçlü")
		elif getIndex == 26 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 22
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Þeytanlara karþý güçlü")
		elif getIndex == 26 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 22
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Þeytanlara karþý güçlü")
		elif getIndex == 26 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 22
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Þeytanlara karþý güçlü")
		elif getIndex == 26 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 22
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Þeytanlara karþý güçlü")
		elif getIndex == 26 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 22
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Þeytanlara karþý güçlü")
		elif getIndex == 26 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 22
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Þeytanlara karþý güçlü")
		elif getIndex == 26 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 22
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Þeytanlara karþý güçlü")
		elif getIndex == 26 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 22
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Þeytanlara karþý güçlü")
		elif getIndex == 26 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 22
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Þeytanlara karþý güçlü")
		elif getIndex == 26 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 22
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Þeytanlara karþý güçlü")
		elif getIndex == 27 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 48
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Sersemlik karþýsýnda baðýþýklýk")
		elif getIndex == 27 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 48
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Sersemlik karþýsýnda baðýþýklýk")
		elif getIndex == 27 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 48
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Sersemlik karþýsýnda baðýþýklýk")
		elif getIndex == 27 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 48
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Sersemlik karþýsýnda baðýþýklýk")
		elif getIndex == 27 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 48
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Sersemlik karþýsýnda baðýþýklýk")
		elif getIndex == 27 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 48
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Sersemlik karþýsýnda baðýþýklýk")
		elif getIndex == 27 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 48
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Sersemlik karþýsýnda baðýþýklýk")
		elif getIndex == 27 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 48
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Sersemlik karþýsýnda baðýþýklýk")
		elif getIndex == 27 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 48
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Sersemlik karþýsýnda baðýþýklýk")
		elif getIndex == 27 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 48
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Sersemlik karþýsýnda baðýþýklýk")
		elif getIndex == 28 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 49
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Yavaþlama karþýsýnda baðýþýklýk")
		elif getIndex == 28 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 49
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Yavaþlama karþýsýnda baðýþýklýk")
		elif getIndex == 28 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 49
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Yavaþlama karþýsýnda baðýþýklýk")
		elif getIndex == 28 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 49
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Yavaþlama karþýsýnda baðýþýklýk")
		elif getIndex == 28 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 49
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Yavaþlama karþýsýnda baðýþýklýk")
		elif getIndex == 28 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 49
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Yavaþlama karþýsýnda baðýþýklýk")
		elif getIndex == 28 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 49
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Yavaþlama karþýsýnda baðýþýklýk")
		elif getIndex == 28 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 49
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Yavaþlama karþýsýnda baðýþýklýk")
		elif getIndex == 28 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 49
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Yavaþlama karþýsýnda baðýþýklýk")
		elif getIndex == 28 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 49
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Yavaþlama karþýsýnda baðýþýklýk")
		elif getIndex == 29 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 27
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Beden karþýsýnda ataklarýn bloklanmasý")
		elif getIndex == 29 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 27
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Beden karþýsýnda ataklarýn bloklanmasý")
		elif getIndex == 29 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 27
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Beden karþýsýnda ataklarýn bloklanmasý")
		elif getIndex == 29 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 27
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Beden karþýsýnda ataklarýn bloklanmasý")
		elif getIndex == 29 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 27
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Beden karþýsýnda ataklarýn bloklanmasý")
		elif getIndex == 29 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 27
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Beden karþýsýnda ataklarýn bloklanmasý")
		elif getIndex == 29 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 27
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Beden karþýsýnda ataklarýn bloklanmasý")
		elif getIndex == 29 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 27
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Beden karþýsýnda ataklarýn bloklanmasý")
		elif getIndex == 29 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 27
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Beden karþýsýnda ataklarýn bloklanmasý")
		elif getIndex == 29 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 27
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Beden karþýsýnda ataklarýn bloklanmasý")
		elif getIndex == 30 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 28
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Oklardan korunma þansý")
		elif getIndex == 30 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 28
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Oklardan korunma þansý")
		elif getIndex == 30 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 28
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Oklardan korunma þansý")
		elif getIndex == 30 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 28
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Oklardan korunma þansý")
		elif getIndex == 30 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 28
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Oklardan korunma þansý")
		elif getIndex == 30 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 28
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Oklardan korunma þansý")
		elif getIndex == 30 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 28
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Oklardan korunma þansý")
		elif getIndex == 30 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 28
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Oklardan korunma þansý")
		elif getIndex == 30 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 28
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Oklardan korunma þansý")
		elif getIndex == 30 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 28
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Oklardan korunma þansý")
		elif getIndex == 31 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 39
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Vücut darbelerini yansýtma þansý")
		elif getIndex == 31 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 39
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Vücut darbelerini yansýtma þansý")
		elif getIndex == 31 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 39
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Vücut darbelerini yansýtma þansý")
		elif getIndex == 31 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 39
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Vücut darbelerini yansýtma þansý")
		elif getIndex == 31 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 39
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Vücut darbelerini yansýtma þansý")
		elif getIndex == 31 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 39
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Vücut darbelerini yansýtma þansý")
		elif getIndex == 31 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 39
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Vücut darbelerini yansýtma þansý")
		elif getIndex == 31 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 39
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Vücut darbelerini yansýtma þansý")
		elif getIndex == 31 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 39
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Vücut darbelerini yansýtma þansý")
		elif getIndex == 31 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 39
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Vücut darbelerini yansýtma þansý")
		elif getIndex == 32 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 41
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Zehire Karþý Koyma")
		elif getIndex == 32 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 41
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Zehire Karþý Koyma")
		elif getIndex == 32 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 41
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Zehire Karþý Koyma")
		elif getIndex == 32 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 41
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Zehire Karþý Koyma")
		elif getIndex == 32 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 41
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Zehire Karþý Koyma")
		elif getIndex == 32 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 41
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Zehire Karþý Koyma")
		elif getIndex == 32 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 41
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Zehire Karþý Koyma")
		elif getIndex == 32 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 41
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Zehire Karþý Koyma")
		elif getIndex == 32 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 41
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Zehire Karþý Koyma")
		elif getIndex == 32 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 41
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Zehire Karþý Koyma")
		elif getIndex == 33 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 43
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus EXP Bonus Þansý")
		elif getIndex == 33 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 43
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus EXP Bonus Þansý")
		elif getIndex == 33 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 43
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus EXP Bonus Þansý")
		elif getIndex == 33 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 43
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus EXP Bonus Þansý")
		elif getIndex == 33 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 43
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus EXP Bonus Þansý")
		elif getIndex == 33 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 43
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus EXP Bonus Þansý")
		elif getIndex == 33 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 43
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus EXP Bonus Þansý")
		elif getIndex == 33 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 43
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus EXP Bonus Þansý")
		elif getIndex == 33 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 43
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus EXP Bonus Þansý")
		elif getIndex == 33 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 43
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus EXP Bonus Þansý")
		elif getIndex == 34 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 44
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Ýki kat yang düþme þansý")
		elif getIndex == 34 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 44
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Ýki kat yang düþme þansý")
		elif getIndex == 34 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 44
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Ýki kat yang düþme þansý")
		elif getIndex == 34 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 44
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Ýki kat yang düþme þansý")
		elif getIndex == 34 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 44
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Ýki kat yang düþme þansý")
		elif getIndex == 34 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 44
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Ýki kat yang düþme þansý")
		elif getIndex == 34 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 44
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Ýki kat yang düþme þansý")
		elif getIndex == 34 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 44
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Ýki kat yang düþme þansý")
		elif getIndex == 34 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 44
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Ýki kat yang düþme þansý")
		elif getIndex == 34 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 44
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Ýki kat yang düþme þansý")
		elif getIndex == 35 and uiSwitchBonus.Bonus0 == 0 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 45
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "1.Bonus Ýki kat eþya düþme þansý")
		elif getIndex == 35 and uiSwitchBonus.Bonus1 == 0 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Bonus1 = 45
			uiSwitchBonus.Presswish1 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "2.Bonus Ýki kat eþya düþme þansý")
		elif getIndex == 35 and uiSwitchBonus.Bonus2 == 0 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Bonus2 = 45
			uiSwitchBonus.Presswish2 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "3.Bonus Ýki kat eþya düþme þansý")
		elif getIndex == 35 and uiSwitchBonus.Bonus3 == 0 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Bonus3 = 45
			uiSwitchBonus.Presswish3 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "4.Bonus Ýki kat eþya düþme þansý")
		elif getIndex == 35 and uiSwitchBonus.Bonus4 == 0 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Bonus4 = 45
			uiSwitchBonus.Presswish4 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "5.Bonus Ýki kat eþya düþme þansý")
		elif getIndex == 35 and uiSwitchBonus.Overwrite0 == 1 and uiSwitchBonus.Presswish0 == 1:
			uiSwitchBonus.Bonus0 = 45
			uiSwitchBonus.Presswish0 = 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 1.Bonus Ýki kat eþya düþme þansý")
		elif getIndex == 35 and uiSwitchBonus.Overwrite1 == 1 and uiSwitchBonus.Presswish1 == 1:
			uiSwitchBonus.Presswish1 = 0
			uiSwitchBonus.Bonus1 = 45
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 2.Bonus Ýki kat eþya düþme þansý")
		elif getIndex == 35 and uiSwitchBonus.Overwrite2 == 1 and uiSwitchBonus.Presswish2 == 1:
			uiSwitchBonus.Presswish2 = 0
			uiSwitchBonus.Bonus2 = 45
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 3.Bonus Ýki kat eþya düþme þansý")
		elif getIndex == 35 and uiSwitchBonus.Overwrite3 == 1 and uiSwitchBonus.Presswish3 == 1:
			uiSwitchBonus.Presswish3 = 0
			uiSwitchBonus.Bonus3 = 45
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 4.Bonus Ýki kat eþya düþme þansý")
		elif getIndex == 35 and uiSwitchBonus.Overwrite4 == 1 and uiSwitchBonus.Presswish4 == 1:
			uiSwitchBonus.Presswish4 = 0
			uiSwitchBonus.Bonus4 = 45
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yeni 5.Bonus Ýki kat eþya düþme þansý")
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Hiçbir bonus seçili deðil.")		
		self.Hide()
	
	def OnCloseInputDialog(self):
		self.inputDialog.Close()
		self.inputDialog = None
		return True

	def OnCloseQuestionDialog(self):
		self.questionDialog.Close()
		self.questionDialog = None
		return True

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()
