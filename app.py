import streamlit as st
from PIL import Image
import pytesseract
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A5, LETTER, LEGAL
st.set_page_config(
    page_title="SmartDoc Analyzer",
    page_icon="📊",
    layout="wide"
)
if "pages" not in st.session_state:
    st.session_state.pages = []
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
st.sidebar.title("📌 SmartDoc")
st.sidebar.write("Your PDF & Document Toolkit")

menu = st.sidebar.radio(
    "Choose a feature",
    [
        "🏠 Dashboard",
        "📝 Image → Text",
        "📄 Text → PDF",
        "🖼️ Image → PDF",
        "📚 Multiple Images → PDF"
    ]
)
st.markdown(
    "<h1 style='text-align: center;'>📊 SmartDoc Analyzer</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center;'>"
    "Document Intelligence & PDF Generator"
    "</h3>",
    unsafe_allow_html=True
)

if menu == "🏠 Dashboard":

    st.markdown(
        "<h3 style='text-align: center;'>"
        "👋 Welcome to SmartDoc!"
        "</h3>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align: center;'>"
        "Convert, edit, and manage your documents easily."
        "</p>",
        unsafe_allow_html=True
    )

    st.divider()

    st.subheader("✨ Available Features")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            "📝 **Image → Text**\n\n"
            "Extract text from images using OCR."
        )

        st.info(
            "📄 **Text → PDF**\n\n"
            "Convert typed text into a PDF document."
        )

    with col2:
        st.info(
            "🖼️ **Image → PDF**\n\n"
            "Convert an image into a PDF."
        )

        st.info(
            "📚 **Multiple Images → PDF**\n\n"
            "Combine multiple images into one PDF."
        )

    st.success(
        "💡 Select a feature from the left sidebar to get started."
    )

elif menu == "📝 Image → Text":

    st.header("📝 Image → Text")

    st.write(
        "Upload an image containing text and extract the text automatically."
    )

    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"],
        key="ocr_upload"
    )

    if uploaded_file is not None:

        st.success("Image uploaded successfully!")

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Document",
            use_container_width=True
        )

        if st.button("🔍 Extract Text"):

            text = pytesseract.image_to_string(image)

            if text.strip():

                st.subheader("📝 Extracted Text")

                st.text_area(
                    "Text found in image:",
                    text,
                    height=250
                )

            else:

                st.warning(
                    "No text was found in the image."
                )

    st.divider()

    try:

        version = pytesseract.get_tesseract_version()

        st.success(
            f"✅ Tesseract is connected! Version: {version}"
        )

    except Exception as e:

        st.error("❌ Tesseract is not connected.")

        st.write(e)
elif menu == "📄 Text → PDF":

    st.header("📄 Text → PDF")

    st.write(
        "Enter your text and convert it into a PDF document."
    )

    pdf_text = st.text_area(
        "Enter your text here:",
        height=300
    )

    if st.button("📄 Generate PDF"):

        pdf_path = "text_document.pdf"

        c = canvas.Canvas(pdf_path)

        text_object = c.beginText(50, 800)

        for line in pdf_text.split("\n"):

            text_object.textLine(line)

        c.drawText(text_object)

        c.save()

        with open(pdf_path, "rb") as file:

            st.download_button(
                label="⬇️ Download PDF",
                data=file,
                file_name="text_document.pdf",
                mime="application/pdf"
            )
elif menu == "🖼️ Image → PDF":

    st.header("🖼️ Image → PDF")

    st.write(
        "Upload an image and convert it into a PDF."
    )

    image_file = st.file_uploader(
        "Upload an image",
        type=["png", "jpg", "jpeg"],
        key="image_to_pdf"
    )

    if image_file is not None:

        image = Image.open(image_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        if st.button("📄 Convert Image to PDF"):

            pdf_path = "image_document.pdf"

            image.save(
                pdf_path,
                "PDF"
            )

            with open(pdf_path, "rb") as file:

                st.download_button(
                    label="⬇️ Download PDF",
                    data=file,
                    file_name="image_document.pdf",
                    mime="application/pdf"
                )

elif menu == "📚 Multiple Images → PDF":

    st.header("📚 Multiple Images → PDF")

    st.write(
        "Upload multiple images and manage them as PDF pages."
    )

    image_files = st.file_uploader(
        "Upload multiple images",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True,
        key="multiple_images"
    )

    if image_files and not st.session_state.pages:

        for image_file in image_files:

            image = Image.open(image_file).convert("RGB")

            st.session_state.pages.append(image)

    st.write(
        f"📄 {len(st.session_state.pages)} pages"
    )
    page_size = st.selectbox(
        "📄 Choose PDF Page Size",
        ["A4", "A5", "Letter", "Legal"]
    )

    if page_size == "A4":

        selected_size = A4

    elif page_size == "A5":

        selected_size = A5

    elif page_size == "Letter":

        selected_size = LETTER

    else:

        selected_size = LEGAL


    for i, page in enumerate(
        st.session_state.pages
    ):

        st.image(
            page,
            caption=f"Page {i + 1}",
            use_container_width=True
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            if st.button(
                "🗑️ Delete",
                key=f"delete_{i}"
            ):

                st.session_state.pages.pop(i)

                st.rerun()


        with col2:

            if st.button(
                "📋 Duplicate",
                key=f"duplicate_{i}"
            ):

                st.session_state.pages.insert(
                    i + 1,
                    page.copy()
                )

                st.rerun()


        with col3:

            if st.button(
                "🔄 Rotate",
                key=f"rotate_{i}"
            ):

                st.session_state.pages[i] = page.rotate(
                    90,
                    expand=True
                )

                st.rerun()



    if st.session_state.pages:

        st.divider()

        if st.button("📄 Create PDF"):

            pdf_path = "pages.pdf"

            c = canvas.Canvas(
                pdf_path,
                pagesize=selected_size
            )

            page_width, page_height = selected_size

            for page in st.session_state.pages:

                image_path = "temp_page.jpg"

                page.save(
                    image_path,
                    "JPEG"
                )

                c.drawImage(
                    image_path,
                    0,
                    0,
                    width=page_width,
                    height=page_height,
                    preserveAspectRatio=True,
                    anchor="c"
                )

                c.showPage()

            c.save()

            with open(pdf_path, "rb") as file:

                st.download_button(
                    "⬇️ Download PDF",
                    data=file,
                    file_name="pages.pdf",
                    mime="application/pdf"
                )