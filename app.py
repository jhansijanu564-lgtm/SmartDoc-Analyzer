import streamlit as st
from PIL import Image
import pytesseract
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A5, LETTER, LEGAL
from io import BytesIO
import os
st.set_page_config(
    page_title="SmartDoc",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)
if "menu" not in st.session_state:
    st.session_state.menu = "Home"
if "pages" not in st.session_state:
    st.session_state.pages = []
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "show_login" not in st.session_state:
    st.session_state.show_login = False
if "show_signup" not in st.session_state:
    st.session_state.show_signup = False
tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
if os.path.exists(tesseract_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fff8fb;
    }
    .block-container {
        max-width: 1200px;
        padding-top: 1.5rem;
    }
    h1, h2, h3 {
        color: #222222;
    }
    .pink {
        color: #e83e8c;
    }
    div.stButton > button {
        border-radius: 10px;
        font-weight: 600;
    }
    div.stButton > button:hover {
        border-color: #e83e8c;
        color: #e83e8c;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .top-navigation {
        background: white;
        border-bottom: 2px solid #f8d7e5;
        padding: 14px 25px;
        margin: -1rem -1rem 30px -1rem;
        min-height: 70px;
    }
    .smartdoc-brand {
        font-size: 28px;
        font-weight: 800;
        color: #222222;
        white-space: nowrap;
        padding-top: 8px;
    }
    .smartdoc-brand span {
        color: #e83e8c;
    }
    .smartdoc-subtitle {
        font-size: 12px;
        color: #777777;
        margin-top: -4px;
    }
    div.stButton > button {
        height: 42px;
        border-radius: 10px;
        border: 1px solid #f3c4d8;
        background: white;
        color: #333333;
        font-weight: 600;
        font-size: 14px;
        white-space: nowrap;
    }

    div.stButton > button:hover {
        background: #ffe4f0;
        border-color: #e83e8c;
        color: #e83e8c;
    }

    .login-button div.stButton > button {
        border: 2px solid #e83e8c;
        color: #e83e8c;
    }

    
    .signup-button div.stButton > button {
        background: #e83e8c;
        color: white;
        border: 2px solid #e83e8c;
    }

    .signup-button div.stButton > button:hover {
        background: #d63384;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

nav1, nav2, nav3, nav4, nav5, nav6, nav7 = st.columns(
    [2.8, 1.0, 1.2, 1.0, 1.2, 1.0, 1.1],
    vertical_alignment="center"
)

with nav1:
    st.markdown(
        """
        <div class="smartdoc-brand">
            🅂 Smart<span>Doc</span>
        </div>
        <div class="smartdoc-subtitle">
            Document Intelligence
        </div>
        """,
        unsafe_allow_html=True
    )

with nav2:
    home_button = st.button(
        "🏠 Home",
        key="nav_home"
    )

with nav3:
    pdf_button = st.button(
        "📄 PDF Tools",
        key="nav_pdf"
    )

with nav4:
    ocr_button = st.button(
        "⌗ OCR",
        key="nav_ocr"
    )

with nav5:
    convert_button = st.button(
        "🔄 Convert",
        key="nav_convert"
    )

with nav6:
    login_button = st.button(
        "Login",
        key="nav_login"
    )

with nav7:
    signup_button = st.button(
        "Sign Up",
        key="nav_signup"
    )

if st.session_state.show_login:

    st.title("🔐 Login")

    st.write("Sign in to continue using SmartDoc.")

    email = st.text_input(
        "Email address",
        key="login_email"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    login_col1, login_col2 = st.columns(2)

    with login_col1:
        if st.button("Login", key="login_submit"):
            if email and password:
                st.session_state.logged_in = True
                st.session_state.show_login = False
                st.success("Login successful!")
                st.rerun()
            else:
                st.warning("Please enter your email and password.")

    with login_col2:
        if st.button("Close", key="login_close"):
            st.session_state.show_login = False
            st.rerun()

elif st.session_state.show_signup:

    st.title("📝 Create your SmartDoc Account")

    st.write("Create an account to use SmartDoc.")

    name = st.text_input(
        "Full Name",
        key="signup_name"
    )

    email = st.text_input(
        "Email address",
        key="signup_email"
    )

    password = st.text_input(
        "Create Password",
        type="password",
        key="signup_password"
    )

    signup_col1, signup_col2 = st.columns(2)

    with signup_col1:
        if st.button("Create Account", key="signup_submit"):

            if name and email and password:

                st.success(
                    "Account created successfully!"
                )

                st.session_state.show_signup = False
                st.rerun()

            else:
                st.warning(
                    "Please fill in all fields."
                )

    with signup_col2:
        if st.button("Close", key="signup_close"):
            st.session_state.show_signup = False
            st.rerun()

elif st.session_state.menu == "Home":

    st.title("Your Documents.")
    st.header("Simplified.")

    st.write(
        "Convert, organize, extract and manage "
        "your documents in one simple workspace."
    )

    st.write(
        "**Convert • Extract • Organize • Create**"
    )

    st.divider()

    st.subheader("📤 Start with your document")

    st.write(
        "Upload an image or document and choose "
        "what you want to do with it."
    )

    uploaded_home_files = st.file_uploader(
        "Choose files",
        type=["jpg", "jpeg", "png", "pdf"],
        accept_multiple_files=True,
        key="home_file_upload"
    )

    st.caption(
        "Maximum 200MB per file • JPG • JPEG • PNG • PDF"
    )

    st.write(
        "You can also drag and drop your files into the box above."
    )

    st.divider()

    st.header("✨ Popular Tools")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📝 Image → Text")
        st.write(
            "Extract text from images using OCR."
        )

        if st.button(
            "Use Tool",
            key="home_tool_ocr"
        ):
            st.session_state.menu = "OCR"
            st.rerun()


    with col2:
        st.subheader("📄 Text → PDF")
        st.write(
            "Create PDF documents from your text."
        )

        if st.button(
            "Use Tool",
            key="home_tool_text_pdf"
        ):
            st.session_state.menu = "Text PDF"
            st.rerun()


    with col3:
        st.subheader("🖼️ Image → PDF")
        st.write(
            "Convert images into PDF documents."
        )

        if st.button(
            "Use Tool",
            key="home_tool_image_pdf"
        ):
            st.session_state.menu = "Image PDF"
            st.rerun()


    col4, col5, col6 = st.columns(3)

    with col4:
        st.subheader("📚 Multiple Images → PDF")
        st.write(
            "Combine and manage multiple pages."
        )

        if st.button(
            "Use Tool",
            key="home_tool_multiple_pdf"
        ):
            st.session_state.menu = "Multiple PDF"
            st.rerun()


    with col5:
        st.subheader("🔄 Convert")
        st.write(
            "Convert documents between formats."
        )

        if st.button(
            "Use Tool",
            key="home_tool_convert"
        ):
            st.session_state.menu = "Convert"
            st.rerun()


    with col6:
        st.subheader("🛠️ More Tools")
        st.write(
            "More SmartDoc features coming soon."
        )

        if st.button(
            "Explore",
            key="home_tool_more"
        ):
            st.session_state.menu = "PDF Tools"
            st.rerun()


    st.divider()
    st.header("⚡ How SmartDoc Works")

    step1, step2, step3 = st.columns(3)

    with step1:
        st.subheader("1️⃣ Choose")
        st.write(
            "Choose the document tool you need."
        )

    with step2:
        st.subheader("2️⃣ Upload")
        st.write(
            "Upload your image or enter your text."
        )

    with step3:
        st.subheader("3️⃣ Create")
        st.write(
            "Create and download your document."
        )

    st.info(
        "💡 Select a tool above to get started!"
    )

elif st.session_state.menu == "OCR":

    st.title("📝 Image → Text")

    st.write(
        "Upload an image and SmartDoc will extract "
        "the text from it."
    )

    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"],
        key="ocr_file_upload"
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        if st.button(
            "🔍 Extract Text",
            key="ocr_extract"
        ):

            try:

                text = pytesseract.image_to_string(image)

                if text.strip():

                    st.subheader("📝 Extracted Text")

                    st.text_area(
                        "Text found:",
                        text,
                        height=300,
                        key="ocr_result"
                    )

                else:

                    st.warning(
                        "No text was found in this image."
                    )

            except Exception as error:

                st.error(
                    "OCR could not run. "
                    "Please check that Tesseract OCR is installed."
                )




elif st.session_state.menu == "Text PDF":

    st.title("📄 Text → PDF")

    st.write(
        "Enter your text below and create a PDF document."
    )

    pdf_text = st.text_area(
        "Enter your text:",
        height=300,
        key="text_pdf_input"
    )

    if st.button(
        "📄 Generate PDF",
        key="generate_text_pdf"
    ):

        if not pdf_text.strip():

            st.warning(
                "Please enter some text first."
            )

        else:

            pdf_buffer = BytesIO()

            c = canvas.Canvas(
                pdf_buffer,
                pagesize=A4
            )

            text_object = c.beginText(
                50,
                800
            )

            text_object.setFont(
                "Helvetica",
                12
            )

            for line in pdf_text.split("\n"):

                text_object.textLine(line)

                if text_object.getY() < 50:

                    c.drawText(text_object)
                    c.showPage()

                    text_object = c.beginText(
                        50,
                        800
                    )

                    text_object.setFont(
                        "Helvetica",
                        12
                    )

            c.drawText(text_object)
            c.save()

            pdf_buffer.seek(0)

            st.success(
                "Your PDF has been created!"
            )

            st.download_button(
                "⬇️ Download PDF",
                data=pdf_buffer,
                file_name="smartdoc_text.pdf",
                mime="application/pdf",
                key="download_text_pdf"
            )


elif st.session_state.menu == "Image PDF":

    st.title("🖼️ Image → PDF")

    st.write(
        "Upload an image and convert it into a PDF document."
    )

    image_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"],
        key="image_pdf_file"
    )

    if image_file is not None:

        image = Image.open(
            image_file
        ).convert("RGB")

        st.image(
            image,
            caption="Selected Image",
            use_container_width=True
        )

        if st.button(
            "📄 Convert Image to PDF",
            key="convert_image_pdf"
        ):

            pdf_buffer = BytesIO()

            image.save(
                pdf_buffer,
                format="PDF"
            )

            pdf_buffer.seek(0)

            st.success(
                "Image converted to PDF successfully!"
            )

            st.download_button(
                "⬇️ Download PDF",
                data=pdf_buffer,
                file_name="smartdoc_image.pdf",
                mime="application/pdf",
                key="download_image_pdf"
            )



elif st.session_state.menu == "Multiple PDF":

    st.title("📚 Multiple Images → PDF")

    st.write(
        "Upload multiple images and arrange them as pages "
        "before creating your PDF."
    )

    image_files = st.file_uploader(
        "Choose multiple images",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="multiple_pdf_upload"
    )

    if image_files:

        if not st.session_state.pages:

            for image_file in image_files:

                image = Image.open(
                    image_file
                ).convert("RGB")

                st.session_state.pages.append(
                    image
                )

    st.write(
        f"📄 Number of pages: {len(st.session_state.pages)}"
    )


   
    page_size = st.selectbox(
        "📄 Page Size",
        ["A4", "A5", "Letter", "Legal"],
        key="page_size"
    )

    orientation = st.selectbox(
        "↔️ Orientation",
        ["Portrait", "Landscape"],
        key="page_orientation"
    )


    if page_size == "A4":
        selected_size = A4

    elif page_size == "A5":
        selected_size = A5

    elif page_size == "Letter":
        selected_size = LETTER

    else:
        selected_size = LEGAL


    if orientation == "Landscape":

        selected_size = (
            selected_size[1],
            selected_size[0]
        )


   

    for i, page in enumerate(
        st.session_state.pages
    ):

        st.image(
            page,
            caption=f"Page {i + 1}",
            use_container_width=True
        )

        page_col1, page_col2, page_col3, page_col4 = st.columns(4)


        with page_col1:

            if st.button(
                "⬆️ Move Up",
                key=f"move_up_{i}"
            ):

                if i > 0:

                    pages = st.session_state.pages

                    pages[i - 1], pages[i] = (
                        pages[i],
                        pages[i - 1]
                    )

                    st.rerun()


        with page_col2:

            if st.button(
                "⬇️ Move Down",
                key=f"move_down_{i}"
            ):

                if i < len(st.session_state.pages) - 1:

                    pages = st.session_state.pages

                    pages[i], pages[i + 1] = (
                        pages[i + 1],
                        pages[i]
                    )

                    st.rerun()


        with page_col3:

            if st.button(
                "📋 Duplicate",
                key=f"duplicate_page_{i}"
            ):

                st.session_state.pages.insert(
                    i + 1,
                    page.copy()
                )

                st.rerun()


        with page_col4:

            if st.button(
                "🗑️ Delete",
                key=f"delete_page_{i}"
            ):

                st.session_state.pages.pop(i)

                st.rerun()



    if st.session_state.pages:

        rotate_page = st.selectbox(
            "🔄 Select page to rotate",
            list(
                range(
                    1,
                    len(st.session_state.pages) + 1
                )
            ),
            key="rotate_page_select"
        )

        if st.button(
            "🔄 Rotate Selected Page",
            key="rotate_selected_page"
        ):

            index = rotate_page - 1

            st.session_state.pages[index] = (
                st.session_state.pages[index]
                .rotate(
                    90,
                    expand=True
                )
            )

            st.rerun()


    

    if st.session_state.pages:

        if st.button(
            "📄 Create PDF",
            key="create_multiple_pdf"
        ):

            pdf_buffer = BytesIO()

            c = canvas.Canvas(
                pdf_buffer,
                pagesize=selected_size
            )

            page_width, page_height = selected_size


            for page in st.session_state.pages:

                image_buffer = BytesIO()

                page.save(
                    image_buffer,
                    format="JPEG"
                )

                image_buffer.seek(0)

                from reportlab.lib.utils import ImageReader

                image_reader = ImageReader(
                    image_buffer
                )

                image_width, image_height = page.size

                scale = min(
                    page_width / image_width,
                    page_height / image_height
                )

                draw_width = image_width * scale
                draw_height = image_height * scale

                x = (
                    page_width - draw_width
                ) / 2

                y = (
                    page_height - draw_height
                ) / 2

                c.drawImage(
                    image_reader,
                    x,
                    y,
                    width=draw_width,
                    height=draw_height
                )

                c.showPage()


            c.save()

            pdf_buffer.seek(0)

            st.success(
                "Your PDF has been created successfully!"
            )

            st.download_button(
                "⬇️ Download PDF",
                data=pdf_buffer,
                file_name="smartdoc_pages.pdf",
                mime="application/pdf",
                key="download_multiple_pdf"
            )


    if st.button(
        "🗑️ Clear All Pages",
        key="clear_all_pages"
    ):

        st.session_state.pages = []

        st.rerun()



elif st.session_state.menu == "Convert":

    st.title("🔄 Convert")

    st.write(
        "Choose a document conversion tool."
    )

    st.subheader("Available Conversions")

    st.write("🖼️ JPG → PDF")
    st.write("📄 Text → PDF")
    st.write("📚 Multiple Images → PDF")
    st.write("📑 PDF → Images")

    st.info(
        "More document conversion options will be added soon."
    )

elif st.session_state.menu == "PDF Tools":

    st.header("📄 PDF Tools")

    st.write(
        "Manage and edit your PDF documents."
    )

    st.subheader("🔀 Merge PDF")

    st.write(
        "Upload multiple PDF files and combine them "
        "into one PDF document."
    )

    pdf_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True,
        key="merge_pdf_files"
    )

    if pdf_files:

        st.write(
            f"📄 {len(pdf_files)} PDF file(s) selected."
        )

        for i, pdf_file in enumerate(pdf_files):
            st.write(
                f"{i + 1}. {pdf_file.name}"
            )

        if st.button(
            "🔀 Merge PDFs",
            key="merge_pdfs_button"
        ):

            from PyPDF2 import PdfMerger

            merger = PdfMerger()

            for pdf_file in pdf_files:
                merger.append(pdf_file)

            merged_path = "merged_document.pdf"

            with open(
                merged_path,
                "wb"
            ) as output_file:

                merger.write(output_file)

            merger.close()

            st.success(
                "✅ PDFs merged successfully!"
            )

            with open(
                merged_path,
                "rb"
            ) as file:

                st.download_button(
                    "⬇️ Download Merged PDF",
                    data=file,
                    file_name="merged_document.pdf",
                    mime="application/pdf",
                    key="download_merged_pdf"
                )

    st.info(
        "More PDF tools will be added soon."
    )
st.divider()

st.caption("📄 SmartDoc")
st.caption("Your Document & PDF Workspace")
st.caption(
    "© 2026 SmartDoc Analyzer • Convert • Extract • Organize • Create"
)