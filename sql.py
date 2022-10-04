import os
import xlwings as xw
import pythoncom

def add(name,function):#增
    path_py = os.path.abspath(__file__)#获取文件路径
    path = os.path.join(path_py,'..\Pokemon\\'+ function +'\\' + name)
    #path = path_py + "..\Pokemon\login"
    if os.path.isfile(path):
        print('文件已存在')
    else:
        with open(path,'w') as f:
            print("已新建",name)

    
def delete(name,function):#删
    path_py = os.path.abspath(__file__)#获取文件路径
    path = os.path.join(path_py,'..\Pokemon\\'+ function +'\\' + name)
    if os.path.isfile(path):
        os.remove(path)
        print(name,'文件已删除')
    else:
        print('未发现文件')

def check_pokemon_excel(function,location):
    pythoncom.CoInitialize()
    path_py = os.path.abspath(__file__)#获取文件路径
    app=xw.App(visible=False,add_book=False)
    app.display_alerts=False
    app.screen_updating=False
    fpath = os.path.join(path_py,'..\Pokemon\\'+ function+'\\' + 'pokemon.xlsx')
    wb = app.books.open(fpath)
    data_a = wb.sheets('sheet1').range(location).value
    print(data_a)
    return data_a



    

