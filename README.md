# "Behave" para entender al usuario

El desarrollo guiado por comportamiento (BDD por sus siglas en inglés) es una técnica ágil de desarrollo de software que fomenta la colaboración entre los desarrolladores, QA y los participantes no técnicos o empresariales en un proyecto de software.

Este es un ejemplo de una implementación de BDD por medio de [Behave](https://behave.readthedocs.io/en/latest/); una herramienta en [Python](https://www.python.org/) que permite escribir pruebas en lenguaje natural utilizando el lenguaje [Gherkin](https://cucumber.io/docs/gherkin/).

## Comenzando 🚀

_Instrucciones para obtener una copia del proyecto en funcionamiento en una máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

_Cosas necesarias para instalar el software y como instalarlas_

```
Python versión 3.x
ChromeDriver - WebDriver for Chrome versión latest
```

### Instalación 🔧

_Crear ambiente virtual_

```
python -m venv env
```

_Activar el ambiente virtual_

```
cd env/Scripts && activate.bat
```

_Instalar requerimientos_

```
pip install -r requirements.txt
```

_Ajustar la variable CHROME_DRIVER en environment.py_

```
CHROME_DRIVER = '/PATH_TO_CHROME_DRIVER'
```

### Ejecución 🏃

_En la raiz del proyecto ejecutar los test_

```
behave
```

_Si hay problemas con el driver de Chrome, descomentarear en environment.py_

```
# chrome_options.add_argument("--no-sandbox")
```

## Construido con 🛠️

_Herramientas_

* [Python](www.python.org) - Lenguaje de programación interpretado
* [Behave](https://behave.readthedocs.io/en/latest/) - behaviour-driven development
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Framework para aplicaciónes móviles web
* [SQLAlchemy](www.sqlalchemy.org) - Kit de herramientas SQL

## Autor ✒️

* María Camila Guerrero Giraldo - [mcguegi](https://github.com/mcguegi/)
