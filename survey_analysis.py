import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set academic/professional plotting style
sns.set_theme(style="whitegrid", font="sans-serif", rc={"axes.labelsize": 12, "xtick.labelsize": 11, "ytick.labelsize": 11})
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']

# Total sample size for percentage calculations
N = 38

def save_figure(fig, filename):
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved: {filename}")

# ==============================================================================
# FIGURE 4.1: Professional Roles of Respondents
# ==============================================================================
roles = ['Clinical providers', 'Health informatics/digital health leads', 
         'IT/cybersecurity professionals', 'Clinical managers/administrators', 
         'Risk/quality/compliance officers', 'Medical engineers', 
         'Public health professionals', 'Midwives']
counts_4_1 = [20, 5, 4, 4, 2, 1, 1, 1]

plt.figure(figsize=(10, 6))
bars = plt.barh(roles, counts_4_1, color='#4C72B0')
plt.xlabel('Number of Respondents (n)')
plt.gca().invert_yaxis() # Highest count at the top

# Add count labels on bars
for bar in bars:
    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, 
             str(int(bar.get_width())), va='center', fontsize=10)

save_figure(plt, "Figure_4_1_Roles.png")


# ==============================================================================
# FIGURE 4.2: Telehealth Utilization
# ==============================================================================
utilization_cats = ['< 10%', '10 - 25%', '26 - 50%', '51 - 75%', '> 75%', 'Don\'t know']
counts_4_2 = [12, 7, 9, 3, 6, 1]
colors_4_2 = ['#4C72B0', '#55A868', '#C44E52', '#8172B2', '#CCB974', '#64B5CD']

plt.figure(figsize=(8, 6))
bars = plt.bar(utilization_cats, counts_4_2, color=colors_4_2)
plt.ylabel('Number of Respondents (n)')
plt.ylim(0, 15)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f"n={int(yval)}\n({(yval/N)*100:.1f}%)", 
             ha='center', va='bottom', fontsize=9)

save_figure(plt, "Figure_4_2_Utilization.png")


# ==============================================================================
# FIGURE 4.3: Availability of Security Controls (Stacked Bar)
# ==============================================================================
controls = ['Data Encryption', 'Multi-Factor Auth (MFA)', 'Downtime Procedures', 
            'Backup Systems', 'Network Segmentation']
yes = [28, 26, 20, 20, 18]
no = [2, 7, 7, 8, 7]
unsure = [8, 5, 11, 10, 10]
na = [0, 0, 0, 0, 3] # Only Segmentation has N/A

x = np.arange(len(controls))
width = 0.6

fig, ax = plt.subplots(figsize=(10, 6))
p1 = ax.bar(x, yes, width, label='Yes', color='#55A868')
p2 = ax.bar(x, no, width, bottom=yes, label='No', color='#C44E52')
p3 = ax.bar(x, unsure, width, bottom=np.array(yes)+np.array(no), label='Unsure', color='#CCB974')
p4 = ax.bar(x, na, width, bottom=np.array(yes)+np.array(no)+np.array(unsure), label='N/A', color='#64B5CD')

ax.set_ylabel('Number of Respondents (n)')
ax.set_xticks(x)
ax.set_xticklabels(controls, rotation=15, ha='right')
ax.legend(loc='upper right')

# Add total N labels on top
for i, total in enumerate(np.array(yes)+np.array(no)+np.array(unsure)+np.array(na)):
    ax.text(i, total + 0.2, f"n={int(total)}", ha='center', fontsize=9)

save_figure(fig, "Figure_4_3_Security_Controls.png")


# ==============================================================================
# FIGURE 4.4: Confidence in Existing Safeguards
# ==============================================================================
confidence_cats = ['Not at all confident', 'Slightly confident', 'Moderately confident', 
                   'Very confident', 'Extremely confident']
counts_4_4 = [5, 8, 12, 10, 3]
colors_4_4 = ['#C44E52', '#E69A4C', '#CCB974', '#55A868', '#4C72B0']

plt.figure(figsize=(8, 6))
bars = plt.bar(confidence_cats, counts_4_4, color=colors_4_4)
plt.ylabel('Number of Respondents (n)')
plt.ylim(0, 15)
plt.xticks(rotation=20, ha='right')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, f"n={int(yval)}\n({(yval/N)*100:.1f}%)", 
             ha='center', va='bottom', fontsize=9)

save_figure(plt, "Figure_4_4_Confidence.png")


# ==============================================================================
# FIGURE 4.5: Cybersecurity Incidents Experienced (Past 24 Months)
# ==============================================================================
incidents = ['None of the above', 'Cloud/platform outages', 'Ransomware attacks', 
             'Compromise of connected devices', 'Data breaches', 'Prefer not to say']
counts_4_5 = [25, 8, 3, 3, 1, 5] # Note: Multiple choice, so total > 38

plt.figure(figsize=(10, 6))
bars = plt.barh(incidents, counts_4_5, color='#4C72B0')
plt.xlabel('Number of Responses (n)')
plt.gca().invert_yaxis()

for bar in bars:
    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, 
             f"n={int(bar.get_width())} ({(bar.get_width()/N)*100:.1f}%)", va='center', fontsize=10)

save_figure(plt, "Figure_4_5_Incidents.png")


# ==============================================================================
# FIGURE 4.6: Perceived Threats to Telehealth Systems
# ==============================================================================
# Combined "Very concerned" and "Extremely concerned"
threats = ['Staff errors', 'System outages', 'Compromise of connected devices', 
           'Breach of patient data', 'Third-party vendor failure', 'Ransomware disrupting platforms']
counts_4_6 = [15, 14, 14, 14, 11, 7]

plt.figure(figsize=(10, 6))
bars = plt.barh(threats, counts_4_6, color='#C44E52')
plt.xlabel('Number of Respondents (n) with High Concern')
plt.gca().invert_yaxis()

for bar in bars:
    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, 
             f"n={int(bar.get_width())} ({(bar.get_width()/N)*100:.1f}%)", va='center', fontsize=10)

save_figure(plt, "Figure_4_6_Threats.png")


# ==============================================================================
# FIGURE 4.7: Consequences of Telehealth Disruptions on Patient Care
# ==============================================================================
consequences = ['Delayed clinical decision-making', 'Delayed consultations', 
                'Communication problems with patients', 'Repeat assessment or data entry', 
                'Communication problems among staff', 'Missed consultations', 
                'No major effect observed', 'Increased patient safety concern', 'Not sure']
counts_4_7 = [18, 17, 15, 12, 10, 9, 8, 7, 6]

plt.figure(figsize=(10, 7))
bars = plt.barh(consequences, counts_4_7, color='#55A868')
plt.xlabel('Number of Respondents (n)')
plt.gca().invert_yaxis()

for bar in bars:
    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, 
             f"n={int(bar.get_width())} ({(bar.get_width()/N)*100:.1f}%)", va='center', fontsize=10)

save_figure(plt, "Figure_4_7_Consequences.png")


# ==============================================================================
# FIGURE 4.8: Organizational Responses During Disruptions
# ==============================================================================
responses = ['Document manually & enter data later', 'Seek immediate technical support', 
             'Use paper or manual workarounds', 'Reschedule consultation', 
             'Use alternative digital platform', 'Escalate to supervisor/incident lead', 
             'Switch to telephone', 'Did not know']
counts_4_8 = [19, 19, 17, 11, 10, 9, 6, 1]

plt.figure(figsize=(10, 7))
bars = plt.barh(responses, counts_4_8, color='#8172B2')
plt.xlabel('Number of Respondents (n)')
plt.gca().invert_yaxis()

for bar in bars:
    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, 
             f"n={int(bar.get_width())} ({(bar.get_width()/N)*100:.1f}%)", va='center', fontsize=10)

save_figure(plt, "Figure_4_8_Responses.png")


# ==============================================================================
# FIGURE 4.9: Primary Barriers to Improving Telehealth Resilience
# ==============================================================================
barriers = ['Technical complexity', 'Shortage of cybersecurity staff', 'Insufficient budget', 
            'Limited staff training', 'Competing clinical priorities', 'Dependence on third-party vendors', 
            'Weak downtime procedures', 'Staff resistance to security procedures', 'Lack of leadership awareness']
counts_4_9 = [23, 22, 21, 18, 14, 14, 14, 12, 11]

plt.figure(figsize=(10, 7))
bars = plt.barh(barriers, counts_4_9, color='#E69A4C')
plt.xlabel('Number of Respondents (n)')
plt.gca().invert_yaxis()

for bar in bars:
    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2, 
             f"n={int(bar.get_width())} ({(bar.get_width()/N)*100:.1f}%)", va='center', fontsize=10)

save_figure(plt, "Figure_4_9_Barriers.png")

print("\nAll 9 figures have been successfully generated and saved as PNG files without titles!")
