wincompile:
	pyinstaller --hidden-import git --hidden-import remover --hidden-import list --hidden-import reader --onefile src/dcpd.py --icon src/logo.ico
	pyinstaller --hidden-import git --hidden-import List --onefile configuration.py --icon src/logo.ico

linuxcompile:
	pyinstaller --hidden-import git --hidden-import toml --hidden-import remover --hidden-import list --hidden-import reader --onefile src/dcpd.py --icon src/logo.ico 
	pyinstaller --hidden-import git --hidden-import List --hidden-import toml --onefile configuration.py --icon src/logo.ico
