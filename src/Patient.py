class Patient:
    def __init__(self, id: str, name: str, city: str,
                 gender: str, age: int, height: float,
                 weight: float, bmi:float, verdict: str):
        self.id = id
        self.name = name
        self.city = city
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.bmi = bmi
        self.verdict = verdict