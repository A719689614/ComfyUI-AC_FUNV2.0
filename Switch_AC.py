from .AC_CATAGORY import AC_CATEGORY

Switch_list = ["One", "Two"]

class Switch(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
            "Switch": (Switch_list,),
            "Prompt_1":("STRING",{"forceInput":True}),
            "Prompt_2":("STRING",{"forceInput":True}),
            }
            }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Prompt",)
    FUNCTION = "switch"

    def switch(self, Switch,Prompt_1, Prompt_2):
        if Switch == "One":
            return (Prompt_1,)
        if Switch == "Two":
            return (Prompt_2,)

class AC_Join(AC_CATEGORY):
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
            "Prompt_1":("STRING",{"forceInput":True}),
            "Prompt_2":("STRING",{"forceInput":True}),
            }
            }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Prompt",)
    FUNCTION = "switch_2"

    def switch_2(self,Prompt_1, Prompt_2):
        result = Prompt_1 + Prompt_2
        return (result,)
