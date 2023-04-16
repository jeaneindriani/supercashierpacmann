import pandas as pd
import os

class Transaction:
    """
    Sebuah class untuk kasir self-service disupermarket
    ...
    Attributes
    ----------
    id_transaksi : int
        id_transaksi berjenis input untuk hasil transaksi customer
    data_item : dict
        data_item adalah tempat penyimpanan data order transaksi yang berhasil diinput oleh customer kedalam sistem
    """

    data_item = {"Nama item": [], "Jumlah item": [], "Harga per item": [], "Total Harga": []}

    def __init__(self):
      """
      Constructor untuk sebuah class Transaction
      Parameters
      ----------
      Tidak terdapat parameter pada fungsi Constructor
      Attributes
      ----------
      id_transaksi : int
          id_transaksi berjenis input untuk hasil transaksi customer
      """

      print("Welcome to Andi Supermarket")
      while 1:
          try:
              id_transaksi = int(input("ID Transaksi: "))
              print("ID Transaksi Aktif {}".format(id_transaksi))
              print("\n")
              break
          except ValueError:
              print("ID Transaksi tidak valid!")
              continue
      while 1:
          print("Menu:")
          print("- Untuk menambahkan item ketik: add_item")
          print("- Untuk mengubah nama item ketik: edit_name")
          print("- Untuk mengubah jumlah item ketik: edit_qty")
          print("- Untuk mengubah harga item ketik: edit_price")
          print("- Untuk memeriksa detail transaksi ketik: check_order")
          print("- Untuk menghapus salah satu item ketik: delete_item")
          print("- Untuk menghapus seluruh item ketik: reset_order")
          print("- Untuk menampilkan total belanja ketik: total_belanja")
          print("- Untuk keluar dari program ketik: exit")
          print("\n")
          edit_order = input("Pilih Menu: ")
          if edit_order.lower() == "add_item":
              self.add_item()
              print("\n")
          elif edit_order.lower() == "edit_name":
              self.edit_name()
              print("\n")
          elif edit_order.lower() == "edit_qty":
              self.edit_qty()
              print("\n")
          elif edit_order.lower() == "edit_price":
              self.edit_price()
              print("\n")
          elif edit_order.lower() == "check_order":
              self.check_order()
              print("\n")
          elif edit_order.lower() == "delete_item":
              self.delete_item()
              print("\n")
          elif edit_order.lower() == "reset_order":
              self.reset_order()
              print("\n")
          elif edit_order.lower() == "total_belanja":
              self.total_price()
              print("\n")
          elif edit_order.lower() == "exit":
              # break
              os._exit(0)
          else:
              print("Menu yang anda pilih tidak tersedia")
              print("\n")

    def add_item(self):
      """
      Sebuah fungsi untuk menambahkan item baru kedalam keranjang
      Parameters
      ----------
      Tidak terdapat parameter pada fungsi add_item
      Attributes
      ----------
      nama_item : str
          nama_item berjenis input untuk menyimpan nama item yang dimasukkan kedalam keranjang
      jumlah_item : int
          jumlah_item berjenis input untuk menyimpan jumlah item yang dimasukkan kedalam keranjang
      harga : int
          harga berjenis input untuk menyimpan harga per item yang dimasukkan kedalam keranjang
      total_harga : int
          Penghitung total_harga dengan melakukan perkalian terhadap jumlah item dan harga per item
      Return
      ------
      Menyimpan seluruh data yang berhasil diinput oleh customer kedalam database
      """

      nama_item = input("Nama item: ")

      while 1:
          try:
              jumlah_item = int(input("Jumlah item: "))
              break
          except ValueError:
              print("Mohon masukkan angka")
              continue

      while 1:
          try:
              harga = int(input("Harga satuan: "))
              break
          except ValueError:
              print("Mohon masukkan angka")
              continue

      self.data_item["Nama item"].append(nama_item)
      self.data_item["Jumlah item"].append(jumlah_item)
      self.data_item["Harga per item"].append(harga)
      self.data_item["Total Harga"].append(jumlah_item * harga)

    def edit_name(self):
      """
      Sebuah fungsi untuk mengubah nama item yang telah diinput oleh customer
      Parameters
      ----------
      Tidak terdapat parameter pada fungsi edit_name
      Attributes
      ----------
      nama_item : str
          nama_item berjenis input untuk nama item yang ingin dilakukan perubahan pada nama item
      edit_name : int
          edit_name berjenis input untuk nama item terbaru
      idx_item : int
          idx_item untuk menyimpan posisi index dari nama item yang diinput oleh customer
      Return
      ------
      Menyimpan seluruh perubahan pada nama item yang berhasil diinput oleh customer kedalam database
      """

      while 1:
          nama_item = input("Nama item: ")

          if nama_item in self.data_item.get("Nama item"):
              edit_name = input("Nama item yang ingin diubah: ")
              idx_item = self.data_item['Nama item'].index(nama_item)
              self.data_item['Nama item'][idx_item] = edit_name
              print("Berhasil dirubah!")
              break

          else:
              print("Nama item tidak terdaftar")

    def edit_qty(self):
      """
      Digunakan untuk mengubah data jumlah item pada order transaksi yang telah diinput oleh customer
      Parameters
      ----------
      Tidak terdapat parameter pada fungsi edit_qty
      Attributes
      ----------
      nama_item : str
          nama_item berjenis input untuk nama item yang ingin dilakukan perubahan pada jumlah item
      edit_qty : int
          edit_qty berjenis input untuk jumlah item terbaru
      idx_item : int
          idx_item untuk menyimpan posisi index dari nama item yang diinput oleh customer
      Return
      ------
      Menyimpan seluruh data perubahan pada jumlah item yang berhasil diinput oleh customer kedalam database
      """

      while 1:
          nama_item = input("Nama item yang ingin diubah: ")

          if nama_item in self.data_item.get("Nama item"):
              while 1:
                  try:
                      edit_qty = int(input("Update jumlah item yang dibeli: "))
                      break
                  except ValueError:
                      print("Mohon masukkan angka")
                      continue
              idx_item = self.data_item['Nama item'].index(nama_item)
              self.data_item['Jumlah item'][idx_item] = edit_qty

              self.data_item["Total Harga"][idx_item] = (
                          edit_qty * self.data_item["Harga per item"][idx_item])

              print("Berhasil dirubah!")
              break

          else:
              print("Nama item tidak terdaftar")

    def edit_price(self):
      """
     Digunakan untuk mengubah data harga per item pada order transaksi yang telah diinput oleh customer
      Parameters
      ----------
      Tidak terdapat parameter pada fungsi edit_price
      Attributes
      ----------
      nama_item : str
          nama_item berjenis input untuk memasukkan nama item yang ingin diubah pada harga per item
      edit_price : int
          edit_price berjenis input untuk harga per item terbaru
      idx_item : int
          idx_item untuk menyimpan posisi index dari nama item yang diinput oleh customer
      Return
      ------
      Menyimpan seluruh data perubahan pada harga per item yang berhasil diinput oleh customer kedalam database
      """

      while 1:
          nama_item = input("Nama item yang ingin diubah: ")

          if nama_item in self.data_item.get("Nama item"):
              while 1:
                  try:
                      edit_price = int(input("Update harga per item yang dibeli: "))
                      break
                  except ValueError:
                      print("Mohon masukkan angka")
                      continue
              idx_item = self.data_item['Nama item'].index(nama_item)
              self.data_item['Harga per item'][idx_item] = edit_price

              self.data_item["Total Harga"][idx_item] = (
                          edit_price * self.data_item["Jumlah item"][idx_item])

              print("Berhasil dirubah!")
              break

          else:
              print("Nama item tidak terdaftar")

    def check_order(self):
      """
      Digunakan untuk memeriksa apakah terdapat kesalahan input data pada transaksi
      Parameters
      ----------
      Tidak terdapat parameter pada fungsi check_order
      Attributes
      ----------
      df : dataframe
          df digunakan untuk menampilkan data-data order transaksi dalam bentuk dataframe atau tabular
      Return
      ------
      Menampilkan apakah terdapat kesalahan dalam penginputan data pada transaksi dan data yang berhasil diinput oleh customer
      """

      if not any(self.data_item.values()):
          print("Tidak ada data transaksi!")
      elif '' in self.data_item['Nama item']:
          print("Mohon mengisi nama item yang kosong!")
          print("Recap Order")
          df = pd.DataFrame(self.data_item)
          print(df)
      else:
          print("Data transaksi sudah benar!")
          print("Recap Order")
          df = pd.DataFrame(self.data_item)
          print(df)

    def delete_item(self):
      """
     Digunakan untuk menghapus salah satu item yang berhasil diinput oleh customer pada transaksi
      Parameters
      ----------
      Tidak terdapat parameter pada fungsi delete_item
      Attributes
      ----------
      nama_item : str
          nama_item berjenis input untuk nama item yang ingin dilakukan penghapusan order transaksi
      df : dataframe
          df digunakan untuk menampilkan data-data order transaksi dalam bentuk dataframe atau tabular
      idx_item : int
          idx_item untuk menyimpan posisi index dari nama item yang diinput oleh customer
      Return
      ------
      Menghapus salah satu order transaksi pada data database
      """

      while 1:
          nama_item = input("Nama item yang ingin dihapus: ")

          if nama_item in self.data_item.get("Nama item"):
              idx_item = self.data_item['Nama item'].index(nama_item)
              for key in list(self.data_item.keys()):
                  del self.data_item[key][idx_item]

              print("Berhasil dihapus!")
              if not any(self.data_item.values()):
                  print("Tidak ada data transaksi!")
              else:
                  df = pd.DataFrame(self.data_item)
                  print(df)
              break

          else:
              print("Nama item tidak terdaftar")

    def reset_transaction(self):
      """
      Sebuah fungsi untuk menghapus seluruh item yang berhasil diinput oleh customer pada transaksi
      Parameters
      ----------
      Tidak terdapat parameter pada fungsi reset_transaction
      Attributes
      ----------
      Tidak terdapat attribute pada fungsi reset_transaction
      Return
      ------
      Menghapus seluruh order transaksi pada data database
      """

      for key in list(self.data_item.keys()):
          del self.data_item[key][:]

      print("Berhasil menghapus seluruh transaksi!")


    def total_belanja(self):
      """
      Digunakan untuk menghitung total biaya yang harus dibayarkan customer dari item-item pada data transaksi
      Parameters
      ----------
      Tidak terdapat parameter pada fungsi total_belanja
      Attributes
      ----------
      df : dataframe
          df digunakan untuk menampilkan data-data order transaksi dalam bentuk dataframe atau tabular
      Return
      ------
      Menampilkan total biaya yang harus dibayar oleh customer tersebut dengan beberapa kriteria yaitu
      - diatas Rp. 500.000 akan mendapatkan potongan biaya sebesar 10% dari total biaya yang harus dibayarkan
      - diatas Rp. 300.000 akan mendapatkan potongan biaya sebesar 8% dari total biaya yang harus dibayarkan
      - diatas Rp. 200.000 akan mendapatkan potongan biaya sebesar 5% dari total biaya yang harus dibayarkan
      """

      if not any(self.data_item.values()):
          print("Tidak ada transaksi!")
      else:
          df = pd.DataFrame(self.data_item)
          print(df)
          if sum(self.data_item["Total Harga"]) > 500000:
              print("Sebelum mendapatkan diskon 10%: Rp.{}".format(sum(self.data_item["Total Harga"])))
              print("Setelah mendapatkan diskon 10%: Rp.{}".format(
                  int(sum(self.data_item["Total Harga"]) - (sum(self.data_item["Total Harga"]) * 0.10))))
          elif sum(self.data_item["Total Harga"]) > 300000:
              print("Sebelum mendapatkan diskon 8%: Rp.{}".format(sum(self.data_item["Total Harga"])))
              print("Setelah mendapatkan diskon 8%: Rp.{}".format(
                  sum(int(self.data_item["Total Harga"]) - (sum(self.data_item["Total Harga"]) * 0.08))))
          elif sum(self.data_item["Total Harga"]) > 200000:
              print("Sebelum mendapatkan diskon 5%: Rp.{}".format(sum(self.data_item["Total Harga"])))
              print("Setelah mendapatkan diskon 5%: Rp.{}".format(
                  sum(int(self.data_item['Total Harga']) - (sum(self.data_item["Total Harga"]) * 0.05))))