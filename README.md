# AI Task Monitor

Bu dastur vazifalar soni va sarflangan daqiqalarni tekshiradi.
Python 3 kerak. Tashqi kutubxona ishlatilmaydi.
Bu boshlang'ich versiya oddiy qoidalar bilan ishlaydi.

## Ishga tushirish

Uchala faylni bitta papkada saqlang. Terminalda shu papkani oching:

```bash
python3 task_monitor.py
```

Dastur so'raganda ro'yxat kiriting: `[10, 10, 10]`.
Har bir son bitta vazifaga sarflangan daqiqadir.

```text
Vazifalar soni: 3
Umumiy vaqt: 30 daqiqa
Holat: me'yorida
```

Agar Python 3 kompyuteringizda `python` buyrug'i bilan ishlasa,
buyruqlarda `python3` o'rniga `python` yozing.

## Qoidalar

Vazifalar soni faqat 3 dan KATTA bo'lsa, vazifa limiti oshadi.
Umumiy vaqt faqat 30 dan KATTA bo'lsa, vaqt limiti oshadi.
Aynan 3 ta vazifa va 30 daqiqa me'yorida.

| Ro'yxat | Holat |
| --- | --- |
| [10, 10, 10] | me'yorida |
| [15, 10, 6] | faqat vaqt limiti oshgan |
| [5, 5, 5, 5] | faqat vazifa limiti oshgan |
| [10, 10, 10, 5] | ikkala limit oshgan |
| [] | me'yorida |

Bo'sh ro'yxat uchun vazifalar soni va umumiy vaqt 0 bo'ladi.
Nol va kasr sonlar ham qabul qilinadi: `[0, 2.5]`.
Manfiy va son bo'lmagan qiymatlar qabul qilinmaydi.
Masalan, `[10, -5]` uchun:
`Xatolik: 2-vazifa vaqti manfiy bo'lishi mumkin emas.`

## Kod qanday ishlaydi?

`task_monitor(vaqtlar)` avval har bir vaqtni tekshiradi.
`len(vaqtlar)` vazifalar sonini, `sum(vaqtlar)` jami vaqtni hisoblaydi.
`>` belgisi limitdan kattaligini tekshiradi.
`if/elif/else` to'rtta holatdan birini tanlaydi.
Natija lug'at (`dict`) sifatida qaytariladi.

`main()` foydalanuvchidan ro'yxat oladi va natijani chiqaradi.
`ValueError` noto'g'ri qiymatni bildiradi.
`try/except` xatoni ushlab, tushunarli xabar chiqaradi.
`ast.literal_eval` ro'yxatni o'qiydi, kiritilgan kodni bajarmaydi.
`ast`, `math` va `unittest` Python tarkibida mavjud.

## Avtomatik tekshirish

Fayllar joylashgan papkada:

```bash
python3 -m unittest -v
```

10 ta test beshta asosiy holatni hamda noto'g'ri qiymatlar, nol va kasrlarni
tekshiradi. Hammasi o'tsa, oxirida `OK` yozuvi chiqadi.
