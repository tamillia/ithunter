from urllib.request import urlopen
import ast
from operator import itemgetter
#
def get_posts():
    url = "https://api.vk.com/method/wall.get?owner_id=-54530371&count=100&filter=owner"
    response = urlopen(url)
    text = response.read()
    return ast.literal_eval(str(text, 'utf-8'))

posts = get_posts()['response']

b = [1, 15, 1, 2, 13, 23, 6, 3, 4, 13, 6, 5, 9, 6, 1, 1, 1, 1, 13, 1, 3, 4, 10, 6, 1, 6, 1, 1, 6, 2, 3, 4, 2, 2, 5, 13, 7, 6, 1, 17, 15, 1, 9, 1, 14, 21, 1, 1, 7, 1, 14, 6, 1, 1, 2, 8, 5]
b.reverse()
#print(b)
posts.remove(posts[0])
l = 0
post_ordered = []
for item in posts:
    example = {}
    example['likes'] = item['likes']['count']
    example['reposts'] = item['reposts']['count']
    example['text'] = item['text']
    example['link'] = 'http://vk.com/wall-54530371_%d' %  item['id']
    post_ordered.append(example)
    print('likes:', example['likes'])
    print('reposts:', example['reposts'])
    print('text:', example['text'])
    print('def: ', b[l])
    l = l + 1
    print('link:', example['link'], '\n')

ids = []
for item in posts:
    ids.append(item['id'])
ids.reverse()
#for i in range(len(ids) - 1):
#    ids[i] = ids[i + 1] - id[i]

#ids.remove(ids[len(ids) - 1])

#print(ids)
#b = [1, 15, 1, 2, 13, 23, 6, 3, 4, 13, 6, 5, 9, 6, 1, 1, 1, 1, 13, 1, 3, 4, 10, 6, 1, 6, 1, 1, 6, 2, 3, 4, 2, 2, 5, 13, 7, 6, 1, 17, 15, 1, 9, 1, 14, 21, 1, 1, 7, 1, 14, 6, 1, 1, 2, 8, 5, 1, 3, 5, 5, 5, 1, 1, 2, 14, 5, 5, 4, 10, 13, 1, 2, 7, 16, 1, 16, 7, 8, 6, 4, 4, 2, 8, 1, 10, 16, 2, 14, 23, 1, 7, 2, 7, 1, 11, 1, 13, 2]
#print(b)
#print(post_ordered)    
#print(posts[1])
#for item in posts:
#    print(item)

