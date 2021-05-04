# fair-child

Welcome to `fair-child`, a project to investigate the fairness of machine learning approaches to predicting the risks of stillborn and pre-term pregnancies. This work is co-authored by Bradley Yam, Cove Geary, and Ivy Fan. We conducted this study for Yale's _CPSC 464, Topics in Foundations of Machine Learning_ with Professor Nisheeth Vishnoi.

## Report

You may find our final report, as well as some supporting slides, in the `report/` directory of this repo.

The remainder of this README is dedicated to outlining the steps that any practitioner/researcher may take to replicate or extend our results.

# Replication

## Data

Data was downloaded from the CDC's Vital Statistics Online Data Portal: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm#Fetal_Death, and the NBER’s Vital Statistics Natality Birth Data: https://www.nber.org/research/data/vital-statistics-natality-birth-data. Original data is stored in the `data/cdc` directory, and processed data is saved to `data/final`.

The original and processed data may also be found at the following Google Drive folder: https://drive.google.com/drive/folders/1N2pb4aAj3M_1Z948yiaYni8AZsBU7VCo?usp=sharing

## Dependencies

This project makes use of both R and Python, so it will be important to be particularly careful with dependencies management and interoperability.

For Python, you may wish to use a (venv)[https://docs.python.org/3/library/venv.html], Conda environment, or other virtualenvironment. Then, Python dependencies are listed in `requirements.txt` and may be installed with the following, once the Python environment is sourced.

```bash
$ pip install -r requirements.txt
```

For R, we require the following packages: `tidyverse`, `data.table`, `pROC`, `naniar`, `caret`, `fakeR`, `ggthemes`; as well as `reticulate`, which provides Python interoperability. For package versions, here is the call to `utils::sessionInfo()` on one machine:

```
R version 4.0.5 (2021-03-31)
Platform: x86_64-pc-linux-gnu (64-bit)
Running under: Arch Linux

Matrix products: default
BLAS:   /usr/lib/libopenblasp-r0.3.14.so
LAPACK: /usr/lib/liblapack.so.3.9.1

locale:
 [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C               LC_TIME=en_US.UTF-8       
 [4] LC_COLLATE=en_US.UTF-8     LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
 [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                  LC_ADDRESS=C              
[10] LC_TELEPHONE=C             LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       

attached base packages:
[1] stats     graphics  grDevices utils     datasets  methods   base     

other attached packages:
 [1] ggcorrplot_0.1.3  reticulate_1.18   fakeR_1.0         ggthemes_4.2.4    caret_6.0-86     
 [6] lattice_0.20-41   naniar_0.6.0      data.table_1.14.0 magrittr_2.0.1    forcats_0.5.1    
[11] stringr_1.4.0     dplyr_1.0.5       purrr_0.3.4       readr_1.4.0       tidyr_1.1.3      
[16] tibble_3.1.0      ggplot2_3.3.3     tidyverse_1.3.0  

loaded via a namespace (and not attached):
 [1] nlme_3.1-152         fs_1.5.0             lubridate_1.7.10     httr_1.4.2           rprojroot_2.0.2     
 [6] tools_4.0.5          backports_1.2.1      utf8_1.2.1           R6_2.5.0             rpart_4.1-15        
[11] DBI_1.1.1            colorspace_2.0-0     nnet_7.3-15          withr_2.4.1          tidyselect_1.1.0    
[16] compiler_4.0.5       polycor_0.7-10       cli_2.3.1            rvest_1.0.0          xml2_1.3.2          
[21] scales_1.1.1         mvtnorm_1.1-1        digest_0.6.27        rmarkdown_2.7        pscl_1.5.5          
[26] pkgconfig_2.0.3      htmltools_0.5.1.1    dbplyr_2.1.0         rlang_0.4.10         readxl_1.3.1        
[31] rstudioapi_0.13      VGAM_1.1-5           generics_0.1.0       jsonlite_1.7.2       ModelMetrics_1.2.2.2
[36] Matrix_1.3-2         Rcpp_1.0.6           munsell_0.5.0        fansi_0.4.2          lifecycle_1.0.0     
[41] visdat_0.5.3         stringi_1.5.3        pROC_1.17.0.1        yaml_2.2.1           MASS_7.3-53.1       
[46] plyr_1.8.6           recipes_0.1.15       grid_4.0.5           crayon_1.4.1         haven_2.3.1         
[51] splines_4.0.5        hms_1.0.0            knitr_1.31           pillar_1.5.1         reshape2_1.4.4      
[56] codetools_0.2-18     stats4_4.0.5         reprex_1.0.0         glue_1.4.2           evaluate_0.14       
[61] modelr_0.1.8         vctrs_0.3.6          foreach_1.5.1        cellranger_1.1.0     gtable_0.3.0        
[66] assertthat_0.2.1     xfun_0.22            gower_0.2.2          prodlim_2019.11.13   broom_0.7.5         
[71] class_7.3-18         survival_3.2-10      timeDate_3043.102    iterators_1.0.13     lava_1.6.9          
[76] ellipsis_0.3.1       ipred_0.9-11
```

## Usage

All of our code lives in `/src/`. If you are running a Unix system everything should run fine, but if you are on Windows you may need to alter bits of code that references the os package. If you want to run training on a gpu, some of the activation functions may need to be tweaked for different versions of tensorflow. 

### Data Ingestion and Exploration

We provide detailed sources for our data in the final report. We have uploaded our own copy of the raw data downloaded directly from CDC and NBER in our google drive. Download data files and place them into appropriate folder structure before running `ingest-clean-realdata.Rmd`

Alternatively, our processed data files are also available on the same drive link in `/data/`. The datasets in the drive are under `data v2/final`.

We provide some directions for data exploration in `synthetic-data-exploration.Rmd`, but the user is encouraged to explore the dataset for themselves.

### Model Training

We provide a jupyter notebook `train-all-models.ipynb` to train all the models for our study, including 12 "race-aware" models and 12 "race-unaware" models.

Alternatively, we also provide all our models pre-trained for download from the drive link in `/models/`.

### Model Evaluation and Vizualisation

We provide code to evaluate the fairness of our models with respect to race on the metrics of TPR, FPR and accuracy in `fairness-eval.Rmd` and provide some helpful visualizations of those metrics in `Viz.Rmd`


## Steps

All code to replicate this project may be found in `src/`. We proceed through the source code via the following steps:

1. **Data Processing and Cleaning.** The CDC natality data is stored in a difficult-to-use “fixed-width” format, so we parse the file into tabular format. We then clean the data, dropping NAs, normalizing continuous variables, and renaming columns.
    * `src/ingest-clean-realdata.Rmd`: Parses CDC and NBER data from all years and combines into one large .csv file.
    * `src/preprocess-realdata_i.R`: Processes the reformatted natality data. Split into four files for memory management reasons; run in order from `i=0` to `3`.

2. **Model Training and Saving.** We provide a small library of Python functions to train, save and load all model objects, as well as a Python notebook to train all models.
    * `src/models.py`: Methods to train, save, and load all models. Neural networks are Tensorflow/Keras models, while logistic regression and LightGBM models are scikit-learn models. If you want to run training on a GPU, some of the activation functions may need to be tweaked for different versions of tensorflow. (Do not need to run this; is sourced by model training.)
    * `src/util.py`: Methods to load training data for the sake of model training. (Do not need to run this; is sourced by model training.)
    * `src/train-all-models.ipynb`: Notebook to train all models, for all tasks, both race-aware and race-unaware.

3. **Model Evaluation and Figures.**
    * `src/fairness-eval.Rmd`: Loads all trained models and evaluates them on TPR, FPR, AUC, TPR @ 10% FPR, Accuracy and Positivity.
    * `src/viz.Rmd`: Loads results and produces charts on model metrics and positivity rates. Also conducts correlation analysis on training data.
    * Compiled .pdf documents from these notebooks are also stored in `src/`.

4. _Future Directions._ We also began to explore model explainability via the Python LIME (library). We paused on this direction due to computational resources. However, preliminary work may be found in `src/lime.ipynb`.

## Models

Trained models are saved to the `models/` directory. Our trained models may be downloaded at the following Google Drive folder: https://drive.google.com/drive/folders/1zffp0o-E9EimBu-9snC-0L9_4mGU3AtA?usp=sharing.
