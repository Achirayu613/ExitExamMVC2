from controller.auth_controller import AuthController
from controller.promise_controller import PromiseController
from controller.politician_controller import PoliticianController

auth = AuthController()
auth.login("admin", "1234")

promise_ctrl = PromiseController()
politician_ctrl = PoliticianController()

promise_ctrl.mock_data()
politician_ctrl.mock_data()

# หน้ารวมคำสัญญา
for p in promise_ctrl.promises:
    print(p.promise_id, p.detail)

# อัปเดตความคืบหน้า
promise_ctrl.add_update("PR002", "2024-03-01", "เริ่มดำเนินการแล้ว")
promise_ctrl.add_update("PR003", "2024-03-02", "ลองอัปเดตคำสัญญาเงียบหาย")

# หน้ารายละเอียด
promise_ctrl.show_detail("PR002")
