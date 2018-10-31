Title: Refactoring biology project : Part 1
Date: 2018-10-29
Category: Project
Tags: Python, Quality Control, Open Source

One of my first coding exercise after having getting introductory certificates in python programmation
is an open project. Due to work at my lab, i had to set up a quality control scheme on our ELISAs.
ELISAs is a method to assay proteins. Quickly said, we put some chemicals and our samples in wells, 
and the stronger the coloration is, the higher concentration of said protein is. 

However, we have to carefully check, if our assay don't get wrong at this point or over time. Imagine 
a product in the kit goes bad, or this day, you made a mistake and put two times more solution! Is your
sample concentration really low or this test wrong?

Quality control (QC) is very important and monitors the processes for detection of error. The solution
we had in the lab was an ugly excel file, updated whenever, with no one really looking at it. After 
having made a better version of it, i searched if my fellow biologists had made already a handy 
application to use simply in the lab, that automate graphing, detect errors and throw warning from 
many files.

I found quickly one item, a paper from Wetzel HN et al, [*"A novel Python program for implementation of quality
control in the ELISA"*](https://www.ncbi.nlm.nih.gov/pubmed/28579365). They describe their quality control
method and objective and states that this program is meant to help laboratories implement good quality control
methods.

But let's look a bit at their program : 

You can find it on their github at [https://github.com/hanna133/ELISA_QC](https://github.com/hanna133/ELISA_QC). 

The repository is composed of the manual, some test csv file supposed to be actual results from an ELISA, and the
main program called elisaqc.py

It uses Tkinter as GUI and matplotlib for the plot. The program is written in pyhton 2. Having some knowledge,
of thoses two, i thought it would be a perfect first project for me to participate in and test
my beginners programming skills.

My first task was to convert the program from python 2 to 3, as python 2 will stop being supported soon and i 
personally prefer python 3. 

After having that, i had a big problem. The program didn't work! And there was no way to understand what was
happening. Base code is a bit messy and uncommented, variables are all over the place with non explicit names 
and the majority of the code is redundant. 

Here a sample of code to let you see what i was dealing with: 
~~~~
for files in glob.glob("*%s.csv"%(userinput1)) :
		count=count+1
		fnames.append(files)
		array=np.genfromtxt(files, delimiter=',', skip_header=userinput3-1, usecols=(userinput4-1,userinput5-1))

		#slice the array
		array1=array[0:3]
		# take out the concentration values
		conc1=array1[:,0]
		#fill in the blank values
		conc1 = conc1[np.logical_not(np.isnan(conc1))]
		inds1=np.where(np.isnan(array1))
		array1[inds1]=np.take(conc1, inds1[1])
		#take the mean of the ODs
		mean1=np.mean(array1, axis=0)
		#pull out the values for the main graph
		x1=array1[:,0]
		y1=array1[:,1]	
		#append the values into the empty list
		y11.append(y1)
		meanind1.append(mean1)

		array2=array[3:6]
		conc2=array2[:,0]
		conc2 = conc2[np.logical_not(np.isnan(conc2))]
		inds2=np.where(np.isnan(array2))
		array2[inds2]=np.take(conc2, inds2[1])
		mean2=np.mean(array2, axis=0)
		x2=array2[:,0]
		y2=array2[:,1]	
		y22.append(y2)
		meanind2.append(mean2)
~~~~

And this is repeated for the amount of time there is points in the standard curve of the test (8 time there). So yeah, 
second task was the biggest. 

**Searching what was going on, what was supposed to happen and then refactoring it, little by little.**

End in part two : )  