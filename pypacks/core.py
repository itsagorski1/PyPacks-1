import os
from .types import PyPackType

class PyPack:
    def __init__(self, name: str, description):
        self.name = name
        self.functions = {}
        self.description = description
    def build(self, pack_type, author):
        os.makedirs(f"{self.name}/{pack_type}", exist_ok=True)
        if pack_type == PyPackType.JAVA:
            with open(f"{self.name}/{pack_type}/pack.mcmeta", "w") as f:
                f.write('{"pack": {"pack_format": 1, "description": "' + self.description + '"}}')
            namespace = self.name.lower()
            os.makedirs(f"{self.name}/{pack_type}/data/{namespace}/function", exist_ok=True)
            for i in self.functions:
                with open(f"{self.name}/{pack_type}/data/{namespace}/function/{i}.mcfunction", "w") as f:
                    for j in self.functions[i]:
                        f.write(f"{j}\n")
        elif pack_type == PyPackType.BEDROCK:
            with open(f"{self.name}/{pack_type}/manifest.json", "w") as f:
                f.write(str({"format_version": 1,"metadata": {"authors": [author],"generated_with": {"pypacks": ["1.0.0"]}},"header": {"name": self.name,"description": self.description,"min_engine_version": [1,0,0],"uuid": "993566e0-5fb1-4124-8639-4e4df07f196a","version": [1,0,0]},"modules": [{"type": "data","uuid": "224a1d1c-b08d-4430-a331-9933d9599529","version": [1,0,0]}]}).replace("'", '"'))
            os.makedirs(f"{self.name}/{pack_type}/functions", exist_ok=True)
            for i in self.functions:
                with open(f"{self.name}/{pack_type}/functions/{i}.mcfunction", "w") as f:
                    for j in self.functions[i]:
                        f.write(f"{j}\n")