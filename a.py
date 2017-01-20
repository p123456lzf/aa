import os
import shutil
os.chdir("ceshi0")
for i in range(999):
    shutil.move("dir1/%s.txt" % i,"dir2/")
    os.chdir("../ceshi1")
for i in range(99):
open('%s.txt' % i,'w')
os.chdir("../ceshi2")
for i in range(99):
os.rename("dir/%s.txt" % i,"dir/a%s.txt" % i)
