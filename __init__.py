from .AC_FUNV2 import *
import os
import shutil
from .Second_Season import *
from .AC_Makemodel import *
from .Negative import *
from .Thirdly_Season import *
from .Switch_AC import *
from .Fourth_Season import *
from .DesignAera import *
from .Fifth_Season import AC_FUN_Fifth
from .Sixth_Season import AC_FUN_Sixth
from .Seven_Season import AC_FUN_Seven
from .Eight_Season import AC_FUN_Eighth
from .translate import TextTranslate

NODE_CLASS_MAPPINGS = {
    # 啊程V2.0
    "Int_数字整形":INT,
    "Int_数字浮点型":Float,
    "Image_图像像素尺寸":ImageSize_AC,
    "Image_加法工具V2.0":AC_sum,
    "Image_乘法工具V2.0":AC_mul,
    "Image_除法工具V2.0":AC_div,
    "Image_计算器工具2.0":MahtExpression,
    "Panel面板": Panel,
    "Image_分辨率选择工具":Solution_list,
    "Make制作模板":Makemodel,
    "Read读取模板":Readmodel,
    "AC_Switch开关": Switch,
    "AC_词汇合并": AC_Join,
    "AC_百度翻译": TextTranslate,
    "AC_DESIGN_AERA":AC_FUN_Design,
    "AC_Negative_prompt提示词":AC_FUN_Negative_Prompt,
    "AC_First_Season提示词":AC_FUN_Prompt,
    "AC_Second_Season提示词":AC_FUN_Prompt_Second,
    "AC_Third_Season提示词":AC_FUN_Thirdly,
    "AC_Fourth_Season提示词":AC_FUN_Fourth,
    "AC_Fifth_Season提示词":AC_FUN_Fifth,
    "AC_Sixth_Season提示词":AC_FUN_Sixth,
    "AC_Seven_Season提示词":AC_FUN_Seven,
    "AC_Eighth_Season提示词":AC_FUN_Eighth,
    

}

NODE_DISPLAY_NAME_MAPPINGS = {

}
