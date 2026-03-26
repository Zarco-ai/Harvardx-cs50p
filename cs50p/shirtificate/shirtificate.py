from fpdf import FPDF

# Define your custom class (Inheriting from FPDF)
class Shirtificate(FPDF):
    def header(self):
        # Set font to something bold and large
        self.set_font("Helvetica", "B", 45)
        # Create a cell that spans the page width to center the title
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        # Move the 'cursor' down so the image doesn't overlap the title
        self.ln(20)

def main():
    # Get the user's name
    name = input("Name: ")

    # Create the PDF object (Portrait, A4)
    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    # Add the page (This triggers the header method automatically!)
    pdf.add_page()
    # Place the Shirt Image
    pdf.image("shirtificate.png", x=10, y=70, w=190)
    # Overlay the User's Name
    pdf.set_font("Helvetica", size=25)
    pdf.set_text_color(255, 255, 255)
    # Move the 'cursor' to the chest area of the shirt
    pdf.y = 140
    pdf.cell(0, 10, f"{name} took CS50", align="C")
    # Save the file
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()



