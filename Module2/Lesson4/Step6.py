import os.path

with open('output6.txt', 'w') as ouf:
    for current_dir, dirs, files in os.walk('main'):
        for i in files:
            if i.endswith('.py'):
                ouf.write(current_dir+'\n')
                break
