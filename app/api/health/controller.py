import psutil, socket, datetime, subprocess

message = {}
class ServerMonitor:

    @staticmethod
    def sample():
        data = {
            "server": "example-server",
            "status": "healthy",
            "timestamp": "2023-08-21T12:00:00Z",
            "uptime": "2 days, 5 hours",
            "cpu_usage": "10%",
            "memory_usage": {
                "used": "4.5 GB",
                "total": "16 GB",
                "percentage": "28%"
            },
            "disk_usage": {
                "used": "150 GB",
                "total": "500 GB",
                "percentage": "30%"
            },
            "services": [
                {
                "name": "web",
                "status": "running"
                },
                {
                "name": "database",
                "status": "running"
                },
                {
                "name": "email",
                "status": "stopped"
                }
            ]
            }

        return data

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
        # cls().get_top_process
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
        cmd = ['ps', '-eo', 'comm,%mem,%cpu', '--sort=-%mem']
        data = str(subprocess.run(cmd, capture_output=True))
        for _d in data.split("\n"):
            print(_d)