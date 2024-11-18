# new_python_project

use this as a template for a python project


## Setup

### install python

- install python (e.g. some version of [python 3.12](https://www.python.org/downloads/) or higher)
	- e. g. select python 3.12.3
	- download links are at the bottom of the page after clicking on the python version link
- check if command `python3 --version` says version `3.12.3` or similar/higher
	- perhaps you need to open a new terminal window or reboot your computer

### clone and open git repo in vscode

- get this repo
	- fork this repo
	- or use template method to create this repo as new repo inside user github account
		- use dashes ( `-` for word seperation in git repo names (NOT underscore ( `_` )))
		- example for new name: `new-name-of-your-project-git-repo`
- clone repo (e. g. with [gh cli](https://cli.github.com/))
- cd into folder of repo
- run command `code .` (dot means current folder, so this command opens the current folder in vscode)

### rename python project

- in case you use the template method and created your own git repo with a different name you could/should rename the python project too
- use dashes ( `-` for word seperation in git repo names (NOT underscore ( `_` )))
- example for new name: `new-name-of-your-project-git-repo`
- python project package name
	- change in `pyproject.toml`:
		```toml
		# previously
		[tool.poetry]
		name = "new-python-project"

		# after change
		[tool.poetry]
		name = "new-name-of-your-project-git-repo"
		```
- rename the python module folder in the root of you git repo
  ```
	# previously
	new_python_project

	# after change
	new_name_of_your_project_git_repo
- fix poetry project lock file
  ```bash
	poetry lock --no-update

- rename the following parts in every python/jupyter notebook file:
  ```
	# previously
	from new_python_project
	import new_python_project

	# after change
	from new_name_of_your_project_git_repo
	import new_name_of_your_project_git_repo


### install vscode extensions

- go to extensions tab on the left
- type `@recommended`
- install the extensions (like git graph, gitlens, black formatter, python, jupyter)

### setup python venv and packages


#### setup poetry

> poetry is used for dependency management

- [install pipx](https://pipx.pypa.io/stable/installation/)
  ```bash
	# for macos
	brew install pipx
	pipx ensurepath
	```
- [install poetry](https://python-poetry.org/docs/#installation)
  ```bash
	# for macos
	pipx install poetry
	```
- configure poetry
	```bash
	# configure poetry to create/use .venv instead of its own venv system
	poetry config virtualenvs.in-project true
	# to check config (otionally)
	poetry config --list
	```


- [more info about python venv](https://docs.python.org/3/library/venv.html)
- create `.venv`
	- sometimes poetry install does not create venv for some reason
	- so we run the create venv command manually
	```bash
	# be sure to cd into git repo folder
	# create python venv
	python3 -m venv .venv
	
	# activate venv (will happen automatically later)
	source .venv/bin/activate
- install dependencies via poetry
	```bash
	poetry install --compile --sync
	```
- install git notebook filter
	- this filter avoids commiting jupyter notebook output to git
	- this makes sense to avoid big files in git
	```bash
	# be sure to cd into git repo folder
	# install git filter
	nbstripout --install

	# check filter afterwards (optionally)
	nbstripout --status
	```

- in the future you can update/install changed dependencies with this command again:
	```bash
	poetry install --compile --sync
	```


### Open python scripts or jupyter notebook

- now you can open python script or jupyter notebooks
- sometime the packages and code references are not detected at once
	- in that case run the notebook one time and reload the vscode window
		- `cmd + shift + p`
		- `>Reload Window`
- then everything *should work as expected*


## vscode setup

- add shortcuts for jupyter notebook too. [details here](/notes/custom-shortcuts.md)
- [change a few vscode settings](/notes/custom-settings.md)
