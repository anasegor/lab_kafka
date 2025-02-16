from sklearn.preprocessing import LabelEncoder


def map_city(city):
    if city in [
        "Ahmedabad",
        "Bangalore",
        "Chennai",
        "Delhi",
        "Hyderabad",
        "Kolkata",
        "Mumbai",
        "Pune",
    ]:
        return "tier1"
    elif city in [
        "Agra",
        "Ajmer",
        "Aligarh",
        "Amravati",
        "Amritsar",
        "Asansol",
        "Aurangabad",
        "Bareilly",
        "Belgaum",
        "Bhavnagar",
        "Bhiwandi",
        "Bhopal",
        "Bhubaneswar",
        "Bikaner",
        "Bilaspur",
        "Bokaro Steel City",
        "Chandigarh",
        "Coimbatore",
        "Cuttack",
        "Dehradun",
        "Dhanbad",
        "Bhilai",
        "Durgapur",
        "Dindigul",
        "Erode",
        "Faridabad",
        "Firozabad",
        "Ghaziabad",
        "Gorakhpur",
        "Gulbarga",
        "Guntur",
        "Gwalior",
        "Gurgaon",
        "Guwahati",
        "Hamirpur",
        "Hubli–Dharwad",
        "Indore",
        "Jabalpur",
        "Jaipur",
        "Jalandhar",
        "Jammu",
        "Jamnagar",
        "Jamshedpur",
        "Jhansi",
        "Jodhpur",
        "Kakinada",
        "Kannur",
        "Kanpur",
        "Karnal",
        "Kochi",
        "Kolhapur",
        "Kollam",
        "Kozhikode",
        "Kurnool",
        "Ludhiana",
        "Lucknow",
        "Madurai",
        "Malappuram",
        "Mathura",
        "Mangalore",
        "Meerut",
        "Moradabad",
        "Mysore",
        "Nagpur",
        "Nanded",
        "Nashik",
        "Nellore",
        "Noida",
        "Patna",
        "Pondicherry",
        "Purulia",
        "Prayagraj",
        "Raipur",
        "Rajkot",
        "Rajahmundry",
        "Ranchi",
        "Rourkela",
        "Ratlam",
        "Salem",
        "Sangli",
        "Shimla",
        "Siliguri",
        "Solapur",
        "Srinagar",
        "Surat",
        "Thanjavur",
        "Thiruvananthapuram",
        "Thrissur",
        "Tiruchirappalli",
        "Tirunelveli",
        "Tiruvannamalai",
        "Ujjain",
        "Bijapur",
        "Vadodara",
        "Varanasi",
        "Vasai-Virar City",
        "Vijayawada",
        "Visakhapatnam",
        "Vellore",
        "Warangal",
    ]:
        return "tier2"
    else:
        return "tier3"


def preprocess_data(data, map_city):

    data["ADDRESS"] = data["ADDRESS"].str.split(",").str[-1].str.strip()
    data["city_tier"] = data["ADDRESS"].apply(map_city)
    data.drop(["POSTED_BY", "BHK_OR_RK", "ADDRESS"], axis=1, inplace=True)
    encoder = LabelEncoder()
    data["city_tier"] = encoder.fit_transform(data["city_tier"])

    return data


# def train_and_save():
#     data = pd.read_csv("train.csv")

#     data = preprocess_data(data, map_city)

#     target = data["TARGET(PRICE_IN_LACS)"]
#     data = data.drop(["TARGET(PRICE_IN_LACS)"], axis=1)

#     X_train, X_test, y_train, y_test = train_test_split(
#         data, target, test_size=0.1, random_state=42
#     )

#     model = DecisionTreeRegressor()
#     model.fit(X_train, y_train)
#     preds = model.predict(X_test)
#     print(r2_score(preds, y_test))

#     joblib.dump(model, "decision_tree_model.pkl")


# if __name__ == "__main__":
#     train_and_save()
