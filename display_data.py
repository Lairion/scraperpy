import os,sqlite3
import settings
name = input('Input name your db:')
conn = sqlite3.connect(os.path.join(settings.PROJECT_DIR,name+".sqlite3"))
cursor = conn.cursor()
for row_comb in cursor.execute("""SELECT id,comb from combinations""").fetchall():
	print(row_comb[1])
	for row_hint in cursor.execute("""SELECT item from hints WHERE combination_id=:comb_id""",{"comb_id":row_comb[0]}).fetchall():
		print("    ",row_hint[0])

conn.close()