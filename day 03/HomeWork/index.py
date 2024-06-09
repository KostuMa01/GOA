age = 19
height = 1.83
name = "გიო"
is_student = ""
favorite_colors = ["შავი", "ყვითელი", "წითელი"]
city = "თბილისში"
person_info = {"name": "გიო", "age": 19, "height": 1.83}


sentence = (
    f"გაიცანით {name}, {age} წლის, რომელიც არის {height} მეტრის სიმაღლის. "
    f"მართალია {is_student} რომ ის სტუდენტია. "
    f"მისი საყვარელი ფერები არის {', '.join(favorite_colors)}. "
    f"ის ცხოვრობს {city}. "
    f"მისი პერსონალური ინფორმაცია: {person_info}. "
)

print(sentence)
