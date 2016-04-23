namespaces = {} #словарь <namespace>: <parent>
variables = {} #слоаврь <namespace>: [<variables>]


def get(namespace, var):
    if variables.get(namespace) is not None and var in variables.get(namespace):
        return namespace #если переменная в пространстве, возвращает его имя
    else:
        if namespaces.get(namespace) is None:
            return None #если предок пространства None, возвращаем None
        else:
            return get(namespaces[namespace], var) #ищем переменную в предке пространства (рекурсия)

n = int(input())
for i in range(n):
    query = input().split()
    if query[0] == 'create':
        namespaces[query[1]] = query[2]
    if query[0] == 'add':
        if variables.get(query[1]):
            variables[query[1]].append(query[2]) #добавляем переменную в список переменных пространства
        else:
            variables[query[1]] = [query[2]] #создаём новый список с переменными для простарнства
    if query[0] == 'get':
        print(get(query[1], query[2]))
