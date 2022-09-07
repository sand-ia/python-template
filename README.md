![alt text](https://img.shields.io/badge/python-3.9-blue)
![alt text](https://img.shields.io/github/issues/sand-ia/fantastic-broccoli)
![alt text](https://img.shields.io/github/forks/sand-ia/fantastic-broccoli)
![alt text](https://img.shields.io/github/stars/sand-ia/fantastic-broccoli)
![alt text](https://img.shields.io/github/license/sand-ia/fantastic-broccoli)

# Fantastic Broccoli

**Fantastic Broccoli** is a simple python backend template.

## Template Usage

1. Click on **Use this template** button:

   ![alt text](../media/readme/use-this-template.png?raw=true)

2. Choose a repository name:

   ![alt text](../media/readme/choose-repository-name.png?raw=true)

## Run Template

The following steps explain how to run this template. If you follow the steps under [Template Usage](#template-usage), dont forget to change the repository name (fantastic-broccoli) and owner (sandia) with the corresponding values.

1. Clone the repository:

```sh
git clone https://github.com/sand-ia/fantastic-broccoli.git
```

2. Move into the project folder:

```sh
cd fantastic-broccoli
```

3. Create a virtual enviroment with Python 3.9:

```sh
virtualenv .venv
```

4. Activate the environment:

```sh
source .venv/bin/activate
```

5. Install the requirements:

```sh
pip install -r requirements.txt
```

6. Create a .env file to setup the environment variables:

```sh
vim .env
```

7. Setup the required enviroment variables into the .env file:

```
# Name of the module to import at start
FLASK_APP=src

# Context in which flask will run
FLASK_ENV=development
```

8. Start flask server:

```
flask run
```

## License & copyright

Copyright Sandia, 2022.

Distributed under the terms of the [MIT License](LICENSE), Fantastic Broccoli is free and open source software.
