import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="123456"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE dormitory_management")
mycursor.execute("USE dormitory_management")
mycursor.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), gender VARCHAR(10), student_id VARCHAR(20))")
mycursor.execute("CREATE TABLE dorms (id INT AUTO_INCREMENT PRIMARY KEY, building VARCHAR(10), room_number VARCHAR(5))")
mycursor.execute("CREATE TABLE roommates (id INT AUTO_INCREMENT PRIMARY KEY, student_id VARCHAR(20), roommate_id VARCHAR(20))")
mycursor.execute("CREATE TABLE visitors (id INT AUTO_INCREMENT PRIMARY KEY, student_id VARCHAR(20), visitor_name VARCHAR(255), visit_date DATE)")
# 添加学生信息
name = input("请输入姓名：")
gender = input("请输入性别：")
student_id = input("请输入学号：")
sql = "INSERT INTO students (name, gender, student_id) VALUES (%s, %s, %s)"
val = (name, gender, student_id)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# 查询学生信息
mycursor.execute("SELECT * FROM students")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# 添加宿舍信息
building = input("请输入宿舍楼号：")
room_number = input("请输入房间号：")
sql = "INSERT INTO dorms (building, room_number) VALUES (%s, %s)"
val = (building, room_number)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# 查询宿舍信息
mycursor.execute("SELECT * FROM dorms")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# 添加同寝信息
student_id = input("请输入学生学号：")
roommate_id = input("请输入同寝室友学号：")
sql = "INSERT INTO roommates (student_id, roommate_id) VALUES (%s, %s)"
val = (student_id, roommate_id)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# 查询同寝信息
mycursor.execute("SELECT * FROM roommates")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# 添加访客信息
student_id = input("请输入学生学号：")
visitor_name = input("请输入访客姓名：")
visit_date = input("请输入来访日期（格式为 YYYY-MM-DD）：")
sql = "INSERT INTO visitors (student_id, visitor_name, visit_date) VALUES (%s, %s, %s)"
val = (student_id, visitor_name, visit_date)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

# 查询访客信息
mycursor.execute("SELECT * FROM visitors")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# 删除学生信息
student_id = input("请输入要删除的学生学号：")
sql = "DELETE FROM students WHERE student_id = %s"
val = (student_id,)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted.")