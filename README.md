# WSNSHOP
Tautan Web: [http://wisnu-nugroho31-wsnshop.pbp.cs.ui.ac.id](http://wisnu-nugroho31-wsnshop.pbp.cs.ui.ac.id)

## Tugas 6

### Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

JavaScript memiliki peran penting dalam pengembangan aplikasi web karena kemampuannya untuk meningkatkan interaktivitas dan dinamisme pada halaman web. Dengan JavaScript, pengembang dapat memanipulasi elemen HTML dan CSS secara langsung, memungkinkan perubahan tampilan dan fungsionalitas tanpa harus memuat ulang halaman. Selain itu, JavaScript memungkinkan validasi data di sisi klien, sehingga mengurangi beban pada server dan meningkatkan efisiensi aplikasi. Bahasa ini juga didukung oleh berbagai pustaka dan kerangka kerja yang membantu mempercepat pengembangan aplikasi web yang lebih kompleks. Kemampuan JavaScript untuk berkomunikasi dengan API eksternal dan backend menjadikannya pilihan utama dalam membuat aplikasi web yang responsif dan interaktif.

### Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?

Penggunaan `await` dengan `fetch()` berfungsi untuk menunggu hasil operasi asinkron tanpa memblokir alur utama program, sehingga memungkinkan interaksi web tetap berjalan dengan lancar. Ketika `fetch()` digunakan untuk mengambil data dari server, fungsi tersebut mengembalikan sebuah promise yang bisa memakan waktu beberapa saat untuk diselesaikan. Dengan await, kita bisa menunggu hasil dari promise tanpa menghentikan proses lain di halaman web (*nonblocking*), memastikan pengguna tetap bisa berinteraksi dengan elemen lain selama data sedang diambil. Jika await tidak digunakan, kode akan dieksekusi secara paralel, sehingga program bisa melanjutkan sebelum respons diterima, yang berpotensi menyebabkan penggunaan data yang belum tersedia atau kosong. Hal ini menjaga performa aplikasi tetap responsif dan tidak membekukan antarmuka pengguna.

### Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

Kita perlu menggunakan dekorator `csrf_exempt` pada view yang akan digunakan untuk permintaan AJAX POST karena mekanisme Cross-Site Request Forgery (CSRF) di Django secara otomatis memeriksa setiap permintaan POST untuk memastikan bahwa permintaan tersebut sah dan berasal dari sumber yang tepercaya. AJAX POST dari sumber eksternal atau dari halaman tanpa token CSRF yang valid akan ditolak oleh Django sebagai langkah keamanan. Namun, dalam beberapa kasus seperti saat membuat API atau layanan AJAX sederhana, kita mungkin tidak ingin menggunakan perlindungan CSRF karena tidak menggunakan form tradisional atau interaksi langsung dengan pengguna. Dalam situasi ini, dekorator `csrf_exempt` digunakan untuk menonaktifkan pemeriksaan CSRF pada view tersebut, memungkinkan permintaan POST dari AJAX untuk diterima tanpa token CSRF.

### Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Melakukan pembersihan data input hanya di sisi frontend tidaklah cukup, karena untuk keamanan yang optimal, pembersihan ini juga harus dilakukan di backend. Validasi di frontend memang bermanfaat untuk memberikan umpan balik instan kepada pengguna, sehingga meningkatkan pengalaman penggunaan. Namun, sisi frontend bisa dengan mudah dimanipulasi oleh pengguna yang berpengalaman atau pihak ketiga. Jika validasi hanya bergantung pada frontend, ada risiko data yang tidak valid atau berbahaya tetap dapat mencapai server tanpa terdeteksi. Oleh karena itu, pembersihan dan validasi di backend sangat penting untuk memastikan data yang masuk aman dan sesuai dengan standar sebelum diproses, sehingga membantu melindungi aplikasi dari ancaman seperti injection, cross-site scripting (XSS), dan manipulasi data.

### Cara Implementasi Proyek

1. Membuat fungsi untuk menghandle tambah produk menggunakan AJAX di `views.py`. Setelah itu, lakukan juga routing fungsi tersebut di `urls.py`.
    ```python
    @csrf_exempt
    @require_POST
    def create_product_ajax(request):
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        user = request.user
        new_mood = Product(name=name, price=price, description=description, user=user)
        new_mood.save()
        return HttpResponse(b"CREATED", status=201)
    ```
    ```python
    urlpatterns = [
        path("create-product-ajax/", create_product_ajax, name="create_product_ajax"),
    ]
    ```
2. Mengubah metode menampilkan data menggunakan AJAX. Pertama, Kita lakukan GET request ke endpoint `/json` untuk mendapatkan seluruh data user yang login saat ini. Lalu, lakukan binding suatu elemen HTML dengan menggunakan `document.getElementById()` yang nantinya akan digunakan untuk menampung tampilan (dalam bentuk cards atau kosong) dari hasil response JSON.
    ```javascript
    <script>
        async function getMoodEntries(){
            return fetch("{% url 'main:show_json' %}").then((res) => res.json())
        }
        async function refreshMoodEntries() {
            document.getElementById("product_cards").innerHTML = "";
            document.getElementById("product_cards").className = "";
            const moodEntries = await getMoodEntries();
            let htmlString = "";
            let classNameString = "";

            if (moodEntries.length === 0) {
                classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
                htmlString = `
                    <!-- HTML dari tampilan kosong -->
                `;
            }
            else {
                classNameString = "w-full grid gap-4 my-12 sm:grid-cols-2 md:grid-cols-4"
                moodEntries.forEach((item) => {
                    htmlString += `
                        <!-- HTML dari tampilan card-card -->
                    `;
                });
            }
            document.getElementById("mood_entry_cards").className = classNameString;
            document.getElementById("mood_entry_cards").innerHTML = htmlString;
        }
        refreshMoodEntries();
    </script>
    ```
3. Menambahkan modal sebagai form untuk membuat produk menggunakan AJAX dan menampilkannya hanya ketika button Tambah Produk by AJAX diklik.
    ```javascript
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    function showModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modal.classList.remove('hidden'); 
        setTimeout(() => {
            modalContent.classList.remove('opacity-0', 'scale-95');
            modalContent.classList.add('opacity-100', 'scale-100');
        }, 50); 
    }

    function hideModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modalContent.classList.remove('opacity-100', 'scale-100');
        modalContent.classList.add('opacity-0', 'scale-95');

        setTimeout(() => {
            modal.classList.add('hidden');
        }, 150); 
    }
    
    document.getElementById("cancelButton").addEventListener("click", hideModal);
    document.getElementById("closeModalBtn").addEventListener("click", hideModal);

    ```
4. Melakukan POST request dari client untuk menambahkan data produk.
    ```javascript
    function addProduct() {
        fetch("{% url 'main:create_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#productForm')),
        })
        .then(response => {
            if (response.ok) {
                refreshProduct();
                document.getElementById("productForm").reset(); 
                document.querySelector("[data-modal-toggle='crudModal']").click();
                hideModal();
            } else {
                alert(`Failed to add Product`)
            }
        })
        .catch(err => alert(`An error occured: ${err.message}`))
    }
    document.getElementById("productForm").addEventListener("submit", (e) => {
        e.preventDefault();
        addProduct();
    })

    ```
5. Melakukan cleaning input user untuk melindungi aplikasi kita dari XSS
    ```python
    def create_product_ajax(request):
        name = strip_tags(request.POST.get("name"))
        price = strip_tags(request.POST.get("price"))
        description = strip_tags(request.POST.get("description"))
        if not name or not description:
            return HttpResponse("HTML tags are not allowed in name or description.", status=400)
        ...
    ```
    ```python
    class ProductForm(ModelForm):
        ...
        def clean_name(self):
            name = self.cleaned_data["name"]
            return strip_tags(name)

        def clean_description(self):
            description = self.cleaned_data["description"]
            return strip_tags(description)

    ```
    ```javascript
    <script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
    <script>
        async function refreshProduct() {
            ...
            products.forEach((item) => {
                const name = DOMPurify.sanitize(item.fields.name);
                const description = DOMPurify.sanitize(item.fields.description);
                ...
            });
            ...
        }
    </script>
    ```

## Tugas 5

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Urutan prioritas CSS selector ditentukan oleh tingkat specificity masing-masing selector, dari yang paling rendah hingga yang paling tinggi. Berikut contoh urutan dari beberapa CSS selector dari yang paling tinggi ke yang paling rendah (urutan atas akan mengoverride style urutan dibawahnya):
1. **`!important`**, jika digunakan, akan mengabaikan semua aturan prioritas yang ada, kecuali jika ada selector lain yang juga menggunakan `!important`.
2. **Inline CSS**, yaitu CSS yang didefinisikan langsung di atribut `style` pada elemen HTML, memiliki prioritas sangat tinggi.
3. **Selector ID**, yang menggunakan atribut `id` seperti `#myId {}`.
4. **Selector atribut dan pseudo-class**, misalnya `[type="text"] {}` atau `:hover`.
5. **Selector kelas (class)**, menggunakan atribut `class` seperti `.myClass {}`.
6. **Selector elemen (tag)**, seperti `p {}`, mengacu pada elemen HTML spesifik.
7. **Selector universal (`*`)** memiliki prioritas paling rendah dan berlaku untuk semua elemen.


### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Responsive design merupakan salah satu konsep penting dalam pengembangan aplikasi web karena pada masa ini perangkat yang digunakan untuk mengakses web sudah sangat bervariasi, mulai dari ponsel, tablet, hingga desktop dengan ukuran layar yang berbeda-beda. Dengan responsive design, tampilan dan fungsionalitas web dapat secara otomatis menyesuaikan diri dengan perangkat pengguna, memberikan pengalaman yang baik pada pengguna tanpa dia perlu melakukan *zoom* atau *scrolling* berlebihan. Hal ini tidak hanya meningkatkan kenyamanan pengguna, tetapi juga dapat meningkatkan performa SEO karena search engine seperti Google biasanya mengutamakan situs yang mobile-friendly. Contoh aplikasi yang sudah menerapkan responsive design adalah **Twitter**, yang memiliki tampilan menyesuaikan ukuran semua layar. Sebaliknya, beberapa situs lama seperti **CS.RIN.RU** masih memiliki desain yang kurang responsif, sehingga cenderung sulit digunakan di perangkat mobile.


### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

**Margin**, **border**, dan **padding** adalah bagian dari *box model* dalam CSS yang menentukan letak suatu elemen di halaman web. Berikut beberapa perbedaan dari margin, border, dan padding:

- **Margin**: Ini adalah ruang di luar elemen yang memisahkan elemen dari elemen lainnya. Margin bersifat eksternal dan tidak memengaruhi ukuran elemen itu sendiri. Kita dapat mengatur margin menggunakan properti css seperti `margin`, `margin-top`, `margin-right`, `margin-bottom`, dan `margin-left`.

- **Border**: Ini adalah garis yang mengelilingi elemen. Border berada di antara margin dan padding, dan dapat memiliki ketebalan, warna, serta style yang bisa disesuaikan. Kita dapat mengatur border menggunakan properti css seperti `border`, `border-width`, `border-style`, dan `border-color`.

- **Padding**: Ini adalah ruang di dalam elemen, antara konten elemen dan *border*-nya. Padding memengaruhi ukuran elemen karena menambah ruang di dalam elemen. Kita dapat mengatur padding dengan properti css seperti `padding`, `padding-top`, `padding-right`, `padding-bottom`, dan `padding-left`.

```css
.element {
  margin: 20px;         /* Elemen memiliki jarak 20px terhadap elemen lainnya */
  border: 2px solid red; /* Menambahkan garis border dengan ketebalan 2px dan berwarna merah */
  padding: 10px;        /* Jarak antara konten di suatu element dengan bordernya */
}
```


### Jelaskan konsep flex box dan grid layout beserta kegunaannya!

**Flexbox (Flexible Box Layout)** adalah sebuah model untuk tata letak satu dimensi yang memungkinkan elemen dalam container untuk disusun secara fleksibel, baik dalam baris (row) maupun kolom (column). Flexbox memudahkan penyesuaian ukuran, urutan, dan jarak antar elemen, serta memungkinkan responsivitas yang lebih baik pada desain web. Kegunaan utama Flexbox adalah untuk menyusun elemen dalam satu dimensi, seperti navbar, cards, atau komponen ui lainnya, sehingga menciptakan sebuah tata letak yang lebih responsif dan teratur.

**Grid Layout**, di sisi lain, adalah model tata letak dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom secara bersamaan. Dengan menggunakan Grid, developer dapat menentukan ukuran dan posisi elemen dengan lebih presisi menggunakan sistem grid. Kegunaan utama Grid Layout adalah untuk membuat tata letak yang lebih kompleks, seperti halaman web yang terdiri dari berbagai bagian, kolom, dan gambar. Grid sangat berguna untuk desain yang memerlukan pengaturan ruang secara lebih terstruktur, seperti halaman galeri, dashboard, atau layout yang mengandung banyak elemen.

### Cara Implementasi Proyek

1. Menambahkan fungsi *edit_product* untuk memungkinkan user untuk mengubah product yang telah dibuat.
   ```python
   def edit_product(request, id):
        product = Product.objects.get(pk=id)
        form = ProductForm(request.POST or None, instance=product)
        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse("main:show_main"))
        context = {"form": form}
        return render(request, "edit_product.html", context)
   ```
2. Menambahkan fungsi *delete_product* supaya user dapat menghapus product yang dipilih.
   ```python
   def delete_product(request, id):
        product = Product.objects.get(pk=id)
        product.delete()
        return HttpResponseRedirect(reverse("main:show_main"))
   ```
3. Melakukan routing url pada fungsi *edit_product* dan *delete_product*.
    ```python
    ...
    path("edit-product/<uuid:id>/", edit_product, name="edit_product"),
    path("delete-product/<uuid:id>/", delete_product, name="delete_product"),
    ...
    
    ```
4. Mengkonfigurasi `settings.py` django agar dapat menyajikan static files.
    ```python
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]
    ```
    ```python
    STATIC_URL = '/static/'
    if DEBUG:
        STATICFILES_DIRS = [
            BASE_DIR / 'static'
        ]
    else:
        STATIC_ROOT = BASE_DIR / 'static'
    ```
5. Theming dengan tailwind untuk page yang diperlukan.

## Tugas 4

### Apa perbedaan antara HttpResponseRedirect() dan redirect()?

Fungsi `HttpResponseRedirect()` maupun `redirect()` biasanya digunakan untuk mengarahkan pengguna ke URL lain, tetapi ada perbedaan dalam cara kerjanya. `HttpResponseRedirect()` adalah fungsi dasar yang membutuhkan URL lengkap sebagai argumen dan mengembalikan respons HTTP dengan status kode 302 untuk redirection. Meskipun memberikan kontrol lebih besar, metode ini kurang fleksibel karena URL harus ditentukan secara langsung. Sementara itu, fungsi `redirect()` lebih sederhana dan fleksibel, karena dapat menerima URL, nama view, atau objek model sebagai argumen. Fungsi ini secara otomatis menghasilkan URL menggunakan `reverse()`, sehingga mempermudah redirection tanpa perlu menentukan URL secara manual. Oleh karena itu, `redirect()` biasanya lebih dipilih karena kemudahannya, terutama saat bekerja dengan nama view atau objek.

### Jelaskan cara kerja penghubungan model Product dengan User!
Di Django, model `Product` dapat dihubungkan dengan model `User` menggunakan foreign key untuk merepresentasikan hubungan satu-ke-banyak, di mana satu pengguna (`User`) dapat memiliki banyak produk (`Product`). Untuk menghubungkan keduanya, pertama, model `User` bawaan dari Django diimpor dari `django.contrib.auth.models`. Setelah itu, di dalam model `Product`, sebuah foreign key ditambahkan yang menghubungkannya dengan model `User`, misalnya melalui field user yang diatur dengan `models.ForeignKey(User, on_delete=models.CASCADE)`. Dengan cara ini, setiap produk akan terkait dengan pengguna yang menjadi pemiliknya. `on_delete=models.CASCADE` memastikan bahwa jika pengguna dihapus, produk yang dimilikinya juga ikut dihapus. 

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

#### Perbedaan *Authentication* dengan *Authorization*

- *Authentication* adalah proses untuk memverifikasi identitas pengguna. Saat pengguna memasukkan username dan password, sistem akan memeriksa apakah kombinasi tersebut sudah terdaftar dan valid. Jika ya, maka pengguna dianggap telah terautentikasi.
-  *Authorization* adalah proses untuk menentukan hak akses pengguna setelah mereka terautentikasi. Setelah pengguna login, sistem akan memeriksa peran atau izin yang dimiliki pengguna tersebut untuk menentukan tindakan apa saja yang boleh dilakukannya di dalam aplikasi.

#### Apa yang dilakukan Django saat pengguna login?

1. Pengguna akan diminta untuk memasukkan username dan password mereka pada form login.
2. Django akan mencari user dengan username yang sesuai di database. Jika user ditemukan, password yang telah dimasukkan akan dibandingkan dengan hash password yang tersimpan di database.
3. Jika password cocok, Django akan membuat sesi untuk pengguna tersebut. Sesi ini adalah sebuah mekanisme untuk melacak status login pengguna selama sesi berlangsung.
4. Setelah sesi dibuat, pengguna akan diarahkan ke halaman yang ditentukan, misalnya dashboard atau halaman utama.

#### Pengimplementasian *Authentication* dan *Authorization* pada Django

Untuk authentication, Django menyediakan modul `django.contrib.auth`, yang mencakup model `User` dan fungsi seperti `authenticate()` untuk memverifikasi username dan password, serta `login()` untuk memulai sesi bagi pengguna yang berhasil login. Proses ini menyimpan ID pengguna dalam sesi yang dapat diakses melalui request berikutnya.

Untuk authorization, Django menggunakan sistem izin berbasis peran dan grup. Setiap User dapat diberikan izin spesifik (misalnya, add_product atau delete_order) atau dapat dimasukkan ke dalam grup dengan izin tertentu. Django memeriksa izin ini melalui metode seperti `has_perm()` untuk memeriksa apakah pengguna diizinkan melakukan suatu tindakan. Django juga menyediakan dekorator seperti `@login_required` dan `@permission_required` untuk membatasi akses ke view berdasarkan authentication dan authorization.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login dengan menggunakan session cookies. Ketika seorang pengguna berhasil login, Django membuat sesi (session) dan menyimpan informasi sesi di server, seperti ID pengguna. Sesi ini diidentifikasi oleh sebuah cookie yang dikirimkan ke browser pengguna. Cookie tersebut berisi ID sesi yang memungkinkan Django mencocokkan pengguna dengan sesi yang tersimpan di server setiap kali pengguna mengirimkan request baru. Dengan begitu, meskipun pengguna berpindah halaman atau memulai request baru, Django tetap bisa mengenali pengguna selama cookie sesi tersebut masih berlaku dan belum kadaluarsa.

Selain untuk sesi login, cookies juga memiliki banyak kegunaan lain, seperti menyimpan preferensi pengguna, melacak aktivitas pengguna, dan menyimpan data sementara. Namun, tidak semua cookies aman digunakan. Risiko keamanan seperti serangan man-in-the-middle (MitM) bisa terjadi jika cookies dikirim tanpa enkripsi HTTPS, dan serangan XSS dapat mengekspos cookies jika situs tidak terlindungi dengan baik. Oleh karena itu, untuk meningkatkan keamanan, cookies harus dikonfigurasi dengan flag Secure agar hanya dikirim melalui HTTPS dan dilindungi dengan mekanisme tambahan seperti perlindungan CSRF, khususnya pada aplikasi web yang memproses data sensitif.

### Membuat Dua Akun dengan Tiga Dummy data di lokal
![Dummy Django 1](https://github.com/user-attachments/assets/78869ef8-1cce-48ed-9fff-59f36ab03b58)
![Dummy Django 2](https://github.com/user-attachments/assets/e79a56f3-a4d0-45fc-b877-c90d5117bb50)


### Cara Implementasi Proyek

- **Registration**
  1. Membuat fungsi `register` pada  `views.py` yang digunakan untuk handling registrasi user pada aplikasi kita.
  2. Menggunakan `UserCreationForm` dari Django untuk memproses data form yang diterima dari client.
  3. Menyimpan data user jika data tersebut valid ke database dan redirect user ke halaman login.
  4. Membuat `register.html` pada direktori `main/templates` yang berfungsi untuk menampilkan halaman registrasi user.
  5. Melakukan routing halaman register pada `main/urls.py`.

- **Login**
  1. Membuat fungsi `login_user` pada `views.py` yang berguna untuk mengautentikasi pengguna yang ingin login.
  2. Menggunakan `UserCreationForm` dari Django untuk memproses data form yang diterima dari client.
  3. Melakukan login berdasarkan data dari form login dengan menggunakan fungsi `login` yang telah disediakan oleh Django.
  4. Redirect request user ke halaman main, jika tidak ada kendala login.
  5. Menggunakan fungsi decorator `@login_required` pada fungsi `show_main` untuk merestriksi halaman main (hanya dapat diakses oleh user yang telah terdaftar).
  6.  Membuat `login.html` pada direktori `main/templates` yang berfungsi untuk menampilkan halaman login user.
  7.  Melakukan routing halaman login pada `main/urls.py`.

- **Logout**
  1. Membuat fungsi `logout_user` pada `views.py` yang berguna untuk menghapus sesi pengguna yang saat ini login.
  2. Melakukan logout dengan menggunakan fungsi `logout` yang telah disediakan oleh Django.
  3. Redirect user ke halaman , jika tidak ada kendala logout.
  4. Menambahkan link yang digunakan untuk logout pada `templates/main.html`.
  5. Melakukan routing logout pada `main/urls.py`.

- **Menggunakan Data dari Cookies**
  1. Memodifikasi bagian dari fungsi `login_user` menggunakan `HTTPResponseRedirect` dan `reverse` agar kita dapat menyisipkan data cookies pada response yang akan dikembalikan ke client sebelum melakukan redirect ke halaman main.
  2. Memodifikasi bagian dari fungsi `logout_user` menggunakan `HTTPResponseRedirect` dan `reverse` agar kita dapat menghapus cookies sebelum melakukan redirect ke halaman login.
  3. Menampilkan last_login dari data cookies di `main.hmtl` 

- **Menghubungkan Model Product dengan User**
  1. Menambahkan field bertipe ForeignKey pada Product model yang menghubungkan antara Product dan User dengan relasi satu User memiliki banyak Product.
  2. Memodifikasi fungsi `create_product` pada `views.py` agar menyimpan data mengenai current user yang membuat suatu product.
  3. Mengubah `templates/main.html` dan `show_main` di `views.py` agar hanya menampilkan product user yang sedang login.  

## Tugas 3

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery merupakan elemen krusial dalam pengimplementasian sebuah platform karena berperan dalam memastikan aliran informasi yang lancar dan efisien antara berbagai komponen, seperti server, database, dan antarmuka pengguna. Dengan sistem pengiriman data yang baik, platform mampu menyediakan akses informasi real-time, yang sangat penting untuk menjaga keakuratan dan relevansi data yang digunakan oleh pengguna. Selain itu, data delivery memastikan sinkronisasi antar sistem yang terintegrasi, sehingga data yang ada tetap konsisten di seluruh platform dan aplikasi terkait. Proses ini juga berdampak signifikan pada pengalaman pengguna, di mana pengiriman data yang cepat dan tepat waktu meningkatkan responsivitas platform, memberikan kesan yang lebih interaktif dan efisien. Dari sisi keamanan, pengiriman data yang handal membantu menjaga integritas dan konsistensi data, mengurangi risiko kebocoran atau pelanggaran, terutama dalam pengelolaan data sensitif.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Secara umum, **JSON** sering dianggap lebih baik dibandingkan **XML** dalam berbagai situasi karena kesederhanaan dan efisiensinya. Berikut adalah beberapa alasan mengapa JSON lebih populer dibandingkan XML:

1. **Lebih Ringkas dan Mudah Dibaca**

    Sintaks JSON lebih sederhana dan lebih mudah dipahami oleh manusia dibandingkan XML, yang menggunakan tag-tag panjang dan bersarang. Ini menjadikan JSON lebih efisien untuk ditransmisikan melalui jaringan karena ukuran datanya lebih kecil.

2. **Lebih Mudah Diproses oleh Mesin**
   
    JSON didukung secara native oleh hampir semua bahasa pemrograman modern, terutama **JavaScript**, tanpa memerlukan parser yang rumit seperti XML. JSON bekerja langsung dengan tipe data JavaScript seperti objek dan array, sehingga proses parsing menjadi lebih cepat dan efisien.

3. **Optimal untuk Aplikasi Web**

   JSON dirancang dengan fokus pada aplikasi web modern yang mengutamakan kecepatan dan kesederhanaan. Karena JSON adalah format bawaan JavaScript, JSON terintegrasi dengan baik dalam pengembangan aplikasi web, terutama dalam komunikasi antara client dan server menggunakan **AJAX** atau **RESTful APIs**.

4. **Struktur Data yang Sederhana**

   JSON lebih efektif dalam merepresentasikan data sederhana, seperti objek, array, dan daftar, tanpa memerlukan kompleksitas hierarki yang biasanya diperlukan dalam XML. Hal ini menjadikan JSON lebih cocok untuk aplikasi yang membutuhkan pertukaran data yang cepat dan sederhana.

Meskipun **XML** memiliki fitur yang kuat untuk pengolahan dokumen yang lebih kompleks, seperti dukungan skema dan namespaces, **JSON** lebih populer di kalangan pengembang web modern. Ini disebabkan oleh kecepatan, kesederhanaan, dan kemudahan integrasi JSON dengan aplikasi web.

### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` pada form Django digunakan untuk memeriksa apakah data yang dikirimkan melalui form sesuai dengan aturan validasi yang telah ditetapkan. Berikut adalah fungsi dari method ini:

1. **Memeriksa Kebenaran Data Input**
   
   `is_valid()` memastikan bahwa semua field dalam form diisi dengan benar, sesuai dengan tipe data, panjang input, atau aturan validasi lainnya yang telah ditentukan.

2. **Mengelola Kesalahan Validasi**
   Jika terdapat kesalahan dalam data input, method ini akan mengisi atribut `errors` pada form. Atribut ini dapat digunakan untuk menampilkan pesan kesalahan kepada pengguna, seperti field yang tidak diisi dengan benar atau format yang salah.

3. **Membersihkan Data Valid**
   Setelah validasi, `is_valid()` juga membersihkan data yang valid sehingga dapat diakses melalui `form.cleaned_data`. Data ini berisi informasi yang telah diverifikasi dan siap digunakan, misalnya untuk disimpan ke dalam database.

Method `is_valid()` sangat penting karena memastikan bahwa data yang diinputkan oleh pengguna aman dan sesuai dengan standar yang ditetapkan sebelum diproses lebih lanjut. Tanpa proses validasi, data yang tidak sesuai atau berpotensi berbahaya dapat masuk ke sistem, yang dapat menyebabkan kesalahan atau masalah keamanan.

###  Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

**CSRF token** (Cross-Site Request Forgery token) sangat penting dalam Django karena berfungsi melindungi aplikasi web dari serangan CSRF. Serangan ini memungkinkan penyerang untuk menyalahgunakan kredensial pengguna yang sah guna melakukan tindakan berbahaya tanpa persetujuan mereka. Dengan memasukkan CSRF token ke dalam form, Django memastikan bahwa setiap permintaan yang berhubungan dengan perubahan data berasal dari sumber yang valid dan terotorisasi. Ini mencegah serangan yang berpotensi mengubah data atau melakukan tindakan yang tidak diinginkan. Tanpa CSRF token, aplikasi menjadi lebih rentan terhadap serangan tersebut, di mana penyerang bisa menggunakan situs web jahat untuk mengirimkan permintaan otomatis ke aplikasi target dengan kredensial pengguna yang valid. Oleh karena itu, CSRF token sangat penting dalam menjaga keamanan aplikasi, melindungi data, dan mencegah penyalahgunaan tindakan pengguna.

### Cara Implementasi Proyek

1. Membuat base template yang akan digunakan sebagai kerangka web. Template ini akan digunakan sebagai dasar html kita yang lain sehingga dapat mengurangi redudansi kode.
    ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {% block meta %}
        {% endblock meta %}
    </head>
    <body>
        {% block content %}
        {% endblock content %}
    </body>
    </html>
   ```
   Mengkonfigurasi direktori template agar dapat digunakan oleh Django.
   ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
        }
    ]
   ```

2. Membuat file baru untuk `form` pada direktori `main` untuk membuat struktur form yang dapat menerima data `Product`.
   ```python
    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description"]

   ```

3. Membuat fungsi baru di `views.py` untuk menangani request dari form buat produk baru.
   ```python
    def create_product(request):
        form = ProductForm(request.POST or None)
        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect("main:show_main")
        context = {"form": form}
        return render(request, "create_product.html", context)
   ```
   Menampilkan form tersebut pada halaman html.
   ```html
    {% extends 'base.html' %}
    {% block content %}
    <section>
        <h1>Create New Product</h1>
        <form method="POST">
            {% csrf_token %}
            <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                <input type="submit" value="Add Product" />
                </td>
            </tr>
            </table>
        </form>
    </section>
    {% endblock content %}

   ```

4. Membuat html file untuk menampilkan semua data product jika ada.
    ```html
    {% extends 'base.html' %}
    {% block content %}
    ...
    <section>
        {% if not products %}
            <p>Belum ada data product pada wsnshop.</p>
        {% else %}
            <table>
            <tr>
                <th>Product ID</th>
                <th>Name</th>
                <th>Price</th>
                <th>Description</th>
            </tr>
            {% for product in products %}
                <tr>
                <td>{{product.id}}</td>
                <td>{{product.name}}</td>
                <td>{{product.price}}</td>
                <td>{{product.description}}</td>
                </tr>
            {% endfor %}
            </table>
        {% endif %}
        <a href="{% url 'main:create_product' %}">
            <button>Add New Product</button>
        </a>
    </section>
    {% endblock content %}

    ```

5. Membuat handler untuk menangani request untuk menampilkan data dalam format xml dan json.
    ```python
    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(
            serializers.serialize("xml", data), content_type="application/xml"
        )
    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(
            serializers.serialize("xml", data), content_type="application/xml"
        )
    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(
            serializers.serialize("json", data), content_type="application/json"
        )
    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(
            serializers.serialize("json", data), content_type="application/json"
        )
    ```

6. Melakukan routing pada `urls.py` agar request pada url tertentu dapat diproses. (`/create_product`, `/xml`, `/xml/:id`, `/json`, `/json/:id`).
   ```python
    urlpatterns = [
        ...
        path("create-product", create_product, name="create_product"),
        path("xml/", show_xml, name="show_xml"),
        path("xml/<str:id>/", show_xml_by_id, name="show_xml_by_id"),
        path("json/", show_json, name="show_json"),
        path("json/<str:id>/", show_json_by_id, name="show_json_by_id"),
    ]
   ```

### Screenshot Response Endpoints Dengan Menggunakan Postman

1. `/xml`
   
    ![XML](https://github.com/user-attachments/assets/e2195a3f-725c-4fad-b5a0-c0f14c9a9526)

2. `/xml/:id`
    
    ![XML By ID](https://github.com/user-attachments/assets/ec62a132-1aa9-49c8-8d6d-e49ccf9dfaaf)

3. `/json`
    
    ![JSON](https://github.com/user-attachments/assets/35ab8f2a-e849-4133-918e-79f3a33823d0)

4. `/json/:id`
    
    ![JSON By ID](https://github.com/user-attachments/assets/b3e942f7-0903-4e41-82f6-2cd2669956c7)



## Tugas 2

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

