# CLPsych18

Code for the submission to the [CLPsych 2018 Shared Task](http://clpsych.org/shared-task-2018/), described in [this paper](Radford-CLPsych2018-final.pdf).

Caveats:
* This is very much research code, get in touch if you're having problems running it.
* This requires the official task data, get in touch with the shared task organisers for access.

## Installation

```bash
python3 -m venv .env
source .env/bin/activate
pip install -U pip wheel
pip install -r requirements.txt
python -m spacy download en
```

## Notebooks

1. [Data exploration](0-Data-exploration.ipynb)
1. [Preparing data.ipynb](1-Preparing-data.ipynb)
1. [Train models](2-Train-models.ipynb)
1. [Make test predictions](3-Make-test-predictions.ipynb)
1. [EXPERIMENTAL Feature Selection](4-Feature-Selection.ipynb)
1. [EXPERIMENTAL fastText features](5-fastText-features.ipynb)
1. [Analysis](6-Analysis.ipynb)
1. [Fairness](7-Fairness.ipynb)
1. [ROC for triage scenario](8-ROC-for-triage-analysis.ipynb)
