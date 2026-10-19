import fpdf
def main():
    name = input("Name: ")
    pdf = fpdf.FPDF()
    pdf = fpdf.FPDF(orientation = "portrait", format = "A4")
    pdf.add_page()
    
    pdf.image("shirtificate.png", x = fpdf.Align.C, y = 60 )
    
    image_size = 593 / 2
    half = abs(pdf.epw - image_size) / 2  
    
    pdf.set_font("Helvetica", size=30, style="B")

    pdf.text(half, 40, "CS50 SHIRTIFICATE")
    
    pdf.set_font("Helvetica", size = 35)
    pdf.set_text_color(255, 255, 255)

    text = f"{name} took CS50"
    text_width = pdf.get_string_width(text)

    pdf.text(abs((half - (text_width / 4))) + text_width / 4, 170, text)
    pdf.output("result1.pdf")

if __name__ == "__main__":
    main() 