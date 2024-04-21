import subprocess
import argparse
import psutil
import time

def parse_arguments():
    parser = argparse.ArgumentParser(description="Get metrics from a command execution and store them in a file.")
    parser.add_argument("directory", type=str, help="Directory where the results will be stored.")
    parser.add_argument("command", nargs='+', help="Command to be executed.")
    return parser.parse_args()

def run_with_strace(command, result_file):
    with subprocess.Popen(
        ["strace", "-o", result_file] + command, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
    ) as proc:
        stdout, stderr = proc.communicate()
        return stdout, stderr

def run_and_monitor_memory(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ps_process = psutil.Process(process.pid)
    memory_info = ps_process.memory_info()
    stdout, stderr = process.communicate()
    return memory_info, stdout, stderr

def run_and_monitor_cpu(command):
    start_time = time.time()
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ps_process = psutil.Process(process.pid)
    stdout, stderr = process.communicate()
    end_time = time.time()
    cpu_times = ps_process.cpu_times()
    return cpu_times, end_time - start_time, stdout, stderr