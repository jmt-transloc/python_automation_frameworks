## Python Automation Exploration
A repository containing multiple Python testing frameworks used for automation research.

### Installing Pipenv
This repository specifically uses Pipenv as a dependency and virtual environment manager. To utilize pipenv, install
the package using pip. Prior to installing Pipenv you must have Python 3.6+ installed. Once installed, 
run `pip3 install pipenv` to install the package.

### Establishing a Virtual Environment
* Navigate into a specific test runner directory
    * Pytest
    * Pytest-BDD
    * Behave
    * Robot
    
Pipenv depends on your Python installation. Link the Python install to Pipenv by running the following:

`pipenv --python {path_to_python}`

Now that Pipenv is linked to your Python installation, you may notice that a virtual environment was
created. You can confirm this by ensuring that your terminal displays the following:

```
Successfully created virtual environment!
Virtualenv location: /Users/{user_name}/.local/share/virtualenvs/{directory_name}-{ID}
```

You must now source the virtual environment to begin using it. To source the environment,
enter the following:

`source {pipenv_virtual_environment_location}/bin/activate`

You can confirm that your virtual environment is now active by viewing your terminal and ensuring that 
the name of the directory selected above is shown to the left of your input. 

_NOTE: You may re-enter the previous source command to activate a virtual environment which you have 
previously deactivated in order to use it once again._

### Using Pipenv to Install Dependencies
_NOTE: To avoid dependency issues, make sure to activate a (or the correct) virtual environment 
prior to installing dependencies._
* run `pipenv install --dev` to install dependencies

### Switching Test Runners
In order to not pollute your virtual environment with additional dependencies, make sure to run `dectivate`
prior to using a new test runner within the automation framework examples. 

Eg. You are currently experimenting with the Pytest-BDD framework and currently have a 'pytest-bdd' virtual
environment established. Prior to navigating to the Behave framework, make sure to send `deactivate` in order
to exit the virtual environment.

#### Running Pytest or Pytest-BDD
* From the directory root (pytest or pytest-bdd) in command line, enter `pytest`

#### Running Behave
* From the directory root (behave) in command line, enter `behave`

#### Running Robot
* From the directory root (robot) in command line, enter `robot google.robot`

### Removing Virtual Environments
To remove a virtual environment, simply call the following in your terminal:

`rm -f {pipenv_virtual_environment_location}`