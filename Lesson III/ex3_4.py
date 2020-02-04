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
#from lxml import etree
import xml.etree.ElementTree as ET

a = '<root><element1 /><element2 /><element3><element4 /></element3></root>'

tree = ET.fromstring(a)

print("'name': '", tree.tag,"'," )
print("'children': [") 

for elem in tree:
    t = 1
    #print(tree.tag)
    print("\t", elem.tag, elem.attrib)
    for subelem in elem:
        t+=1
        print("\t"*t, subelem.tag, subelem.attrib)