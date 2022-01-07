import requests
import codecs
import json


class BotBusSearch():
    def __init__(self):
        self.api = 'http://00237.itstransdata.com:8237/RestLibrary/LinhaService'

    def search_bus_line(self, number: str) -> dict:
        req = requests.request(
            'GET', '{}/Busca?nomeOuNumero={}'.format(self.api, number))
        decoded_data = codecs.decode(req.text.encode(), 'utf-8-sig')
        data = json.loads(decoded_data)

        id = data[0]['Id']
        name = data[0]['Nome']

        req.close()

        return id, name, number

    def search_schedules(self, id_bus_line: int, id_bus_path: int) -> dict:
        req = requests.request(
            'GET', '{}/BuscarHorarios?idLinha={}&idTrajeto={}'.format(self.api, id_bus_line, id_bus_path))

        decoded_data = codecs.decode(req.text.encode(), 'utf-8-sig')
        data = json.loads(decoded_data)

        schedule_going = data[0]
        schedule_coming = data[1]

        req.close()

        return schedule_going, schedule_coming

    def search_paths(self, id_bus_line: int, id_bus_path: int) -> dict:
        req = requests.request(
            'GET', '{}/PontosPorTrajeto?idLinha={}&idTrajeto={}'.format(self.api, id_bus_line, id_bus_path))

        decoded_data = codecs.decode(req.text.encode(), 'utf-8-sig')
        data = json.loads(decoded_data)

        name_path_going = data[0]['Value'][0]['Descricao']
        name_path_coming = data[1]['Value'][0]['Descricao']

        req.close()

        return name_path_going, name_path_coming
