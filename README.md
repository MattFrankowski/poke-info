# PokeInfo
Website that allows to search for any Pokémon and see its detailed information.

Pokémon data is fetched from PokéAPI.


|                     Index Page                     |                    Pokemon Page                    |
| -------------------------------------------------- | -------------------------------------------------- |
|        <img src="screenshots/index_page.png">      |        <img src="screenshots/pokemon_page.png">      |

## Technology Stack
* Django
* REST API
* HTML/CSS
* JavaScript
* Bootstrap 4

## Setup
To run this project locally clone this repository:
```
$ git clone https://github.com/MattFrankowski/poke-info.git
```

Install and activate Virtual Enviroment:
```
$ pip install virtualenv
$ python -m virtualenv env
$ env\Scripts\activate 
```

Install the dependencies:
```
$ pip install -r requirements.txt
```

Next, navigate to poke-info/myproject directory and type in command line:
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
Open browser and go to adress http://127.0.0.1:8000/
