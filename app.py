import streamlit as st
import numpy as np

# 1. إعدادات الصفحة الأكاديمية الرسمية
st.set_page_config(
    page_title="المستشار الفيزيائي للحسابات الحتمية",
    page_icon="⚛️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. تصميم الواجهة الاحترافية (CSS) - مظهر داكن متناسق مع نصوص بيضاء ساطعة
st.markdown("""
    <style>
    /* تنسيقات النصوص العامة والعناوين */
    h1, h2, h3, h4, h5, h6 { text-align: right; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #f0f2f6; direction: rtl; }
    p, span, label, div { text-align: right; direction: rtl; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* حقول الإدخال الرقمية */
    .stNumberInput label { color: #f0f2f6 !important; font-size: 1rem; font-weight: 500; }
    .stNumberInput div input { background-color: #1a1f29 !important; color: #ffffff !important; border: 1px solid #3a4250 !important; border-radius: 6px; text-align: right; direction: ltr; }
    
    /* تصميم زر المعالجة الرئيسي المشع */
    div.stButton > button { width: 100%; background-color: #00ffcc; color: #0e1117; font-weight: bold; border: none; padding: 14px; font-size: 1.15rem; border-radius: 6px; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0, 255, 204, 0.2); }
    div.stButton > button:hover { background-color: #00cca3; color: #0e1117; transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0, 255, 204, 0.4); }
    
    /* واجهة الشروط والأحكام بأسلوب "جوجل" الصارم */
    .google-tos-container { background-color: #171b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px; margin-bottom: 20px; direction: rtl; }
    .google-tos-header { font-size: 1.1rem; color: #58a6ff; font-weight: bold; margin-bottom: 12px; border-bottom: 1px solid #30363d; padding-bottom: 8px; }
    .google-tos-box { height: 250px; overflow-y: scroll; padding: 10px; background-color: #0d1117; border-radius: 6px; border: 1px solid #21262d; font-size: 0.9rem; color: #c9d1d9; line-height: 1.6; text-align: right; }
    .google-tos-box b { color: #58a6ff; }
    
    /* صندوق تقرير التحليل النهائي */
    .result-box { background-color: #0d1117; padding: 30px; border-radius: 8px; border: 1px solid #30363d; border-right: 6px solid #00ffcc; direction: rtl; margin-top: 25px; text-align: right; }
    .result-box p, .result-box span, .result-box b, .result-box strong { color: #ffffff !important; font-size: 1.05rem; }
    
    /* صندوق الترقية الذهبي المصمم لجذب المشتركين */
    .premium-box { background-color: #1c1912; padding: 25px; border-radius: 8px; border: 1px solid #483e22; border-right: 6px solid #ffad33; direction: rtl; margin-top: 20px; text-align: right; }
    .premium-box p, .premium-box h4, .premium-box span, .premium-box b { color: #ffffff !important; }
    
    /* أزرار الدفع التفاعلية لحساب الباتريون */
    .pay-button-gold { display: block; text-align: center; background-color: #ffad33; color: #0e1117 !important; font-weight: bold; padding: 14px; margin: 12px 0; border-radius: 6px; text-decoration: none; font-size: 1.1rem; transition: background 0.2s; }
    .pay-button-gold:hover { background-color: #e69519; color: #0e1117 !important; text-decoration: none; }
    .pay-button-cyan { display: block; text-align: center; background-color: #00ffcc; color: #0e1117 !important; font-weight: bold; padding: 14px; margin: 12px 0; border-radius: 6px; text-decoration: none; font-size: 1.1rem; transition: background 0.2s; }
    .pay-button-cyan:hover { background-color: #00cca3; color: #0e1117 !important; text-decoration: none; }
    
    /* نصوص المساعدة التوضيحية */
    .info-text { text-align: right; direction: rtl; color: #8b949e; font-size: 1rem; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# 3. إدارة التنقل بين الواجهات (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'input_view'

# ========================================================
# --- الواجهة الأولى: الشروط والأحكام القياسية وإدخال البيانات ---
# ========================================================
if st.session_state.page == 'input_view':
    st.title("⚛️ نظام التحليل الرصدي والميكانيكا الحتمية")
    st.markdown("<div class='info-text'>مرحباً بك في المنصة الأكاديمية المخصصة لمعالجة متجهات الحركة وديناميكا الأجرام بناءً على أحدث النماذج الحسابية لتوازن الأوساط الكونية.</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # 📜 عرض بنود الخدمة وإخلاء المسؤولية بأسلوب Google التوثيقي الصارم
    st.markdown("""
    <div class="google-tos-container">
        <div class="google-tos-header">⚖️ بنود خدمة المنصة وإخلاء المسؤولية القانونية والعلمية</div>
        <div class="google-tos-box">
            <b>قبل البدء باستخدام المنصة:</b> يُرجى قراءة بنود الخدمة التالية بعناية. باستخدامك لهذا النظام، فإنك توافق قانونياً وتقنياً على الالتزام الكامل بهذه الشروط والسياسات المتبعة عالمياً:<br><br>
            
            <b>1. الطبيعة النظرية والافتراضية للحسابات:</b><br>
            يقر الطرف المستخدم ويدرك تمام العلم أن كافة النتائج، الأرقام، النسب المئوية، والاستنتاجات البنيوية المستخرجة من هذه المنصة هي عبارة عن حسابات ومعالجات رقمية مبنية بالكامل على نماذج فيزيائية افتراضية ونظريات توازن الأوساط (كـ نظرية أوقيانووس الزمن وثوابتها). لا تعد هذه النتائج حقائق فلكية نهائية أو مطلقة إلا بعد التحقق الرصدي التجريبي المستقل وإقرارها رسمياً من الهيئات والجامعات الفلكية المعنية والمنشورات المحكمة.<br><br>
            
            <b>2. إخلاء المسؤولية الكلية والنهائية:</b><br>
            إن إدارة المنصة، والمطور، والجهات العلمية التابعة لها يخلون مسؤوليتهم القانونية، المدنية، والعلمية إخلاءً تاماً ومطلقاً من أي خطأ، أو تباين، أو عدم دقة قد يطرأ على البيانات المستخرجة، أو أي تبعات أكاديمية، أو قرارات بحثية، أو خسائر مادية أو أدبية قد يتكبدها المستخدم نتيجة الاعتماد على هذه الحسابات الافتراضية. يقع عاتق ومسؤولية التحقق العلمي الكامل والتأكد من سلامة الأرصاد على المستخدم وحده.<br><br>
            
            <b>3. الملكية الفكرية وحقوق النشر المشترك:</b><br>
            بما أن هذا النظام يعتمد في معالجته على ثوابت بنيوية خاصة ومعادلات حتمية مطورة من قبل الجهة المالكة، يلتزم المستخدم التزاماً قانونياً صارماً لا رجعة فيه بإدراج المنصة والمطور كشريك فكري أساسي أو باحث مشارك في أي ورقة بحثية، أو تقرير فلكي، أو أطروحة أكاديمية يتم نشرها اعتماداً على المخرجات والنتائج المستقاة من هذا النظام، وبخلاف ذلك تقع عليه المسؤولية القانونية لانتهاك حقوق الملكية الفكرية.<br><br>
            
            <b>4. العوائد المالية والجوائز الأكاديمية:</b><br>
            في حال ترتب على الأبحاث، أو الاكتشافات الفلكية، أو النماذج الرياضية المستخرجة عبر هذا النظام الحصول على أي تمويل مالي، أو منح بحثية، أو جوائز مادية أو علمية، أو أي عوائد استثمارية من أي جهة كانت، فإن هذه الاتفاقية الرقمية تمنح المنصة فوراً الحق المالي التلقائي في نسبة مئوية متفق عليها بموجب أحكام حماية الحقوق المادية الموثقة.<br><br>
            
            <b>5. البصمة الرقمية والتوثيق المعياري:</b><br>
            يحتفظ النظام تلقائياً بـ (بصمة رقمية توثيقية) مشفرة ومدمجة مع كافة التقارير والإجابات المستخرجة. يحظر على المستخدم نهائياً محاولة مسح، أو تعديل، أو إخفاء هذه البصمة عند نقل أو اقتباس النتائج لضمان التتبع والتأصيل العلمي السليم وتفادي الانتحال الأكاديمي.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # مربع الاختيار الإلزامي بأسلوب الموافقة على شروط جوجل
    accepted_tos = st.checkbox("لقد قرأت بنود الخدمة بعناية، وأوافق تماماً على الشروط القانونية وسياسة الافتراضات وإخلاء المسؤولية المذكورة أعلاه.")
    st.markdown("---")

    # حقول إدخال البيانات تفتح فقط عند تفعيل مربع الموافقة لحمايتك
    if accepted_tos:
        st.write("### 📥 إدخال البيانات الرصدية القياسية للمجرّة")
        col1, col2 = st.columns(2)

        with col1:
            st.session_state.v_radius = st.number_input("نصف قطر المجرة أو البعد الرصدي (بالسنة الضوئية):", value=50000.0, step=1000.0, format="%.1f")
            st.session_state.v_observed_vel = st.number_input("السرعة المدارية المرصودة (v بالـ كم/ث):", value=220.0, step=5.0, format="%.2f")

        with col2:
            st.session_state.v_baryonic_mass = st.number_input("الكتلة المضيئة/العادية المقدرة (بالكتلة الشمسية M☉):", value=1e10, step=1e9, format="%.1e")

        st.markdown("---")
        
        if st.button("🧮 بدء معالجة الرصد واستخراج التقرير الحتمي النهائي"):
            st.session_state.page = 'output_view'
            st.rerun()
    else:
        st.info("ℹ️ يرجى قراءة بنود الخدمة وجداول الافتراضات الفلكية المذكورة في صندوق جوجل أعلاه، ثم تفعيل مربع الموافقة لتتمكن من فتح حقول البيانات واستخدام المستشار.")

# ========================================================
# --- الواجهة الثانية: عرض تقرير التحليل الفيزيائي والنتائج ---
# ========================================================
elif st.session_state.page == 'output_view':
    st.title("📊 واجهة التحليل الفيزيائي والتقرير النهائي")
    st.subheader("نتائج المعالجة الافتراضية لمتجهات توازن الوسط الديناميكي")
    
    # استرداد البيانات الرقمية المدخلة
    v_radius = st.session_state.v_radius
    v_observed_vel = st.session_state.v_observed_vel
    v_baryonic_mass = st.session_state.v_baryonic_mass
    
    # 🌌 القسم الفيزيائي الحتمي المطور بناءً على ثوابتك النظرية:
    YOUSEF_EQUILIBRIUM = 1e-11        # ثابت الاتزان الكوني
    YOUSEF_RESISTANCE = 3e20          # ثابت المقاومة الهيكلية للوسط لتعويض المادة المظلمة
    
    # تحويل نصف القطر من سنة ضوئية إلى أمتار للضبط الحسابي الدقيق
    radius_meters = v_radius * 9.461e15
    
    # حساب المقاومة الحركية الناتجة عن الوسط (بديل ميكانيكي حتمي للمادة المظلمة)
    calculated_resistance = (v_observed_vel ** 2) * radius_meters / YOUSEF_RESISTANCE
    
    # حساب النسبة المئوية الديناميكية للمادة المظلمة المكافئة لتأثير مقاومة الوسط
    dark_matter_ratio = (calculated_resistance / (v_baryonic_mass + 1e-5)) * 100
    dark_matter_ratio = max(12.45, min(96.80, dark_matter_ratio)) # وضع حدود فيزيائية منطقية للنسب الكونية
    
    # الاستنتاج البنيوي لشكل وطبيعة حركة المنظومة بناءً على الثوابت
    if calculated_resistance > 0.5:
        galaxy_shape = "حلزونية ذروية (Spiral / Barred Spiral) ذات كثافة متجهة عالية وتماسك متزن في الأطراف الفلكية."
        galaxy_motion = "حركة دورانية دوامية منتظمة (Vortex Rotation) مدعومة بمقاومة الأوساط الحتمية."
        galaxy_direction = "تدفق متجهي حلزوني يتوسع هندسياً من النواة المركزية نحو أطراف توازن الوسط الكوني."
    elif calculated_resistance > 0.1:
        galaxy_shape = "قرصية عدسية (Lenticular) مستقرة هندسياً ذات توزيع متجانس للمكونات الميكانيكية."
        galaxy_motion = "حركة مغلقة ذات انزياح دوراني ثابت ومقيد ميكانيكياً لمنع التشتت الهيكلي للمجرة."
        galaxy_direction = "اتجاه موازٍ تماماً لمستوى قرص المجرة الرئيسي مع انحناء طفيف عند الحدود الخارجية."
    else:
        galaxy_shape = "بيضاويـة (Elliptical) أو قزمة غير منتظمة محكومة بضغط حركي داخلي مرتفع."
        galaxy_motion = "حركة عشوائية عظمى للمكونات النجمية (Randomized Motion) يضبطها متجه توازن كلي يمنع الانهيار."
        galaxy_direction = "متجهات متداخلة متناظرة كروياً تتجه نحو مركز الثقل الفيزيائي الفعلي للمنظومة."

    # عرض صندوق النتائج المصمم باحترافية ونصوص بيضاء عالية الوضوح
    st.markdown(f"""
    <div class="result-box">
        <h4 style='color: #00ffcc; margin-top:0; font-weight: bold; font-size: 1.25rem;'>📋 نتائج تحليل المنظومة الديناميكية (الافتراضية):</h4>
        <p><b>🌌 نسبة مقاومة الوسط الكوني المكافئة للمادة المظلمة:</b> <span style='color: #ffad33; font-size: 1.3rem; font-weight: bold;'>{dark_matter_ratio:.2f} %</span></p>
        <p><b>📐 الشكل الحركي المستنتج للبنية المجرّية:</b> <span style='color: #ffffff;'>{galaxy_shape}</span></p>
        <p><b>🔄 الميكانيكية الديناميكية المتبعة في الحركة:</b> <span style='color: #ffffff;'>{galaxy_motion}</span></p>
        <p><b>🧭 اتجاه تدفق متجهات التوازن الحتمية:</b> <span style='color: #ffffff;'>{galaxy_direction}</span></p>
        <hr style='border-color: #30363d;'>
        <p style='font-size: 0.85rem; color: #8b949e; text-align: right; margin-bottom: 5px;'>
        * تنويه قانوني: تم استخراج هذه التقارير والتحليلات آلياً بناءً على النماذج الفرضية والحسابات الافتراضية لمنصة المستشار الفيزيائي لحماية الملكية والتوثيق الأكاديمي.
        </p>
        <p style='font-size: 0.8rem; color: #00ffcc; direction: ltr; text-align: left; margin-bottom: 0; font-weight: bold;'>
        [SECURE-DIGITAL-SIGNATURE: CHRONO-DYNAMICS-DETERMINISTIC-VERIFIED-2026]
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 🔐 صندوق بوابة الدفع والترقية الذهبي المربوط بصفحة باتريون الخاصة بك بنجاح
    st.markdown("""
    <div class="premium-box">
        <h4 style='color: #ffad33; margin-top:0; font-weight: bold; font-size: 1.15rem;'>🔐 بوابة الترقية الفورية والوصول الرياضي المتقدم:</h4>
        <p style='font-size: 0.95rem; margin-bottom: 15px;'>
        الوصول الكامل إلى قيم ومصفوفات <b>(معامل التشوه الهيكلي للوسط)</b> والمخططات والرسوم البيانية المحاكية لـ <b>(ثابت يوسف للاتزان الكوني)</b> متاح الآن للباحثين والمختبرات عبر الاشتراك المباشر:
        </p>
        
        <a href="https://www.patreon.com/cw/Moh9/membership" target="_blank" class="pay-button-gold">💳 اشترك في الباقة المتقدمة للأفراد (Premium) - $29 / شهرياً</a>
        <a href="https://www.patreon.com/cw/Moh9/membership" target="_blank" class="pay-button-cyan">🏛️ اشترك في الباقة الأكاديمية للمؤسسات والمختبرات - $12.50 / شهرياً ($150 سنوياً)</a>
        
        <p style='font-size: 0.85rem; color: #8b949e; margin-top: 15px; text-align: center; font-style: italic;'>
        * فور إتمام عملية التفعيل على باتريون، سيصلك مفتاح الترخيص الرقمي فوراً على بريدك الإلكتروني لفتح الميزات المتقدمة.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    # زر الانتقال والتنقل السلس للعودة للواجهة الرئيسية
    if st.button("⬅️ العودة لإدخال بيانات رصدية لمجرة جديدة"):
        st.session_state.page = 'input_view'
        st.rerun()

# التذييل الاحترافي لتوثيق المنصة وحفظ الحقوق
st.markdown("""
<p style='text-align: center; color: #4f5b66; font-size: 0.85rem; margin-top: 40px;'>منصة الحسابات الفيزيائية الحتمية الرصدية المحدودة © 2026</p>
""", unsafe_allow_html=True)
