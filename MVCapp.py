from flask import Flask, render_template, request, redirect, url_for, session
from controller.auth_controller import AuthController
from controller.promise_controller import PromiseController
from controller.politician_controller import PoliticianController

app = Flask(__name__)
app.secret_key = "mvc-simple-secret"

auth = AuthController()
promise_ctrl = PromiseController()
politician_ctrl = PoliticianController()

# โหลดข้อมูล CSV
promise_ctrl.load_data()
politician_ctrl.load_data()

# ---------- LOGIN ----------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if auth.login(request.form["username"], request.form["password"]):
            session["is_admin"] = auth.is_admin
            return redirect(url_for("all_promises"))
        return "Login failed"

    return render_template("login.html")

# ---------- ALL PROMISES ----------
@app.route("/promises")
def all_promises():
    return render_template(
        "all_promises.html",
        promises=promise_ctrl.promises
    )

# ---------- PROMISE DETAIL ----------
@app.route("/promise/<pid>")
def promise_detail(pid):
    promise = promise_ctrl.get_promise(pid)
    updates = promise_ctrl.get_updates(pid)

    return render_template(
        "promise_detail.html",
        promise=promise,
        updates=updates,
        is_admin=session.get("is_admin", False)
    )

# ---------- UPDATE PROMISE ----------
@app.route("/promise/<pid>/update", methods=["GET", "POST"])
def update_promise(pid):
    if not session.get("is_admin"):
        return "เฉพาะผู้ดูแลระบบเท่านั้น"

    promise = promise_ctrl.get_promise(pid)
    if promise.status == "เงียบหาย":
        return "ไม่สามารถอัปเดตคำสัญญาที่เงียบหายได้"

    if request.method == "POST":
        promise_ctrl.add_update(pid, request.form["detail"])
        return redirect(url_for("promise_detail", pid=pid))

    return render_template("promise_update.html", promise=promise)

# ---------- POLITICIAN ----------
@app.route("/politicians/<pol_id>")
def politician_detail(pol_id):
    promises = promise_ctrl.get_by_politician(pol_id)
    politician = politician_ctrl.get(pol_id)

    return render_template(
        "politician.html",
        politician=politician,
        promises=promises
    )

if __name__ == "__main__":
    app.run(debug=True)
