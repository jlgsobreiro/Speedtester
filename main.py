import csv_writer
from speedtester import SpeedTester

csv_path = "C:\\Speedtester\\teste.csv"
csv_writer.make_file(csv_path)

speed_tester = SpeedTester()
speed_tester.servers = []
speed_tester.set_server()

result = speed_tester.make_test()

csv_writer.write_file(csv_path, result["Upload"], result["Download"])


