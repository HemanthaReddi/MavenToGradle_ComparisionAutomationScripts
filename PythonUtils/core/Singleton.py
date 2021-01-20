import threading

class Singleton(object):

	__singleton_lock=threading.Lock()
	__singleton_instance=None

	@classmethod
	def instance(cls):

		#check for the singleton instance
		if not cls.__singleton_instance:
			with cls.__singleton_lock:
				if not cls.__singleton_instance:
					cls.__singleton_instance=cls()


		#return the singleton instance
		return cls.__singleton_instance