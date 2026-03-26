import pandas as pd
import numpy as np
from openai import OpenAI

# 1. Підключення до твого локального ШІ (LM Studio)
# Зверни увагу: base_url вказує на твій власний комп'ютер!
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def load_budget_data(file_path="budget.csv"):
    """Завантажує дані місцевого бюджету з реального CSV-файлу"""
    print(f"📊 Завантажуємо дані з реєстрів (файл {file_path})...")
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"❌ Помилка: Файл {file_path} не знайдено. Покладіть файл у папку зі скриптом.")
        exit()

def find_anomalies_zscore(df, threshold=3.0):
    """Математичний пошук аномалій (Z-Score)"""
    print("🧮 Запускаємо математичний аналіз (Z-Score)...")
    mean = df['Amount_UAH'].mean()
    std = df['Amount_UAH'].std()
    
    # Рахуємо Z-Score для кожної транзакції
    df['Z_Score'] = (df['Amount_UAH'] - mean) / std
    
    # Відфільтровуємо те, що виходить за межі норми
    anomalies = df[df['Z_Score'] > threshold]
    return anomalies

def analyze_with_local_ai(anomaly_data):
    """Відправляє знайдену аномалію в локальну Gemma 3 для аналізу"""
    amount = anomaly_data['Amount_UAH'].values[0]
    category = anomaly_data['Category'].values[0]
    
    prompt = f"""
    Ти - професійний державний аудитор. Ми автоматично виявили підозрілу транзакцію в місцевому бюджеті:
    Категорія: {category}
    Сума: {amount:,.2f} грн.
    
    Середня сума транзакції в цій категорії зазвичай становить близько 500,000 грн. 
    Проаналізуй цю аномалію. Які корупційні ризики тут можуть бути? Що саме треба перевірити слідчим?
    Напиши короткий, структурований висновок.
    """
    
    print(f"🤖 Відправляємо транзакцію на {amount:,.2f} грн у локальну нейромережу...")
    
    # Звернення до твоєї відеокарти
    response = client.chat.completions.create(
        model="google/gemma-3-4b", # Назва не так важлива, LM Studio використає завантажену
        messages=[
            {"role": "system", "content": "Ти експерт з антикорупційних розслідувань."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3 # Низька температура для більш точної і строгої відповіді
    )
    
    return response.choices[0].message.content

# --- ГОЛОВНИЙ ПРОЦЕС ---
if __name__ == "__main__":
    # Етап 1: Дані (тепер вантажимо з реального CSV файлу!)
    budget_df = load_budget_data()
    
    # Етап 2: Математика знаходить відхилення
    suspicious_transactions = find_anomalies_zscore(budget_df)
    
    if not suspicious_transactions.empty:
        print(f"⚠️ Знайдено аномалій: {len(suspicious_transactions)} шт. Передаю ШІ на експертизу...\n")
        # Етап 3: ШІ робить висновок
        ai_report = analyze_with_local_ai(suspicious_transactions)
        
        print("="*50)
        print("📄 ЗВІТ ШІ-АУДИТОРА (Сгенеровано на RTX 3060):")
        print("="*50)
        print(ai_report)
        print("="*50)
    else:
        print("✅ Аномалій не знайдено, всі витрати в нормі.")