import timeit
import os

from core.M2GConverter import M2GConverter
from Generics.Logger import Logger
from Generics.Globals import Globals

if __name__=="__main__":
	start=timeit.default_timer()

	main_path = (input("enter source path:").replace('\\','/'))
	gradlew_path = (input("enter gradlew path-optional:").replace('\\','/'))
	if os.path.exists(main_path):
		if len(gradlew_path) !=0: Globals.GRADLEW_PATH= gradlew_path
		#mvn_settingsxml_path =  (input("enter maven settingsxml path:").replace('\\','/'))
		if not os.path.isabs(main_path):
			main_path=os.path.join(os.getcwd(),main_path).replace('\\','/')
		logger=Logger(main_path)
		Logger.log.info(Globals.EXECUTION_START)
		m2g= M2GConverter()

		## Maven clean install
		m2g.build_maven(main_path)

		## Generate Gradle script
		m2g.generate_gradle_build_script(main_path)

		## Gradle clean Build
		m2g.build_gradle(main_path)

		##artifacts compare
		sd_dict=m2g.source_destination_artifact_dict(main_path)
		m2g.compare_all_modules(sd_dict)


		#source_path=r""
		#destination_path=""
		#m2g.compare_folders(source_path,destination_path)

		#module_path=input("module path")
		#m2g.compare_one_module(sd_dict,module_path)
	else:
		raise ValueError("Invalid path:{}".format(main_path))

	Logger.log.info(Globals.EXECUTION_END)
	stop=timeit.default_timer()
	print("\nExecution Time: M2GConverter %.2f" %(stop-start))










