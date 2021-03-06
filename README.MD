# API BASE

This API y developed with Flask and Flask-RestFul. It work for initial projects, only have one model User with basic field
-name
-lastname
-birthday
-direction

## Instalation

```bash
pip install requirements.txt
```

## Set enviroment for run project

#### Method 1: Set manual enviroment (This way we have to set everytime we wish to run project)

In base folder open a terminal a set:

```bash
export FLASK_APP="entrypoint:app"
export FLASK_ENV="development"
```

#### Method 2: (Recommended - Only one configuration)

Open in editor the activate file contained in env/bin and write at bottom and save

```bash
export FLASK_APP="entrypoint:app"
export FLASK_ENV="development"
```

## Running project

```bash
Flask run
```

## Migrate database

##### Step 1: Set database SQLALCHEMY_DATABASE_URI variable

###### for Mysql: SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://youruser:@localhost:3306/yourdatabase'

###### for SQLite: SQLALCHEMY_DATABASE_URI = 'sqlite:///yourdatabase.sqlite'

## Running migration

In terminal run

```bash
$ flask db init
$ flask db migrate -m "Initial_db"
$ flask db upgrade
```

## Update database with new models

```bash
$ flask db migrate -m "Message with new model"
$ flask db upgrade
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
