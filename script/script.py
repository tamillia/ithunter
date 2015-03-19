import sys
import datetime
import os

arguments = sys.argv
current_time = datetime.datetime.now()
name_of_file = arguments[1]
date = "%04d-%02d-%02d" %  (current_time.year, current_time.month, current_time.day)
time = "%02d:%02d:%02d" % (current_time.hour, current_time.minute, current_time.second)
name_of_file =  date  + '-' + name_of_file + '.md'

isname = False
istags = False
iscat = False
name = ''
tags = ''
cat = ''

for i in range(1, len(arguments)):

    if isname and arguments[i][0] != '-':
        name = name + arguments[i] + " "
    if istags and arguments[i][0] != '-':
         tags = tags + arguments[i] + ', '
    if iscat and arguments[i][0] != '-':
        cat = cat + arguments[i]

    if arguments[i] == '-name' or arguments[i] == '-title':
        isname = True
        istags = False
        iscat = False

    if arguments[i] == '-tags':
        istags = True
        isname = False
        iscat = False

    if arguments[i] == '-cat' or arguments[i] == '-category':
        istags = False
        isname = False
        iscat = True

tags = tags[0:len(tags) - 2]
name = name[0:len(name) - 1]

os.chdir('/Users/artemdremov/Documents/theasder.github.io/_posts')
file = open(name_of_file, 'w')


content = '---\nlayout: post\ntitle: "'
content = content + name + '"\ndate: '
content = content + date + ' ' + time + '\n'
content = content + 'category: ' + cat + '\n'
content = content + 'tags: ' + '[' + tags + ']\n'
content = content + 'published: false\n---\n<img src="https://theasder.github.io/img/" class="img-responsive" /><br />\n\n'

file.write(content)
file.close()

if not os.fork():
    os.execlp('open', 'open', '-a', '/Applications/MacDown.app', name_of_file)



