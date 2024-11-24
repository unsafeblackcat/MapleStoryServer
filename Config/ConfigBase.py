import configparser

class ConfigBase :
    def __init__(self, config_path) -> None: 
        self.config_ini = configparser.ConfigParser()
        self.config_ini.read(config_path, encoding='gbk')
        return
    
    def get_item(self, item_name) -> str: 
        items = self.config_ini.items(item_name)

        data = None
        for it in items:
            if it[0] == 'data':
                data = it[1]
                break
        return data
