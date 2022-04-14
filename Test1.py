import xml.etree.ElementTree as et
class People:
    def __init__(self, ID, name , age):
         self.__id = ID
         self.__name = name
         self.__age = age

    def __str__(self):
         return f'People[id=(self.__id), name=(self.__name), age=(self.__age)]'
    property
    def ID(self):
        return self.__id
    property
    def name(self):
        return self.__name
    property
    def age(self):
        return self.__age


    def parse_xml(XMLFile1):
        xml_tree = et.parse(XMLFile1)
        root = xml_tree.getroot()
        list = []
        for item in root:
            ID = item[0].text
            name = item[1].text
            age = item[2].text
            list.append(People(ID,name , age))
        return list

    def show_list(list):
        for item in list:
            print(item)


    if __name__ =='__main__':
        file = 'XMLFile1.xml'
        XMLFile1_list = parse_xml(file)
        print('===============================')
        print("Danh sách người:")
        show_list(XMLFile1_list)

