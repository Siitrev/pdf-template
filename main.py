from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")



pdf = FPDF(orientation="P", unit="mm", format="A4")

for index,row in df.iterrows():
    pages_num = int(row["Pages"])
    
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1)
    pdf.line(10,23,200,23)
    for _ in range(pages_num-1):
        pdf.add_page()
        
    
    


pdf.output("output.pdf")