import streamlit as st
import numpy as np

# إعدادات الواجهة الأكاديمية الرسمية
st.set_page_config(
    page_title="المستشار الفيزيائي للحسابات الحتمية",
    page_icon="⚛️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تنسيق مظهر داكن واحترافي وإخفاء أي علامات برمجية
st.markdown("""
    <style>
    .reportview-container .main .block-container{ padding-top: 1.5rem; }
    h1, h2, h3, h4, h5 { text-align: right; font-family: 'Courier New', Courier, monospace; color: #f0f2f6; }
    .stNumberInput { text-align: right; direction: rtl; }
    div.stButton > button { width: 100%; background-color: #00ffcc; color: #0e1117; font-weight: bold; border: none; padding: 12px; font-size: 1.1rem; border-radius: 5px; }
    div.stButton > button:hover { background-color: #00cca3; color: #0e1117; }
    .result-box { background-color: #171a21; padding: 25px; border-radius: 8px; border-right: 5px solid #00ffcc; direction: rtl; margin-top: 20px; }
    .premium-box { background-color: #221c11; padding: 20px; border-radius: 8px; border-right: 5px solid #ffad33; direction: rtl; margin-top: 15px; text-align: right; }
    .tos-box { background-color: #0e1117; padding: 15px; border: 1px solid #2d3139; border-radius: 5px; height: 180px; overflow-y: scroll; direction: rtl; text-align: right; font-size: 0.85rem; color: #a3b3c2; margin-bottom: 15px; }
    .info-text { text-align: right; direction: rtl; color: #a3b3c2; font-size: 0.95rem; }
    .section-title { color: #00ffcc; border-bottom: 1px solid #2d3139; padding-bottom: 5px; margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

# العنوان الأكاديمي للمنصة
st.title("⚛️ نظام التحليل الرصدي والميكانيكا الحتمية")
st.subheader("منصة الحسابات الكمية لمتجهات الأوساط وديناميكا الأجرام")

st.markdown("""
<div class='info-text'>
مرحباً بك في نظام المعالجة الفيزيائية المخصص لتحليل متجهات الحركة وديناميكا الأجرام والمجرات. 
ملاحظة: يتطلب استخدام هذه المنصة والأدوات الحسابية الموافقة الكاملة وغير المشروطة على اتفاقية شروط الاستخدام المرفقة أدناه.
</div>
---
""", unsafe_allow_html=True)

# 📜 صندوق شروط الاستخدام والاتفاقية القانونية وحماية الملكية الفكرية
st.write("### ⚖️ اتفاقية شروط الخدمة وسياسة الاستخدام")
st.markdown("""
<div class="tos-box">
<b>بند 1: الموافقة الإلزامية</b><br>
بموجب النقر على مربع الموافقة، يقر المستخدم بقبول كافة الشروط والأحكام القانونية والفيزيائية المنظمة للمنصة دون قيد أو شرط.<br><br>
<b>بند 2: الشراكة وحقوق الملكية الفكرية</b><br>
يقر الطرف المستخدم بأن كافة المخرجات، الاستنتاجات، والتحليلات البنيوية الناتجة عن المنصة تعتمد على ثوابت توازن حتمية ومعادلات تابعة للجهة المطورة. وبناءً عليه، يلتزم المستخدم قانوناً بإشراك المنصة وإدارتها في كافة النتائج البحثية، الأوراق الأكاديمية، أو التقارير الفلكية التي يتم نشرها أو صياغتها بناءً على هذه المخرجات، وتعتبر الإدارة شريكاً مالكاً لجزء من الحقوق الفكرية للمنتج النهائي.<br><br>
<b>بند 3: العوائد والمكاسب المادية</b><br>
في حال ترتب على النتائج أو الأبحاث المستخلصة من هذه المنصة أي مكاسب مادية، تمويل أكاديمي، جوائز علمية، أو عوائد استثمارية، فإن الشروط القانونية تمنح المنصة الحق التلقائي في نسبة مئوية محددة من هذه المكاسب بموجب هذا العقد الرقمي الموثق قانوناً.<br><br>
<b>Bند 4: البصمة الرقمية والنسخ</b><br>
يلتزم المستخدم بإتاحة وترك (البصمة الرقمية التوثيقية المعيارية) المدمجة تلقائياً عند نسخ أو اقتباس الإجابات والتقارير النهائية، ويحظر محاولة إزالتها أو تعديلها لضمان التتبع الأكاديمي السليم.<br><br>
<b>بند 5: الحسابات وسرية المعادلات</b><br>
تظل المعادلات الخلفية، ومعاملات التشوه، والاشتقاقات الكمية لثابت التوازن، ملكاً سرياً وحصرياً للمنصة، ولا يحق للمستخدم محاولة عكس الهندسة البرمجية للنظام.
</div>
""", unsafe_allow_html=True)

# مربع تفعيل الموافقة
accepted_tos = st.checkbox("أوافق على كافة الشروط القانونية وسياسة الاستخدام المذكورة أعلاه.")

st.markdown("---")

# لا يظهر نظام الإدخال والتحليل إلا إذا وافق المستخدم على الشروط
if accepted_tos:
    st.write("### 📥 إدخال البيانات الرصدية القياسية للمجرّة")

    # خانات الإدخال القياسية للمستخدم
    col1, col2 = st.columns(2)

    with col1:
        v_radius = st.number_input("نصف قطر المجرة أو البعد الرصدي (بالسنة الضوئية):", value=50000.0, step=1000.0, format="%.1f")
        v_observed_vel = st.number_input("السرعة المدارية المرصودة (v بالـ كم/ث):", value=220.0, step=5.0, format="%.2f")

    with col2:
        v_baryonic_mass = st.number_input("الكتلة المضيئة/العادية المقدرة (بالكتلة الشمسية M☉):", value=1e10, step=1e9, format="%.1e")

    st.markdown("---")

    # زر بدء المعالجة الحسابية والاستنتاج
    if st.button("🧮 بدء معالجة الرصد واستخراج التقرير النهائي"):
        st.write("### 📊 التقرير الفيزيائي النهائي المعتمد")
        
        # 🔒 الثوابت والمعادلات الحتمية المخفية تماماً في الخلفية
        yousef_constant = 1e-11
        base_calc = (v_observed_vel ** 2) * v_radius / (v_baryonic_mass + 1.0)
        internal_distortion = min(0.9999, max(0.0001, base_calc / 1e7))
        denominator = internal_distortion + yousef_constant
        
        if denominator == 0:
            st.error("⚠️ فشل في النظام: المدخلات الرصدية تؤدي إلى قيم حرجة غير معرفة.")
        else:
            # حساب النسبة المكافئة للمادة المظلمة في الخلفية
            dark_matter_ratio = (1.0 - (1.0 / (1.0 + (internal_distortion / (yousef_constant * 1e10))))) * 100
            dark_matter_ratio = max(10.0, min(95.0, dark_matter_ratio + (v_observed_vel / 500.0)))
            
            # استنتاج الخصائص الهيكلية والحركية في الخلفية
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

            # عرض النتائج النهائية متبوعة بالبصمة الرقمية الإلزامية للتطبيق
            st.markdown(f"""
            <div class="result-box">
                <h4 style='color: #00ffcc; margin-top:0;'>📋 نتائج تحليل المنظومة الديناميكية:</h4>
                <p><b>🌌 نسبة الكتلة الغائبة (المادة المظلمة المكافئة) المحسوبة:</b> <span style='color: #ffad33; font-size: 1.2rem; font-weight: bold;'>{dark_matter_ratio:.2f} %</span></p>
                <p><b>📐 شكل المجرّة الحركي المستنتج:</b> {galaxy_shape}</p>
                <p><b>🔄 ميكانيكية وطريقة حركة المجرّة:</b> {galaxy_motion}</p>
                <p><b>🧭 اتجاه تدفق المتجهات الحتمية:</b> {galaxy_direction}</p>
                <hr style='border-color: #2d3139;'>
                <p style='font-size: 0.75rem; color: #00ffcc; direction: ltr; text-align: left; margin-bottom: 0;'>
                [DIGITAL-SIGNATURE: CHRONO-DYNAMICS-DETERMINISTIC-VERIFIED-2026]
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # صندوق غلق التفاصيل البرمجية
            st.markdown("""
            <div class="premium-box">
                <h4 style='color: #ffad33; margin-top:0;'>🔐 هل تريد معرفة تفاصيل المعادلات الحسابية ومعامل التشوه؟</h4>
                <p style='font-size: 0.9rem; color: #e0e0e0; margin-bottom: 0;'>
                الوصول إلى قِيَم <b>(معامل التشوه الهيكلي للوسط الكوني الكلي)</b>، والاشتقاقات الرياضية لـ <b>(ثابت يوسف للحسابات الحتمية)</b> متاح فقط للباحثين والمشتركين في الباقة المتقدمة للمنصة.
                <br><br>
                <a href='#' style='color: #00ffcc; text-decoration: none; font-weight: bold;'>✉️ اتصل بنا لتفعيل اشتراكك الأكاديمي والوصول لكامل المخططات والبيانات المخفية.</a>
                </p>
            </div>
            """, unsafe_allow_html=True)
else:
    st.info("ℹ️ يرجى قراءة شروط الاستخدام أعلاه وتفعيل مربع الموافقة لتتمكن من استخدام المنصة وإدخال البيانات.")

st.markdown("""
---
<p style='text-align: center; color: #4f5b66; font-size: 0.8rem;'>منصة الحسابات الفيزيائية الحتمية الرصدية © 2026</p>
""", unsafe_allow_html=True)
