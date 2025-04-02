import streamlit as st

def calculate_bmi(weight, height):
    """Compute the Body Mass Index (BMI) from weight (kg) and height (m)."""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def main():
    st.title("🔢 BMI Calculator")
    st.write("Easily determine your Body Mass Index (BMI) and assess your health status.")

    # User Input
    weight = st.number_input("Enter your weight in kilograms (kg):", min_value=1.0, format="%.2f")
    height = st.number_input("Enter your height in meters (m):", min_value=0.5, format="%.2f")

    if st.button("Compute BMI"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"Your BMI Score: {bmi}")

            # BMI Classification
            if bmi < 18.5:
                st.warning("🚨 You are underweight. Consider a balanced diet!")
            elif 18.5 <= bmi < 24.9:
                st.success("🎉 Great! You have a healthy weight.")
            elif 25 <= bmi < 29.9:
                st.warning("⚠️ You are overweight. Exercise and diet can help!")
            else:
                st.error("❌ Obesity detected! Prioritize a healthier lifestyle.")
        else:
            st.error("⚠️ Please enter a valid height.")

if __name__ == "__main__":
    main()
