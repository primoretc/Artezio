'''
4. На вход функции передается строка с xml документом (тэги без аттрибутов, корневой элемент 
только один). 
Нужно выполнить следующее преобразование и вывести максимальную вложенность.
Пример: 
    a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
    foo(a) -> 
    {
        'name': 'root', 
        'children': [
            {'name': 'element1', 'children': []},
            {'name': 'element2', 'children': []},
            {
                'name': 'element3', 
                'children': [
                    {'name': 'element4', 'children': []}
                ]
            }
        ]
    }, 2
    в данном случае у element4 тэга вложенность/глубина 2

    <element1 /> - тэг  пустого элемента
    <element3></element3> - тэги начала и конца элемента
'''


a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'
def treeXml(a):
    def tagList(x): 
        tag = ""
        lt=[]
        print(a)
        l=a.split("<")
        l.remove("")
        for i, value in enumerate(l):
            tag = "<" + value
            lt.append(tag)
        return lt
    tagList(a)

treeXml(a)