# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.boot_timeout = 600  # 600 seconden (10 minuten)
  config.vm.box_version = "20230607.0.5"


  # Poortdoorsturing (bijv. voor webserver op poort 8000)
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Provisioning: updates, Python3-venv, zip en alias
  config.vm.provision "shell", inline: <<-SHELL
    sudo systemctl disable apt-daily.service apt-daily.timer apt-daily-upgrade.timer apt-daily-upgrade.service

    sudo apt-get update -y
    sudo apt-get install -y --no-install-recommends python3-venv zip

    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
    fi
  SHELL
end
