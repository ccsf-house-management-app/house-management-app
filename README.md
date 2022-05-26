# house-management-app

This repo contains the Django Back-End application for the "House Management App".

## Requirements

 - Python 3
    - `3.8.13` or higher
    - https://www.python.org/downloads/
 - MySQL Installation for use with the `mysqlclient` python package
   - On Mac and Linux, use a package manager such as homebrew to install MySQL:
     - `brew install mysql`
   - Otherwise, check https://pypi.org/project/mysqlclient/ for recomemndations on connecting a locally installed version of MySQL on Windows.
  - A virtual environment that uses pip to install packages only in this environment
      - Virtualenv: https://virtualenv.pypa.io/en/latest/
      - venv: https://docs.python.org/3/tutorial/venv.html
      - virtualenvwrapper: https://pypi.org/project/virtualenvwrapper/
      - conda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html
          - NOTE: The env's pip must be used, not the global pip that anaconda aliases.  eg. `which pip` will not point to the env's pip.
          - To work around this, either link pip to the full path to the envs pip or create an env specific alias for the full path:
              -  https://stackoverflow.com/questions/41060382/using-pip-to-install-packages-to-anaconda-environment
              -  https://tomroth.com.au/pip-conda/

## Instructions to start the local Back-End development server
After git cloning this repository you will need to install the dependencies using pip.

 - In a terminal, cd into the repo directory `house-management-app` containing the `requirements.txt` file.
 - Run `pip install -r requirements.txt` and wait for the installation to complete.

After pip finishes installing the dependencies, move into the `house_app` folder to run the django server.
- cd into `house_app`
- run `./manage.py runserver`

## Using the App with local development server

In the browser go to 
- `http://127.0.0.1:8000/` to interact with the app's backend as a user.
- `http://127.0.0.1:8000/api/` to explore the app's REST endpoints.
- `http://127.0.0.1:8000/admin/`to update records using django's built-in admin pages (using credentials provided by the app maintainers).

Or proceed to use the Front-End Repo for a limited demonstration of the app's CRUD operations: https://github.com/ccsf-house-management-app/house-management-app-frontend


