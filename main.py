class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print(f"Kontak dengan nama {name} sudah ada.")
        else:
            self.contacts[name] = {'phone': phone, 'email': email}
            print(f"Kontak {name} berhasil ditambahkan.")

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            print(f"Kontak {name} berhasil diperbarui.")
        else:
            print(f"Kontak dengan nama {name} tidak ditemukan.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Kontak {name} berhasil dihapus.")
        else:
            print(f"Kontak dengan nama {name} tidak ditemukan.")

    def display_contacts(self):
        if self.contacts:
            for name, info in self.contacts.items():
                print(f"Nama: {name}, Telepon: {info['phone']}, Email: {info['email']}")
        else:
            print("Tidak ada kontak yang tersimpan.")

    def search_contact(self, name):
        if name in self.contacts:
            info = self.contacts[name]
            print(f"Nama: {name}, Telepon: {info['phone']}, Email: {info['email']}")
        else:
            print(f"Kontak dengan nama {name} tidak ditemukan.")


# Contoh penggunaan
if __name__ == "__main__":
    cm = ContactManager()
while True:
    print("Pilih Opsi: ")
    print("1. Tambahkan kontak ")
    print("2. Mencari Kontak ")
    print("3. Update Kontak ")
    print("4. Hapus Kontak ")
    pilih = input("Masukkan pilihan opsi: ")

    # Menambahkan kontak
    if pilih == "1":
        nama = input("Masukkan nama  : ")
        nomor = input("Masukkan nomor : ")
        email = input("Masukkan nama  : ")
        cm.add_contact(nama, nomor, email)
        cm.display_contacts()

    elif pilih == "2":
        cm.display_contacts()
        nama = input("Masukkan nama  : ")
        cm.search_contact(nama)

    elif pilih == "3":
        nama = input("Masukkan nama  : ")
        nomor = input("Masukkan nomor : ")
        email = input("Masukkan nama  : ")
        cm.update_contact(nama, nomor, email)

    elif pilih == "4":
        nama = input("Masukkan nama  : ")
        cm.delete_contact(nama)

    else:
        print("Inputan Anda Salah")