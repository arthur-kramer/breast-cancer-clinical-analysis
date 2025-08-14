# Statistical Analysis of Breast Cancer Clinical Data

## 📌 Overview

This study hypothesizes that there are significant associations between patients’ diagnostic characteristics, including age, menopause status, tumor size, presence of invasive nodes, affected breast, metastasis status, breast quadrant, history of breast disease, and the breast cancer diagnosis outcome.

The dataset, with 213 patient observations, was obtained from the cancer registry of Calabar University Hospital over a 24-month period (January 2019 to August 2021). The data include eleven features: year of diagnosis, age, menopause status, tumor size in cm, number of invasive nodes, affected breast (left or right), metastasis (yes or no), affected breast quadrant, history of breast disease, and diagnosis outcome (benign or malignant).

Dataset source: [Kaggle – Breast Cancer Prediction](https://www.kaggle.com/datasets/fatemehmehrparvar/breast-cancer-prediction)

## 🎯 Objectives

- Assess the distribution and relationships of clinical variables.
- Perform normality tests for key continuous variables.
- Test hypotheses regarding associations between clinical features and diagnosis results.

## 📂 Dataset Description

| Variable            | Type       | Description |
|---------------------|------------|-------------|
| Year                | Numeric    | Year of diagnosis |
| Age                 | Numeric    | Patient's age in years |
| Menopause           | Categorical| Menopause status (Yes/No) |
| Tumor Size (cm)     | Numeric    | Tumor size in centimeters |
| Inv-Nodes           | Categorical| Number of invasive nodes |
| Breast              | Categorical| Affected breast (Left/Right) |
| Metastasis          | Categorical| Presence of metastasis (Yes/No) |
| Breast Quadrant     | Categorical| Affected breast quadrant |
| History             | Categorical| History of breast disease (Yes/No) |
| Diagnosis Result    | Categorical| Diagnosis outcome (Benign/Malignant) |

## 🛠️ Methodology

- Python Libraries: pandas, matplotlib, seaborn, scipy.stats
- Statistical Tests: Shapiro-Wilk (normality), Mann-Whitney U and Chi-Square (group comparisons)
- Exploratory Analysis: Histograms, boxplots, scatterplots, stacked bar charts

## 📊 Dataset Exploration

### **Histogram and Boxplot of Age**
<img width="1064" height="435" alt="image" src="https://github.com/user-attachments/assets/b26e7d6a-4e29-497c-b182-443613c0631d" />

### **Histogram and Boxplot of Tumor Size**
<img width="1064" height="436" alt="image" src="https://github.com/user-attachments/assets/aa3fd062-4688-491f-80bb-fc143675b0b4" />

### **Boxplot of Tumor Size by Diagnosis**
<img width="705" height="525" alt="image" src="https://github.com/user-attachments/assets/287fe51e-3f3a-4565-9d51-ed77a3317ce8" />

### **Boxplot of Age by Diagnosis**
<img width="705" height="525" alt="image" src="https://github.com/user-attachments/assets/02f15828-f409-4b38-8eaa-caf084109ff6" />

### **Boxplot of Tumor Size by Family History**
<img width="707" height="527" alt="image" src="https://github.com/user-attachments/assets/0e6f0f52-9525-4441-84f2-353f7d1cde34" />

### **Proportion of Family History by Diagnosis**
<img width="705" height="523" alt="image" src="https://github.com/user-attachments/assets/a0d7fd5c-b0d2-4ce1-8fdd-4c73f844e360" />

### **Proportion of Diagnosis by Menopause Status**
<img width="705" height="525" alt="image" src="https://github.com/user-attachments/assets/da3364a5-a84a-47b5-a9e6-df9f5e879ee5" />

### **Scatterplot between Age and Tumor Size by Diagnosis**
<img width="757" height="488" alt="image" src="https://github.com/user-attachments/assets/762bff53-fa9e-4853-aea4-b44094f45714" />

## 📈 Key Results

- Normality Tests: Age and tumor size are not normally distributed.
- Hypothesis 1: Tumor size differs significantly between benign and malignant diagnoses (p < 0.05).
- Hypothesis 2: Patient age differs significantly between benign and malignant diagnoses (p < 0.05).
- Hypothesis 3: Tumor size differs significantly between patients with and without family history of breast cancer (p < 0.05).
- Hypothesis 4: There is a significant association between family history and diagnostic outcome (p < 0.05).
- Hypothesis 5: There is a significant association between menopause status and diagnostic outcome. (p < 0.05).
