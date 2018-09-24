import pandas as pd 
import sqlite3 as sl 

#filename = 'Data'
#nut = pd.read_excel(filename+'.xls')
#conn = sl.connect(filename+'.db')
#nut.to_sql('Diet',conn,if_exists='replace',index=False)
#conn.commit()
#data = pd.read_sql(sql='SELECT * FROM Diet;',con=conn)
#print(data)
#conn.close()

class Data():
	def __init__(self):
		self.filename='Data'
		self.tablename='Ingredients'
		self.con_cur()
		self.read_xl()
		self.validate_db()
		self.close_con()

	def con_cur(self):
		self.conn=sl.connect(self.filename+'.db')
		print('Connected to '+self.filename+' database')
		self.cur=self.conn.cursor()
		print('Cursor object created...')

	def read_xl(self):
		try:
			self.ingredients=pd.read_excel(self.filename+'.xls')
		except FileNotFoundError as e:
			print('An error occured:\n', e)
		else:
			print('Excel file read...')

	def validate_db(self):
		try:
			self.ingredients.to_sql(self.tablename,self.conn,index=False,if_exists='replace')
		except ValueError as e:
			print('An error occured:\n', e)
		else:
			print('Data was inserted into '+self.filename+'.db/'+self.tablename)

	def close_con(self):
		self.conn.close()
		print('Connection to '+self.filename+' database closed')

if __name__ == '__main__':
	data = Data()