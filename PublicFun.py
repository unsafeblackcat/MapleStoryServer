'''
    create: 阿虚
    blog: www.dbglog.com
'''
import inspect 
import xml.etree.ElementTree as ET
import random 
import os 
from pathlib import Path 

from WZ.DataType import *

MAPLESTORY_SERVER_VERSION = 83

g_dbg_log:int = 0

def set_dbg():
    global g_dbg_log
    g_dbg_log = 1
    return
   
def dbg_print(*args, **kwargs) -> None:
    if g_dbg_log != 0:
        stack = inspect.stack()
        caller_frame_info = stack[1]
        filename = os.path.basename(caller_frame_info.filename) + ',' + caller_frame_info.function
        lineno = caller_frame_info.lineno 
        print(f"[{filename}:{lineno}]", *args, **kwargs)
    return

def generateSend() -> bytes:
    ivSend = [82, 48, 120, 1] #(random.randint(0, 255) * 255) & 0xff
    return bytes(ivSend)

def generateReceive() -> bytes:
    ivRecv = [70, 114, 122, 2] #(random.randint(0, 255) * 255) & 0xff
    return bytes(ivRecv)
 
'''
    枚举指定文件夹下所有文件
    dir_path: 给定文件夹路径
    返回值: 文件夹下所有文件的list[]
'''
def enum_dir(dir_path:str) -> list:
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            full_path = os.path.join(root, file)
            file_list.append(full_path)
    return file_list

'''
    判断文件是否存在
    file_path: 需要判断的文件路径
    返回值 bool: 
            true 文件存在
            , false 文件不存在
'''
def is_file_exist(file_path:str) -> bool:
    return Path(file_path).is_file()

def is_dir_exist(file_path:str) -> bool:
    return Path(file_path).is_dir()

'''
    切割路径得到文件名
    file_path: c\test_dir\1.txt
    返回值: 1.txt
'''
def path_get_short_name(file_path:str) -> str:
    return os.path.basename(file_path)

def xml_get_element_to_int(skill_element:ET.Element, element:str, def_ret:int = 0) -> int:
    iret = def_ret 
    for node in skill_element.iter(): 
        dbg_print(node.tag, node.attrib, node.text)
        if node.attrib.get('name') == element:
            value = node.attrib.get('value')
            if value != None:
                iret = int(value)
                pass 

            break

    return iret

def xml_get_element_to_float(skill_element:ET.Element, element:str, def_ret:float = 0) -> float:
    iret = def_ret 
    for node in skill_element.iter(): 
        dbg_print(node.tag, node.attrib, node.text)
        if node.attrib.get('name') == element:
            value = node.attrib.get('value')
            if value != None:
                iret = float(value)
                pass 

            break

    return iret
  
def xml_get_element_to_str(skill_element:ET.Element, element:str, def_ret:str) -> str:
    sret = def_ret

    for node in skill_element.iter():
        if node.attrib.get('name') == element:
            sret = skill_element.get('value') 
            break

    return sret

def xml_is_element(skill_element:ET.Element, element:str) -> bool:
    bret:bool = False

    query_element, rest = element.split('/', 1)

    for node in skill_element.iter():
        if node.attrib.get(query_element) == element:
            if len(rest):
                bret = xml_is_element(node, rest)
            else:
                bret = True
            break

    return bret

def xml_get_element_item(skill_element:ET.Element, element:str) -> ET.Element:
    
    query_element = element.split('/')
    if query_element[0] == "..": 
        return 

    item:ET.Element = None 
    for node in skill_element.iter():
        if node.attrib.get("name") == element:
            item = node
            break

    return item

def xml_get_file_parse(dir:str, file:str) -> ET.ElementTree:
    ret:ET.ElementTree = None
    xml_file = dir + '/' + file + '.xml'
    if is_file_exist(xml_file):
        ret = ET.parse(xml_file)
        pass

    return ret


def xml_get_type_data(item:ET.Element, subitem:str):

    if (item.tag.lower() == DataType.INT.value.lower()
        or item.tag.lower() == DataType.SHORT.value.lower()):
        return xml_get_element_to_int(item, subitem)

    
    if (item.tag.lower() == DataType.DOUBLE.value.lower()
        or item.tag.lower() == DataType.FLOAT.value.lower()):
        return xml_get_element_to_float(item, subitem)
    
    if (item.tag.lower() == DataType.STRING.value.lower()
        or item.tag.lower() == DataType.UOL.value.lower()):
        return xml_get_element_to_str(item, subitem)
    
    if (item.tag.lower() == DataType.VECTOR.value.lower()):
        x:int = xml_get_element_to_int(item, "x")
        y:int = xml_get_element_to_int(item, "y")
        return tuple(x, y)
    
    if (item.tag.lower() == DataType.CANVAS.value.lower()):
        x:int = xml_get_element_to_int(item, "width")
        y:int = xml_get_element_to_int(item, "height")
        return tuple(x, y)

    return None