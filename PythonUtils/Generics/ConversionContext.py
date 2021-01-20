from core.Singleton import Singleton



class ConversionContext(Singleton):
	def __init__(self)
		self.classPaths=[]
		self.applyPlugins=[]
		self.subprojects={}
		self.excludeDependencies=[]
		self.dependencies={}
		self.reverse_map_data={} #Stores reverseMap data like properties, dependencies of parent and root
		self.parent_pom_data={} #Stores parent pom plugins from pluginManagement section

	def clear_Context(self):
		"""This function invoked during M2GConverter clear_gradle_environment to clear context Variables"""
		self.classPaths=[]
		self.applyPlugins=[]
		self.subprojects={}
		self.excludeDependencies=[]
		self.dependencies={}
		self.reverse_map_data={} 
		self.parent_pom_data={}