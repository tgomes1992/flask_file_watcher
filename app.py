from flask import Flask , jsonify
from threading import Thread
from FileWatcher.MonitorPastas import MonitorPastasControl


app = Flask(__name__)
monitor = MonitorPastasControl()
t_watcher = Thread(target=monitor.start_monitor)




@app.route("/")
def main():
    return jsonify({"message":"hellor world"})



@app.route("/start_watcher")
def start_watcher():    
    t_watcher.start()
    t_watcher.join()
    return jsonify({"message":"Watcher start"})




@app.route("/stop_watcher")
def stop_watcher():    
    global t_watcher    
    monitor.stop_monitor()
    return jsonify({"message":"Watcher stop"})





if __name__== '__main__':
    app.run(debug=True)
