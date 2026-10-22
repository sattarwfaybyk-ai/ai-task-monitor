"""Avtomatik testlar: python3 -m unittest -v."""
import unittest
from task_monitor import task_monitor


class TaskMonitorTest(unittest.TestCase):
    def test_meyorida(self):
        self.assertEqual(task_monitor([10, 10, 10]), {
            "vazifalar_soni": 3, "umumiy_vaqt": 30, "holat": "me'yorida"})

    def test_faqat_vaqt(self):
        self.assertEqual(task_monitor([15, 10, 6])["holat"], "faqat vaqt limiti oshgan")

    def test_faqat_vazifa(self):
        self.assertEqual(task_monitor([5, 5, 5, 5])["holat"], "faqat vazifa limiti oshgan")

    def test_ikkala_limit(self):
        self.assertEqual(task_monitor([10, 10, 10, 5])["holat"], "ikkala limit oshgan")

    def test_bosh_royxat(self):
        self.assertEqual(task_monitor([]), {
            "vazifalar_soni": 0, "umumiy_vaqt": 0, "holat": "me'yorida"})

    def test_manfiy(self):
        with self.assertRaisesRegex(ValueError, "manfiy"):
            task_monitor([10, -5])

    def test_son_emas(self):
        for qiymat in ["salom", "10", None, True, [], {}]:
            with self.subTest(qiymat=qiymat):
                with self.assertRaisesRegex(ValueError, "son bo'lishi kerak"):
                    task_monitor([qiymat])

    def test_royxat_emas(self):
        with self.assertRaisesRegex(ValueError, "Ro'yxat"):
            task_monitor("10, 20")

    def test_cheksiz_va_nan(self):
        for qiymat in [float("inf"), float("-inf"), float("nan")]:
            with self.subTest(qiymat=qiymat):
                with self.assertRaisesRegex(ValueError, "chekli"):
                    task_monitor([qiymat])

    def test_nol_va_kasr(self):
        self.assertEqual(task_monitor([0, 10.5, 19.5])["holat"], "me'yorida")

    def test_qoshimcha_holatlar(self):
        holatlar = [
            ([], 0, 0, "me'yorida"),
            ([0, 0, 0], 3, 0, "me'yorida"),
            ([30], 1, 30, "me'yorida"),
            ([31], 1, 31, "faqat vaqt limiti oshgan"),
            ([1, 1, 1, 1], 4, 4, "faqat vazifa limiti oshgan"),
            ([10.5, 5], 2, 15.5, "me'yorida"),
        ]
        for vaqtlar, soni, jami, holat in holatlar:
            with self.subTest(vaqtlar=vaqtlar):
                self.assertEqual(task_monitor(vaqtlar), {
                    "vazifalar_soni": soni, "umumiy_vaqt": jami, "holat": holat})

    def test_qoshimcha_xatolar(self):
        holatlar = [
            ([-5, 10], "1-vazifa vaqti manfiy bo'lishi mumkin emas."),
            ([10, "abc"], "2-vazifa vaqti son bo'lishi kerak."),
        ]
        for vaqtlar, xabar in holatlar:
            with self.subTest(vaqtlar=vaqtlar):
                with self.assertRaises(ValueError) as natija:
                    task_monitor(vaqtlar)
                self.assertEqual(str(natija.exception), xabar)


if __name__ == "__main__":
    unittest.main()
