import pandas as pd
from fpdf import FPDF

# Load the enhanced CSV
df = pd.read_csv("D:/Programs/Python/Report Generator/student_scores.csv")


# Calculate overall statistics
overall_avg = df["Score"].mean()

# Calculate subject-wise averages
subject_avg = df.groupby("Subject")["Score"].mean().reset_index()

# Find top scorer per subject
top_scorers = df.loc[df.groupby("Subject")["Score"].idxmax()].reset_index(drop=True)

# Initialize PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "Student Performance Report", ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.ln(10)
pdf.cell(200, 10, f"Overall Average Score: {overall_avg:.2f}", ln=True)
pdf.ln(5)

# Subject-wise average
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, "Subject-wise Average Score:", ln=True)
pdf.set_font("Arial", '', 12)
for index, row in subject_avg.iterrows():
    pdf.cell(200, 10, f"{row['Subject']}: {row['Score']:.2f}", ln=True)

pdf.ln(5)

# Top Scorers per Subject
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, "Top Scorers Per Subject:", ln=True)
pdf.set_font("Arial", '', 12)
for index, row in top_scorers.iterrows():
    pdf.cell(200, 10, f"{row['Name']} - {row['Subject']} ({row['Score']} marks)", ln=True)

pdf.ln(10)

# Individual Student Report
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, "Detailed Student Report:", ln=True)
pdf.set_font("Arial", '', 11)

# Table header
pdf.set_fill_color(200, 220, 255)
pdf.cell(40, 10, "Name", 1, 0, 'C', True)
pdf.cell(30, 10, "Subject", 1, 0, 'C', True)
pdf.cell(20, 10, "Score", 1, 0, 'C', True)
pdf.cell(20, 10, "Grade", 1, 0, 'C', True)
pdf.cell(80, 10, "Remarks", 1, 1, 'C', True)

# Table rows
for index, row in df.iterrows():
    pdf.cell(40, 10, row['Name'], 1)
    pdf.cell(30, 10, row['Subject'], 1)
    pdf.cell(20, 10, str(row['Score']), 1)
    pdf.cell(20, 10, row['Grade'], 1)
    pdf.cell(80, 10, row['Remarks'], 1)
    pdf.ln()

# Save PDF
pdf.output("enhanced_report.pdf")
print("✅ Enhanced report generated: enhanced_report.pdf")
