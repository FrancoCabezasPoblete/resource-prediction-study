from cpuinfo import get_cpu_info
import subprocess
import argparse
import psutil
import time

def parse_arguments():
    parser = argparse.ArgumentParser(description="Get metrics from a command execution and store them in a file.")
    parser.add_argument("benchmark", type=str, help="Name of the benchmark.")
    parser.add_argument("command", nargs='+', help="Command to be executed.")
    return parser.parse_args()

def syscalls(command, result_file):
    res = subprocess.run(["strace", "-o", result_file, *command], text=True, capture_output=True)
    return res.stdout, res.stderr

def memory_and_cpu_usage(command, interval=1e-2):
    memory_records = []
    cpu_records = []
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ps_process = psutil.Process(process.pid)
    try:
        while process.poll() is None:
            memory_records.append(ps_process.memory_info()._asdict())
            cpu_records.append(ps_process.cpu_times()._asdict())
            time.sleep(interval)  # Wait until the next record
    except psutil.NoSuchProcess:
        print("The process finished before the end of the monitoring.")
    stdout, stderr = process.communicate()
    return cpu_records, memory_records, stdout, stderr

def execution_time(command, iterations=1):
    execution_times = []
    time_format = "%e, %P, %K, %M, %W"
    for _ in range(iterations):
        result = subprocess.run(["/bin/time", "-f", time_format, *command], text=True, capture_output=True)
        execution_times.append(result.stderr)
    return execution_times

def pc_info():
    info = get_cpu_info()
    return {
        'brand_raw': info['brand_raw'],
        'vendor_id_raw': info['vendor_id_raw'],
        'arch': info['arch'],
        'count': info['count'],
        'l2_cache_size': info['l2_cache_size'],
        'l3_cache_size': info['l3_cache_size'],
        'hz_actual_friendly': info['hz_actual_friendly'],
        'hz_advertised_friendly': info['hz_advertised_friendly'],
        'l2_cache_line_size': info['l2_cache_line_size'],
        'l2_cache_associativity': info['l2_cache_associativity'],
    }