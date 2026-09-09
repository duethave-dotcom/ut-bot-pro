# MetaTrader 5 Bot System

ده مشروع Python بسيط مبني باستخدام Flask. النسخة الحالية بتشغّل Web Server وتعرض صفحة حالة للمشروع. المشروع لسه **مش متصل فعلياً بـ MetaTrader 5** ومفيهوش منطق تداول في الوقت الحالي.

الهدف من الملف ده إن أي مطور جديد يفهم المشروع بسرعة، يشغّله على جهازه، يختبره، ويعمل أول Pull Request من غير ما يتوه.

## المشروع بيعمل إيه؟

لما التطبيق يشتغل، بيفتح endpoint رئيسي على `/`. الصفحة بتعرض إن السيرفر شغال ومستني إعدادات MetaTrader 5.

| العنوان | النتيجة المتوقعة |
| --- | --- |
| `/` | صفحة HTML فيها اسم المشروع وحالته |
| أي عنوان غير معروف | استجابة `404 Not Found` |

## المتطلبات

هتحتاج:

- Python 3.10 أو أحدث.
- Git.
- حساب GitHub لو هترفع تغييرات.

## تشغيل المشروع على جهازك

نزّل نسخة من المشروع وادخل على مجلده:

```bash
git clone https://github.com/duethave-dotcom/ut-bot-pro.git
cd ut-bot-pro
```

اعمل Virtual Environment منفصلة:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

على Windows:

```powershell
.venv\Scripts\activate
```

ثبّت المكتبات:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

شغّل السيرفر:

```bash
python main.py
```

افتح [http://localhost:10000](http://localhost:10000) في المتصفح.

التطبيق بيقرأ رقم الـ Port من متغير البيئة `PORT`. لو المتغير مش موجود، بيستخدم `10000` تلقائياً:

```bash
PORT=5000 python main.py
```

في Windows PowerShell:

```powershell
$env:PORT = "5000"
python main.py
```

## تشغيل التطبيق باستخدام Gunicorn

للتشغيل بطريقة أقرب لبيئة الإنتاج:

```bash
gunicorn main:app
```

## شكل المشروع

```text
ut-bot-pro/
├── .github/
│   ├── pull_request_template.md  # قالب الـ Pull Request
│   └── workflows/
│       └── ci.yml                # الفحص الأوتوماتيكي على GitHub
├── tests/
│   └── test_main.py              # اختبارات pytest
├── CONTRIBUTING.md               # دليل المساهمين والاختبار
├── README.md                     # الملف اللي إنت بتقرأه
├── main.py                       # نقطة بداية تطبيق Flask
└── requirements.txt              # مكتبات Python المطلوبة
```

### الملفات المهمة

| الملف | وظيفته |
| --- | --- |
| `main.py` | بينشئ تطبيق Flask، وبيعرّف الصفحة الرئيسية، وبيشغّل السيرفر محلياً. |
| `tests/test_main.py` | بيختبر إن الصفحة الرئيسية شغالة، ومحتواها صحيح، والـ routes غير الموجودة بترجع `404`. |
| `requirements.txt` | فيه Flask وGunicorn وpytest. |
| `.github/workflows/ci.yml` | بيشغّل الفحوصات تلقائياً مع كل Pull Request أو Push على `main`. |
| `CONTRIBUTING.md` | شرح تفصيلي لطريقة الاختبار والمساهمة في المشروع. |

## Unit Tests بـ pytest

الـ Unit Test هو اختبار صغير بيركّز على جزء محدد من الكود. في المشروع ده بنستخدم Flask test client، وده بيسمح لنا نطلب `/` من غير ما نشغّل سيرفر حقيقي على Port.

شغّل كل الاختبارات بالأمر ده:

```bash
python -m pytest -q
```

المفروض تشوف نتيجة شبيهة بـ:

```text
5 passed
```

كل اختبار في `tests/test_main.py` بيعمل حاجة واحدة واضحة:

| الاختبار | بيتأكد من إيه؟ |
| --- | --- |
| `test_home_returns_successful_response` | إن `/` بترجع Status Code رقم `200`. |
| `test_home_contains_project_status` | إن الصفحة فيها النصوص الأساسية. |
| `test_unknown_route_returns_not_found` | إن العنوان غير الموجود بترجع `404`. |
| `test_port_defaults_to_10000` | إن الـ Port الافتراضي هو `10000`. |
| `test_port_can_be_read_from_environment` | إن التطبيق يقدر يقرأ Port من البيئة. |

لما تضيف Feature جديدة، حاول تضيف Test يغطي السلوك المتوقع قبل فتح Pull Request. الاختبار الجيد يركّز على نتيجة واحدة، واسمه يشرح هو بيختبر إيه.

## GitHub Actions بيعمل إيه؟

الـ Workflow الموجود في `.github/workflows/ci.yml` بيشتغل تلقائياً عند:

- عمل Push على فرع `main`.
- فتح أو تحديث Pull Request هدفها `main`.

الفحص بيعمل الخطوات دي:

1. ينزّل الكود.
2. يجهّز Python 3.11.
3. يثبّت المكتبات من `requirements.txt`.
4. يفحص Syntax ملفات Python.
5. يشغّل `pytest`.
6. يشغّل Smoke Test ويتأكد إن السيرفر بيرد.

لو أي خطوة فشلت، افتح تبويب **Actions** في GitHub واقرأ الـ Logs قبل الدمج.

## إنشاء Branch جديد وفتحه كـ Pull Request

### 1. حدّث `main`

```bash
git checkout main
git pull origin main
```

### 2. اعمل Branch جديد

اختار اسم واضح، مثلاً:

```bash
git checkout -b feature/add-home-test
```

تقدر تتأكد إنك على الفرع الصح:

```bash
git branch --show-current
```

المفروض يطبع:

```text
feature/add-home-test
```

### 3. عدّل واختبر

بعد ما تعدّل الكود أو تضيف Test، شغّل:

```bash
python -m pytest -q
python -m compileall -q .
git diff --check
```

### 4. اعمل Commit

راجع الملفات الأول:

```bash
git status
git diff
```

بعدها أضف الملفات واعمل Commit:

```bash
git add .
git commit -m "Add homepage unit tests"
```

اكتب رسالة Commit قصيرة وواضحة، وتشرح التغيير مش كل التفاصيل.

### 5. اربط الـ Branch بـ GitHub

أول مرة ترفع الفرع استخدم:

```bash
git push -u origin feature/add-home-test
```

الخيار `-u` بيربط الفرع المحلي بالفرع اللي على GitHub. بعد كده تقدر تستخدم `git push` بس.

### 6. افتح Pull Request

بعد نجاح الـ Push:

1. افتح صفحة الريبو على GitHub.
2. اضغط **Compare & pull request**.
3. خلّي الـ Base branch هو `main`.
4. اختار الـ Compare branch بتاعك، مثل `feature/add-home-test`.
5. اكتب ملخص التغيير.
6. اكتب أوامر الاختبار ونتيجتها.
7. راجع الـ Checklist الموجود في قالب الـ Pull Request.
8. اضغط **Create pull request**.

بعد فتح الـ PR، استنى GitHub Actions يخلص. لو الفحص أخضر، اطلب من المراجع يراجع التغيير. لو الفحص أحمر، أصلح المشكلة على نفس الـ Branch واعمل Push جديد؛ الـ PR هيتحدّث تلقائياً.

## مثال لو أول Pull Request ليك

```bash
git checkout main
git pull origin main
git checkout -b test/add-homepage-tests

# عدّل أو أضف الملفات هنا
python -m pytest -q
python -m compileall -q .
git diff --check

git add tests/test_main.py requirements.txt .github/workflows/ci.yml
git commit -m "Add pytest coverage for homepage"
git push -u origin test/add-homepage-tests
```

بعد آخر أمر، افتح الرابط أو زر **Compare & pull request** اللي GitHub هيظهره لك.

## قواعد بسيطة للمساهمة

- ما ترفعش كلمات سر أو مفاتيح API أو ملفات `.env`.
- خليك محدد: كل Pull Request يفضل يعالج موضوع واحد.
- أي Feature جديدة يفضل يكون معاها Test.
- لو ضفت مكتبة، حدّث `requirements.txt` واختبر التثبيت من بيئة نظيفة.
- اكتب في الـ PR إيه اللي اتغير، وإزاي اختبرته، وهل فيه حاجة لسه ناقصة.
- ما تدمجش PR لو GitHub Actions فاشل إلا لو سبب الفشل معروف ومش متعلق بالتغيير، واكتب السبب بوضوح.

للتفاصيل الإضافية، راجع [دليل المساهمين](CONTRIBUTING.md).
