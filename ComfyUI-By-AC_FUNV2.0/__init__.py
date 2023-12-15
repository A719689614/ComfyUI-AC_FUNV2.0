from .AC_FUNV2 import *
import os
import shutil



NODE_CLASS_MAPPINGS = {
    # 啊程V2.0
    "模板选择工具": Promptlist_index,
    "读取提示词": Promptlist_read,
    "减法工具V2.0":AC_sub,
    "加法工具V2.0":AC_sum,
    "乘法工具V2.0":AC_mul,
    "除法工具V2.0":AC_div,
    "计算器工具2.0":MahtExpression,
    "Panel面板V2.0": Panel,
    "分辨率选择工具":Solution_list,
    "模板工具V2.0新版":AC_FUN_Prompt,


}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {

}

__all__ = ["NODE_CLASS_MAPPINGS"]

THIS_DIR=os.path.dirname(os.path.abspath(__file__))
DIR_DEV_JS=os.path.abspath(f'{THIS_DIR}/js')
DIR_PY=os.path.abspath(f'{THIS_DIR}/py')
DIR_WEB_JS=os.path.abspath(f'{THIS_DIR}/../../web/extensions/AC_Testing')

if not os.path.exists(DIR_WEB_JS):
    os.makedirs(DIR_WEB_JS)

shutil.copytree(DIR_DEV_JS, DIR_WEB_JS, dirs_exist_ok=True)

print("Cc啊程、模组加载......")