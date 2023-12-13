import os
import subprocess
import time
import re
import io
import sys
import getpass
import os.path
import click


user = getpass.getuser()
sudo = subprocess.getoutput("groups "+user+"| grep -oE sudo")
ip = subprocess.getoutput("hostname -I").strip()

def install():
    install = ["sudo killall apt apt-get","sudo rm /var/lib/apt/lists/lock","sudo rm /var/cache/apt/archives/lock","sudo rm /var/lib/dpkg/lock*",
               "sudo dpkg --configure -a","sudo apt update && sudo apt upgrade -y","sudo apt install nginx",
               "sudo apt install nginx","sudo systemctl start nginx","sudo systemctl start nginx",
               "sudo useradd --no-create-home --shell /bin/false prome","sudo useradd --no-create-home --shell /bin/false node_exporter",
               "sudo mkdir /etc/prometheus","sudo mkdir /var/lib/prometheus","sudo wget https://github.com/prometheus/prometheus/releases/download/v2.0.0/prometheus-2.0.0.linux-amd64.tar.gz",
               "sudo tar xvf prometheus-2.0.0.linux-amd64.tar.gz","sudo cp prometheus-2.0.0.linux-amd64/prometheus /usr/local/bin/",
               "sudo cp prometheus-2.0.0.linux-amd64/promtool /usr/local/bin/",
               "sudo chown prome:prome /usr/local/bin/prometheus","sudo chown prome:prome /usr/local/bin/promtool",
               "sudo cp -r prometheus-2.0.0.linux-amd64/consoles /etc/prometheus","sudo wget https://raw.githubusercontent.com/Alexandrdsds/Alexandrdsds/main/prometheus",
               "sudo cp -r prometheus-2.0.0.linux-amd64/console_libraries /etc/prometheus",
               "sudo chown -R prome:prome /etc/prometheus/consoles","sudo chown -R prome:prome /etc/prometheus/console_libraries",
               "sudo touch /etc/prometheus/prometheus.yml","sudo chmod 777 /etc/prometheus/prometheus.yml",
               "sudo touch /etc/systemd/system/prometheus.service","sudo chmod 777 /etc/systemd/system/prometheus.service","sudo cat prometheus > /etc/systemd/system/prometheus.service",
               "sudo chmod 777 /var/lib/prometheus"]
    command = '\n'.join(install)
    os.system(command)
    file = '/etc/prometheus/prometheus.yml'
    with open(file , "w") as f:
        f.write("global:\n"
                "  scrape_interval: 15s\n\n"
                "scrape_configs:\n"
                "  - job_name: 'prometheus'\n"
                "    scrape_interval: 5s\n"
                "    static_configs:\n"
                "      - targets: ['localhost:9090']\n")
    install2 = ["sudo systemctl daemon-reload",
                "sudo systemctl start prometheus","sudo systemctl enable prometheus","sudo systemctl restart prometheus"]
    command2 = '\n'.join(install2)
    os.system(command2)

    os.system("clear")
    print("\t\tПерейдіть за посиланням в браузері http://localhost:9090\n")

install()
