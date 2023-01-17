from fpdf import FPDF
import pandas as pd


df = pd.read_csv("topics.csv")



pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index,row in df.iterrows():
    pages_num = int(row["Pages"])
    
    pdf.add_page()
    
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0,0,0)
    pdf.cell(w=0,h=12,txt=row["Topic"],align="L",ln=1)
    pdf.line(10,20,200,20)
    
    lines_num = (297-21)//10
    
    for i in range(30,297,10):
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
        
    
    


pdf.output("output.pdf")