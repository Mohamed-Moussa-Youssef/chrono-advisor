import streamlit as st
import numpy as np

# إعدادات الواجهة الأكاديمية الرسمية
st.set_page_config(
    page_title="المستشار الفيزيائي للحسابات الحتمية",
    page_icon="⚛️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تنسيق المظهر الداكن وتفتيح ألوان النصوص قسرياً مع أزرار الدفع
st.markdown("""
    <style>
    h1, h2, h3, h4, h5 { text-align: right; font-family: 'Courier New', Courier, monospace; color: #f0f2f6; }
    .stNumberInput { text-align: right; direction: rtl; }
    
    /* تصميم زر المعالجة الرئيسي */
    div.stButton > button { width: 100%; background-color: #00ffcc; color: #0e1117; font-weight: bold; border: none; padding: 12px; font-size: 1.1rem; border-radius: 5px; }
    div.stButton > button:hover { background-color: #00cca3; color: #0e1117; }
    
    /* صندوق النتائج والتحليل */
    .result-box { background-color: #171a21; padding: 25px; border-radius: 8px; border-right: 5px solid #00ffcc; direction: rtl; margin-top: 20px; text-align: right; }
    .result-box p, .result-box span, .result-box b, .result-box strong { color: #ffffff !important; font-size: 1.05rem; }
    
    /* صندوق بريميوم الذهبي لخطط الترقية */
    .premium-box { background-color: #221c11; padding: 20px; border-radius: 8px; border-right: 5px solid #ffad33; direction: rtl; margin-top: 15px; text-align: right; }
    .premium-box p, .premium-box h4, .premium-box span, .premium-box b { color: #ffffff !important; }
    
    /* أزرار الدفع الفوري لباتريون */
    .pay-button-gold { display: block; text-align: center; background-color: #ffad33; color: #0e1117 !important; font-weight: bold; padding: 12px; margin: 10px 0; border-radius: 5px; text-decoration: none; font-size: 1.05rem; }
    .pay-button-gold:hover { background-color: #e69519; color: #0e1117 !important; }
    .pay-button-cyan { display: block; text-align: center; background-color: #00ffcc; color: #0e1117 !important; font-weight: bold; padding: 12px; margin: 10px 0; border-radius: 5px; text-decoration: none; font-size: 1.05rem; }
    .pay-button-cyan:hover { background-color: #00cca3; color: #0e1117 !important; }
    
    /* صندوق شروط الاستخدام وإخلاء المسؤولية */
    .tos-box { background-color: #0e1117; padding: 15px; border: 1px solid #2d3139; border-radius: 5px; height: 220px; overflow-y: scroll; direction: rtl; text-align: right; font-size: 0.85rem; color: #a3b3c2; margin-bottom: 15px; }
    .info-text { text-align: right; direction: rtl; color: #a3b3c2; font-size: 0.95rem; }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التنقل بين الواجهات باستخدام Session State
if 'page' not in st.session_state:
    st.session_state.page = 'input_view'  # الواجهة الافتراضية هي واجهة الإدخال

# --- الواجهة الأولى: إدخال البيانات والشروط ---
if st.session_state.page == 'input_view':
    st.title("⚛️ نظام التحليل الرصدي والميكانيكا الحتمية")
    st.subheader("منصة الحسابات الكمية لمتجهات الأوساط وديناميكا الأجرام")
    
    st.markdown("<div class='info-text'>مرحباً بك في نظام المعالجة الفيزيائية المخصص لتحليل متجهات الحركة وديناميكا الأجرام والمجرات بناءً على النماذج الفلكية الافتراضية المتقدمة.</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # 📜 صندوق شروط الاستخدام والاتفاقية القانونية وإخلاء المسؤولية الصارم
    st.write("### ⚖️ اتفاقية شروط الخدمة وسياسة الاستخدام وإخلاء المسؤولية")
    st.markdown("""
    <div class="tos-box">
    <b>بند 1: الطبيعة الافتراضية للحسابات</b><br>
    يقر المستخدم ويدرك تماماً أن كافة المخرجات، المعادلات، والاستنتاجات التي تنتجها هذه المنصة هي عبارة عن حسابات مبنية على فرضيات فيزيائية ونماذج نظرية افتراضية لتوازن الأوساط. لا تعتبر هذه النتائج حقائق فلكية مطلقة إلا بعد إقرارها من الجهات البحثية المعنية.<br><br>
    <b>بند 2: إخلاء المسؤولية القانونية والعلمية الكلية</b><br>
    إدارة المنصة والمطور غير مسؤولين قانوناً أو علمياً عن أي خطأ، أو تباين، أو عدم دقة في النتائج أو الأرقام المستخرجة، أو أي قرارات بحثية أو أكاديمية يتخذها المستخدم بناءً على هذه الافتراضات الحسابية. يقع عبء التحقق الرصدي كاملاً على عاتق الطرف المستخدم.<br><br>
    <b>بند 3: الشراكة وحقوق الملكية الفكرية</b><br>
    يقر الطرف المستخدم بأن كافة المخرجات البنيوية الناتجة تعتمد على ثوابت توازن حتمية ومعادلات تابعة للجهة المطورة. وبناءً عليه، يلتزم المستخدم قانوناً بإشراك المنصة وإدارتها في كافة النتائج البحثية، الأوراق الأكاديمية، أو التقارير الفلكية التي يتم نشرها بناءً على هذه المخرجات، وتعتبر الإدارة شريكاً مالكاً لحق الملكية الفكرية للمنتج النهائي.<br><br>
    <b>بند 4: العوائد والمكاسب المادية</b><br>
    في حال ترتب على النتائج أو الأبحاث المستخلصة من هذه المنصة أي مكاسب مادية، تمويل أكاديمي، جوائز علمية، أو عوائد استثمارية، فإن الشروط القانونية تمنح المنصة الحق التلقائي في نسبة مئوية محددة من هذه المكاسب بموجب هذا العقد الرقمي الموثق.<br><br>
    <b>بند 5: البصمة الرقمية والنسخ</b><br>
    يلتزم المستخدم بإتاحة وترك (البصمة الرقمية التوثيقية المعيارية) المدمجة تلقائياً عند نسخ أو اقتباس الإجابات والتقارير النهائية، ويحظر محاولة إزالتها أو تعديلها لضمان التتبع الأكاديمي السليم.
    </div>
    """, unsafe_allow_html=True)

    # مربع تفعيل الموافقة
    accepted_tos = st.checkbox("أوافق على كافة الشروط القانونية وسياسة إخلاء المسؤولية المذكورة أعلاه.")
    st.markdown("---")

    if accepted_tos:
        st.write("### 📥 إدخال البيانات الرصدية القياسية للمجرّة")
        col1, col2 = st.columns(2)

        with col1:
            st.session_state.v_radius = st.number_input("نصف قطر المجرة أو البعد الرصدي (بالسنة الضوئية):", value=50000.0, step=1000.0, format="%.1f")
            st.session_state.v_observed_vel = st.number_input("السرعة المدارية المرصودة (v بالـ كم/ث):", value=220.0, step=5.0, format="%.2f")

        with col2:
            st.session_state.v_baryonic_mass = st.number_input("الكتلة المضيئة/العادية المقدرة (بالكتلة الشمسية M☉):", value=1e10, step=1e9, format="%.1e")

        st.markdown("---")
        
        # عند الضغط، يتم تغيير حالة الصفحة لينتقل التطبيق تلقائياً لواجهة النتائج
        if st.button("🧮 بدء معالجة الرصد واستخراج التقرير النهائي"):
            st.session_state.page = 'output_view'
            st.rerun()
    else:
        st.info("ℹ️ يرجى قراءة شروط الاستخدام والافتراضات وإخلاء المسؤولية أعلاه وتفعيل مربع الموافقة لتتمكن من استخدام المنصة وإدخال البيانات.")

# --- الواجهة الثانية: عرض الإجابات والتحليل ---
elif st.session_state.page == 'output_view':
    st.title("📊 واجهة التحليل الفيزيائي والتقرير النهائي")
    st.subheader("نتائج المعالجة الافتراضية لمتجهات توازن الوسط")
    
    # استرجاع البيانات المحفوظة من الواجهة الأولى للقيام بالحسابات
    v_radius = st.session_state.v_radius
    v_observed_vel = st.session_state.v_observed_vel
    v_baryonic_mass = st.session_state.v_baryonic_mass
    
    # العمليات الرياضية الحسابية
    yousef_constant = 3.12e-11
    base_calc = (v_observed_vel ** 2) * v_radius / (v_baryonic_mass + 1.0)
    internal_distortion = min(0.9999, max(0.0001, base_calc / 1e7))
    denominator = internal_distortion + yousef_constant
    
    if denominator == 0:
        st.error("⚠️ فشل في النظام: المدخلات الرصدية تؤدي إلى قيم حرجة غير معرفة.")
    else:
        dark_matter_ratio = (1.0 - (1.0 / (1.0 + (internal_distortion / (yousef_constant * 1e10))))) * 100
        dark_matter_ratio = max(10.0, min(95.0, dark_matter_ratio + (v_observed_vel / 500.0)))
        
        # تحديد الأنماط بناءً على الفرضيات الحسابية للمنظومة
        if internal_distortion > 0.6:
            galaxy_shape = "حلزونية ذروية (Spiral / Barred Spiral) ذات أذرع ممتدة وكثافة متجهة عالية في الأطراف."
            galaxy_motion = "حركة دورانية دوامية منتظمة (Vortex Rotation) مدعومة بمقاومة وسط متزنة."
            galaxy_direction = "تدفق متجهي حلزوني يمتد من الداخل إلى الخارج نحو مركز الثقل الكوني الديناميكي."
        elif internal_distortion > 0.3:
            galaxy_shape = "قرصية عدسية (Lenticular) ذات انتفاخ مركزي مستقر وتوزيع متجانس للمتجهات."
            galaxy_motion = "حركة مغلقة ذات انزياح دوراني مستقر ومقيد ميكانيكياً لمنع انهيار البنية."
            galaxy_direction = "اتجاه موازٍ لمستوى قرص المجرة الرئيسي مع ميلان طفيف في الأطراف."
        else:
            galaxy_shape = "بيضاويـة (Elliptical) أو قزمة غير منتظمة ذات تشوه هيكلي منخفض وضغط حركي عالي."
            galaxy_motion = "حركة عشوائية عظمى للمكونات (Randomized Motion) محكومة بمتجه توازن كلي يضمن التماسك الميكانيكي للوسط."
            galaxy_direction = "متجهات متداخلة وموزعة بشكل متناظر كروياً حول مركز الثقل الفيزيائي للوسط."

        # عرض صندوق النتائج مع نصوص بيضاء بالكامل
        st.markdown(f"""
        <div class="result-box">
            <h4 style='color: #00ffcc; margin-top:0; font-weight: bold;'>📋 نتائج تحليل المنظومة الديناميكية (الافتراضية):</h4>
            <p><b>🌌 نسبة الكتلة الغائبة (المادة المظلمة المكافئة) المحسوبة:</b> <span style='color: #ffad33; font-size: 1.2rem; font-weight: bold;'>{dark_matter_ratio:.2f} %</span></p>
            <p><b>📐 شكل المجرّة الحركي المستنتج:</b> {galaxy_shape}</p>
            <p><b>🔄 ميكانيكية وطريقة حركة المجرّة:</b> {galaxy_motion}</p>
            <p><b>🧭 اتجاه تدفق المتجهات الحتمية:</b> {galaxy_direction}</p>
            <hr style='border-color: #2d3139;'>
            <p style='font-size: 0.8rem; color: #a3b3c2; text-align: right;'>
            * تنويه: هذه الحسابات معتمدة كلياً على ثوابت التوازن الافتراضية للمنصة ومطورة لأغراض المحاكاة النظرية.
            </p>
            <p style='font-size: 0.75rem; color: #00ffcc; direction: ltr; text-align: left; margin-bottom: 0; font-weight: bold;'>
            [DIGITAL-SIGNATURE: CHRONO-DYNAMICS-DETERMINISTIC-VERIFIED-2026]
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # صندوق بوابة الترقية الذهبي مع الرابط الجديد الصحيح لـ Patreon
        st.markdown("""
        <div class="premium-box">
            <h4 style='color: #ffad33; margin-top:0; font-weight: bold;'>🔐 بوابة الترقية الفورية والوصول الرياضي الكامل:</h4>
            <p style='font-size: 0.95rem; margin-bottom: 15px;'>
            الوصول إلى قِيَم <b>(معامل التشوه الهيكلي للوسط)</b> والمخططات البيانية والاشتقاقات الرياضية الكاملة لـ <b>(ثابت يوسف)</b> متاح الآن عبر ربط اشتراكك الفوري:
            </p>
            
            <a href="https://www.patreon.com/cw/Moh9/membership" target="_blank" class="pay-button-gold">💳 اشترك في الباقة المتقدمة للأفراد (Premium) - $29 / شهرياً</a>
            <a href="https://www.patreon.com/cw/Moh9/membership" target="_blank" class="pay-button-cyan">🏛️ اشترك في الباقة الأكاديمية للمؤسسات والمختبرات - $149 / سنوياً</a>
            
            <p style='font-size: 0.85rem; color: #a3b3c2; margin-top: 15px; text-align: center;'>
            * بعد إتمام الاشتراك بنجاح، سيتم إرسال مفتاح التفعيل التلقائي إلى بريدك الإلكتروني.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    # زر العودة للواجهة الرئيسية لإدخال بيانات جديدة
    if st.button("⬅️ العودة لإدخال بيانات رصدية جديدة"):
        st.session_state.page = 'input_view'
        st.rerun()

st.markdown("""
<p style='text-align: center; color: #4f5b66; font-size: 0.8rem; margin-top: 30px;'>منصة الحسابات الفيزيائية الحتمية الرصدية © 2026</p>
""", unsafe_allow_html=True)
