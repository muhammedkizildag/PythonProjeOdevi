import json
from PIL import Image
from models.filmModel import FilmModel


class Database():

    def __init__(self):
        with open("./database/database.json", "r", encoding="utf-8") as f:
            self._data = json.load(f)

        self.list = [FilmModel(id=k, name=v["name"], year=v["year"], type=v["type"], director=v["director"], state=v["state"], picPath=v["picPath"],point=v["point"]) for k, v in self._data.items()]


    def save(self, name, year, type, director, state, point, pic):
        if len(list(self._data.keys())) != 0:
            id = int(list(self._data.keys())[-1]) + 1
        else:
            id = 0

        self._data[id] = {"name": name,
                          "year": year,
                          "type": type,
                          "director": director,
                          "state": state,
                          "point": point,
                          "picPath": f"{id}.jpg"}

        with open("./database/database.json", "w", encoding="utf-8") as f:
            json.dump(self._data, f, ensure_ascii=False, indent=4)

        _img = Image.open(pic)
        _img.save(f"./database/pics/{id}.jpg", format="JPEG")















