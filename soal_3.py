class Student:
    lulus = 0
    tidak_lulus = 0
    def __init__(self, name, nilai, absen):
        self.name = name
        self.nilai = nilai
        self.absen = absen

    def status(self):
        if self.nilai > 80:
            Student.lulus += 1

            print(f"nilai {self.name} adalah {self.nilai} sehingga LULUS")

        else:
            Student.tidak_lulus += 1
            print("tidak lulus")

    def jumlah_kelulusan():
        print("Jumlah siswa lulus = ", Student.lulus)
        print("Jumlah siswa tidak lulus = ", Student.tidak_lulus)
    

siswa_1 = Student("devina", 95, 2)

siswa_1.status()
Student.jumlah_kelulusan()
