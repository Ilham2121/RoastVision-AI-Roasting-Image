import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Set up model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to generate roast based on image
def generate_roast(image, style, language):
    try:
        prompt_templates = {
            "b aja": "Berikut adalah gambar yang perlu kamu kritik dengan gaya roasting yang lucu dan ringan. Buatlah kritikan yang jenaka tapi sopan, fokus pada elemen visual dalam gambar.",
            "lumayan": "Berikut adalah gambar yang perlu kamu roast dengan gaya yang sarkastik dan lucu. Buatlah roasting yang cukup pedas tapi tidak terlalu kasar, fokus pada elemen visual dalam gambar.",
            "kena mental": "Berikut adalah gambar yang perlu kamu roast dengan gaya yang sangat sarkastik dan pedas. Buatlah roasting yang tajam dan menusuk tapi tetap lucu, fokus pada elemen visual dalam gambar."
        }
        
        language_instructions = {
            "indonesia": "Berikan respons dalam Bahasa Indonesia.",
            "english": "Provide the response in English.",
            "sunda": "Berikan respons dalam Bahasa sunda dengan gaya bercanda khas sunda."
        }
        
        prompt = f"{prompt_templates[style]} {language_instructions[language]}"
        
        response = model.generate_content([prompt, image])
        return response.text
    except Exception as e:
        return f"Error saat menghasilkan roast: {str(e)}"

# Main app
def main():
    st.set_page_config(page_title="RoastVision", page_icon="🔥")
    
    st.title("RoastVision 🔥")
    st.markdown("Upload gambar untuk mendapatkan 'roasting' pedas!")
    
    # Sidebar for settings
    with st.sidebar:
        st.header("Pengaturan")
        roast_style = st.select_slider(
            "Mau di roasting kaya gimana?",
            options=["b aja", "lumayan", "kena mental"],
            value="lumayan"
        )
        
        language = st.radio(
            "Bahasa",
            options=["indonesia", "english", "sunda"],
            index=0
        )
        
        st.markdown("---")
        st.markdown("### Tentang RoastVision")
        st.markdown("""
        RoastVision menggunakan AI untuk memberikan kritik humoris pada gambar.
        Aplikasi ini dibuat hanya untuk keperluan hiburan dan tidak bermaksud menyinggung siapapun.

        Powered by Google Gemini API.
        """)
        
        # Menambahkan hak cipta dengan logo dan link
        st.markdown("---")
        st.markdown("### Dibuat oleh:")

        # Custom CSS untuk styling link
        st.markdown("""
            <style>
                .social-links {
                    display: flex;
                    gap: 10px;
                    align-items: center;
                }
                .social-links a {
                    display: flex;
                    align-items: center;
                    text-decoration: none;
                    color: black;
                    font-weight: bold;
                    transition: 0.3s;
                }
                .social-links a:hover {
                    color: #2b8cf0;
                }
                .social-links img {
                    width: 25px;
                    margin-right: 5px;
                }
            </style>
        """, unsafe_allow_html=True)
                
        # Link GitHub & Instagram dengan ikon
        st.markdown("""
            <div class="social-links">
                <a href="https://github.com/Ilham2121" target="_blank">
                    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png">
                    GitHub: Ilham2121
                </a>
                <a href="https://instagram.com/ilhaamaly_" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg">
                    Instagram: ilhaamaly_
                </a>
            </div>
        """, unsafe_allow_html=True)
    
    # Hanya menampilkan opsi upload gambar
    uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar Terupload", use_column_width=True)
        
        if st.button("Roast Gambar Ini!", key="roast_upload"):
            with st.spinner("AI sedang menyiapkan roastingan..."):
                result = generate_roast(image, roast_style, language)
                st.markdown("### Hasil Roasting:")
                st.markdown(f">{result}")
                
                # Opsi untuk berbagi
                st.markdown("---")
                st.markdown("### Bagikan Roasting Ini")
                share_text = f"Saya baru saja di-roast oleh AI di RoastVision! 🔥"
                st.markdown(f'<a href="https://twitter.com/intent/tweet?text={share_text}" target="_blank"><button style="background-color:#1DA1F2; color:white; border:none; padding:10px; border-radius:5px;">Bagikan ke Twitter</button></a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main() 