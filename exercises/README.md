# Exercises in reproducibility

After going through the slides on how to make our research projects reproducible,
it is time to go through a practice scenario!

The code in `problem/` is an example of a research project which has not taken 
reproducibility into account.

## Data

If you are trying to work through these exercises, you will need the data that
the scripts rely on, which can be found here: https://doi.org/10.5281/zenodo.7014332.

## Instructions:

1. Create a new repository on your local machine with `git init repro-examples`
2. Copy the files in the `problem` directory into the new repository
3. Download the data needed for the analysis from https://doi.org/10.5281/zenodo.7014332

## Section 1: Version control

Try to answer the following questions:

1. Which files should be tracked?
2. Are there any files in the project that should not be tracked?
3. Are there any files missing that are needed to run the analysis?

## Section 2: Dependencies

Try to answer the following questions:

1. What are the python dependencies for the analysis? 
2. What are the system dependencies?

Task: Document the dependencies that you find
Extension: Using your favourite dependency management tool (e.g. Conda, Nix),
create a reproducible environment configuration.

## Section 3: Automation

Tasks:

1. Create an automated pipeline for producing all the figures
2. Automate the fetching of the necessary data

## Section 4: Documentation

Tasks:

1. Create a README for the repository
2. Add comments and docstrings where you think is necessary

Extension: Use an documentation tool, such as Sphinx, to automate building the
documentation.

## Section 5: Try it out!

Tasks:

1. Share your repository with the person near you
2. Try to reproduce the results using the repo that you have been shared
