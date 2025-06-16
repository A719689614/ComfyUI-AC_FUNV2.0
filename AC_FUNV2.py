import os
from torch import Tensor
from .AC_CATAGORY import AC_CATEGORY
# 定义全局变量
Maxresolution = 99999999999999999

script_dir = os.path.dirname(os.path.abspath(__file__))
absolute_path = ('First-Season')

# 获取相对路径
file_path = os.path.join(script_dir,absolute_path)

txt_files = []
for file in os.listdir(file_path):
    if file.endswith(".txt"):
        txt_files.append(file)


# 读取模板
class Promptlist_index(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            "ModeList":(txt_files,),
        }}
    # 返回结果类型
    RETURN_TYPES = ('STRING',)
    
    # 返回节点命名
    RETURN_NAMES = ('INDEX',)
    FUNCTION = "promptlist_index" 


    def promptlist_index(self,ModeList):
        # 打开txt文件
        return (ModeList,)        

# =============================================================
class Promptlist_read(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            "INDEX":("STRING",{"forceInput": True})
        }}
    # 返回结果类型
    RETURN_TYPES = ("STRING",)
    
    # 返回节点命名
    # RETURN_NAMES = ()
    FUNCTION = "promptlist_read" 


    def promptlist_read(self,INDEX):
        new_path = os.path.join(file_path,INDEX)
        f = open(new_path,'r',encoding='utf-8')
        result = f.read()
        f.close()
        return (result,) 
# =================================================
class INT(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            "INT":("INT",{"min": 0,"max":Maxresolution,"step":1,"default":0})
        }}
    # 返回结果类型
    RETURN_TYPES = ('INT',)
    
    # 返回节点命名
    RETURN_NAMES = ('INT',)
    FUNCTION = "int" 


    def int(self,INT):
        # 打开txt文件
        return (INT,)
# =================================================
class Float(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            "Float":("FLOAT",{"min": 0.00,"max":99999999999999999.00,"step":1.00,"default":0.00})
        }}
    # 返回结果类型
    RETURN_TYPES = ('FLOAT',)
    
    # 返回节点命名
    RETURN_NAMES = ('FLOAT',)
    FUNCTION = "float" 
    def float(self,Float):
        # 打开txt文件
        return (Float,)
    
# =================================================

class AC_sub(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{
               "int_1":("INT",{"forceInput": True}),
               "int_2":("INT",{"forceInput": True}),
               "widthscale":("INT",{"min": 0,"max":Maxresolution,"step":1,"default":64}),
               "heightscale":("INT",{"min": 0,"max":Maxresolution,"step":1,"default":64}),
        }}
    RETURN_TYPES = ("INT","INT","STRING","STRING")
    RETURN_NAMES = ("width","height"," STRING","SCALE RS")
    FUNCTION = "ac_sub" 

    def ac_sub(self,int_1,int_2,widthscale,heightscale):
        width = int_1 - widthscale
        height = int_2 - heightscale
        result = int_1, int_2
        SCALE_RS = width, height 
        result = int_1,int_2
        return (width,height,result,SCALE_RS)
# =================================================
# 获取图片尺寸
class ImageSize_AC(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {"image": ("IMAGE",),},
                }
    RETURN_TYPES = ("INT","INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "image_size"

# TODO:
    def image_size(self,image: Tensor):
        ( height, width) = image.shape[1:3]
        return (width, height)
    
# =================================================
class AC_sum(AC_CATEGORY):
   
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{
               "int_1":("INT",{"forceInput": True}),
               "int_2":("INT",{"forceInput": True}),
               "widthscale":("INT",{"min": 0,"max":Maxresolution,"step":1,"default":64}),
               "heightscale":("INT",{"min": 0,"max":Maxresolution,"step":1,"default":64}),   
        }}
    RETURN_TYPES = ("INT","INT","STRING","STRING")
    RETURN_NAMES = ("width","height"," STRING","SCALE RS")
    FUNCTION = "ac_sum" 

    def ac_sum(self,int_1,int_2,widthscale,heightscale):
        width = int_1 + widthscale
        height = int_2 + heightscale
        result = int_1, int_2
        SCALE_RS = width, height 
        return (width,height,result,SCALE_RS)
# =================================================
class AC_mul(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{
               "int_1":("INT",{"forceInput": True}),
               "int_2":("INT",{"forceInput": True}),
               "Scale":("INT",{"min": 1,"max": 10,"step":1,"default":2}),

            
        }}
    RETURN_TYPES = ("INT","INT","STRING")
    RETURN_NAMES = ("width","height"," STRING")
    FUNCTION = "ac_mul" 

    def ac_mul(self,int_1,int_2, Scale):
        width = int_1 * Scale
        height = int_2 * Scale
        result = width, height
        return (width,height,result)
# =================================================
class AC_div(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{
               "int_1":("INT",{"forceInput": True}),
               "int_2":("INT",{"forceInput": True}),
               "reduce":("INT",{"min": 0,"max": 10,"step":1,"default":2}),

            
        }}
    RETURN_TYPES = ("INT","INT","STRING")
    RETURN_NAMES = ("width","height"," STRING")
    FUNCTION = "ac_div" 

    def ac_div(self,int_1,int_2, reduce):
        width = int_1 / reduce
        height = int_2 / reduce
        result = width, height
        return (width,height,result)

# 数学表达式
math_list=['SUM+','SUB-','MUL*','DIV/']


class MahtExpression(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{
            "MahtExpression":(math_list,),
            "int_1":("INT",{"min": 0,"max":Maxresolution,"step":1,"default":0}),
            "int_2":("INT",{"min": 0,"max":Maxresolution,"step":1,"default":0}),   
        }}
    RETURN_TYPES = ("INT","STRING")
    FUNCTION = "mahtexpression" 
  
    def mahtexpression(self,int_1,int_2,MahtExpression):
        x = math_list.index(MahtExpression)
        if x==0:
            SUM = int_1 + int_2
            return( SUM,str(SUM))
        if x==1:
            SUB = int_1 - int_2
            return( SUB,str(SUB))
        if x==2:
            MUL = int_1 * int_2
            return( MUL,str(MUL))
        if x==3: 
            DIV = int_1 / int_2
            return( DIV,str(DIV))

# =================================================
class Panel(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    def notify(self, text, unique_id=None, extra_pnginfo=None):
        if unique_id is not None and extra_pnginfo is not None:
            if not isinstance(extra_pnginfo, list):
                print("Error: extra_pnginfo is not a list")
            elif (
                not isinstance(extra_pnginfo[0], dict)
                or "workflow" not in extra_pnginfo[0]
            ):
                print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
            else:
                workflow = extra_pnginfo[0]["workflow"]
                node = next(
                    (x for x in workflow["nodes"] if str(x["id"]) == str(unique_id[0])),
                    None,
                )
                if node:
                    node["widgets_values"] = [text]

        return {"ui": {"text": text}, "result": (text,)}

# ====================================================================

class AC_FUN_Prompt(AC_CATEGORY):
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

# ===============================================================
# 自动分辨率选择
resolution_list =['512*512','512*768','768*768','832*832',
                  '768*896','960*560','1024*1024','1280*720','1280*800',
                  '1366*768','1440*900','1600*900','1920*1080',
                  '2560*1440','3840*2160']
class Solution_list(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{
               "Resolution_List":(resolution_list,)}
               }
    # 返回结果类型
    RETURN_TYPES = ('INT','INT','STRING',)
    
    # 返回节点命名
    RETURN_NAMES = ('HEIGTH','WIDHT',)
    FUNCTION = "Solution_list" 

    def Solution_list(self,Resolution_List):
        str = Resolution_List
        list = str.split('*')
        height,width = list[0],list[1]
        height,width = int(height),int(width)
        new_str =f"{height},{width}"
        return (height,width,new_str) 

# ==============================================================
if __name__ == "__main__":
    pass

