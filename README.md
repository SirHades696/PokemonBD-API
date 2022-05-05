# Welcome to Pokémon DB API
Pokémon API esta hecha para mostrar información referente a cada uno de los Pokémon existentes en la Base de Datos de `pokemondb.net`

La información mostrada por esta API es: 
<ul>
    <li>Nombre</li>
    <li>Tipo</li>
    <li>Total</li>
    <li>Puntos de vida</li>
    <li>Ataque</li>
    <li>Defensa</li>
    <li>Ataque especial</li>
    <li>Defensa especial</li>
    <li>Velocidad</li>
</ul>

La información extraída de la página web es a través de Pandas, además se utiliza un poco de web scraping para anexar la imagen de cada Pokémon al registro correspondiente.

# ¿Qué Packages son necesarios?
Todos los recursos usados para el desarrollo se encuentran en: `requirements.txt`

> `pip install -r requirements.txt`

# Preperación del Entorno
Antes de comenzar a realizar las peticiones GET es necesario preparar el entorno, para ello se necesita haber instalado previamente todos los packages contenidos en  `requirements.txt`

Una vez instalados los requisitos es necesario ejecutar los siguientes comandos en orden:

> `flask db init`:  para inicialar la base de datos.

> `flask db migrate`: para crear la base de datos a partir de una plantilla base.

> `flask db upgrade`: para crear la tabla contenida en nuestro esquema `db.py` (contiene la tabla para almancenar los Pokémon y los campos necesarios para almacenar la información de cada registro)

> `flask load-data`: para cargar la base de datos con la información extraída de `pokemonsdb.net`

> `flask run`: para ejecutar el servidor y comenzar a realizar las peticiones GET

# Screenshots
<img src="doc\img\1.png">

<img src="doc\img\2.png">

<img src="doc\img\3.png">

<img src="doc\img\4.png">

<img src="doc\img\5.png">

# Recursos
Flask: https://flask.palletsprojects.com/en/2.0.x/

FLask-Alchemy: https://flask-sqlalchemy.palletsprojects.com/en/2.x/

Flask-Restful: https://flask-restful.readthedocs.io/en/latest/

Flask-Migrate: https://flask-migrate.readthedocs.io/en/latest/

Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Click: https://click.palletsprojects.com/en/8.0.x/
