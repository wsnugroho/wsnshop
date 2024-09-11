# WSNSHOP
[Tautan web: http://pbp.cs.ui.ac.id/wisnu.nugroho31/wsnshop]()

## Tugas 2 - PBP 24/25

### Cara Implementasi Proyek
1. **Membuat proyek Django baru**
Untuk menginisiasi sebuah project baru pada Django, kita dapat menjalankan command berikut `django-admin startproject nama_project`. Framework akan menyiapkan berbagai struktur yang diperlukan setelahnya.
2. **Membuat main app pada proyek django**
Untuk membuat aplikasi main kita dapat menggunakan perintah `python manage.py startapp main`.
3. **Mendefinisikan model pada proyek**
Di dalam direktori main, dapat dibuat model baru pada file `models.py`. Dalam tugas ini, model yang diperlukan adalah Product dengan atribut nama dengan tipe CharField, price dengan tipe IntegerField, dan description dengan tipe TextField.
4. **Menampilkan html berdasarkan data**
Kita dapat membuat fungsi di `views.py` yang akan melakukan rendering template html agar bisa ditampilkan ke user.
5. **Melakukan routing pada `urls.py`**
Pada direktori proyek, kita dapat melakukan routing untuk mengarahkan url ke main app.
6. **Melakukan deployment melalui PWS**
Apabila aplikasi sudah cukup baik, kita bisa melakukan deployment di Pacil Web Service agar web kita dapat diakses melalui internet.

### Django Workflow
![Django Workflow Placeholder]()

### Fungsi Git
Git berfungsi sebagai version control system dalam pengembangan perangkat lunak, memungkinkan developer untuk melacak perubahan kode, berkolaborasi secara efektif, dan mengelola proyek dengan lebih baik. Dengan Git, setiap perubahan yang dibuat dalam kode dapat dicatat, memungkinkan rollback ke versi sebelumnya jika diperlukan, serta memfasilitasi pengembangan secara paralel melalui fitur branching. Ini memungkinkan tim untuk bekerja pada fitur-fitur baru atau perbaikan bug secara terpisah tanpa mengganggu kode utama, dan kemudian menggabungkan perubahan tersebut dengan mudah. Git juga menyediakan mekanisme untuk menangani konflik yang muncul ketika beberapa developer mengedit bagian kode yang sama, menjadikannya alat penting untuk manajemen proyek perangkat lunak yang kompleks.

### Mengapa Django digunakan sebagai permulaan pembelajaran pengembangan perangkat lunak?
Django sering digunakan sebagai permulaan dalam pembelajaran pengembangan perangkat lunak karena framework ini menawarkan struktur yang jelas dan komprehensif, memudahkan pemula untuk memahami konsep-konsep dasar seperti MVT (Model-View-Template), ORM (Object-Relational Mapping), dan routing. Django juga menyediakan banyak fitur bawaan seperti autentikasi, formulir, dan panel admin, yang memungkinkan pelajar untuk fokus pada pengembangan aplikasi tanpa harus memikirkan detail-detail teknis yang rumit. Selain itu, Django memiliki dokumentasi yang sangat baik dan komunitas yang besar, sehingga memudahkan pemula untuk menemukan sumber daya belajar dan bantuan saat mengalami kesulitan.

### Mengapa model di Django disebut ORM
Model di Django disebut ORM (Object-Relational Mapping) karena memungkinkan developer untuk bekerja dengan database menggunakan objek Python, bukan query SQL langsung. Dengan ORM, setiap tabel di database direpresentasikan sebagai kelas, dan setiap baris dalam tabel direpresentasikan sebagai objek dari kelas tersebut. Ini menyederhanakan interaksi dengan database, memungkinkan operasi CRUD (Create, Read, Update, Delete) dilakukan dengan metode Python, sehingga membuat pengembangan aplikasi lebih efisien dan terstruktur.

