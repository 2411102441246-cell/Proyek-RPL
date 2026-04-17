class VehicleType:
    GORIDE = "GORIDE"
    GOCAR = "GOCAR"

# Konstanta untuk menghindari Magic Numbers
RATES = {
    VehicleType.GORIDE: {"per_km": 2000, "per_minute": 500, "promo_discount": 5000},
    VehicleType.GOCAR: {"per_km": 5000, "per_minute": 1000, "promo_discount": 10000}
}

def calculate_base_fare(distance_km, time_minutes, vehicle_type):
    """Menghitung tarif dasar berdasarkan jarak dan waktu."""
    rates = RATES.get(vehicle_type)
    if not rates:
        raise ValueError("Tipe kendaraan tidak valid")
    return (distance_km * rates["per_km"]) + (time_minutes * rates["per_minute"])

def apply_promo_discount(fare, vehicle_type, has_promo):
    """Menerapkan diskon jika ada promo."""
    if not has_promo:
        return fare
    discount = RATES[vehicle_type]["promo_discount"]
    return max(0, fare - discount)

def calculate_total_fare(distance_km, time_minutes, vehicle_type, has_promo=False):
    """Fungsi utama untuk menghitung total tarif (SRP)."""
    base_fare = calculate_base_fare(distance_km, time_minutes, vehicle_type)
    total_fare = apply_promo_discount(base_fare, vehicle_type, has_promo)
    return total_fare

def print_receipt(total_fare):
    """Fungsi terpisah khusus untuk mencetak (SRP)."""
    print(f"Total harga adalah: Rp {total_fare}")
