import psutil

def run():

    cpu_nb = psutil.cpu_count()
    print(f'nb of cpu : {cpu_nb}')

if __name__ == "__main__":
    run()