from os import sep
import txtopp as tp


namelistpath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Person ID App/files/data/namelist.txt'
agepath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Person ID App/files/data/age.txt'
emailpath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Person ID App/files/data/email.txt'
phonepath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Person ID App/files/data/phone.txt'
addresspath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Person ID App/files/data/address.txt'
occupationpath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Person ID App/files/data/occupation.txt'
relationpath = 'C:/Users/mani/Desktop/Desktop/All Files/All Coding/Github/Person ID App/files/data/relation.txt'


namelist = tp.read_list(file=namelistpath, separator='\n')
agelist = tp.read_list(file=agepath, separator='\n')
phonelist = tp.read_list(file=phonepath, separator='\n')
emaillist = tp.read_list(file=emailpath, separator='\n')
addresslist = tp.read_list(file=addresspath, separator='\n')
relationlist = tp.read_list(file=relationpath, separator='\n')
occupationlist = tp.read_list(file=occupationpath, separator='\n')

basiclist = [
    'Name:          ',
    'Age:           ',
    'Relation:      ',
    'Phone:         ',
    'Email:         ',
    'Address:       ',
    'Occupation:    '
    ]

def updatelb():
    namelist = tp.read_list(file=namelistpath, separator='\n')
    
    return namelist

def delete(name):
    n = namelist.index(name)
    print(tp.delete_object(file=agepath, separator='\n', object=agelist[n]))
    print(tp.delete_object(file=relationpath, separator='\n', object=relationlist[n]))
    print(tp.delete_object(file=emailpath, separator='\n', object=emaillist[n]))
    print(tp.delete_object(file=namelistpath, separator='\n', object=namelist[n]))
    print(tp.delete_object(file=phonepath, separator='\n', object=phonelist[n]))
    print(tp.delete_object(file=addresspath, separator='\n', object=addresslist[n]))
    print(tp.delete_object(file=occupationpath, separator='\n', object=occupationlist[n]))
    

def delall():
    tp.delete_list(file=namelistpath, separator='\n', list=namelist)
    tp.delete_list(file=agepath, separator='\n', list=agelist)
    tp.delete_list(file=relationpath, separator='\n', list=relationlist)
    tp.delete_list(file=phonepath, separator='\n', list=phonelist)
    tp.delete_list(file=emailpath, separator='\n', list=emaillist)
    tp.delete_list(file=addresspath, separator='\n', list=addresslist)
    tp.delete_list(file=occupationpath, separator='\n', list=occupationlist)


def download(data, file):
    info = []
    for i in range(len(data)):
        info.append(basiclist[i]+data[i])
    print(info)

    
    tp.add_list(file=file, separator='\n', list=info)


def add(infolist):
    tp.add_object(file=namelistpath, separator='\n', object=infolist[0])
    tp.add_object(file=agepath, separator='\n', object=infolist[1])
    tp.add_object(file=relationpath, separator='\n', object=infolist[2])
    tp.add_object(file=phonepath, separator='\n', object=infolist[3])
    tp.add_object(file=emailpath, separator='\n', object=infolist[4])
    tp.add_object(file=addresspath, separator='\n', object=infolist[5])
    tp.add_object(file=occupationpath, separator='\n', object=infolist[6])

def viewinfo(name):
    namelist = tp.read_list(file=namelistpath, separator='\n')
    n = namelist.index(name)
    info = []
    
    info.append(name)
    info.append(tp.read_list(file=agepath, separator='\n')[n])
    info.append(tp.read_list(file=relationpath, separator='\n')[n])
    info.append(tp.read_list(file=emailpath, separator='\n')[n])
    info.append(tp.read_list(file=phonepath, separator='\n')[n])
    info.append(tp.read_list(file=addresspath, separator='\n')[n])
    info.append(tp.read_list(file=occupationpath, separator='\n')[n])
    
    print(info)
    return info
    

    
