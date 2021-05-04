# fair-child

_In development._

## Motivation

The motivation and report for our project is detailed in our project report https://github.com/bradleyyam/fair-child/blob/master/CPSC_464_Fairness_in_Birth_Outcomes_Final.pdf, along with the paper we are referencing and detailed explanations for the decisions that we made in data cleaning and model training.

## Development

This project makes use of both R and Python, so we will need to be extra careful with dependencies management and interoperability.

### Python setup

For Python, I've been working in a virtual environment titled "venv" in the root directory of this project. Create one with:

```bash
$ python -m venv venv
```

To execute anything Python-related from the command line, source the virtual environment first.

```bash
$ source venv/bin/activate
```

To install the same packages across machines, run (after having sourced the venv):

```bash
$ pip install -r requirements.txt
```

Or to save a new dependencies list:

```bash
$ pip freeze > requirements.txt
```

If the pip install doesn't work, I believe that all the packages used for now are: `numpy`, `pandas`, `tensorflow`, `scikit-learn`, and `lightgbm`.

### R setup

For our R scripts and mixed R/Python scripts, RStudio is an editor and interpreter. We currently require the `tidyverse`, `caret`, and `fakeR` packages, as well as `reticulate`, which provides Python interoperability.

For package versions, here is the call to `utils::sessionInfo()` on one machine:

```
R version 4.0.4 (2021-02-15)
Platform: x86_64-pc-linux-gnu (64-bit)

...abridged...

attached base packages:
[1] stats     graphics  grDevices utils     datasets  methods   base     

other attached packages:
 [1] reticulate_1.18 forcats_0.5.1   stringr_1.4.0   dplyr_1.0.4     purrr_0.3.4     readr_1.4.0     tidyr_1.1.2    
 [8] tibble_3.0.6    tidyverse_1.3.0 fakeR_1.0       caret_6.0-86    ggplot2_3.3.3   lattice_0.20-41

loaded via a namespace (and not attached):
 [1] Rcpp_1.0.6           lubridate_1.7.9.2    mvtnorm_1.1-1        class_7.3-18         assertthat_0.2.1    
 [6] rprojroot_2.0.2      ipred_0.9-11         foreach_1.5.1        cellranger_1.1.0     R6_2.5.0            
[11] plyr_1.8.6           backports_1.2.1      reprex_1.0.0         stats4_4.0.4         httr_1.4.2          
[16] pillar_1.4.7         rlang_0.4.10         readxl_1.3.1         pscl_1.5.5           rstudioapi_0.13     
[21] data.table_1.13.6    rpart_4.1-15         Matrix_1.3-2         splines_4.0.4        gower_0.2.2         
[26] munsell_0.5.0        broom_0.7.5          compiler_4.0.4       modelr_0.1.8         pkgconfig_2.0.3     
[31] nnet_7.3-15          tidyselect_1.1.0     prodlim_2019.11.13   polycor_0.7-10       codetools_0.2-18    
[36] crayon_1.4.1         dbplyr_2.1.0         withr_2.4.1          MASS_7.3-53          recipes_0.1.15      
[41] ModelMetrics_1.2.2.2 grid_4.0.4           nlme_3.1-152         jsonlite_1.7.2       gtable_0.3.0        
[46] lifecycle_1.0.0      DBI_1.1.1            magrittr_2.0.1       pROC_1.17.0.1        scales_1.1.1        
[51] cli_2.3.0            stringi_1.5.3        reshape2_1.4.4       fs_1.5.0             timeDate_3043.102   
[56] xml2_1.3.2           ellipsis_0.3.1       generics_0.1.0       vctrs_0.3.6          lava_1.6.9          
[61] iterators_1.0.13     tools_4.0.4          glue_1.4.2           hms_1.0.0            survival_3.2-7      
[66] colorspace_2.0-0     rvest_0.3.6          VGAM_1.1-5           haven_2.3.1
```

## Usage

All of our code lives in /src/. If you are running a Unix system everything should run fine, but if you are on Windows you may need to alter bits of code that references the os package. If you want to run training on a gpu, some of the activation functions may need to be tweaked for different versions of tensorflow. 

### Data Ingestion and Exploration

We provide detailed sources for our data in the final report. We have uploaded our own copy of the raw data downloaded directly from CDC and NBER in our google drive. Download data files and place them into appropriate folder structure before running 'ingest-clean-realdata.Rmd'

Alternatively, our processed data files are also available on the same drive link in /data/

We provide some directions for data exploration in 'synthetic-data-exploration.Rmd', but the user is encouraged to explore the dataset for themselves.

### Model Training

We provide a jupyter notebook 'train-all-models.ipynb' to train all the models for our study, including 12 "race-aware" models and 12 "race-unaware" models.

Alternatively, we also provide all our models pre-trained for download from the drive link in /models/

### Model Evaluation and Vizualisation

We provide code to evaluate the fairness of our models with respect to race on the metrics of TPR, FPR and accuracy in 'fairness-eval.Rmd' and provide some helpful visualizations of those metrics in 'Viz.Rmd'
