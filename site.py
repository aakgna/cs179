import pyspark
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegressionModel
from pyspark.ml.feature import VectorAssembler

# Load the PySpark session
# spark = pyspark.sql.SparkSession.builder.appName("LinearRegressionApp").getOrCreate()
spark = SparkSession.builder \
                    .master("yarn") \
                    .appName("My App") \
                    .getOrCreate()

# Load the saved model
model_path = "/home/cs179g/workspace/ml_data/model_AllData"
model = LinearRegressionModel.load(model_path)

# Specify the input column names
input_cols = ["startingAirport_mapped", "destinationAirport_mapped", "isBasicEconomy_mapped", "seatsRemaining", "segmentsAirlineName_mapped"]

# Create a VectorAssembler to combine the input features
feature_assembler = VectorAssembler(inputCols=input_cols, outputCol="features")

def predict(features):
    # Convert the input features to a PySpark DataFrame
    df = spark.createDataFrame([features])

    # Combine the features using VectorAssembler
    feature_vector = feature_assembler.transform(df)

    # Make predictions using the loaded model
    predictions = model.transform(feature_vector)

    # Extract the prediction result
    prediction = predictions.select("prediction").collect()[0]["prediction"]

    return prediction

import streamlit as st

def app():
    st.title("Linear Regression Model")

    # Get user input features
    starting_airport = st.sidebar.number_input("Starting Airport", value=0.0)
    destination_airport = st.sidebar.number_input("Destination Airport", value=0.0)
    is_basic_economy = st.sidebar.number_input("Is Basic Economy", value=0.0)
    seats_remaining = st.sidebar.number_input("Seats Remaining", value=0.0)
    airline_name = st.sidebar.number_input("Airline Name", value=0.0)

    # Create a dictionary with the input features
    input_features = {
        "startingAirport_mapped": starting_airport,
        "destinationAirport_mapped": destination_airport,
        "isBasicEconomy_mapped": is_basic_economy,
        "seatsRemaining": seats_remaining,
        "segmentsAirlineName_mapped": airline_name,
    }

    # Make a prediction using the input features
    prediction = predict(input_features)

    # Display the prediction result
    st.write(f"The predicted value is: {prediction}")

if __name__ == "__main__":
    app()
