# WSNSHOP
Tautan Web: [http://wisnu-nugroho31-wsnshop.pbp.cs.ui.ac.id](http://wisnu-nugroho31-wsnshop.pbp.cs.ui.ac.id)

## Tugas 2 - PBP 24/25

### Cara Implementasi Proyek
1. **Membuat proyek Django baru**

    Untuk menginisiasi sebuah project baru pada Django, kita dapat menjalankan command berikut `django-admin startproject nama_project`. Django akan menghasilkan file dan direktori projek yang diperlukan.

2. **Membuat main app pada proyek django**

    Untuk membuat aplikasi main kita dapat menggunakan perintah `python manage.py startapp main`.

3. **Mendefinisikan model pada proyek**
   
    Di dalam direktori main, dapat dibuat model baru pada file `models.py`. Dalam tugas ini, model yang diperlukan adalah Product yang memiliki atribut nama dengan tipe CharField, price dengan tipe IntegerField, dan description dengan tipe TextField.

4. **Menampilkan html berdasarkan data**

    Kita dapat membuat fungsi di `views.py` yang akan melakukan rendering template html. Fungsi ini digunakan untuk menyuplai data (dalam hal ini berupa nama dan kelas) ke file template html yang akan dirender.

5. **Melakukan routing pada `urls.py`**

    Pada direktori proyek, kita dapat melakukan routing untuk mengarahkan root url ke main app kita.

6. **Melakukan deployment melalui PWS**

    Apabila aplikasi sudah cukup baik, kita bisa melakukan deployment di Pacil Web Service agar web kita dapat diakses melalui internet.

### Django Workflow
![Bagan Django Workflow](https://github.com/user-attachments/assets/a533084b-720a-4b73-8ae1-88599284c704)

#### Penjelasan Bagan
1. Client mengirimkan permintaan HTTP ke server Django. Ini bisa berupa permintaan GET, POST, atau metode HTTP lainnya.
2. Django menerima permintaan ini dan memeriksa URL-nya. Django menggunakan URLconf (konfigurasi URL) untuk mencocokkan URL yang diminta dengan pola yang telah ditentukan dalam urls.py. Jika ada kecocokan, permintaan diteruskan ke view yang sesuai.
3. Setelah URL dicocokkan, Django memanggil fungsi view yang terkait. View adalah fungsi Python yang menerima objek request sebagai parameter dan berisi logika untuk memproses permintaan tersebut. Di sini, view bisa berinteraksi dengan model, mengakses database, memproses formulir, dll.
4. Jika view membutuhkan data dari database, maka akan mengakses models. Models adalah representasi dari data yang disimpan dalam database. Django ORM (Object-Relational Mapping) memungkinkan interaksi dengan database menggunakan kode Python alih-alih SQL langsung.
5. Jika response yang diminta adalah halaman HTML, view biasanya akan mengembalikan HttpResponse dengan merender template. Template adalah file HTML yang mungkin berisi tag Django untuk menampilkan data dinamis. Data dari view diberikan ke template dalam bentuk konteks, yang kemudian dirender menjadi HTML.
6. View mengembalikan objek HttpResponse yang berisi data yang akan dikirim kembali ke klien. Ini bisa berupa HTML, JSON, XML, atau bahkan file. Django kemudian mengirimkan response ini kembali ke klien melalui HTTP.
7. Client menerima response ini dan menampilkannya ke pengguna.

### Fungsi Git
Git berfungsi sebagai version control system dalam pengembangan perangkat lunak, memungkinkan developer untuk melacak perubahan kode, berkolaborasi secara efektif, dan mengelola proyek dengan lebih baik. Dengan Git, setiap perubahan yang dibuat dalam kode dapat dicatat, memungkinkan rollback ke versi sebelumnya jika diperlukan, serta memfasilitasi pengembangan secara paralel melalui fitur branching. Ini memungkinkan tim untuk bekerja pada fitur-fitur baru atau perbaikan bug secara terpisah tanpa mengganggu kode utama, dan kemudian menggabungkan perubahan tersebut dengan mudah. Git juga menyediakan mekanisme untuk menangani konflik yang muncul ketika beberapa developer mengedit bagian kode yang sama, menjadikannya alat penting untuk manajemen proyek perangkat lunak yang kompleks.

### Mengapa Django digunakan sebagai permulaan pembelajaran pengembangan perangkat lunak?
Django sering digunakan sebagai permulaan dalam pembelajaran pengembangan perangkat lunak karena framework ini menawarkan struktur yang jelas dan komprehensif, memudahkan pemula untuk memahami konsep-konsep dasar seperti MVT (Model-View-Template), ORM (Object-Relational Mapping), dan routing. Django juga menyediakan banyak fitur bawaan seperti autentikasi, formulir, dan panel admin, yang memungkinkan pelajar untuk fokus pada pengembangan aplikasi tanpa harus memikirkan detail-detail teknis yang rumit. Selain itu, Django memiliki dokumentasi yang sangat baik dan komunitas yang besar, sehingga memudahkan pemula untuk menemukan sumber daya belajar dan bantuan saat mengalami kesulitan.

### Mengapa model di Django disebut ORM
Model di Django disebut ORM (Object-Relational Mapping) karena memungkinkan developer untuk bekerja dengan database menggunakan objek Python, bukan query SQL langsung. Dengan ORM, setiap tabel di database direpresentasikan sebagai kelas, dan setiap baris dalam tabel direpresentasikan sebagai objek dari kelas tersebut. Ini menyederhanakan interaksi dengan database, memungkinkan operasi CRUD (Create, Read, Update, Delete) dilakukan dengan metode Python, sehingga membuat pengembangan aplikasi lebih efisien dan terstruktur.

