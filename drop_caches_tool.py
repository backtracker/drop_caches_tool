import subprocess
import logging
import time

low_mem=500
logging.basicConfig(filename='../logs/drop_caches_tool.log', level=logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)
log = logging.getLogger('drop_caches_tool')


def get_time_str():
    return str(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))

def execute_shell(shell):
    log.info("Execute shell: "+shell)
    process = subprocess.Popen(shell, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    out, err = process.communicate()
    errcode = process.returncode
    out_str = out.decode("utf-8")
    return out_str

if __name__ == "__main__":
    log.info(get_time_str()+" starting...")
    get_free_mem_shell="free -m | awk 'NR==2{print $4}'"
    drop_mem_caches_shell="sync;echo 3 > /proc/sys/vm/drop_caches"
    current_free_mem = int(execute_shell(get_free_mem_shell))
    log.info("Current free mem : "+str(current_free_mem)+"M")
    if current_free_mem < low_mem:
        log.info("Current free mem < "+str(low_mem)+"M，starting drop mem caches...")
        execute_shell(drop_mem_caches_shell)
    else:
        log.info("Current free memory sufficient, exit the program.")
    log.info("==================================================")