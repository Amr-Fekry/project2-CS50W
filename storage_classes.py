
class Storage():
	def __init__(self):
		self.channels = {}
		self.users = []


class Channel():
	def __init__(self, name):
		self.name = name
		self.messages = []

	def print_data(self):
		"""print data stored in a channel for testing porpuses"""
					
		print(f"------- channel: {self.name}")
		for msg in self.messages:
			print(f"avatar {msg.avatar_number}, {msg.username}:")
			print(msg.text)

	def keep_100_messages(self):
		"""make sure channel is saving up to 100 messages maximum"""
		if len(self.messages) > 100:
			del self.messages[0]


class Message():
	def __init__(self, avatar_number, username, time, text):
		self.avatar_number = avatar_number
		self.username = username
		self.time = time
		self.text = text


class User():
	def __init__(self, name, status):
		self.name = name
		self.status = status

