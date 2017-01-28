# Lab 1

Welcome to the first COSC 480 Data Science Lab!

You are encouraged to work with a partner for this lab.  If you do not have a partner, let me know and I can assign one to you.  (While you can choose your partner, you may be asked to choose *different* partners for each lab for the first couple of labs.)

## Your tasks

Your tasks include the following:

- **Setup** During lab on Tuesday, complete the [setup instructions](setup.md).
- If you also plan to do work on your own machine, complete the setup on your own machine as well.
- **Prelab** Before coming to lab on Tuesday, I would like you to work through the prelab assignment.  The prelab is described in a python notebook called `pythonpractice.ipynb`.  If you have completed the setup instructions on your own computer, you can complete the prelab before class.  If you have not set up your own machine, you can simply open up `pythonpractice.ipynb` and `pythonpractice.py` in a web browser and read them.  Work out as much of a solution as you can and come to lab on Tuesday with a rough first draft solution.  
- **Lab 1** Complete the lab itself.  After you have completed the setup instructions, open up the `lab1.ipynb` python notebook and follow the instructions there.

The lab is due **Monday, Feb. 6th 2017 at 11:59pm**.


## Submission instructions

To submit your work, you must *commit* your changes, *tag* them, and then *push* those changes to GitHub. 

1. Check the status to see what changes have been made.

		vagrant@ubuntu:~$ cd /vagrant/lab1/
		vagrant@ubuntu:~$ git status 
		...

2. Use `git add` to move these changes to the "staging area."  By using the `-u` flag you will only add files that already exist in the repository.  This is probably what you want to do in general.  Please **never** do `git add -A` because it will add all sorts of junk files (such as hidden files left by applications like PyCharm).  First, do a dry run with the `-n` flag:

		vagrant@ubuntu:~$ git add -un .           
		...	

	If everything looks good, add them for real:

		vagrant@ubuntu:~$ git add -u .            
		...	

3. *Commit* the changes to your local repository.  Please write a commit message having the following form.  Please fill in the blank with a word or phrase that captures your sentiments (e.g., "fun", "terrifying", "invigorating", "never-ending", "delightful", etc.).

		vagrant@ubuntu:~$ git commit -m 'completed lab1: this lab was _____'

4. *Tag* your commit.  I will grade your work by checking out the tag.  If you don't tag your work, you won't be graded!  Let's tag this lab as `lab1`.  (We'll use a [lightweight tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging).)

		vagrant@ubuntu:~$ git tag lab1

5. *Push* these changes to GitHub.  Be sure to push the tag!

		vagrant@ubuntu:~$ git push origin lab1   # where lab1 is the name of your tag


