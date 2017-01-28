
# Lab 0: Setting up the lab workspace

## Setup Vagrant and your cosc480ds virtual machine

These instructions assume that Vagrant and VirtualBox have already been installed on the machine.  I recommend you read a little about Vagrant [here](https://www.vagrantup.com/docs/getting-started/) so you are familiar with the following concepts: `vagrant up`, `vagrant ssh`, synced folders, and teardown.

Open Terminal (or your preferred command line program).

Check that vagrant is installed.

	$ which vagrant
	/usr/local/bin/vagrant

Create a directory where you will do work for this course.

	$ mkdir cosc480ds
	$ cd cosc480ds

All instructions, unless otherwise specified assume that you are located in the `cosc480ds` directory.

Download the [course-specific Vagrantfile](https://raw.githubusercontent.com/colgate-cosc480ds/lecture/master/Vagrantfile) and put it in this directory.  To initialize the vagrant VM, do the following:

	$ vagrant up

This may take a while, especially the first time that it is run.  Once this command completes, there is a virtual machine running on your computer.  We will use the terminology *host* to refer to your computer and *guest* to refer to the VM that is being run on the host.

Now ssh into the vagrant virtual machine.  
	
	$ vagrant ssh
	Welcome to Ubuntu 12.04 LTS (GNU/Linux 3.2.0-23-generic x86_64)

	 * Documentation:  https://help.ubuntu.com/
	New release '14.04.5 LTS' available.
	Run 'do-release-upgrade' to upgrade to it.

	Welcome to your Vagrant-built virtual machine.
	Last login: Fri Sep 14 06:23:18 2012 from 10.0.2.2
	vagrant@ubuntu:~$

Try out the following command.  Run it twice.  The first time you may see a warning message.  The second time, the warning should not be there.  

	vagrant@ubuntu:~$ python -c "import matplotlib; import matplotlib.pyplot as plt; print matplotlib.__version__"

It should simply print `1.5.1`.  If it does not, notify me with the error you received.

When you are done working, you can logout of the ssh session

	vagrant@ubuntu:~$ logout
	Connection to 127.0.0.1 closed.

You should also remember to suspend (or halt, see the difference [here](https://www.vagrantup.com/docs/getting-started/teardown.html)) your VM.

	$ vagrant suspend
	==> default: Saving VM state and suspending execution...

To restart the VM, simply do

	$ vagrant up


## Clone first lab

Clone this repo.  

	vagrant@ubuntu:~$ cd /vagrant/
	vagrant@ubuntu:~$ git clone XXXXXX

Change into the `lab1` directory.

	vagrant@ubuntu:~$ cd lab1
	vagrant@ubuntu:~$ ls
	XXXXXX

Since this folder is shared between the guest and host machine, you can see these files on your host machine as well.  

Let's make sure you can commit changes to this repo.

	vagrant@ubuntu:~$ echo "Hello world!" > hello.txt
	vagrant@ubuntu:~$ git add hello.txt
	vagrant@ubuntu:~$ git commit -m 'committing hello world file'
	vagrant@ubuntu:~$ git push origin master

Make sure you can see this file in your repo on [GitHub](https://github.com/).


## Setup Jupyter Notebook

A Jupyter notebook lets you write and execute Python code interactively in your web browser. It is a powerful way to interact with code and also to mix Python code with beatifully rendered text and math for the purposes of exposition. (Jupyter notebooks were formerly called iPython notebooks.) 

Inside your VM, do the following:

	vagrant@ubuntu:~$ cd /vagrant/lab1/
	vagrant@ubuntu:~$ jupyter notebook --no-browser --ip=0.0.0.0 --port=8888

In the output of this command, you should see a line that looks something like this:

	The Jupyter Notebook is running at: http://0.0.0.0:8888/?token=[authentication token]

The **authentication token** part of the URL is something you will need later. Copy and paste that url into a web browser on your host machine, and you should see a jupyter notebook environment.  

Click on any file ending in `.ipynb` and it should open up a Python Notebook.


## Setup PyCharm, an IDE

PyCharm is a cross-platform integrated development environment (IDE) for Python which has many popular programming features, including syntax highlighting, code autocompletion, and a debugger.

These instructions assume that PyCharm professional edition has been installed and a free license obtained.  You can obtain a license by applying [here](https://www.jetbrains.com/student/) and using your .edu email).  You should be granted a license immediately.  If you don't, notify me.

We will set up PyCharm so it runs all code inside our VM.

Open PyCharm.  Choose "Create New Project."  Under Location, choose your cosc480ds directory.  Under Interpreter, click the little "..." button and select "Add remote."  A window should pop up: check the Vagrant button, set the "Vagrant Instance Folder" to be cosc480ds and the "Python interpreter path" to be `/home/vagrant/miniconda/bin/python`.  Click OK.  A window may pop up that asks if you are sure you want to continue connecting. Click Yes.

Another window will eventually pop up asking, "Would you like to create a project from existing sources instead?"  Click Yes.

Open any python notebook (i.e., any file ending in `.ipynb`) in PyCharm.  Click the green "play" button at the top of the python notebook.  If prompted for your authentication token, copy and paste from the vagrant command line (see above).

In addition to running notebooks, you can also execute python code.  Open any file ending in `.py` and go up to the Run menu and select the first option.

