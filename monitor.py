#!/usr/bin/env python3
from bottle import route, run as bottle_run
from subprocess import run, PIPE


@route('/')
def index():
    items = []
    items.extend([
        call("lscpu"),

        b"cpufreq: " +
        call("cat", "/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq"),

        call("/opt/vc/bin/vcgencmd", "measure_temp"),

        call("cat", "/proc/meminfo"),

    ])

    return b"".join(map(wrap_p, items))


def call(*args):
    return run(args, stdout=PIPE).stdout


def wrap_p(text):
    return b"<p>" + text + b"</p>"

bottle_run(host='0.0.0.0', port=5000)
