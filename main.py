# import os
# import sys
#
# # اضافه کردن مسیر src به sys.path
# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
#
# from src.config import MODEL_PATH
# from src.loader import load_data
# from src.trainer import train_and_save_model
# from src.predictor import predict_message
#
#
# def main():
#     print("=" * 50)
#     print("📧 Spam Filter - Spam Detection System")
#     print("=" * 50)
#
#     # ۱. بارگذاری دیتاست
#     print("\n[1/3] Loading dataset...")
#     df = load_data()
#
#     # ۲. آموزش یا بارگذاری مدل
#     if not os.path.exists(MODEL_PATH):
#         print(f"\n[2/3] Model not found at {MODEL_PATH}")
#         print("Training new model...")
#         train_and_save_model(df)
#     else:
#         print(f"\n[2/3] Model found at {MODEL_PATH}")
#         print("Skipping training.")
#
#     # ۳. تست با چند نمونه
#     print("\n[3/3] Testing model with sample messages:")
#     print("-" * 50)
#
#     test_messages = [
#         "Congratulations! You won a free iPhone. Click here now!",
#         "Hey, are we still meeting for lunch tomorrow?",
#         "URGENT: Your account has been compromised. Verify now!",
#         "Don't forget to bring the documents to the meeting.",
#     ]
#
#     for i, msg in enumerate(test_messages, 1):
#         result = predict_message(msg)
#         emoji = "🚫" if result['prediction'] == 'spam' else "✅"
#         print(f"\n{i}. {msg[:70]}...")
#         print(f"   {emoji} Prediction: {result['prediction'].upper()}")
#         print(f"   📊 Ham: {result['ham_prob']:.2%} | Spam: {result['spam_prob']:.2%}")
#
#     print("\n" + "=" * 50)
#     print("Done! Run 'python -m src.ui' to launch the web interface.")
#     print("=" * 50)
#
#
# if __name__ == '__main__':
#     main()