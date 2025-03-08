import streamlit as st
from pint import UnitRegistry

# Initialize UnitRegistry
uReg = UnitRegistry()
st.title("Unit Converter")

categories = {
    'Length': ["meter", "kilometer", "centimeter", "millimeter", "micrometer", "nanometer", "mile", "yard", "foot", "inch"],
    'Mass': ["kilogram", "gram", "milligram", "microgram", "ton", "pound", "ounce"],
    'Time': ["second", "minute", "hour", "day", "week", "month", "year"],
    'Temperature': ["celsius", "fahrenheit", "kelvin"],
    'Speed': ["meter/second", "kilometer/hour", "mile/hour"],
    'Area': ["square meter", "hectare", "square kilometer", "square foot", "square mile", "acre"],
    'Volume': ["cubic meter", "liter", "milliliter", "cubic foot", "cubic inch", "gallon", "quart", "pint", "cup", "fluid ounce"],
    'Pressure': ["pascal", "kilopascal", "bar", "psi", "ksi"],
    'Energy': ["joule", "kilojoule", "calorie", "kilocalorie", "watt hour", "kilowatt hour", "electronvolt"],
    'Power': ["watt", "kilowatt", "horsepower"],
    'Data': ["bit", "byte", "kilobit", "kilobyte", "megabit", "megabyte", "gigabit", "gigabyte", "terabit", "terabyte", "petabit", "petabyte"],
    'Frequency': ["hertz", "kilohertz", "megahertz", "gigahertz"],
    'Angle': ["radian", "degree", "gradian", "minute", "second"],
    'Fuel Consumption': ["miles/gallon", "liter/100km"],
    'Digital Storage': ["bit", "byte", "kilobit", "kilobyte", "megabit", "megabyte", "gigabit", "gigabyte", "terabit", "terabyte", "petabit", "petabyte"],
}

# Dropdowns
category = st.selectbox("Select a category", categories.keys())
from_unit = st.selectbox("From unit", categories[category])
to_unit = st.selectbox("To unit", categories[category])

# User Input
value = st.number_input("Enter a value", min_value=0.0, step=0.1)

# Convert Button
if st.button("Convert"):
    try:
        if category == 'Temperature':
            if from_unit == 'celsius' and to_unit == 'fahrenheit':
                result = (value * 9/5) + 32
            elif from_unit == 'celsius' and to_unit == 'kelvin':
                result = value + 273.15
            elif from_unit == 'fahrenheit' and to_unit == 'celsius':
                result = (value - 32) * 5/9
            elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == 'kelvin' and to_unit == 'celsius':
                result = value - 273.15
            elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
                result = (value - 273.15) * 9/5 + 32  
            else:
                result = value
        else:
            # Convert using pint
            result = uReg.Quantity(value, from_unit).to(to_unit).magnitude

        # Display Result
        st.success(f"{value} {from_unit} = {result} {to_unit}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
