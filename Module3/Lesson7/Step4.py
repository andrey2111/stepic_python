from xml.etree import ElementTree


def getChildren(root, level):
    for child in root:
        colors[child.attrib['color']] += level
        getChildren(child, level+1)

colors = {'red': 0, 'green': 0, 'blue': 0}
tree = ElementTree.fromstring(input())

colors[tree.attrib['color']] += 1
getChildren(tree, 2)

print(colors['red'], colors['green'], colors['blue'])
