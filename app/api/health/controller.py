import psutil, socket, datetime, subprocess
from random import randint

message = {}
class ServerMonitor:

    @classmethod
    def get(cls):
        current_timestamp = datetime.datetime.now()
        try:
            ram_info = psutil.virtual_memory()
            disk_info = psutil.disk_usage("/")
            message["memory_usage"] = cls.memory_usage(ram_info)
            message["disk_usage"] = cls.memory_usage(disk_info)

        except FileNotFoundError:
            message['status'] = "No disk found in the server"
        except:
            message['status'] = "No-Info"
        message['server'] = socket.gethostname()
        message['uptime'] = cls().uptime
        message['timestamp'] = current_timestamp.strftime("%m-%d-%Y %H:%M:%S")
        message['services'] = cls().get_top_process
        return message

    @classmethod
    def memory_usage(cls, object):
        total = f"{object.total / 1024 / 1024 / 1024:.2f}GB"
        used = f"{object.used / 1024 / 1024 / 1024:.2f}GB"
        return {
            "total": total,
            "used": used,
        }

    @property
    def uptime(self):
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
        minutes, seconds = divmod(uptime_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{'%d hours %02d minutes %02d seconds' % (hours, minutes, seconds)}"

    @property
    def get_top_process(self):
        _data_dict = {}
        cmd = ['ps', '-eo', 'comm,%mem,%cpu', '--sort=-%mem']
        proc1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        proc2 = subprocess.Popen(
            ['head', '-10'],
            stdin=proc1.stdout,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )

        proc1.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.
        out, err = proc2.communicate()
        for line in str(out).split("\\n")[1:-1]:
            data = line.split()
            service_name = data[0]
            memory = f"{float(data[1]):.2f}%"
            cpu = f"{float(data[2]):.2f}%"
            print(line)
            if service_name in _data_dict.keys():
                service_name = f"{service_name}{randint(1, 9)}"
            _data_dict[service_name] = {
                "cpu_usage": cpu,
                "memory_usage": memory
            }
        return _data_dict
