import streamlit as st
import numpy as np

# إعدادات الواجهة الأكاديمية
st.set_page_config(
    page_title="المستشار الفيزيائي للحسابات الحتمية",
    page_icon="⚛️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تنسيق المظهر الداكن والخلفية البرمجية المنسقة
st.markdown("""
    <style>
    .reportview-container .main .block-container{ padding-top: 1.5rem; }
    h1, h2, h3, h4, h5 { text-align: right; font-family: 'Courier New', Courier, monospace; color: #f0f2f6; }
    .stNumberInput { text-align: right; direction: rtl; }
    div.stButton > button { width: 100%; background-color: #00ffcc; color: #0e1117; font-weight: bold; border: none; padding: 10px; font-size: 1.1rem; }
    div.stButton > button:hover { background-color: #00cca3; color: #0e1117; }
    .result-box { background-color: #171a21; padding: 25px; border-radius: 8px; border-right: 5px solid #00ffcc; direction: rtl; margin-top: 20px; }
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
يقوم هذا المستشار باستقبال البيانات الرصدية القياسية المتوفرة عالمياً، ويجري معالجتها في الخلفية بناءً على آليات التوازن الرياضية الصارمة ومعاملات الوسط المتصل لتقدير متجهات الأوساط ونسب الكتلة الغائبة (المادة المظلمة الافتراضية) بدقة عالية مع تلافي القيم غير المعرفة.
</div>
---
""", unsafe_allow_html=True)

st.write("### 📥 إدخال البيانات الرصدية القياسية للمجرّة")

# تقسيم المدخلات القياسية
col1, col2 = st.columns(2)

with col1:
    v_radius = st.number_input("نصف قطر المجرة أو البعد الرصدي (بالسنة الضوئية):", value=50000.0, step=1000.0, format="%.1f")
    v_observed_vel = st.number_input("السرعة المدارية المرصودة (v بالـ كم/ث):", value=220.0, step=5.0, format="%.2f")

with col2:
    v_baryonic_mass = st.number_input("الكتلة المضيئة/العادية المقدرة (بالكتلة الشمسية M☉):", value=1e10, step=1e9, format="%.1e")

st.markdown("---")

# زر بدء المعالجة الحسابية والاستنتاج
if st.button("🧮 بدء معالجة الرصد واستخراج النتائج والخصائص الهيكلية"):
    st.write("### 📊 التقرير الفيزيائي المستنتج")
    
    # 🔒 الثوابت والمعادلات الحتمية المخفية في الخلفية (ثابت يوسف وعامل الاتزان)
    yousef_constant = 1e-11
    
    # حساب أساسي لربط الطاقة الحركية بالكتلة المادية المتوفرة رصدياً
    base_calc = (v_observed_vel ** 2) * v_radius / (v_baryonic_mass + 1.0)
    
    # استخلاص معامل التشوه الهيكلي داخلياً في الخلفية
    internal_distortion = min(0.9999, max(0.0001, base_calc / 1e7))
    
    # المقام الحتمي الآمن من الصفر المطلق
    denominator = internal_distortion + yousef_constant
    
    if denominator == 0:
        st.error("⚠️ فشل في النظام: المدخلات الرصدية تؤدي إلى قيم حرجة غير معرفة.")
    else:
        # 1. حساب المركب الكلي للمتجه الحتمي الناتج داخلياً
        result_vector = (v_baryonic_mass * v_observed_vel * yousef_constant) / denominator
        
        # 2. حساب النسبة المكافئة للمادة المظلمة في الوسط بناءً على معامل التشوه وثابت يوسف
        dark_matter_ratio = (1.0 - (1.0 / (1.0 + (internal_distortion / (yousef_constant * 1e10))))) * 100
        dark_matter_ratio = max(10.0, min(95.0, dark_matter_ratio + (v_observed_vel / 500.0)))
        
        # 3. استنتاج شكل المجرة بناءً على معامل التشوه الداخلي ونسبة الكتلة الغائبة
        if internal_distortion > 0.6:
            galaxy_shape = "حلزونية ذروية (Spiral / Barred Spiral) ذات أذرع ممتدة وكثافة متجهة عالية في الأطراف."
            galaxy_motion = "حركة دورانية دوامية منتظمة (Vortex Rotation) مدعومة بمقاومة وسط متزنة تمنع تشتت الأطراف الخارجية للمجرة."
            galaxy_direction = "اتجاه متقارب محورياً نحو مركز الثقل الكوني الديناميكي، مع تدفق متجهي حلزوني يمتد من الداخل إلى الخارج."
        elif internal_distortion > 0.3:
            galaxy_shape = "قرصية عدسية (Lenticular) ذات انتفاخ مركزي مستقر وتوزيع متجانس للمتجهات الكتلية."
            galaxy_motion = "حركة مغلقـة ذات انزياح دوراني مستقر ومقيد ميكانيكياً بواسطة ثابت التوازن الحتمي لمنع انهيار البنية الهيكلية."
            galaxy_direction = "اتجاه موازٍ لمستوى قرص المجرة الرئيسي مع ميلان طفيف في المتجهات الطرفية الحتمية."
        else:
            galaxy_shape = "بيضاويـة (Elliptical) أو قزمة غير منتظمة ذات تشوه هيكلي منخفض وضغط حركي عالي."
            galaxy_motion = "حركة عشوائية عظمى للمكونات (Randomized Motion) محكومة بمتجه توازن كلي يضمن الحفاظ على التماسك الميكانيكي الهيكلي للوسط."
            galaxy_direction = "متجهات متداخلة وموزعة بشكل متناظر كروياً حول مركز الثقل الفيزيائي للوسط الكوني."

        # عرض التقرير المتكامل والنتائج الدقيقة للمستخدم
        st.markdown(f"""
        <div class="result-box">
            <h4 style='color: #00ffcc; margin-top:0;'>📋 أولاً: الحسابات الرقمية الدقيقة للكتلة والمتجهات:</h4>
            <table style='width: 100%; border-collapse: collapse; color: #f0f2f6; direction: rtl;'>
                <tr style='border-bottom: 1px solid #2d3139;'>
                    <td style='padding: 10px 0;'><b>المركب الحتمي الكلي لمتجه الوسط الناتج:</b></td>
                    <td style='text-align: left; color: #00ffcc; font-size: 1.2rem;'><b>{result_vector:.6e}</b></td>
                </tr>
                <tr style='border-bottom: 1px solid #2d3139;'>
                    <td style='padding: 10px 0;'><b>نسبة الكتلة الغائبة (المادة المظلمة المكافئة) المستنتجة:</b></td>
                    <td style='text-align: left; color: #ffad33; font-size: 1.2rem;'><b>{dark_matter_ratio:.2f} %</b></td>
                </tr>
                <tr>
                    <td style='padding: 10px 0;'><b>حالة استقرار النظام الرياضي الحتمي:</b></td>
                    <td style='text-align: left; color: #00ffaa;'><b>مستقر كلياً (آمن من الصفر والمالانهاية)</b></td>
                </tr>
            </table>
            
            <h4 class="section-title">🌌 ثانياً: الخصائص البنيوية والحركية المستنتجة خلف الكواليس:</h4>
            <p><b>📐 شكل المجرّة المتوقع بنبوياً:</b><br>{galaxy_shape}</p>
            <p><b>🔄 طريقة حركة المجرّة وميكانيكيتها:</b><br>{galaxy_motion}</p>
            <p><b>🧭 اتجاه المتجهات الكلية وحركتها:</b><br>{galaxy_direction}</p>
            
            <p style='font-size: 0.8rem; color: #8892b0; margin-top: 20px; text-align: right;'>
            * ملحوظة علمية: تم استنتاج هذه البيانات الهيكلية والحركية تلقائياً من خلال معالجة نسب التشوه والربط الميكانيكي للوسط الفيزيائي المتصل عبر حسابات ثابت الاتزان الحتمي المدمج.
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
---
<p style='text-align: center; color: #4f5b66; font-size: 0.8rem;'>منصة الحسابات الفيزيائية الحتمية الرصدية © 2026</p>
""", unsafe_allow_html=True)
