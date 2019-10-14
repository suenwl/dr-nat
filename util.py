import fitz
from PIL import Image
from IPython.display import clear_output, display


def convert_pdf_to_image(PDF_path):
    document = fitz.open(PDF_path, width=3307, height=4678)
    pages = []
    for page in document:
        zoom = 3
        mat = fitz.Matrix(
            zoom, zoom
        )  # This is done because getPixmap would otherwise pick the default resolution
        pix = page.getPixmap(matrix=mat)
        mode = "RGBA" if pix.alpha else "RGB"
        img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
        pages.append(img)
    return pages


def print_progress(current, total, text):
    percentage = round(current / total * 100, 1)
    done = "#" * int(float(str(percentage / 2)))
    todo = "-" * (50 - int(float(str(percentage / 2))))
    string = (
        "{text}<{display}>".format(text=text, display=done + todo)
        + " "
        + str(percentage)
        + "%"
    )
    clear_output(wait=True)
    print(string, end="")


category_mappings = {
    "Others": 0,
    "Account number": 1,
    "Consumption period": 2,
    "Country of consumption": 3,
    "Currency of invoice": 4,
    "Date of invoice": 5,
    "Invoice number": 6,
    "Name of provider": 7,
    "PO Number": 8,
    "Tax": 9,
    "Total amount": 10,
    0: "Others",
    1: "Account number",
    2: "Consumption period",
    3: "Country of consumption",
    4: "Currency of invoice",
    5: "Date of invoice",
    6: "Invoice number",
    7: "Name of provider",
    8: "PO Number",
    9: "Tax",
    10: "Total amount",
}


features_to_use = [
    # "char_count",
    # "word_count",
    # "height",
    # "width",
    # "dist_top",
    # "dist_left",
    # "dist_bottom",
    # "dist_right",
    # "dist_top_outer",
    # "dist_left_outer",
    # "dist_bottom_outer",
    # "dist_right_outer",
    # "rel_size_page_x",
    # "rel_size_page_y",
    # "average_dist_neighbours_pixel",
    # "average_dist_neighbours_rel",
    # "average_dist_N_nearest_neighbours_pixel",
    # "average_dist_N_nearest_neighbours_rel",
    # "percentile_width",
    # "percentile_height",
    "contains_date",
    "contains_currency",
    "contains_address",
    # "contains_num_label",
    # "contains_total_label",
    # "contains_amount_label",
    # "contains_date_label",
    # "contains_date_of_invoice_label",
    "contains_digit",
    "contains_company",
    # "contains_tax_label",
    # "vert_align_to_cell_w_date",
    # "vert_align_to_cell_w_currency",
    # "vert_align_to_cell_w_address",
    "vert_align_to_cell_w_datelabel",
    "vert_align_to_cell_w_dateofinvoicelabel",
    "vert_align_to_cell_w_numlabel",
    "vert_align_to_cell_w_totallabel",
    "vert_align_to_cell_w_amountlabel",
    # "vert_align_to_cell_w_digit",
    "vert_align_to_cell_w_invoicenum_label",
    "vert_align_to_cell_w_accountnum_label",
    "vert_align_to_cell_w_ponum_label",
    "vert_align_to_cell_w_tax_label",
    # "hori_align_to_cell_w_date",
    # "hori_align_to_cell_w_currency",
    # "hori_align_to_cell_w_address",
    "hori_align_to_cell_w_datelabel",
    "hori_align_to_cell_w_dateofinvoicelabel",
    "hori_align_to_cell_w_numlabel",
    "hori_align_to_cell_w_totallabel",
    "hori_align_to_cell_w_amountlabel",
    # "hori_align_to_cell_w_digit",
    "hori_align_to_cell_w_invoicenum_label",
    "hori_align_to_cell_w_accountnum_label",
    "hori_align_to_cell_w_ponum_label",
    "hori_align_to_cell_w_tax_label",
    # "rel_dist_nearest_cell_w_date",
    # "rel_dist_nearest_cell_w_currency",
    # "rel_dist_nearest_cell_w_address",
    "rel_dist_nearest_cell_w_datelabel",
    "rel_dist_nearest_cell_w_invoicedatelabel",
    "rel_dist_nearest_cell_w_numlabel",
    "rel_dist_nearest_cell_w_invoicenumlabel",
    "rel_dist_nearest_cell_w_accnumlabel",
    "rel_dist_nearest_cell_w_ponumlabel",
    "rel_dist_nearest_cell_w_totallabel",
    "rel_dist_nearest_cell_w_amountlabel",
    # "rel_dist_nearest_cell_w_digit",
    "rel_dist_nearest_cell_w_tax_label",
]
