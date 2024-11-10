from datetime import datetime
from tkinter import filedialog
from CustomTkinterMessagebox import CTkMessagebox
from docling.document_converter import DocumentConverter


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
        print(self.source_filename)
        self.conversion()
        return self.source_filename

    def conversion(self):
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

        # source = "/content/ocred.pdf"  # PDF path or URL

        # create destination path
        source_str = self.source_filename.split(sep="/")
        # grab only the first part of the filepath to be used as destination
        source_str_destination = "/".join(source_str[0:-1])
        print("Source string destination:", source_str_destination)
        converter = DocumentConverter()
        result = converter.convert(self.source_filename)
        markdown_out = result.document.export_to_markdown()
        with open(
            f"{source_str_destination}/md_conversion_{timestamp}.md",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(markdown_out)

        CTkMessagebox.messagebox(
            "Conversion to .md",
            "Conversion PDF -> .md completed 🎉\n Find your result in the same folder as the input file.",
        )
