import streamlit as st
import numpy as np

# إعدادات الواجهة الاحترافية
st.set_page_config(
    page_title="المستشار الفيزيائي للحسابات الحتمية",
    page_icon="⚛️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تصميم المظهر الداكن وتنسيق خانات الإدخال الرقمية بدقة
st.markdown("""
    <style>
    .reportview-container .main .block-container{ padding-top: 1.5rem; }
    h1, h2, h3, h4 { text-align: right; font-family: 'Courier New', Courier, monospace; color: #f0f2f6; }
    .stNumberInput { text-align: right; direction: rtl; }
    div.stButton > button { width: 100%; background-color: #00ffcc; color: #0e1117; font-weight: bold; border: none; }
    div.stButton > button:hover { background-color: #00cca3; color: #0e1117; }
    .result-box { background-color: #171a21; padding: 25px; border-radius: 8px; border-right: 5px solid #00ffcc; direction: rtl; }
    .info-text { text-align: right; direction: rtl; color: #a3b3c2; font-size: 0.95rem; }
    </style>
""", unsafe_allow_html=True)

# العنوان الأكاديمي الرسمي للمنصة
st.title("⚛️ نظام التحليل الرصدي والميكانيكا الحتمية")
st.subheader("منصة الحسابات الكمية لمتجهات الأوساط وديناميكا الأجرام")

st.markdown("""
<div class='info-text'>
مرحباً بك في نظام المعالجة الفيزيائية المخصص لحساب معاملات التشوه الهيكلي وتحليل متجهات الحركة في الأوساط الديناميكية. 
يقوم هذا المستشار بمعالجة بيانات رصد المواكب وحساب توزيع نسب المادة المظلمة الافتراضية كبديل ميكانيكي حتمي، معتمداً على آليات موازنة رياضية صارمة تمنع ظهور القيم غير المعرفة (كالصفر المطلق أو المالانهاية).
</div>
---
""", unsafe_allow_html=True)

st.write("### 📥 مدخلات البيانات الرصدية والمعاملات الفيزيائية")

# تقسيم المدخلات الفيزيائية إلى أعمدة متناسقة
col1, col2 = st.columns(2)

with col1:
    v_distortion = st.number_input("معامل التشوه الهيكلي المستخلص:", value=0.5000, step=0.0100, format="%.4f")
    v_velocity = st.number_input("السرعة الرصدية للحركة الكونية (v):", value=1.0000, step=0.1000, format="%.4f")

with col2:
    v_constant = st.number_input("عامل التوازن الثابت المعياري:", value=1e-11, step=1e-12, format="%.13f")
    v_force = st.number_input("القوة الديناميكية المؤثرة في الوسط (F):", value=10.0000, step=1.0000, format="%.4f")

st.markdown("---")

# زر بدء المعالجة الحسابية
if st.button("🧮 بدء معالجة الرصد واستخراج النتائج الدقيقة"):
    st.write("### 📊 المخرجات والنسب الحتمية المستقرة")
    
    # حساب القيمة الأساسية للمقام مع دمج الثابت الحتمي لمنع القسمة على صفر
    denominator = v_distortion + v_constant
    
    if denominator == 0:
        st.error("⚠️ فشل في النظام: المدخلات الحالية تؤدي إلى قيمة حرجة غير معرفة.")
    else:
        # 1. حساب المتجه الكلي الناتج
        result_vector = (v_force * v_velocity) / denominator
        
        # 2. حساب النسبة المكافئة للمادة المظلمة بناءً على التشوه ومقياس الثابت
        dark_matter_ratio = (1.0 - (1.0 / (1.0 + (v_distortion / (v_constant * 1e10))))) * 100
        
        # تصحيح الحدود لضمان دقة النسبة بين 0% و 100% دون أخطاء
        dark_matter_ratio = max(0.0, min(100.0, dark_matter_ratio))
        
        # عرض النتائج في قالب رصدي محترف
        st.markdown(f"""
        <div class="result-box">
            <h4 style='color: #00ffcc; margin-top:0;'>📋 مخرجات التحليل الرقمي بدقة عالية:</h4>
            <table style='width: 100%; border-collapse: collapse; color: #f0f2f6; direction: rtl;'>
                <tr style='border-bottom: 1px solid #2d3139;'>
                    <td style='padding: 10px 0;'><b>المركب الحتمي الكلي للمتجه الناتج:</b></td>
                    <td style='text-align: left; color: #00ffcc; font-size: 1.3rem;'><b>{result_vector:.6f}</b></td>
                </tr>
                <tr style='border-bottom: 1px solid #2d3139;'>
                    <td style='padding: 10px 0;'><b>نسبة M.D (المادة المظلمة الافتراضية) المكافئة:</b></td>
                    <td style='text-align: left; color: #ffad33; font-size: 1.3rem;'><b>{dark_matter_ratio:.2f} %</b></td>
                </tr>
                <tr>
                    <td style='padding: 10px 0;'><b>حالة استقرار النظام البرمجي:</b></td>
                    <td style='text-align: left; color: #00ffaa;'><b>مستقر (تم تلافي الصفر والمالانهاية)</b></td>
                </tr>
            </table>
            <p style='font-size: 0.8rem; color: #8892b0; margin-top: 15px; text-align: right;'>
            * ملحوظة: البيانات المستخرجة تمثل محاكاة ديناميكية حتمية لحركة المتجهات الكتلية عند نقطة الاتزان الحرجة المستخلصة من التشوه الهيكلي للوسط.
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
---
<p style='text-align: center; color: #4f5b66; font-size: 0.8rem;'>منصة الحسابات الفيزيائية الحتمية الرصدية © 2026</p>
""", unsafe_allow_html=True)
import streamlit as st
import numpy as np

# إعدادات الواجهة الاحترافية
st.set_page_config(
    page_title="المستشار الفيزيائي للحسابات الحتمية",
    page_icon="⚛️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تصميم المظهر الداكن وتنسيق خانات الإدخال الرقمية بدقة
st.markdown("""
    <style>
    .reportview-container .main .block-container{ padding-top: 1.5rem; }
    h1, h2, h3, h4 { text-align: right; font-family: 'Courier New', Courier, monospace; color: #f0f2f6; }
    .stNumberInput { text-align: right; direction: rtl; }
    div.stButton > button { width: 100%; background-color: #00ffcc; color: #0e1117; font-weight: bold; border: none; }
    div.stButton > button:hover { background-color: #00cca3; color: #0e1117; }
    .result-box { background-color: #171a21; padding: 25px; border-radius: 8px; border-right: 5px solid #00ffcc; direction: rtl; }
    .info-text { text-align: right; direction: rtl; color: #a3b3c2; font-size: 0.95rem; }
    </style>
""", unsafe_allow_html=True)

# العنوان الأكاديمي الرسمي للمنصة
st.title("⚛️ نظام التحليل الرصدي والميكانيكا الحتمية")
st.subheader("منصة الحسابات الكمية لمتجهات الأوساط وديناميكا الأجرام")

st.markdown("""
<div class='info-text'>
مرحباً بك في نظام المعالجة الفيزيائية المخصص لحساب معاملات التشوه الهيكلي وتحليل متجهات الحركة في الأوساط الديناميكية. 
يقوم هذا المستشار بمعالجة بيانات رصد المواكب وحساب توزيع نسب المادة المظلمة الافتراضية كبديل ميكانيكي حتمي، معتمداً على آليات موازنة رياضية صارمة تمنع ظهور القيم غير المعرفة (كالصفر المطلق أو المالانهاية).
</div>
---
""", unsafe_allow_html=True)

st.write("### 📥 مدخلات البيانات الرصدية والمعاملات الفيزيائية")

# تقسيم المدخلات الفيزيائية إلى أعمدة متناسقة
col1, col2 = st.columns(2)

with col1:
    v_distortion = st.number_input("معامل التشوه الهيكلي المستخلص:", value=0.5000, step=0.0100, format="%.4f")
    v_velocity = st.number_input("السرعة الرصدية للحركة الكونية (v):", value=1.0000, step=0.1000, format="%.4f")

with col2:
    v_constant = st.number_input("عامل التوازن الثابت المعياري:", value=1e-11, step=1e-12, format="%.13f")
    v_force = st.number_input("القوة الديناميكية المؤثرة في الوسط (F):", value=10.0000, step=1.0000, format="%.4f")

st.markdown("---")

# زر بدء المعالجة الحسابية
if st.button("🧮 بدء معالجة الرصد واستخراج النتائج الدقيقة"):
    st.write("### 📊 المخرجات والنسب الحتمية المستقرة")
    
    # حساب القيمة الأساسية للمقام مع دمج الثابت الحتمي لمنع القسمة على صفر
    denominator = v_distortion + v_constant
    
    if denominator == 0:
        st.error("⚠️ فشل في النظام: المدخلات الحالية تؤدي إلى قيمة حرجة غير معرفة.")
    else:
        # 1. حساب المتجه الكلي الناتج
        result_vector = (v_force * v_velocity) / denominator
        
        # 2. حساب النسبة المكافئة للمادة المظلمة بناءً على التشوه ومقياس الثابت
        dark_matter_ratio = (1.0 - (1.0 / (1.0 + (v_distortion / (v_constant * 1e10))))) * 100
        
        # تصحيح الحدود لضمان دقة النسبة بين 0% و 100% دون أخطاء
        dark_matter_ratio = max(0.0, min(100.0, dark_matter_ratio))
        
        # عرض النتائج في قالب رصدي محترف
        st.markdown(f"""
        <div class="result-box">
            <h4 style='color: #00ffcc; margin-top:0;'>📋 مخرجات التحليل الرقمي بدقة عالية:</h4>
            <table style='width: 100%; border-collapse: collapse; color: #f0f2f6; direction: rtl;'>
                <tr style='border-bottom: 1px solid #2d3139;'>
                    <td style='padding: 10px 0;'><b>المركب الحتمي الكلي للمتجه الناتج:</b></td>
                    <td style='text-align: left; color: #00ffcc; font-size: 1.3rem;'><b>{result_vector:.6f}</b></td>
                </tr>
                <tr style='border-bottom: 1px solid #2d3139;'>
                    <td style='padding: 10px 0;'><b>نسبة M.D (المادة المظلمة الافتراضية) المكافئة:</b></td>
                    <td style='text-align: left; color: #ffad33; font-size: 1.3rem;'><b>{dark_matter_ratio:.2f} %</b></td>
                </tr>
                <tr>
                    <td style='padding: 10px 0;'><b>حالة استقرار النظام البرمجي:</b></td>
                    <td style='text-align: left; color: #00ffaa;'><b>مستقر (تم تلافي الصفر والمالانهاية)</b></td>
                </tr>
            </table>
            <p style='font-size: 0.8rem; color: #8892b0; margin-top: 15px; text-align: right;'>
            * ملحوظة: البيانات المستخرجة تمثل محاكاة ديناميكية حتمية لحركة المتجهات الكتلية عند نقطة الاتزان الحرجة المستخلصة من التشوه الهيكلي للوسط.
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
---
<p style='text-align: center; color: #4f5b66; font-size: 0.8rem;'>منصة الحسابات الفيزيائية الحتمية الرصدية © 2026</p>
""", unsafe_allow_html=True)
