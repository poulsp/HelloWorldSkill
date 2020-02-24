
from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler

class HelloWorldSkill(AliceSkill):
	def __init__(self):
		super().__init__()
		self._offline = False


	@IntentHandler('HelloWorldIntent')
	def helloWorldIntent(self, session: DialogSession):
		"""
			skills can log useful information.
			These will appear in the Web Interface and the logs file.
		"""
		#self.logInfo("This is an info level log message. - helloWorldIntent")
		self.endDialog(session.sessionId, self.randomTalk(text='helloWorld'))
