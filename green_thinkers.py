import streamlit as st
import torch
from PIL import Image
import torchvision.transforms as transforms
from torchvision import models

# ----------------------------
# 🌿 Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Green Thinkers 🌱",
    page_icon="🌿",
    layout="wide"
)

# ----------------------------
# 🎨 Custom Styles
# ----------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #e8f5e9, #c8e6c9);
    font-family: "Segoe UI", sans-serif;
}
.card {
    background-color: #ffffff;
    border-radius: 15px;
    padding: 20px;
    margin: 10px 0;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
}
.risk-low {color: green; font-weight: bold;}
.risk-medium {color: orange; font-weight: bold;}
.risk-high {color: red; font-weight: bold;}
h1, h2, h3, h4 { color: #2e7d32; }
.sidebar .sidebar-content {
    background: linear-gradient(180deg, #a5d6a7, #81c784);
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# 🌿 Header
# ----------------------------
st.markdown("""
<h1 style='text-align:center;'>🌿 Green Thinkers</h1>
<h4 style='text-align:center;color:#388e3c;'>AI-Based Plant Disease Detection | एआई आधारित पौध रोग पहचान</h4>
""", unsafe_allow_html=True)
st.markdown("---")

# ----------------------------
# 🌐 Sidebar
# ----------------------------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2909/2909767.png", width=100)
st.sidebar.markdown("## 🌾 About")
st.sidebar.info("""
**Green Thinkers** is an AI-based agricultural assistant that helps farmers identify 
plant diseases and provides treatment, prevention, and seasonal awareness in **English and Hindi**.
""")

language = st.sidebar.radio(
    "Select Language / भाषा चुनें:",
    ("English", "हिन्दी")
)

# ----------------------------
# 📸 Upload Section
# ----------------------------
upload_text = "📷 Upload a Leaf Image" if language == "English" else "📷 पत्ती की छवि अपलोड करें"
uploaded_file = st.file_uploader(upload_text, type=["jpg", "jpeg", "png"])

# ----------------------------
# 🧠 Load Model
# ----------------------------
@st.cache_resource
def load_model():
    model = models.resnet18(pretrained=True)
    model.fc = torch.nn.Linear(model.fc.in_features, 10)
    model.eval()
    return model

model = load_model()

# ----------------------------
# 🌾 Disease Information
# ----------------------------
DISEASE_DATA_EN = {
    "Apple Scab": {
        "about": "Fungal disease caused by *Venturia inaequalis*, affecting apple leaves and fruits.",
        "symptoms": [
            "Olive-green or brown leaf spots",
            "Cracked fruit skin and distorted shape",
            "Premature leaf drop"
        ],
        "treatment": [
            "Spray Mancozeb or Captan every 10–15 days",
            "Prune infected branches",
            "Avoid overhead irrigation"
        ],
        "prevention": [
            "Ensure proper air circulation between trees",
            "Avoid dense planting",
            "Use resistant apple varieties"
        ],
        "season": "High risk during **spring and early summer** (March–June)",
        "risk": "🟡 Moderate"
    },
    "Apple Black Rot": {
        "about": "Caused by *Botryosphaeria obtusa*, leading to black leaf spots and fruit rot.",
        "symptoms": [
            "Dark circular spots with brown margins",
            "Mummified fruits remain on tree",
            "Cankers on bark"
        ],
        "treatment": [
            "Remove infected fruits and branches",
            "Apply copper-based fungicides",
            "Ensure airflow within canopy"
        ],
        "prevention": [
            "Avoid pruning during wet weather",
            "Disinfect tools after pruning",
            "Apply protective fungicides before rainfall"
        ],
        "season": "High risk during **monsoon and humid periods** (July–September)",
        "risk": "🔴 High"
    },
    "Healthy": {
        "about": "Your plant looks healthy! Keep maintaining good practices.",
        "symptoms": [
            "Green leaves with no spots",
            "Smooth fruit surface",
            "No wilting or yellowing"
        ],
        "treatment": ["No treatment required — continue routine care."],
        "prevention": [
            "Use organic compost",
            "Water plants early morning",
            "Keep monitoring for pests"
        ],
        "season": "All seasons safe 🌿",
        "risk": "🟢 Low"
    }
}

DISEASE_DATA_HI = {
    "एप्पल स्कैब": {
        "about": "*Venturia inaequalis* फफूंद से होने वाला रोग, जो पत्तियों और फलों को प्रभावित करता है।",
        "symptoms": [
            "पत्तियों पर जैतूनी या भूरे धब्बे",
            "फलों की त्वचा पर दरारें और विकृति",
            "संक्रमण से पत्तियाँ जल्दी झड़ जाती हैं"
        ],
        "treatment": [
            "हर 10–15 दिन में Mancozeb या Captan का छिड़काव करें",
            "संक्रमित शाखाएँ काटें",
            "ऊपर से पानी देने से बचें"
        ],
        "prevention": [
            "पेड़ों के बीच उचित दूरी रखें",
            "घनी बागवानी से बचें",
            "प्रतिरोधी किस्में लगाएँ"
        ],
        "season": "**वसंत और प्रारंभिक गर्मी** (मार्च–जून) के दौरान उच्च जोखिम",
        "risk": "🟡 मध्यम"
    },
    "एप्पल ब्लैक रॉट": {
        "about": "*Botryosphaeria obtusa* फफूंद से होने वाला रोग, जो पत्तियों और फलों को सड़ा देता है।",
        "symptoms": [
            "भूरे किनारे वाले गहरे धब्बे",
            "सूखे हुए फल पेड़ पर लटकते रहते हैं",
            "छाल पर घाव और दरारें"
        ],
        "treatment": [
            "संक्रमित फल और शाखाएँ हटाएँ",
            "कॉपर फफूंदनाशी छिड़कें",
            "पेड़ों में वायु संचार बनाए रखें"
        ],
        "prevention": [
            "बरसात में छंटाई से बचें",
            "उपकरणों को संक्रमणमुक्त करें",
            "बरसात से पहले फफूंदनाशी छिड़कें"
        ],
        "season": "**मानसून और आर्द्र मौसम** (जुलाई–सितंबर) में उच्च जोखिम",
        "risk": "🔴 उच्च"
    },
    "संपूर्ण स्वस्थ": {
        "about": "आपका पौधा स्वस्थ है! 🌿",
        "symptoms": ["पत्तियाँ हरी और चमकदार हैं", "कोई धब्बे नहीं दिखते", "फल सामान्य हैं"],
        "treatment": ["कोई उपचार आवश्यक नहीं।"],
        "prevention": [
            "जैविक खाद डालें",
            "सुबह जल्दी पानी दें",
            "कीटों की नियमित जांच करें"
        ],
        "season": "सभी मौसमों में सुरक्षित 🌿",
        "risk": "🟢 कम"
    }
}

# ----------------------------
# 🔍 Prediction Section
# ----------------------------
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="🌿 " + ("Uploaded Leaf" if language == "English" else "अपलोड की गई पत्ती"), use_column_width=True)

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(input_tensor)
        _, pred_idx = torch.max(outputs, 1)

    class_en = list(DISEASE_DATA_EN.keys())
    class_hi = list(DISEASE_DATA_HI.keys())
    pred_en = class_en[pred_idx.item() % len(class_en)]
    pred_hi = class_hi[pred_idx.item() % len(class_hi)]

    st.markdown("---")
    st.markdown("### 🧬 " + ("Diagnosis Report" if language == "English" else "निदान रिपोर्ट"))

    if language == "English":
        info = DISEASE_DATA_EN[pred_en]
        st.success(f"🩺 Disease Detected: {pred_en}")
        st.markdown(f"<div class='card'><b>About:</b> {info['about']}</div>", unsafe_allow_html=True)
        st.markdown("<div class='card'><b>Symptoms:</b><ul>" + "".join([f'<li>{s}</li>' for s in info['symptoms']]) + "</ul></div>", unsafe_allow_html=True)
        st.markdown("<div class='card'><b>Treatment:</b><ul>" + "".join([f'<li>{t}</li>' for t in info['treatment']]) + "</ul></div>", unsafe_allow_html=True)
        st.markdown("<div class='card'><b>Prevention Tips:</b><ul>" + "".join([f'<li>{p}</li>' for p in info['prevention']]) + "</ul></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card'><b>🌤 Seasonal Risk:</b> {info['season']} (<span class='risk-{ 'high' if 'High' in info['risk'] else 'medium' if 'Moderate' in info['risk'] else 'low'}'>{info['risk']}</span>)</div>", unsafe_allow_html=True)

    else:
        info = DISEASE_DATA_HI[pred_hi]
        st.success(f"🩺 पहचाना गया रोग: {pred_hi}")
        st.markdown(f"<div class='card'><b>विवरण:</b> {info['about']}</div>", unsafe_allow_html=True)
        st.markdown("<div class='card'><b>लक्षण:</b><ul>" + "".join([f'<li>{s}</li>' for s in info['symptoms']]) + "</ul></div>", unsafe_allow_html=True)
        st.markdown("<div class='card'><b>उपचार:</b><ul>" + "".join([f'<li>{t}</li>' for t in info['treatment']]) + "</ul></div>", unsafe_allow_html=True)
        st.markdown("<div class='card'><b>रोकथाम के उपाय:</b><ul>" + "".join([f'<li>{p}</li>' for p in info['prevention']]) + "</ul></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card'><b>🌤 मौसमी जोखिम:</b> {info['season']} (<span class='risk-{ 'high' if 'उच्च' in info['risk'] else 'medium' if 'मध्यम' in info['risk'] else 'low'}'>{info['risk']}</span>)</div>", unsafe_allow_html=True)

# ----------------------------
# 🌿 Footer
# ----------------------------
st.markdown("---")
st.markdown("<p style='text-align:center;color:#1b5e20;'>🌿 Developed by Green Thinkers | Empowering Smart Agriculture 🌾</p>", unsafe_allow_html=True)
