import os
from .AC_CATAGORY import AC_CATEGORY

# 获取当前脚本所在的目录路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 给定的绝对路径
# catelogue = ('ComfyUI-By-AC_FUNV2.0')
absolute_path = ('Design_Aera')
specialty = ['Architecture','InDoor_AC','Landscape','Factory']

# 获取相对路径
def get_file_path(x):
     return os.path.join(script_dir,absolute_path,specialty[x])

# 使用相对路径来获取所有 txt 文件名
list_1 = []
list_2 = []
list_3 = []
list_4 = []

for file in os.listdir(get_file_path(0)):
    if file.endswith(".txt"):
        list_1.append(file)

for file in os.listdir(get_file_path(1)):
    if file.endswith(".txt"):
        list_2.append(file)

for file in os.listdir(get_file_path(2)):
    if file.endswith(".txt"):
        list_3.append(file)

for file in os.listdir(get_file_path(3)):
    if file.endswith(".txt"):
        list_4.append(file)

class AC_FUN_Design(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
            "ARCHI":(list_1,),
            "IND":(list_2,),
            "LAD":(list_3,),
            "FAC":(list_4,),
            "Prompt": ("STRING", {
                    "multiline": True, 
                    "default": '请手动输入提示词'}),
         
        }}
    # 返回结果类型
    RETURN_TYPES = ('STRING','STRING','STRING','STRING','STRING')
    
    # 返回节点命名
    RETURN_NAMES = ('Architecture','InDoor','Landscape','Factory','Prompt')
    FUNCTION = "promptlist_index" 
 
    def promptlist_index(self,ARCHI,IND,LAD,FAC,Prompt):
        path_1 = os.path.join(get_file_path(0),ARCHI)
        f = open(path_1,'r',encoding='utf-8')
        result_1 = f.read()
        f.close()
        path_2 = os.path.join(get_file_path(1),IND)
        f = open(path_2,'r',encoding='utf-8')
        result_2 = f.read()
        f.close()
        path_3 = os.path.join(get_file_path(2),LAD)
        f = open(path_3,'r',encoding='utf-8')
        result_3 = f.read()
        f.close()
        path_4 = os.path.join(get_file_path(3),FAC)
        f = open(path_4,'r',encoding='utf-8')
        result_4 = f.read()
        f.close() 
        return (result_1, result_2, result_3, result_4, Prompt)     
    

if __name__ == '__main__':
        pass