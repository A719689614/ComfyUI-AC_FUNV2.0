import glob
import nodes
import pygame

"""


    Simple utility custom nodes for ComfyUI regarding experimentation with SDXL
    
    By Jens Jakob Kramhøft

    Copyright (c) 2023  

"""

MANIFEST = {
    "name": "AC_Testing",
    "version": (0,1,1),
    "author": "Jens Jakob Kramhøft",
    "project": "https://github.com/jjkramhoeft/util-nodes-for-comfyui",
    "description": "A small node suite for ComfyUI",
}


# 定义全局变量
Maxresolution = 99999999999999999
# 获取 D 盘下所有 txt 文件的路径列表
file_paths = glob.glob('D:/AC_FUNTION/Tags/*.txt')
# 读取模板
class Promptlist_index:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            "ModeList":(file_paths,),
            "tips": ("STRING", {
                    "multiline": False, 
                    "default": '读取你的模板列表'}),
                    
         
        }}
    # 返回结果类型
    RETURN_TYPES = ('STRING',)
    
    # 返回节点命名
    RETURN_NAMES = ('INDEX',)
    FUNCTION = "promptlist_index" 
    CATEGORY = "AC_FUNV2.0" 

    def promptlist_index(self,ModeList,tips=None):
        # 打开txt文件
        return (ModeList,)        

# =============================================================
class Promptlist_read:
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
    CATEGORY = "AC_FUNV2.0" 

    def promptlist_read(self,INDEX):
        f = open(INDEX,'r',encoding='utf-8')
        result = f.read()
        f.close()
        return (result,) 
# =================================================
class AC_sub:
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{
               "int_1":("INT",{"forceInput": True}),
               "int_2":("INT",{"forceInput": True}),
               "widthscale":("INT",{"min": 0,"max":Maxresolution,"step":1,"default":64}),
               "heightscale":("INT",{"min": 0,"max":Maxresolution,"step":1,"default":64}),
               "tips": ("STRING", {
                    "multiline": False, 
                    "default": '精确缩小图片像素'}),
        }}
    RETURN_TYPES = ("INT","INT","STRING","STRING")
    RETURN_NAMES = ("width","height"," STRING","SCALE RS")
    FUNCTION = "ac_sub" 
    CATEGORY = "AC_FUNV2.0"

    def ac_sub(self,int_1,int_2,widthscale,heightscale,tips = None):
        width = int_1 - widthscale
        height = int_2 - heightscale
        result = int_1, int_2
        SCALE_RS = width, height 
        result = int_1,int_2
        return (width,height,result,SCALE_RS)
# =================================================

class AC_sum:
   
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{
               "int_1":("INT",{"forceInput": True}),
               "int_2":("INT",{"forceInput": True}),
               "widthscale":("INT",{"min": 0,"max":Maxresolution,"step":1,"default":64}),
               "heightscale":("INT",{"min": 0,"max":Maxresolution,"step":1,"default":64}),
               "tips": ("STRING", {
                    "multiline": False, 
                    "default": '精确放大图片像素'}),
            
        }}
    RETURN_TYPES = ("INT","INT","STRING","STRING")
    RETURN_NAMES = ("width","height"," STRING","SCALE RS")
    FUNCTION = "ac_sum" 
    CATEGORY = "AC_FUNV2.0"

    def ac_sum(self,int_1,int_2,widthscale,heightscale,tips=None):
        width = int_1 + widthscale
        height = int_2 + heightscale
        result = int_1, int_2
        SCALE_RS = width, height 
        return (width,height,result,SCALE_RS)
# =================================================
class AC_mul:
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{
               "int_1":("INT",{"forceInput": True}),
               "int_2":("INT",{"forceInput": True}),
               "放大倍数":("INT",{"min": 0,"max": 10,"step":1,"default":2}),

            
        }}
    RETURN_TYPES = ("INT","INT","STRING")
    RETURN_NAMES = ("width","height"," STRING")
    FUNCTION = "ac_mul" 
    CATEGORY = "AC_FUNV2.0"

    def ac_mul(self,int_1,int_2, 放大倍数,):
        width = int_1 * 放大倍数
        height = int_2 * 放大倍数
        result = int_1, int_2
        return (width,height,result)
# =================================================
class AC_div:
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{
               "int_1":("INT",{"forceInput": True}),
               "int_2":("INT",{"forceInput": True}),
               "缩小倍数":("INT",{"min": 0,"max": 10,"step":1,"default":2}),

            
        }}
    RETURN_TYPES = ("INT","INT","STRING")
    RETURN_NAMES = ("width","height"," STRING")
    FUNCTION = "ac_div" 
    CATEGORY = "AC_FUNV2.0"

    def ac_div(self,int_1,int_2, 缩小倍数,):
        width = int_1 / 缩小倍数
        height = int_2 / 缩小倍数
        result = int_1, int_2
        return (width,height,result)

# 数学表达式
math_list=['SUM+','SUB-','MUL*','DIV/']


class MahtExpression:
    @classmethod
    def INPUT_TYPES(s):
        return{"required":{
            "MahtExpression":(math_list,),
            "int_1":("INT",{"min": 0,"max":Maxresolution,"step":1,"default":0}),
            "int_2":("INT",{"min": 0,"max":Maxresolution,"step":1,"default":0}),
            
            
        }}
    RETURN_TYPES = ("INT","STRING")
    FUNCTION = "mahtexpression" 
    CATEGORY = "AC_FUNV2.0"
    
    

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
class Panel:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            }
        }
    
    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "show_value"
    CATEGORY = "AC_FUNV2.0"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    def show_value(self, text):
        print(f"show text: {text}")
        return {"ui": {"text": text}, "result": (text,)}
# ====================================================================
# 获取 D 盘下所有 txt 文件的路径列表
# file_paths = glob.glob('D:/AC_FUNTION/Tags/*.txt')
# 读取模板
class AC_FUN_Prompt:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
            "ModeList":(file_paths,),
            "tips": ("STRING", {
                    "multiline": False, 
                    "default": '读取你的模板列表'}),
                    
         
        }}
    # 返回结果类型
    RETURN_TYPES = ('STRING',)
    
    # 返回节点命名
    RETURN_NAMES = ('STRING',)
    FUNCTION = "promptlist_index" 
    CATEGORY = "AC_FUNV2.0" 

    def promptlist_index(self,ModeList,tips=None):
        f = open(ModeList,'r',encoding='utf-8')
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
class Solution_list:
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
    CATEGORY = "AC_FUNV2.0" 

    def Solution_list(self,Resolution_List,tips=None):
        str = Resolution_List
        list = str.split('*')
        height,width = list[0],list[1]
        new_str =f"{height},{width}"
        return (height,width,new_str) 






#do some processing on the image, in this example I just invert it   
# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "模板选择工具": Promptlist_index,
    "模板工具V2.0新版":AC_FUN_Prompt,
    "读取提示词": Promptlist_read,
    "减法工具V2.0":AC_sub,
    "加法工具V2.0":AC_sum,
    "乘法工具V2.0":AC_mul,
    "除法工具V2.0":AC_div,
    "计算器工具2.0":MahtExpression,
    "Panel面板V2.0": Panel,
    "分辨率选择工具":Solution_list,
    
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {

}





