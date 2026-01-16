import webview
import doc_gen.Excel2PDF
import doc_gen.stapler

class CompilerAPI:
    def __init__(self):
        self.window = None

    def test(self):
        print("Button Pressed")

    def set_window(self, window):
        self.window = window

    def select_file(self):
        """Opens a file dialog and returns the selected .xlsx path."""
        file_types = ('Excel Files (*.xlsm;*.xls)', 'All files (*.*)')
        result = self.window.create_file_dialog(webview.FileDialog.OPEN, file_types=file_types)
        return result[0] if result else ""

    def select_folder(self):
        """Opens a folder dialog and returns the selected directory path."""
        result = self.window.create_file_dialog(webview.FileDialog.FOLDER)
        return result[0] if result else ""
    
    def compile(self, data):
        print(data)
        #Extract inputs from JS
        excel_path = str(data['excel_path'])
        calc_pdf_folder = str(data['calc_pdf_folder'])
        swap_folder = str(data['swap_folder'])
        print_excel_flag = bool(data['print_excel_flag'])                                
        swap_reports_flag = bool(data['swap_reports_flag'])
        
        # print excel
        if print_excel_flag: 
            #Empty directory
            doc_gen.Excel2PDF.empty_directory(calc_pdf_folder)

            #Print excel to pdf
            doc_gen.Excel2PDF.export_sheets_to_pdf(excel_path)

        # swap
        if swap_reports_flag: doc_gen.Excel2PDF.swap(swap_folder, calc_pdf_folder)

        # staple
        doc_gen.stapler.staple(calc_pdf_folder)




def main():
    api = CompilerAPI()
    window = webview.create_window("ZFA Calc Compiler by Owen Hodges", "index.html", js_api=api, width=800, height=600)
    api.set_window(window)

    webview.start(debug=False)

if __name__ == "__main__":
    main()