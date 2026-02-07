import csv
from model.promises import Promise
from model.promise_updates import PromiseUpdate

class PromiseController:
    def __init__(self):
        self.promises = []
        self.updates = []

    def load_data(self):
        # load promises
        with open("data/promises.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.promises.append(
                    Promise(
                        row["promise_id"],
                        row["pol_id"],
                        row["detail"],
                        row["announce_date"],
                        row["status"]
                    )
                )

        # load updates
        with open("data/promise_updates.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.updates.append(
                    PromiseUpdate(
                        row["promise_id"],
                        row["update_date"],
                        row["detail"]
                    )
                )

    # ===== methods ที่คุณเรียกใช้ =====
    def get_promise(self, pid):
        for p in self.promises:
            if p.promise_id == pid:
                return p
        return None

    def get_updates(self, pid):
        return [u for u in self.updates if u.promise_id == pid]

    def add_update(self, pid, detail):
        from datetime import date
        self.updates.append(
            PromiseUpdate(pid, date.today().isoformat(), detail)
        )

    def get_by_politician(self, pol_id):
        return [p for p in self.promises if p.pol_id == pol_id]
