# COMPAS Notebook Report
Generated: 2025-12-04T13:08:26.892651Z

## 1) Dataset
- Original dataframe (df) shape: (7214, 12)
- Features used (X) shape: (7214, 11)
- Training set: (5771, 11)
- Testing set: (1443, 12)
- Encoded protected attribute: `race` (encoding map available)

## 2) Preprocessing
- Several irrelevant or duplicate columns were dropped.
- Object/string race values were normalized and encoded into integers.
- Label encoding applied to remaining categorical columns.

## 3) Model
- Model: LogisticRegression
- Test accuracy: 0.9757 (higher values indicate good overall classification accuracy)
- Note: accuracy alone can hide subgroup performance disparities.

## 4) Fairness evaluation (AIF360)
Computed metrics (where available):
- Disparate Impact Ratio: 1.3781262057595847
- Mean Difference: 0.14600912895667129
- Equal Opportunity Difference: 0.0
- Theil Index: 0.0

Interpretation:
- Disparate Impact close to 1.0 suggests parity in favorable outcome rates; deviations indicate potential disparate treatment.
- Mean difference and equal opportunity difference near 0.0 indicate low group-level bias in these aspects.
- Theil index summarizes prediction distribution inequality.

## 5) Group-level performance (by race)
False Positive Rates (FPR) by race:
  - Other (0): 0.0182
  - African-American (1): 0.0501
  - Caucasian (2): 0.0312
  - Hispanic (3): 0.0361
  - Native American (4): 0.5000
  - Asian (5): 0.2500

True Positive Rates (TPR / Sensitivity) by race:
  - Other (0): 1.0000
  - African-American (1): 0.9973
  - Caucasian (2): 1.0000
  - Hispanic (3): 1.0000
  - Native American (4): 1.0000
  - Asian (5): 1.0000

Observation:
- Even with high overall accuracy, FPR and TPR vary across race groups. This indicates disparate impact in error types across protected groups.

## 6) Key findings
- The trained logistic regression achieves very high test accuracy (0.9757) on this split.
- There are measurable differences in false positive rates across races (see section 5), which may disadvantage certain groups despite overall accuracy.
- Some fairness metrics (disparate impact, mean difference) indicate mild bias in favorability; equal opportunity difference and Theil index may be low depending on the fold.

## 7) Recommendations
- Report both overall metrics and per-group metrics (FPR, TPR, precision, recall) for transparency.
- Consider mitigation strategies:
  - Preprocessing: reweighing (AIF360 Reweighing is already available).
  - In-processing: use fairness-aware training algorithms (e.g., constrained optimization).
  - Post-processing: calibrate or adjust decision thresholds per group ensuring legal/ethical compliance.
- Validate fairness on multiple random splits / cross-validation folds to ensure stability.
- If deploying, gather stakeholder input and perform impact assessments for affected groups.

## 8) Next steps (code pointers)
- Apply AIF360 Reweighing on the training dataset and retrain the classifier.
- Evaluate fairness-aware algorithms available in AIF360 / Fairlearn.
- Produce per-group confusion matrices and visualize distributions (ROC, calibration).

---

This file summarizes the preprocessing, modeling, and fairness analysis performed in the notebook. For reproducibility, rerun the notebook cells in order and then regenerate this report.

