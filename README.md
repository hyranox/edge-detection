Welcome to CUSBS Modelling!
===================

To get started it is suggested that you use Linux for programming. The most user-friendly 'flavour' is Ubuntu which you can get [here](https://www.ubuntu.com/download). 

Quickstart
---------------

1. Open up a terminal
2. Install **python** (2.7.x) and **git** by typing, in the command line:
sudo apt-get update
sudo apt-get install git python2.7
3. Next, to copy the project run:`
git clone https://github.com/cusbs/edge-detection.git`
4. [Optional] Install a text editor [sublime-text-3](https://www.sublimetext.com/3) and [pip](https://pip.pypa.io/en/stable/installing/) - the python package management tool for installing python software libraries

Git usage basics
-----------------------
Here is a list of basic git commands that should cover the most common usage of git and GitHub. It's useful to make the distinction that while "git" is a software tool - GitHub is a hosting service, perhaps in analogy: git is the equivalent of a browser while GitHub is the equivalent of a website/server that hosts the contents that git can fetch.

Assuming that you have previously configured your git repository, the typical flow of work when writing software is:

 - **Pull** latest changes from the remote (GitHub) repository into the local one
 - Perform changes to the code - you can find what you have changed using the command: `git status`
 - **Add** the changes you have made to the code
 - **Commit** the changes to your local repository
 - **Push** the changes to the remote

### Commands 
 - `git init`
	 - Creates a new git repository inside a folder by making a new hidden folder `.git/` storing metadata about the code
 - `git pull`
	 - Pull from code from another repository and merges those changes with yours. A combination of `git fetch` to grab new changes and `git merge` to integrate them with your changes.
	
 - `git status`
	 - Shows differences between the last commit and the current "working tree" - the files inside the folder containing the git repository (`.git` folder)
 - `git add`
	 - Adds the updated version of the file to the pre-commit "index". The next commit you make will contain only the updates inside the files that have been added to the index
 - `git commit`
	 - Stores the most recent changes added to the  "index" in a new commit. Each commit is atomic and requires a message from the user to give a brief description of the contents. New commits, when pushes into Github can trigger events such as messages to chats or automated builds of new versions of software.
 - `git push`
	 - Publish changes from your local repository to the remote repository (in our case Github) for others to see and pull.
