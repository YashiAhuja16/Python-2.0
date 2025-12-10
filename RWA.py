# READ FILE 
with open ("file1.txt" , "r") as discord : 
  content = discord.read()
  print (content) 
# WRITE File
with open ("file2.txt", "w") as x :
  x.write ("C is a Programming Language.") # it replaces content
  
# APPEND File
with open ("file2.txt", "a") as x :
  x.write ("Life is beautiful.") # it appends (adds after)


