# 🐥 Chicken Suitability Checker API 🌡️

**Built for: [Hack4Livestock Hackathon 2025]**  
A temperature-based tool to help poultry farmers decide if it's suitable to place **young chicks** based on **7-day weather predictions**.

---

## 🚀 API Overview

This FastAPI service uses **Google Gemini 2.0** to predict average temperatures for the next 7 days in a given location and determines whether the climate is suitable for placing young chickens.

Supports multi-language responses in **English** and **Hausa**.

---

## 📡 Endpoints

### 🔍 `POST /check-suitability`

Check if a location is suitable for raising chicks based on projected heat conditions.

**Request Body:**

| Field     | Type   | Required | Description                                  |
|-----------|--------|----------|----------------------------------------------|
| `location`| string | ✅ Yes   | City, village, or area name (e.g., "Kano")   |
| `lang`    | string | ❌ No    | `"english"` (default) or `"hausa"`           |

**Example (JSON):**

```json
{
  "location": "Kano",
  "lang": "hausa"
}
```

## 📤 Sample Response

```json
{
  "location": "Kano",
  "average_temperature_celsius": 38.57,
  "suitability": "AN YARDA",
  "message": "✅ Matsakaicin zafin jiki yana tsammanin BA zai wuce 40°C ba..."
}
```
## 🏠 GET `/`

Returns a welcome message and basic usage guide.

### 📥 Sample Response

```json
{
  "message": "Welcome to the Chicken Suitability Checker API! Use POST /check-suitability...",
  "hausa_message": "Barka da zuwa API na Duba Yanayin Kaji..."
}
```

---

## 🛠️ How It Works

- 📍 Accepts a `location` name and optional `lang` (`english` or `hausa`).
- 🔮 Uses **Google Gemini** to simulate a **7-day temperature forecast**.
- 📊 Parses predicted values and calculates the **average temperature**.
- ✅ Determines suitability for placing chicks (based on **40°C threshold**).
- 🗣️ Returns responses in either **English or Hausa** based on the `lang` field.

---

## 📈 Why It Matters

- 🐣 **Protects young poultry** from fatal heat exposure during placement.
- 🧑‍🌾 **Empowers local farmers** with AI-driven, language-specific insights.
- 📱 Optimized for **mobile and lightweight usage**, even in rural zones.
- 🌍 Designed to be **accessible in Hausa** for inclusive decision-making.

---

## 🧪 Tech Stack

| Tool       | Purpose                                      |
|------------|----------------------------------------------|
| FastAPI    | Backend API framework                        |
| Gemini     | Temperature forecast generation              |
| pydantic   | Request validation & structure enforcement   |
| random     | Distributes load across multiple API keys    |
| os.getenv  | Securely loads API keys from environment     |

---

## ⚠️ Limitations

- 🔌 **Internet Required** – Gemini is a cloud-based model.
- 🧪 **Simulated Forecast** – Not actual meteorological data.
- 🌡️ **Prediction Variability** – Dependent on LLM output accuracy.

---

## 🔮 Future Improvements

- 🛰️ Integrate with real weather APIs (e.g., OpenWeather, WeatherStack)
- 📴 Enable offline support using local quantized LLMs
- 🌍 Expand to more languages: **Yoruba**, **Igbo**, **Fulfulde**
- 📊 Build visual dashboards for temperature trends
- 🤖 Integrate with other livestock decision systems

---

## 👨‍💻 Developers

- 🧪 **Project by**: EJAZTECH.AI  
- 👨‍🔬 **Lead Developer**: Ismail Ismail Tijjani  
- 🏫 **Institution**: Bayero University, Kano  
- 🏁 **Hackathon**: Hack4Livestock Hackathon 2025

---

## 📜 License

This project is licensed under the **MIT License**  
✅ Free to use, distribute, and build upon with proper attribution.

---

## 🤝 Contributing

We welcome contributions from everyone!

- 🍴 **Fork** this repository  
- ✅ **Submit** a pull request  
- 💬 **Suggest** improvements or new features  

**Let’s help rural farmers make smarter, heat-aware poultry decisions!** 🐔🔥

