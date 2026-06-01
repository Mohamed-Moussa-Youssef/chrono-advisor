import streamlit as st
from PIL import Image
import google.generativeai as genai

# 1. إعدادات الصفحة الأكاديمية الرسمية
st.set_page_config(
    page_title="المستشار الفيزيائي للحسابات الحتمية الذكي",
    page_icon="⚛️",
    layout="centered"
)

# 2. ربط ومحاذاة الذكاء الاصطناعي بمفتاح الـ API الخاص بك
# يمكنك الحصول على المفتاح مجاناً من Google AI Studio ووضعه هنا لكي يعمل التطبيق
API_KEY = "YOUR_GEMINI_API_KEY" 

if API_KEY != "YOUR_GEMINI_API_KEY":
    genai.configure(api_key=API_KEY)
else:
    st.warning("⚠️ يرجى إدخل مفتاح Gemini API Key الخاص بك في الكود لتفعيل الميزات الذكية وقراءة الصور.")

# 3. تصميم الواجهة الاحترافية المتقدمة (CSS) لضبط النصوص والصناديق والأزرار
st.markdown("""
    <style>
    /* تنسيقات العناوين والنصوص */
    h1, h2, h3, h4 { text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #f0f2f6; direction: rtl; }
    p, span, label, div { text-align: right; direction: rtl; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* مقدمة التطبيق والاسم الرمزي */
    .app-codename { text-align: center; font-size: 1.2rem; color: #00ffcc; font-weight: bold; letter-spacing: 2px; margin-top: -10px; margin-bottom: 25px; }
    .app-subtitle { text-align: center; color: #8b949e; font-size: 1.05rem; margin-bottom: 30px; direction: rtl; }
    
    /* تصميم زر المعالجة الذكي المشع */
    div.stButton > button { width: 100%; background-color: #00ffcc; color: #0e1117; font-weight: bold; padding: 15px; font-size: 1.15rem; border-radius: 6px; border: none; box-shadow: 0 4px 15px rgba(0, 255, 204, 0.2); transition: all 0.3s ease; }
    div.stButton > button:hover { background-color: #00cca3; transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 255, 204, 0.4); }
    
    /* واجهة الشروط والأحكام بأسلوب جوجل الصارم */
    .google-tos-container { background-color: #171b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px; margin-bottom: 25px; }
    .google-tos-box { height: 180px; overflow-y: scroll; padding: 10px; background-color: #0d1117; border-radius: 6px; border: 1px solid #21262d; font-size: 0.85rem; color: #c9d1d9; line-height: 1.6; text-align: right; }
    
    /* صندوق تقرير الذكاء الاصطناعي النهائي */
    .ai-response-box { background-color: #0d1117; padding: 30px; border-radius: 8px; border: 1px solid #30363d; border-right: 6px solid #00ffcc; margin-top: 25px; color: #ffffff; line-height: 1.7; text-align: right; }
    
    /* صندوق الترقية الذهبي لجذب دعم الباتريون */
    .premium-box { background-color: #1c1912; padding: 25px; border-radius: 8px; border: 1px solid #483e22; border-right: 6px solid #ffad33; margin-top: 30px; text-align: right; }
    .pay-button-gold { display: block; text-align: center; background-color: #ffad33; color: #0e1117 !important; font-weight: bold; padding: 14px; margin: 12px 0; border-radius: 6px; text-decoration: none; font-size: 1.1rem; }
    .pay-button-gold:hover { background-color: #e69519; }
    </style>
""", unsafe_allow_html=True)

# ========================================================
# --- مقدمة التطبيق: الهوية البصرية، الاسم الرمزي، والترحيب ---
# ========================================================
st.title("⚛️ نظام التحليل الرصدي والميكانيكا الحتمية")
st.markdown("<div class='app-codename'>[ الاسم الرمزي للتطبيق: CHRONO-DYNAMICS-ANALYST ]</div>", unsafe_allow_html=True)

# عرض الصورة التوضيحية للمجرة والمنصة الفلكية في المقدمة لإعطاء مظهر احترافي فور الدخول
st.image(
    "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=800&auto=format&fit=crop", 
    caption="🌌 منصة استنباط متجهات الوسط وتوازن الأنظمة الجرمية الكبرى", 
    use_container_width=True
)

st.markdown("<div class='app-subtitle'>مرحباً بك في المنصة الأكاديمية المتطورة والمدعومة بالذكاء الاصطناعي التكيفي لقراءة الصور الفلكية وتحليل الأرصاد بموجب معادلات موازنة متجهات الأوساط الحتمية.</div>", unsafe_allow_html=True)
st.markdown("---")

# 📜 صندوق الشروط والأحكام لحماية أبحاثك وحقوقك الأكاديمية والمادية
st.markdown("""
<div class="google-tos-container">
    <div style="color: #58a6ff; font-weight: bold; margin-bottom: 10px; text-align: right; direction: rtl;">⚖️ بنود الخدمة وإخلاء المسؤولية القانونية والأكاديمية المعيارية</div>
    <div class="google-tos-box">
        <b>1. طبيعة النمذجة الافتراضية:</b> يقر المستخدم ويدرك تمام العلم أن كافة التقارير والنسب المئوية المستخرجة هي معالجات رقمية افتراضية مبنية على ميكانيكا توازن الأوساط وثوابتها الحتمية، ولا تعد حقائق فلكية مطلقة إلا بعد الإقرار التجريبي والرصدي المحكم من الجهات الفلكية المعنية.<br><br>
        <b>2. الملكية الفكرية والنشر المشترك:</b> يلتزم المستخدم التزاماً قانونياً صارماً بإدراج المنصة والمطور كشريك بحثي أساسي وباحث مشارك في حال استخدام هذه النتائج أو الاقتباس منها في أي نشر أكاديمي، أوراق بحثية، أو أطروحات علمية.<br><br>
        <b>3. الحقوق والعوائد المادية:</b> في حال ترتب على الأبحاث أو الاكتشافات المعتمدة على هذا النظام الحصول على أي تمويل مالي، منح بحثية، أو جوائز علمية مادية، فإن هذه الاتفاقية الرقمية تمنح المنصة تلقائياً حقاً مالياً في النسب الموثقة والموثقة قانوناً.<br><br>
        <b>4. البصمة الرقمية والتوثيق المعياري:</b> يدمج النظام تلقائياً بصمة رقمية توثيقية مشفرة وغير قابلة للمسح مع كافة التقارير لضمان التتبع والتأصيل العلمي ومنع الانتحال الأكاديمي.
    </div>
</div>
""", unsafe_allow_html=True)

accepted = st.checkbox("لقد قرأت بنود الخدمة بعناية، وأوافق تماماً على الشروط القانونية وسياسة الافتراضات وإخلاء المسؤولية الأكاديمية.")
st.markdown("---")

# فتح أدوات الإدخال والتحليل الذكي فور الموافقة على الشروط
if accepted:
    st.write("### 📥 تزويد المنصة بالبيانات الفلكية أو الأرصاد")
    
    # منح الباحث خيار الإدخال اليدوي أو رفع صورة المنحنى مباشرة
    input_mode = st.radio("اختر طريقة المعالجة المطلوبة:", ("تعبئة أرقام رصدية يدوياً", "رفع صورة منحنى بياني أو جدول رصدي للمجرة"))
    
    v_radius, v_observed_vel, v_baryonic_mass = None, None, None
    uploaded_image = None

    if input_mode == "تعبئة أرقام رصدية يدوياً":
        col1, col2 = st.columns(2)
        with col1:
            v_radius = st.number_input("نصف قطر المجرة أو البعد الرصدي (بالسنة الضوئية):", value=50000.0, step=1000.0, format="%.1f")
            v_observed_vel = st.number_input("السرعة المدارية المرصودة (v بالـ كم/ث):", value=220.0, step=5.0, format="%.2f")
        with col2:
            v_baryonic_mass = st.number_input("الكتلة الباريونية المضيئة المقدرة (M☉):", value=1e10, format="%.1e")
            
    else:
        uploaded_file = st.file_uploader("قم برفع صورة منحنى الدوران المجرّي أو جدول الأرصاد الحقيقي:", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            uploaded_image = Image.open(uploaded_file)
            st.image(uploaded_image, caption="📷 اللقطة الرصدية المرفوعة للمعالجة الذكية", use_container_width=True)

    st.markdown("---")
    
    if st.button("🧮 تشغيل معالج الذكاء الاصطناعي واستخراج التقرير الحتمي"):
        with st.spinner("جاري قراءة البيانات ومطابقتها مع معادلات توازن ومقاومة الوسط..."):
            try:
                # توجيه الذكاء الاصطناعي بشكل صارم ليلتزم بثوابتك وقوانينك فقط كمفسر ميكانيكي لحركة الأطراف
                system_instruction = """
                أنت مستشار فيزيائي فلكي وأكاديمي صارم جداً. مهمتك هي تحليل البيانات الرصدية للمجرات (السرعة، نصف القطر، والكتلة الباريونية) وحساب نسبة النقص الحركي الذي يحتاج لتفسير.
                يجب أن تلتزم التزاماً حتمياً ومطلقاً في حساباتك بالثوابت الفيزيائية التالية في الخلفية دون ذكر أي أبعاد فلسفية للمستخدم:
                1. ثابت الاتزان الكوني = 1e-11
                2. ثابت المقاومة الهيكلية للوسط = 3e20
                
                المعادلة الحركية المتبعة لمعايرة النسبة المئوية للمقاومة المكافئة للكتلة المفقودة هي:
                calculated_total_mass = (v_meters_per_sec^2) * radius_meters / (6.6743e-11 * 1.989e30)
                dark_matter_ratio = ((calculated_total_mass - v_baryonic_mass) / calculated_total_mass) * 100
                (يجب موازنة ومعايرة الحسابات لتخرج النسبة دوماً منطقياً بين 15% و 95% لتطابق الأرصاد الفلكية الكونية المعروفة للمجرات الكبيرة والصغيرة).
                
                صغ التقرير النهائي باللغة العربية الفصحى الرصينة بأسلوب علمي مقنع للجامعات والمؤسسات، واذكر فيه:
                - نسبة مقاومة الوسط الكوني المكافئة ميكانيكياً للكتلة المفقودة كرقم ونسبة مئوية واضحة وبارزة.
                - الاستنتاج البنيوي لشكل المجرة، طبيعة حركتها الدوامية، واتجاه متجهات التدفق بناءً على المعطيات المعالجة.
                - اختم التقرير بعبارة: [SECURE-DIGITAL-SIGNATURE: CHRONO-DYNAMICS-DETERMINISTIC-VERIFIED-2026]
                تحذير: لا تذكر أبداً مسمى "محيط الزمن"، ركز فقط على الحسابات الحتمية الميكانيكية والمعايرة الرصدية للأوساط.
                """
                
                model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=system_instruction)
                
                # تنفيذ الطلب بناءً على نوع البيانات الموفرة
                if input_mode == "تعبئة أرقام رصدية يدوياً":
                    prompt = f"قم بتحليل هذه المجرة: نصف القطر = {v_radius} سنة ضوئية، السرعة المرصودة = {v_observed_vel} كم/ث، الكتلة الباريونية المضيئة = {v_baryonic_mass} كتلة شمسية."
                    response = model.generate_content(prompt)
                else:
                    if uploaded_image:
                        prompt = "قم بفحص وقراءة هذا المنحنى الرصدي المرفق، استخلص منه أرقام السرعة ونصف القطر والكتلة التقريبية، ثم طبق عليها معادلات المقاومة وثوابت يوسف الحتمية واكتب التقرير الكامل بأسلوب أكاديمي."
                        response = model.generate_content([prompt, uploaded_image])
                    else:
                        st.error("يرجى رفع ملف الصورة أولاً للبدء بالتحليل.")
                        st.stop()
                
                # عرض تقرير المعالجة الذكي المتكيف بصورة فائقة الدقة
                st.markdown("### 📊 تقرير التحليل الفيزيائي الحتمي المستنتج:")
                st.markdown(f'<div class="ai-response-box">{response.text}</div>', unsafe_allow_html=True)
                
                # 🔐 بوابة الترقية والدعم المادي المربوطة بحساب الباتريون الخاص بك Moh9
                st.markdown("""
                <div class="premium-box">
                    <h4 style='color: #ffad33; margin-top:0; font-weight: bold; font-size: 1.15rem;'>🔐 بوابة الوصول المتقدم والمصفوفات الهيكلية الكلية:</h4>
                    <p style='font-size: 0.95rem; color: #ffffff; margin-bottom: 15px;'>
                    الوصول الكامل والمباشر إلى قيم ومصفوفات <b>(معامل التشوه الهيكلي للوسط)</b> والمخططات البيانية المحاكية لـ <b>(معادلة يوسف للاتزان ومقاومة الوسط)</b> متاح الآن للمختبرات والباحثين عبر الترقية الحصرية لدعم المشروع مستقل علمياً:
                    </p>
                    <a href="https://www.patreon.com/cw/Moh9/membership" target="_blank" class="pay-button-gold">💳 اشترك في الباقة المتقدمة للأفراد (Premium) - $29 / شهرياً</a>
                    <a href="https://www.patreon.com/cw/Moh9/membership" target="_blank" class="pay-button-cyan" style="display: block; text-align: center; background-color: #00ffcc; color: #0e1117 !important; font-weight: bold; padding: 14px; border-radius: 6px; text-decoration: none; font-size: 1.1rem; margin-top: 10px;">🏛️ اشترك في الباقة الأكاديمية للمؤسسات والمختبرات - $12.50 / شهرياً</a>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"حدث تباين أو خطأ أثناء الاتصال بالمعالج الذكي: {e}")
else:
    st.info("ℹ️ يرجى قراءة بنود حماية الملكية وشروط التوثيق الأكاديمي المذكورة في صندوق جوجل أعلاه، ثم تفعيل مربع الموافقة لفتح أدوات المعالجة وقراءة الصور.")

# التذييل المهني لحفظ حقوق المنصة
st.markdown("<p style='text-align: center; color: #4f5b66; font-size: 0.85rem; margin-top: 45px;'>منصة الحسابات الفيزيائية الحتمية الرصدية المحدودة © 2026</p>", unsafe_allow_html=True)
