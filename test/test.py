# test.py

#from lib.test2 import popup
import test2

#popup()

class All(test2.Mixin): # Could inherit many more mixins
	def popup(self):	
		self.popup_mixin()

bot = All()

bot.popup_mixin()