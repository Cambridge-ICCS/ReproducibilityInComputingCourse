<img src="ICCS_logo.png"  width="600">

# Reproducibility in Computing

This repository contains documentation, resources, and code for the Reproducibility in Computing session
designed and delivered by Jack Franklin and Marion Weinzierl of [ICCS](https://github.com/Cambridge-ICCS).  
All materials, including slides and videos, are available such that individuals can cover the
course in their own time.

A website for this workshop can be found at https://cambridge-iccs.github.io/ReproducibilityInComputingCourse/.


## Contents

- [Learning Objectives](#learning-objectives)
- [Teaching material](#teaching-material)
- [Preparation and prerequisites](#preparation-and-prerequisites)
- [Installation and setup](#installation-and-setup)
- [License information](#license)
- [Contribution Guidelines and Support](#contribution-guidelines-and-support)


## Learning Objectives

The key learning objective from this workshop is to raise the awareness of the importance of software reproducibility, and give the participants an understanding
and basic tools to improve it. We will do a whistle-stop tour through the basics of scientific software reproducibility, and touch on topics such as Version Control, READMEs,
Licenses, Automation, Testing and the FAIR principles, and how those apply to software reproducibility. Finally, we will also talk about various initiatives promoting research and software reproducibility.

## Teaching Material

### Slides
The slides for this workshop can be viewed on the [website of this course](https://cambridge-iccs.github.io/ReproducibilityInComputingCourse/).

### Exercises

The exercises for this course are listed in the quarto markdown files which can be found in the [exercises](exercises/) directory. The tasks are
divided into those that can be answered/solved during the session, and also "Extension" tasks which can be worked on outside of the session.

There is a small group of python scripts in the [problem](exercises/problem/) sub-directory. These act as an example of a non-reproducible workflow. The tasks involve understanding and 
improving the reproducibility of the scripts using what is covered in the session. It is recommended to download these scripts to a seperate location on your local machine for 
this purpose.

### Worked Solution

Worked solutions for all of the exercises can be found in the [worked solutions](worked-solutions/) directory.  
These cover the tasks that require any modifications/improvements to the example workflow provided. They are not exhaustive, but use common technologies and approaches
to solving the tasks.

### Mini ReproHack

The [Mini ReproHack repository](https://github.com/Cambridge-ICCS/MiniReproHack) can be used before, alongside or after this course, to learn hands-on what makes software reproducible. It contains instructions on how do a [reproducibility hackathon](www.reprohack.org) by trying to reproduce the results of real climate science papers.


## Preparation and prerequisites

### Prerequisites

To get the most out of the session we assume a basic understanding of the research process, programming in Python and research software.

The ICCS [RSE Skills workshop](https://github.com/jatkinson1000/rse-skills-workshop) gives you an overview of many of the topics mentioned in this course.


### Preparation

It is helpful but not mandatory to do a [mini ReproHack](#mini-reprohack) before the session to get a better understanding of the problem of software and research reproducibility. 

If you want to follow along with the exercises, basic Python coding skills and a Python development environment are required.


## Installation and setup

To complete the exercises, you will need to download the dataset used by the python scripts. This can be found [here](https://www.metoffice.gov.uk/hadobs/hadcrut5/data/HadCRUT.5.0.0.0/download.html)
As part of the exercises will be assessing the data dependencies of the scripts, it will be left as a task to find out which of the datasets you need!

It is recommended to download the python scripts from [exercises/problem](exercises/problem/) to your local machine, in a new directory.
This will allow you to develop the code as you would in practice.


## License

The code materials in this project are licensed under the [MIT License](LICENSE).


## Contribution Guidelines and Support

If you spot an issue with the materials please let us know by
[opening an issue](https://github.com/Cambridge-ICCS/ReproducibilityInComputingCourse/issues)
here on GitHub clearly describing the problem.

If you are able to fix an issue that you spot, or an
[existing open issue](https://github.com/Cambridge-ICCS/ReproducibilityInComputingCourse/issues)
please get in touch by commenting on the issue thread.

Contributions from the community are welcome.
To contribute back to the repository please first
[fork it](https://github.com/Cambridge-ICCS/ReproducibilityInComputingCourse/fork),
make the necessary changes to fix the problem, and then open a pull request back to
this repository clearly describing the changes you have made.
We will then preform a review and merge once ready.

If you would like support using these materials, adapting them to your needs, or
delivering them please get in touch either via GitHub or via
[ICCS](https://github.com/Cambridge-ICCS).
