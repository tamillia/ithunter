import sys
import datetime
import os

arguments = sys.argv
current_time = datetime.datetime.now(datetime.timezone.utc)
name_of_file = arguments[1]
date = str(current_time.year) + '-' + str(current_time.month) + '-' + str(current_time.day)
time = str(current_time.hour) + ':' + str(current_time.minute) + ':' + str(current_time.second)
name_of_file =  date  + '-' + name_of_file + '.md'

isname = False
istags = False
iscat = False
name = ''
tags = ''
cat = ''

for i in range(1, len(arguments)):

    if isname:
        name = name + arguments[i]
    if istags:
        tags = tags + arguments[i] + ', '
    if iscat:
        cat = cat + arguments[i]

    if arguments[i] == '-name':
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

os.chdir('/Documents/theasder.github.io/_posts')
file = open(name_of_file, 'w')

content = '---\nlayout: post\ntitle: "'
content = content + name + '"\ndate: '
content = content + date + ' ' + time + '\n'
content = content + 'category: ' + cat + '\n'
content = content + '['+ tags + ']\n'


