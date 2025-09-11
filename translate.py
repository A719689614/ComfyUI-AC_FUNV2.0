
import random
import requests

from .AC_CATAGORY import AC_CATEGORY
from hashlib import md5

class TextTranslate(AC_CATEGORY):
    translate_list = ["zh","en"]
    @classmethod
    def INPUT_TYPES(self):
        return {
            'required': {
                'text': ('STRING', {'multiline': True}),
                "translate_from": (self.translate_list,),
                "translate_to": (self.translate_list,),
                "APIID":  ('STRING', {'multiline': False}),
                "APIKEY":  ('STRING', {'multiline': False}),
            },
        }

    RETURN_TYPES = ('STRING',)
    FUNCTION = 'text_translation'

    @classmethod
    def make_md5(self,s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    def text_translation(self, text,translate_from,translate_to, APIID='20250517002359356', APIKEY="HMAxM6QBzWFHG4sAzuOQ"):
        query = text
        appid = APIID
        appkey = APIKEY
        from_lang = translate_from
        to_lang =  translate_to
        endpoint = 'http://api.fanyi.baidu.com'
        path = '/api/trans/vip/translate'
        url = endpoint + path
        salt = random.randint(32768, 65536)
        sign = self.make_md5(appid + query + str(salt) + appkey)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
        try:
            r = requests.post(url, params=payload, headers=headers)
            result = r.json()
            result = result['trans_result'][0]['dst']
        except:
            result = 'Error'
        
        return (result,)

  