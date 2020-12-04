import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# c.execute('''CREATE TABLE geo (ip text, location text, symbol text)''')
# c.execute("INSERT INTO geo VALUES ('0.0.0.2','Poland','PL')")
# c.execute("INSERT INTO geo VALUES ('0.0.0.3','Poland','PL')")
#
ip = ('0.0.0.5',)

c.execute('SELECT * FROM geo WHERE ip=?', ip)
args = {
    "ip": "0.0.0.2",
    "location": "Germany",
    "symbol": "GER"
}
updateData = (args['location'], args['symbol'], args['ip'])
if c.fetchall():
    print('someting')
else:
    print('nothing')


c.execute('SELECT * FROM geo')
print(c.fetchall())
conn.commit()
conn.close()