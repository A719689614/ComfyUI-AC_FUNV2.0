import os
from .AC_CATAGORY import AC_CATEGORY

# 获取当前脚本所在的目录路径
script_dir = os.path.dirname(os.path.abspath(__file__))
# print(script_dir)
# print('================================================')
# 给定的绝对路径
absolute_path = ('Eighth-Season')

# 获取相对路径
file_path = os.path.join(script_dir,absolute_path)

# 使用相对路径来获取所有 txt 文件名
txt_files = []
for file in os.listdir(file_path):
    if file.endswith(".txt"):
        txt_files.append(file)

# print(txt_files)



class AC_FUN_Eighth(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            "ModeList":(txt_files,),
        }}
    # 返回结果类型
    RETURN_TYPES = ('STRING',)
    
    # 返回节点命名
    RETURN_NAMES = ('STRING',)
    FUNCTION = "promptlist_index" 

    def promptlist_index(self,ModeList):
        new_path = os.path.join(file_path,ModeList)
        f = open(new_path,'r',encoding='utf-8')
        result = f.read()
        f.close()
        # 打开txt文件 
        return (result,)     
    

    if __name__ == '__main__':
        pass