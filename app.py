import streamlit as st
import numpy as np

# إعداد واجهة التطبيق
st.set_page_config(page_title="المستشار الكرونوديناميكي", page_icon="🌊")
st.title("🌊 المستشار الفيزيائي الحتمي الكرونوديناميكي")
st.write("نظام مستقل محكوم بنظرية محيط الزمن وقانون إلغاء الصفر والمالانهاية - الباحث المستقل: محمد موسى يوسف")

# الثوابت الصارمة للنظام
ETA_Y = 1e-11

st.header("🔬 وحدة الحساب الديناميكي للوسط")

# خانات الإدخال للمستخدم
value_input = st.number_input("أدخل القيمة المادية (المقدار الحركي):", value=0.0, step=1.0)
omega_input = st.number_input("أدخل السرعة الزاوية للوسط الدوار (الدوامة) ω:", value=1e9, step=1e8)

if st.button("احسب النتيجة الحتمية للوسط"):
    # 1. تطبيق قانون إلغاء الصفر المطلق
    if abs(value_input) < ETA_Y:
        retained_value = ETA_Y
        st.warning(f"⚠️ تم رصد محاولة إدخال قيمة صفرية! النظام قام تلقائياً بإلغاء الصفر والتعويض بممانعة الوسط الحتمية: {ETA_Y}")
    else:
        retained_value = value_input

    # 2. حساب الانحراف الزاوي الحتمي بناءً على ثابت يوسف
    delta_theta_rad = ETA_Y * omega_input
    delta_theta_deg = np.degrees(delta_theta_rad)

    # 3. حساب الممانعة وتعديل المقدار
    final_magnitude = retained_value / (1 + ETA_Y * abs(omega_input))

    # عرض النتائج بصيغة علمية صارمة
    st.success("📊 النطق بالحقيقة الفيزيائية الحتمية للوسط:")
    st.write(f"**المقدار الحركي النهائي بعد الممانعة:** {final_magnitude:.6e}")
    st.write(f"**الانحراف الزاوي الحتمي الناتح (زاوية انكسار الزمن):** {delta_theta_deg:.6f}°")
    
    st.info("💡 هذا الحساب ناتج مباشرة عن دمج ثابت يوسف الكوني الكاشف لشذوذ المادة المظلمة، دون استخدام احتمالات لغوية.")
