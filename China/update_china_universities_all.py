import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'\[\d+\]', '', text)
    text = re.sub(r'\[[a-z]{2}\]', '', text)
    return text.strip()

def normalize(name):
    return re.sub(r'[\s\(\)（）]', '', name)

def update_all_provinces():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'china_universities.json')
    links_path = os.path.join(base_dir, 'province_links.json')
    
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return
    if not os.path.exists(links_path):
        print(f"Error: {links_path} not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        universities = json.load(f)
    
    with open(links_path, 'r', encoding='utf-8') as f:
        province_import requests
from bs4 import BeautifulSoup
import json
import os
import re
import time

def clean_te)}from bs4 imporerimport json
import os
import'Mimport os
 (import rh;import tac
def clean5_7    if not text:
    (        return ko    text = re.su72    text = re.sub(r'\[[a-z]{2}\]', '',ik    return text.strip()

def normalize(nameur
def normalize(name):
       return re.sub(rin
def update_all_provinces():
    base_dir = ol h    base_dir = os.path.dir      json_path = os.path.join(base_dir, 'china_universiti..    links_path = os.path.    response = requests.get(url, headers=    
    if not os.path.exists(json_path):
        print(f"Er00             print(f"Error: {json_path} n {        return
    if not os.path.exists(links c    if not os          print(f"Error: {links_path} np(        return

    with open(json_path, 'r', es 
    with opell(        universities = json.load(f)
    
    with op      
    with open(links_path, 'r'     ov        province_import requests
from bs4 import Beaue from bs4 import BeautifulSoup
i =import json
import os
import  import os
 nimport r
 import    
def     contimport os
import'Mimport os
 (import rh;adimport'M=  (import rh;impotrdef clean5_7    if non     (        return ko    t']
def normalize(nameur
def normalize(name):
       return re.sub(rin
def update_all_provinces():
        idef normalize(name) h       return re.su'idef update_all_provincei;    base_dir = ol h    basr     if not os.path.exists(json_path):
        print(f"Er00             print(f"Error: {json_path} n {        return
    if not os.path.exists(links c    if not os          pr_n        print(f"Er00             pridx    if not os.path.exists(links c    if not os          print(f"Error: {linkls
    with open(json_path, 'r', es 
    with opell(        universities = json.load(f)
    
    with  
     with opell(        universitco    
    with op      
    with open(links_path,            with open(li  from bs4 import Beaue from bs4 import BeautifulSoup
i =import json
  i =import json
import os
import  import os
 nimpor  import os
i    import  br nimport r
 impo   import   
def     co  import'Mimport os
 (am (import rhame:
  def normalize(nameur
def normalize(name):
       return re.sub(rin
def update  norm_chi = normadef normalize(name)         return re.su  def update_all_province:
        idef normalize(nam          print(f"Er00             print(f"Error: {json_path} n {        return
    if not os.path.exists(links c    if not os          pr_n  en    if not os.path.exists(links c    if not os          pr_n        print(f"_n    with open(json_path, 'r', es 
    with opell(        universities = json.load(f)
    
    with  
     with opell(        universitco    
    with op      
    with open(li      with opell(        universich(    
    with  
     with opell(        universit]'   ex     with      with op      
    with open(links_      with open(li mi =import json
  i =import json
import os
import  import os
 nimpor  import os
i    import  br nimpor    i =import ji_import os
impor  impo       nimpor  import  =i    import  br nme impo   import   
def     def     co  imponi (am (import rhame:
  def         idx = uni_map[nodef normalize(name):
         re    provincedef update  norm_chi =           idef normalize(nam          print(f"Er00             print(f"Error: {json_path} n {  iv    if not os.path.exists(links c    if not os          pr_n  en    if not os.path.exists(links c    if       with opell(        universities = json.load(f)
    
    with  
     with opell(        universitco    
    with op      
    with open(li      with opell(        universiio    
    with  
     with opell(        universith    n(     with,     with op      
    with open(li    so .dump(universitie    with  
     with opell(        universit]'   ex     M     withto    with open(links_      with open(li mi =import json
  i =import __  i =import json
import_provinces()
