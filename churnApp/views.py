import os
import pickle
import pandas as pd

from django.conf import settings
from django.shortcuts import render
from django.views import View

from .forms import ChurnForm


class PredictView(View):
    template_name = 'create.html'

    def get(self, request):
        form = ChurnForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ChurnForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            input_df = pd.DataFrame([{
                "Gender": data["Gender"],
                "Age": data["Age"],
                "MembershipType": data["MembershipType"],
                "PreferredCategory": data["PreferredCategory"],
                "TotalOrders": data["TotalOrders"],
                "TotalSpent": data["TotalSpent"],
                "LastPurchaseDaysAgo": data["LastPurchaseDaysAgo"],
                "PurchaseFrequencyPerMonth": data["PurchaseFrequencyPerMonth"],
                "AppLoginFrequency": data["AppLoginFrequency"],
                "CouponUsageCount": data["CouponUsageCount"],
                "ReturnCount": data["ReturnCount"],
                "SatisfactionScore": data["SatisfactionScore"],
            }])

            # Load encoders
            encoders_path = os.path.join(settings.BASE_DIR, "fashion_rf_label_encoders.pkl")
            target_encoder_path = os.path.join(settings.BASE_DIR, "fashion_rf_target_encoder.pkl")
            model_path = os.path.join(settings.BASE_DIR, "fashion_churn_rf_model.pkl")

            label_encoders = pickle.load(open(encoders_path, "rb"))
            target_encoder = pickle.load(open(target_encoder_path, "rb"))
            model = pickle.load(open(model_path, "rb"))

            # Encode categorical columns like notebook style
            for col in input_df.columns:
                if col in label_encoders:
                    try:
                        input_df[col] = label_encoders[col].transform(input_df[col].astype(str))
                    except ValueError:
                        # Unknown category fallback
                        input_df[col] = 0

            # Predict
            pred = model.predict(input_df)
            final_result = target_encoder.inverse_transform(pred)[0]

            if str(final_result).lower() == "yes":
                result = "Customer Likely To Churn (Withdraw)"
            else:
                result = "Customer Will Stay (Continue)"

            # Optional confidence
            confidence = None
            if hasattr(model, "predict_proba"):
                probs = model.predict_proba(input_df)[0]
                confidence = round(max(probs) * 100, 2)

            return render(request, 'result.html', {
                'result': result,
                'raw_result': final_result,
                'confidence': confidence
            })

        return render(request, self.template_name, {'form': form})
