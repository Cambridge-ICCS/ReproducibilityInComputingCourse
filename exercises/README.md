# Exercises in reproducibility

After going through the slides on how to make our research projects reproducible,
it is time to go through a practice scenario!

The code in `problem/` is an example of a research project which has not taken 
reproducibility into account.

## Data

The scripts rely on the HadCRUT.5.0.0.0 dataset, available from
https://www.metoffice.gov.uk/hadobs/hadcrut5/data/HadCRUT.5.0.0.0/download.html

Only the "HadCRUT5 analysis time series: ensemble means and uncertainties"
NetCDF files are needed:

- `HadCRUT.5.0.0.0_analysis_summary-series_global_annual.nc`
- `HadCRUT.5.0.0.0_analysis_summary-series_northern-hemisphere_annual.nc`
- `HadCRUT.5.0.0.0_analysis_summary-series_southern-hemisphere_annual.nc`
- `HadCRUT.5.0.0.0_analysis_summary-series_global_monthly.nc`

Download these four files from the "Summary series" table (NetCDF → Annual/Monthly per region),
and place them in a `data/` directory next to the `problem/` scripts, so the
scripts can find them automatically.
This is better that downloading the whole dataset which is rather large!

## Instructions:

1. Create a new repository on your local machine with `git init repro-examples`
2. Copy the files in the `problem` directory into the new repository
3. Download the four NetCDF files listed above into a `data/` directory next to the scripts
4. Work through the exercise files in order.
   During the workshop the slides will tell you when to tackle each one.
   - `01_version_control_exercises.qmd` - version control
   - `02_dependencies_exercises.qmd` - dependencies
   - `03_automation_exercises.qmd` - automation
   - `04_testing_exercises.qmd` - testing
   - `05_documentation_exercises.qmd` - documentation
   - `06_final_exercises.qmd` - try it all out

   Some tasks are achievable during the session, others are "Extension" tasks that
   could be worked on in your own time.
