import pandas as pd
import numpy as np
from scipy import stats

# Load the cleaned dataset
df = pd.read_csv(r"C:\Users\New\AppData\Local\Programs\Python\Python310\Cleaned_Analytical_Dataset_N38.csv", encoding='utf-8-sig')
df.columns = df.columns.str.strip()

print("="*60)
print("RUNNING INFERENTIAL STATISTICS (N=38)")
print("="*60)

# --- HELPER: Map Likert scales to numeric values (1 to 5) ---
likert_map_conf = {
    'Not at all confident': 1, 'Slightly confident': 2, 'Moderately confident': 3, 
    'Very confident': 4, 'Extremely confident': 5
}
likert_map_fam = {
    'Not at all familiar': 1, 'Slightly familiar': 2, 'Moderately familiar': 3, 
    'Very familiar': 4, 'Extremely familiar': 5
}
likert_map_agree = {
    'Strongly disagree': 1, 'Disagree': 2, 'Neutral': 3, 'Agree': 4, 'Strongly agree': 5
}

# Map the columns
df['B6_numeric'] = df['B6.  How confident are you that these safeguards are followed consistently in practice?'].map(likert_map_conf)
df['A4_numeric'] = df["A4. How familiar are you with your organization's telehealth systems, workflows, or downtime procedures?"].map(likert_map_fam)

# Aggregate Adaptive Capacity (E3a, E3b, E3c) into a single score (3 to 15)
df['E3a_num'] = df['E3. Please indicate your agreement: [I feel able to make safe real-time decisions during telehealth disruptions.]'].map(likert_map_agree)
df['E3b_num'] = df['E3. Please indicate your agreement: [My organization supports flexible but safe responses when systems fail.]'].map(likert_map_agree)
df['E3c_num'] = df['E3. Please indicate your agreement: [After an incident, my organization reflects on what worked well as well what went wrong.]'].map(likert_map_agree)
df['E3_Total_Score'] = df['E3a_num'] + df['E3b_num'] + df['E3c_num']

# Binary Incident variable (1 if any incident selected besides "None of the above" or "Prefer not to say")
df['Incident_Yes_No'] = df['C1. In the past 24 months, to your knowledge, has your organization experienced any of the following? (Select all that apply)'].apply(
    lambda x: 1 if pd.notna(x) and 'None of the above' not in str(x) and 'Prefer not to say' not in str(x) else 0
)

# Binary Org Type (Public vs. Non-Public)
df['Org_Public'] = df['A2. In what type of organization do you primarily work? (Select one)'].apply(
    lambda x: 1 if 'Public' in str(x) else 0
)

# Binary Downtime Procedures (Yes vs. No/Don't Know)
df['B5_Yes'] = df['B5. Are offline, fallback, or downtime procedures available when primary telehealth systems fail?'].apply(
    lambda x: 1 if str(x).strip() == 'Yes' else 0
)

# Drop NaNs for specific tests
df_stats = df.dropna(subset=['A4_numeric', 'B6_numeric', 'E3_Total_Score', 'Incident_Yes_No'])

# --- TEST 1: Spearman's Rank Correlation (Familiarity vs. Confidence) ---
rho, p_val_1 = stats.spearmanr(df_stats['A4_numeric'], df_stats['B6_numeric'])
print(f"\n1. Spearman's Correlation: Familiarity (A4) vs. Confidence (B6)")
print(f"   Correlation Coefficient (rs): {rho:.3f}")
print(f"   p-value: {p_val_1:.4f}")
print(f"   Result: {'Significant' if p_val_1 < 0.05 else 'Not significant'} (p < 0.05)")

# --- TEST 2: Mann-Whitney U Test (Incident Experience vs. Adaptive Capacity) ---
group_no_incident = df_stats[df_stats['Incident_Yes_No'] == 0]['E3_Total_Score']
group_incident = df_stats[df_stats['Incident_Yes_No'] == 1]['E3_Total_Score']
u_stat, p_val_2 = stats.mannwhitneyu(group_no_incident, group_incident, alternative='two-sided')
print(f"\n2. Mann-Whitney U Test: Incident Experience vs. Adaptive Capacity Score")
print(f"   U-statistic: {u_stat:.3f}")
print(f"   p-value: {p_val_2:.4f}")
print(f"   Result: {'Significant' if p_val_2 < 0.05 else 'Not significant'} (p < 0.05)")

# --- TEST 3: Fisher's Exact Test (Public Org vs. Downtime Procedures) ---
# Create contingency table
contingency_table = pd.crosstab(df['Org_Public'], df['B5_Yes'])
# Fisher's exact test requires a 2x2 table. If it's larger, we use Chi-square, but let's force 2x2 logic.
# 0=Non-Public, 1=Public. 0=No/Unsure, 1=Yes.
try:
    oddsratio, p_val_3 = stats.fisher_exact(contingency_table)
    test_name = "Fisher's Exact Test"
except ValueError:
    chi2, p_val_3, dof, expected = stats.chi2_contingency(contingency_table)
    test_name = "Chi-Square Test"
    oddsratio = "N/A"

print(f"\n3. {test_name}: Public Organization vs. Availability of Downtime Procedures")
print(f"   Contingency Table:\n{contingency_table}")
print(f"   p-value: {p_val_3:.4f}")
print(f"   Result: {'Significant' if p_val_3 < 0.05 else 'Not significant'} (p < 0.05)")

print("\n" + "="*60)
print("Copy the p-values and statistics above into your Chapter 4 text.")
print("="*60)
import pandas as pd
import numpy as np
from scipy import stats

# Load the cleaned dataset
df = pd.read_csv(r"C:\Users\New\AppData\Local\Programs\Python\Python310\Cleaned_Analytical_Dataset_N38.csv", encoding='utf-8-sig')
df.columns = df.columns.str.strip()

print("="*60)
print("RUNNING INFERENTIAL STATISTICS (N=38)")
print("="*60)

# --- HELPER: Map Likert scales to numeric values (1 to 5) ---
likert_map_conf = {
    'Not at all confident': 1, 'Slightly confident': 2, 'Moderately confident': 3, 
    'Very confident': 4, 'Extremely confident': 5
}
likert_map_fam = {
    'Not at all familiar': 1, 'Slightly familiar': 2, 'Moderately familiar': 3, 
    'Very familiar': 4, 'Extremely familiar': 5
}
likert_map_agree = {
    'Strongly disagree': 1, 'Disagree': 2, 'Neutral': 3, 'Agree': 4, 'Strongly agree': 5
}

# Map the columns
df['B6_numeric'] = df['B6.  How confident are you that these safeguards are followed consistently in practice?'].map(likert_map_conf)
df['A4_numeric'] = df["A4. How familiar are you with your organization's telehealth systems, workflows, or downtime procedures?"].map(likert_map_fam)

# Aggregate Adaptive Capacity (E3a, E3b, E3c) into a single score (3 to 15)
df['E3a_num'] = df['E3. Please indicate your agreement: [I feel able to make safe real-time decisions during telehealth disruptions.]'].map(likert_map_agree)
df['E3b_num'] = df['E3. Please indicate your agreement: [My organization supports flexible but safe responses when systems fail.]'].map(likert_map_agree)
df['E3c_num'] = df['E3. Please indicate your agreement: [After an incident, my organization reflects on what worked well as well what went wrong.]'].map(likert_map_agree)
df['E3_Total_Score'] = df['E3a_num'] + df['E3b_num'] + df['E3c_num']

# Binary Incident variable (1 if any incident selected besides "None of the above" or "Prefer not to say")
df['Incident_Yes_No'] = df['C1. In the past 24 months, to your knowledge, has your organization experienced any of the following? (Select all that apply)'].apply(
    lambda x: 1 if pd.notna(x) and 'None of the above' not in str(x) and 'Prefer not to say' not in str(x) else 0
)

# Binary Org Type (Public vs. Non-Public)
df['Org_Public'] = df['A2. In what type of organization do you primarily work? (Select one)'].apply(
    lambda x: 1 if 'Public' in str(x) else 0
)

# Binary Downtime Procedures (Yes vs. No/Don't Know)
df['B5_Yes'] = df['B5. Are offline, fallback, or downtime procedures available when primary telehealth systems fail?'].apply(
    lambda x: 1 if str(x).strip() == 'Yes' else 0
)

# Drop NaNs for specific tests
df_stats = df.dropna(subset=['A4_numeric', 'B6_numeric', 'E3_Total_Score', 'Incident_Yes_No'])

# --- TEST 1: Spearman's Rank Correlation (Familiarity vs. Confidence) ---
rho, p_val_1 = stats.spearmanr(df_stats['A4_numeric'], df_stats['B6_numeric'])
print(f"\n1. Spearman's Correlation: Familiarity (A4) vs. Confidence (B6)")
print(f"   Correlation Coefficient (rs): {rho:.3f}")
print(f"   p-value: {p_val_1:.4f}")
print(f"   Result: {'Significant' if p_val_1 < 0.05 else 'Not significant'} (p < 0.05)")

# --- TEST 2: Mann-Whitney U Test (Incident Experience vs. Adaptive Capacity) ---
group_no_incident = df_stats[df_stats['Incident_Yes_No'] == 0]['E3_Total_Score']
group_incident = df_stats[df_stats['Incident_Yes_No'] == 1]['E3_Total_Score']
u_stat, p_val_2 = stats.mannwhitneyu(group_no_incident, group_incident, alternative='two-sided')
print(f"\n2. Mann-Whitney U Test: Incident Experience vs. Adaptive Capacity Score")
print(f"   U-statistic: {u_stat:.3f}")
print(f"   p-value: {p_val_2:.4f}")
print(f"   Result: {'Significant' if p_val_2 < 0.05 else 'Not significant'} (p < 0.05)")

# --- TEST 3: Fisher's Exact Test (Public Org vs. Downtime Procedures) ---
# Create contingency table
contingency_table = pd.crosstab(df['Org_Public'], df['B5_Yes'])
# Fisher's exact test requires a 2x2 table. If it's larger, we use Chi-square, but let's force 2x2 logic.
# 0=Non-Public, 1=Public. 0=No/Unsure, 1=Yes.
try:
    oddsratio, p_val_3 = stats.fisher_exact(contingency_table)
    test_name = "Fisher's Exact Test"
except ValueError:
    chi2, p_val_3, dof, expected = stats.chi2_contingency(contingency_table)
    test_name = "Chi-Square Test"
    oddsratio = "N/A"

print(f"\n3. {test_name}: Public Organization vs. Availability of Downtime Procedures")
print(f"   Contingency Table:\n{contingency_table}")
print(f"   p-value: {p_val_3:.4f}")
print(f"   Result: {'Significant' if p_val_3 < 0.05 else 'Not significant'} (p < 0.05)")

print("\n" + "="*60)
print("Copy the p-values and statistics above into your Chapter 4 text.")
print("="*60)
