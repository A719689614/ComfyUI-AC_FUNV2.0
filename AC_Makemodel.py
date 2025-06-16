import os
from .AC_CATAGORY import AC_CATEGORY
# 获取当前脚本所在的目录路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 给定的绝对路径
absolute_path = ("AC_MODEL")

# 获取相对路径
relative_path = os.path.join(script_dir, absolute_path)
# print('==========')
print(relative_path)

# 读取模式
read_list = []
def Readlist():
    for file in os.listdir(relative_path):
        if file.endswith(".txt"):
            read_list.append(file)
            return read_list

# path = os.path.join(relative_path,Readlist()[0])
# print(path)

list = ['添加','写入']
class Makemodel(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":{
            "Mode":(list,),
            "Title":("STRING",{"multiline":False,}),   
            "Main":("STRING",{"multiline":True,}),   
                }}
    
    RETURN_TYPES =("STRING",)
    RETURN_NAMES =("tips",)
    FUNCTION ="makemodel"

    def makemodel(self,Mode,Title,Main):
        if Mode == "添加":
            end = (".txt")
            path = os.path.join(relative_path,Title)
            newpath = f"{path}"+ f"{end}"
            f = open(newpath, 'a', encoding='utf-8')
            f.write(Main)
            f.close()
            result = "添加成功"
            return (result,)
        if Mode == "写入":
            end = (".txt")
            path = os.path.join(relative_path,Title)
            newpath = f"{path}"+ f"{end}"
            f = open(path, 'w', encoding='utf-8')
            f.write(Main)
            f.close()
            result = "写入并覆盖原有内容成功"
            return (result,)

class Readmodel(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":{
            "Mode_List":(Readlist(),),
                }}
    RETURN_TYPES =("STRING",)
    RETURN_NAMES =("STRING",)
    FUNCTION ="readmodel"

    def readmodel(self,Mode_List):
        path = os.path.join(relative_path,Mode_List)
        f = open(path, 'r', encoding='utf-8')
        result = f.read()
        f.close()
        return(result,)

NODE_CLASS_MAPPINGS = {

}    
    

