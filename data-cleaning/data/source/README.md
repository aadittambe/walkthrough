# Post and Courier web app

The South Carolina Department of Education publishes School and District Report Cards each year on [this](https://screportcards.ed.sc.gov/) website. The report cards include information about each school and school district, including test performances, teacher qualifications, student, student safety, awards and parent involvement. 

The government site primarily allows users to review one institution at a time, or compare a few institutions that they (users) choose. We would like to produce an app that will allow Post & Courier staff to examine this data in a more exploratory manner.

Features might include, for example, the ability to examine academic performance across South Carolina when schools are grouped by region, racial makeup or percentage of students receiving free or reduced lunch. The design for this app will be functional more than aesthetic. It will allow reporters without extensive statistical background to identify trends and outliers that can lead to compelling stories about education in South Carolina.


## GitHub folder structure and code environments

- We will use git for version control and collaboration. This is an overview of the repository folder structure, which draws inspiration from the AP Datakit and Howard Center projects.

	```
    +-- analysis
    | +-- etl
    | +-- final-scripts
    +-- data
      +-- source
      +-- processed
      +-- testing
    +--visualizations
    | +-- external-app
    | +-- internal-tool

	```

- Explanation of directory structure:
    - The `analysis` directory will include our scripts which will clean, analyze and process the raw data. 
    - Preliminary analysis will be done in the `analysis/etl` directory. This will include R / Jupyter notebooks we use to testing any code.
    - Once we have gotten our code to work, we can generate a clean and heavily-commented notebook and store that in the `analysis/final-scripts` directory.
    - All data files — raw and processed — can be stored in the `data` directory.
    - The `data/source` directory will include files that we download directly. Be sure to not open these files in Microsoft Excel, as this can cause data distortion.
    - Data files that we are testing out, but are not completely processed to be uploaded to the final app, can be stored in the `data/test` directory.
    - Data files that are processed and cleaned can be stored in the `data/processed` directory.
    - Depending on which framework we choose, code files that power the two web apps — the news app and the internal analysis tool — can be stores in the `visualizations/external-tool` and `visualizations/internal-tool` directories.