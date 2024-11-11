from datetime import datetime
from tkinter import filedialog, Tk
from CustomTkinterMessagebox import CTkMessagebox
import fitz  # PyMuPDF
import markdown2
import pypandoc


class Pdf2MD:
    """Class to convert a PDF containing mostly mathematical syntax to a markdown.
    The output will be then inserted into ChatGPT (or other AI models) to be converted
    more easily to a Latex code. The main advantage is that the GPT model can work better
    than having to extract first the content of a PDF and then convert it to a Latex file.
    In addition, the free ChatGPT version is able to convert only portions of a large PDF:
    the user runs out of the free tier very quickly.
    By using this method of first converting it to .md, ChatGPT runs much faster in converting
    the corresponding .md to Latex, giving a better final result.
    """

    def __init__(self) -> None:
        self.source_filename = None  # the file to be converted
        # self.root = Tk()

    def search_filename(self):
        """self.source_filename will contain the full path to the file

        Returns
        -------
        _type_
            _description_
        """
        # browse the PDF file to be opened
        self.source_filename = filedialog.askopenfilename(
            filetypes=[("PDF file", ".pdf")]
        )
        # print(self.source_filename)
        self.conv2md()
        # NOTE: for now, do not call the conversion to latex.
        # self.root.after(5000, self.convmd2latex)
        return self.source_filename

    def conv2md(self):
        # Open the PDF file
        pdf_path = self.source_filename
        doc = fitz.open(pdf_path)

        # Initialize a Markdown string to hold the document's content
        markdown_content = ""

        # Iterate over each page
        for page_num in range(doc.page_count):
            page = doc[page_num]  # Get the page
            blocks = page.get_text("blocks")  # Extract text as blocks

            # Add a page title in Markdown
            markdown_content += f"# Page {page_num + 1}\n\n"

            for block in blocks:
                # Each block is a tuple (x0, y0, x1, y1, "text", block_no, block_type)
                text = block[4]  # The text content of the block

                # Convert each block into a Markdown-friendly format
                markdown_content += (
                    f"{text}\n\n"  # Add block text followed by a newline
                )

        # create destination path
        source_str = self.source_filename.split(sep="/")
        # grab only the first part of the filepath to be used as destination
        source_str_destination = "/".join(source_str[0:-1])
        print("Source string destination:", source_str_destination)

        # Save to a Markdown file
        with open(
            f"{source_str_destination}/md_conversion.md",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(markdown_content)

        CTkMessagebox.messagebox(
            "Conversion to .md",
            "Conversion PDF -> .md completed 🎉\n Find your result in the same folder as the input file.",
        )

    def convmd2latex(self):
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        # create destination path
        source_str = self.source_filename.split(sep="/")
        # grab only the first part of the filepath to be used as destination
        source_str_destination = "/".join(source_str[0:-1])

        # Read the Markdown file
        with open(
            f"{source_str_destination}/md_conversion.md", "r", encoding="utf-8"
        ) as file:
            markdown_text = file.read()

        # Convert Markdown to HTML
        html_content = markdown2.markdown(markdown_text)
        pypandoc.download_pandoc()
        # Convert HTML to LaTeX using Pandoc
        latex_content = pypandoc.convert_text(html_content, to="latex", format="html")

        # Save to a .tex file
        with open(
            f"{source_str_destination}/tex_conversion_{timestamp}.tex",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(latex_content)

        CTkMessagebox.messagebox(
            "Conversion to .tex",
            "Conversion .md -> .tex completed 🎉\n Find your result in the same folder as the input file.",
        )
