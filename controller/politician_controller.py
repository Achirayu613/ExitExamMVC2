import csv
from model.politicians import Politician

class PoliticianController:
    def __init__(self):
        self.politicians = []

    def load_data(self):
        with open("data/politicians.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.politicians.append(
                    Politician(
                        row["pol_id"],
                        row["name"],
                        row["party"]
                    )
                )

    def get(self, pol_id):
        for p in self.politicians:
            if p.pol_id == pol_id:
                return p
        return None
