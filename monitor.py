#!/usr/bin/env python3
from bottle import route, static_file, run as bottle_run
from subprocess import run, PIPE

@route('/')
def index():
    items = []
    items.extend([
        run(["lscpu"], stdout=PIPE).stdout,

        b"cpufreq: " + run(
            ["cat", "/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq"],
            stdout=PIPE).stdout,

        run(["/opt/vc/bin/vcgencmd", "measure_temp"], stdout=PIPE).stdout,

        run(["cat", "/proc/meminfo"], stdout=PIPE).stdout,

    ])

    return b"".join(map(wrap_p, items))
    

def wrap_p(text):
    return b"<p>" + text + b"</p>"

bottle_run(host='0.0.0.0', port=5000)
