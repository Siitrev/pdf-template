from fpdf import FPDF
import pandas as pd

# Read csv file with properties for each page
df = pd.read_csv("topics.csv")

# Generate FPDF object
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Create certain pages
for index,row in df.iterrows():
    pages_num = int(row["Pages"])
    
    pdf.add_page()
    
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0,0,0)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1)
    
    # Add lines
    for i in range(20,297,10):
        pdf.line(10,i,200,i)
    
    pdf.ln(266)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    
    for _ in range(pages_num-1):
        pdf.add_page()
        for i in range(10,297,10):
            pdf.line(10,i,200,i)
        pdf.ln(278)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        
# Output the file
pdf.output("output.pdf")