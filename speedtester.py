import speedtest


class SpeedTester:
    def __init__(self):
        self.servers = []
        self.threads = None
        self.s = speedtest.Speedtest()

    def set_server(self):
        self.s.get_servers(servers=self.servers)
        self.s.get_best_server()

    def make_test(self):
        self.s.download(threads=self.threads)
        self.s.upload(threads=self.threads)
        self.s.results.share()
        results_dict = self.s.results.dict()

        return {"Download": round((results_dict["download"] / (1024 * 1024)), 2),
                "Upload": round((results_dict["upload"] / (1024 * 1024)), 2)}
