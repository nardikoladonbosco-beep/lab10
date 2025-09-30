shuma = 0.0

while True:
    hyrje = input("Vlera: ").strip().lower()
    if hyrje == "stop":
        break
    try:
        numri = float(hyrje)
        shuma += numri
    except ValueError:
        print("Vlerë e pavlefshme")
        continue

print(f"Shuma: {shuma:.2f}")
