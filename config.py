from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'my_secret_password'
app.config['MYSQL_DATABASE_DB'] = 'bax01'
app.config['MYSQL_DATABASE_HOST'] = '34.143.212.43'
mysql.init_app(app)