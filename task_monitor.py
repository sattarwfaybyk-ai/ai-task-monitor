"""Vazifalar soni va vaqtini tekshiruvchi o'quv dasturi."""
import ast
import math

VAZIFA_LIMITI = 3
VAQT_LIMITI = 30


def task_monitor(vaqtlar):
    """Daqiqalar ro'yxatini tekshiradi va natija lug'atini qaytaradi."""
    if not isinstance(vaqtlar, list):
        raise ValueError("Ro'yxat kiriting, masalan [10, 5].")
    for tartib, vaqt in enumerate(vaqtlar, start=1):
        if isinstance(vaqt, bool) or not isinstance(vaqt, (int, float)):
            raise ValueError(f"{tartib}-vazifa vaqti son bo'lishi kerak.")
        if isinstance(vaqt, float) and not math.isfinite(vaqt):
            raise ValueError(f"{tartib}-vazifa vaqti chekli son bo'lishi kerak.")
        if vaqt < 0:
            raise ValueError(f"{tartib}-vazifa vaqti manfiy bo'lishi mumkin emas.")
    soni = len(vaqtlar)
    jami = sum(vaqtlar)
    vazifa_oshgan = soni > VAZIFA_LIMITI
    vaqt_oshgan = jami > VAQT_LIMITI
    if vazifa_oshgan and vaqt_oshgan:
        holat = "ikkala limit oshgan"
    elif vaqt_oshgan:
        holat = "faqat vaqt limiti oshgan"
    elif vazifa_oshgan:
        holat = "faqat vazifa limiti oshgan"
    else:
        holat = "me'yorida"
    return {"vazifalar_soni": soni, "umumiy_vaqt": jami, "holat": holat}


def main():
    print("AI Task Monitor")
    try:
        matn = input("Vaqtlarni kiriting, masalan [10, 10, 10]: ")
        try:
            # Ma'lumotni o'qiydi, kiritilgan kodni bajarmaydi.
            vaqtlar = ast.literal_eval(matn)
        except (ValueError, SyntaxError):
            raise ValueError("To'g'ri ro'yxat kiriting, masalan [10, 5].") from None
        natija = task_monitor(vaqtlar)
    except ValueError as xato:
        print(f"Xatolik: {xato}")
        return 1
    except EOFError:
        print("Xatolik: ro'yxat kiritilmadi.")
        return 1
    print(f"Vazifalar soni: {natija['vazifalar_soni']}")
    print(f"Umumiy vaqt: {natija['umumiy_vaqt']} daqiqa")
    print(f"Holat: {natija['holat']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
