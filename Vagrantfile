VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.box = "ubuntu/trusty64"

    config.vm.provider "virtualbox" do |v|
      v.memory = 4096
      v.cpus = 4
    end

	config.vm.provision "docker", version: "1.3.3"
	config.vm.network :public_network
	config.vm.network :private_network, ip: "192.168.0.0"



	config.vm.provision "shell",inline: "sudo apt-get -y update"
	config.vm.provision "shell",inline: "echo --------------------------------------apt-get updated-------"
    config.vm.provision "shell",inline: "sudo docker run --rm -v /usr/local/bin:/target jpetazzo/nsenter"
	config.vm.provision "shell",inline: "echo --------------------------------------docker nsenter-------"
	config.vm.provision "shell",inline: "sudo apt-get install -y  keychain"
	config.vm.provision "shell",inline: "echo --------------------------------------apt-get keychain-------"
	config.vm.provision "shell",inline: "sudo apt-get install -y python-setuptools python-pip python-dev build-essential"
	config.vm.provision "shell",inline: "sudo pip install --no-input -U fig"
	config.vm.provision "shell",inline: "echo --------------------------------------fig install complete-------"
	config.vm.provision "shell",inline: "sudo cp -f /vagrant/bin/call_my_profile_d.sh  /etc/profile.d/"
	config.vm.provision "shell",inline: "echo --------------------------------------add startup config set path-------"

end
