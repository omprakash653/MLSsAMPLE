# from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData,PredictPipeline

# from flask import Flask,request,render_template,jsonify


# app=Flask(__name__)


# # @app.route('/')
# # def home_page():
# #     return render_template("index.html")


# @app.route("/",methods=["GET","POST"])
# def predict_datapoint():
#     if request.method == "GET":
#         return render_template("form.html")
    
#     else:
#         data=CustomData(
            
#             carat=float(request.form.get('carat')),
#             depth = float(request.form.get('depth')),
#             table = float(request.form.get('table')),
#             x = float(request.form.get('x')),
#             y = float(request.form.get('y')),
#             z = float(request.form.get('z')),
#             cut = request.form.get('cut'),
#             color= request.form.get('color'),
#             clarity = request.form.get('clarity')
#         )
        
#         final_data=data.get_data_as_dataframe()
        
#         predict_pipeline=PredictPipeline()
        
#         pred=predict_pipeline.predict(final_data)
        
#         result=round(pred[0],2)
        
#         return render_template("result.html",final_result=result)

# if __name__ == '__main__':
#     app.run(debug=True)




from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData, PredictPipeline
from flask import Flask, request, render_template,redirect

app = Flask(__name__)
EXCHANGE_RATE = 83

@app.route('/')
def home_page():
    return render_template("index.html")
@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        # Collect data from the form
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )

        # Convert data to a dataframe
        final_data = data.get_data_as_dataframe()

        # Predict the result
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_data)
        result = round(pred[0], 2)

        # Convert result to INR
        final_result = round(result * EXCHANGE_RATE, 2)


        # Determine background color and image based on the result
        
        if final_result <= 951*83:
            bg_color = "red"
            image_path = "images/red-icon.jpg"
        elif final_result > 951*83 and final_result <= 2401*83:
            bg_color = "green"
            image_path = "images/green-icon.jpg"
        elif final_result > 2401*83 and final_result <= 5408*83:
            bg_color = "blue"
            image_path = "images/blue-icon.jpg"
        else:
            bg_color = "grey"
            image_path = "images/grey-icon.jpg"

        # Render the result page
        return render_template(
        "result.html",
        final_result=final_result,
        bg_color=bg_color,
        image_path=image_path
    )


if __name__ == '__main__':
    app.run(debug=True)
