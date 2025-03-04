import json


def get_json(id: str) -> dict:
    try:
        with open(f"../data/individual_json/{id}.json") as fd:
            return json.load(fd)
    except FileNotFoundError:
        return {"message": f"{id} Not Found"}
