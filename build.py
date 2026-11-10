#!/usr/bin/env python3
"""Builds the QME homepage in English (index.html) and Arabic (ar/index.html).
Edit the text in EN / AR below, then run:  python3 build.py
"""
import json, os, html

SITE = "https://www.qme-eg.com"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

# number, English name, Arabic name, category key, existing page path
STANDARDS = [
    ("ISO 9001", "Quality management", "إدارة الجودة", "quality", "/quality-management-system-iso9001-2015/"),
    ("ISO 14001", "Environmental management", "الإدارة البيئية", "env", "/environmental-management-system-iso14001-2015/"),
    ("ISO 45001", "Occupational health and safety", "السلامة والصحة المهنية", "safety", "/occupational-health-safety-iso450012018/"),
    ("ISO 50001", "Energy management", "إدارة الطاقة", "env", "/energy-management-system-iso50001-2018/"),
    ("ISO 22000", "Food safety management", "إدارة سلامة الغذاء", "food", "/services/certification/food-safety-management-system-iso-22000/"),
    ("ISO 13485", "Medical devices quality management", "إدارة جودة الأجهزة الطبية", "quality", "/services/certification/elementor-page-4335/"),
    ("ISO 21001", "Educational organizations management", "إدارة المؤسسات التعليمية", "quality", "/educational-organization-management-system-iso21001-2018/"),
    ("ISO/IEC 27001", "Information security management", "إدارة أمن المعلومات", "it", "/information-security-management-system-iso27001-2013/"),
    ("ISO/IEC 20000-1", "IT service management", "إدارة خدمات تقنية المعلومات", "it", "/services/certification/it-service-management-system-iso-iec-20000-1/"),
    ("ISO/IEC 42001", "Artificial intelligence management", "إدارة الذكاء الاصطناعي", "it", "/services/certification/artificial-intelligence-management-system-iso-iec-42001/"),
    ("ISO 37001", "Anti-bribery management", "إدارة مكافحة الرشوة", "gov", "/services/certification/antibribery-management-system-iso37001-2016/"),
    ("ISO 37301", "Compliance management", "إدارة الامتثال", "gov", "/services/certification/compliance-management-system-iso-37301/"),
    ("ISO 22301", "Business continuity management", "إدارة استمرارية الأعمال", "gov", "/business-continuity-iso223012019/"),
    ("ISO 55001", "Asset management", "إدارة الأصول", "assets", "/asset-management-system-iso550012014/"),
    ("ISO 41001", "Facility management", "إدارة المرافق", "assets", "/facility-management-system-iso410012018/"),
]

EN = dict(
    lang="en", dir="ltr", path="/", alt_path="/ar/", alt_label="العربية", alt_lang="ar",
    font_href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&display=swap",
    font_stack="'Archivo', system-ui, -apple-system, 'Segoe UI', Arial, sans-serif",
    title="QME | ISO Certification, Lead Auditor Training & Sustainability Services in Egypt",
    desc="QME (Quality Middle East) is an EGAC-accredited certification body in Cairo. ISO 9001, 14001, 45001, 27001, 22000 and more, plus lead auditor training and carbon footprint services.",
    skip="Skip to content", menu="Menu",
    nav_cert="Certification", nav_train="Training", nav_sus="Sustainability", nav_acc="Accreditation",
    nav_verify="Verify a certificate", nav_contact="Contact", cta_quote="Request a quote",
    h1="ISO certification, auditor training and sustainability services in Egypt",
    lead="QME (Quality Middle East) audits and certifies management systems for organizations in Egypt and abroad. We are accredited by the Egyptian Accreditation Council (EGAC), a member of the International Accreditation Forum.",
    hero_fact="EGAC registration CAB 12203",
    reg_title="Standards we certify", reg_hint="Choose what you need to manage",
    cats=[("all", "All standards"), ("quality", "Quality"), ("env", "Environment and energy"), ("safety", "Health and safety"),
          ("food", "Food"), ("it", "IT and AI"), ("gov", "Governance and continuity"), ("assets", "Assets and facilities")],
    reg_note="Not sure which standard fits? Tell us your sector and we will point you to the right one.",
    reg_note_link="Ask us",
    proc_h="How certification works",
    proc_p="The same six steps apply to every standard. Your certificate is valid for three years and kept current through yearly audits.",
    steps=[
        ("Application and quote", "Send us your activities, sites and number of employees. We reply with a proposal and audit duration."),
        ("Stage 1 audit", "We review your documented system and confirm you are ready for the full audit."),
        ("Stage 2 audit", "Our auditors check on site that the system is implemented and working."),
        ("Certification decision", "The audit report is reviewed independently before the certificate is issued."),
        ("Surveillance audits", "A yearly audit confirms the system is maintained and improving."),
        ("Recertification", "A full audit before the three-year cycle ends renews your certificate."),
    ],
    proc_doc="Read the full certification process document",
    train_h="Training for auditors and teams",
    train_p="Courses in management systems, soft skills and technical subjects, taught by auditors who work with these standards every day.",
    train_items=[
        ("Lead Auditor courses", "Delivered through an international partner approved by Exemplar Global, for ISO 9001, 14001, 45001, 27001, 22000 and other standards.", "/lead-auditor-training/", "See Lead Auditor courses"),
        ("Internal auditor and transition courses", "Prepare your own team to audit your system and move to new versions of a standard.", "/list-of-courses/", "See the list of courses"),
        ("Courses built for your company", "We study your needs and design a programme around them. Check the dates already planned.", "/training-plan/", "See the training plan"),
    ],
    sus_h="Sustainability and carbon services",
    sus_p="Measure, report and reduce your environmental impact, with support for exporters who must meet EU carbon rules.",
    sus_items=[
        ("Organizational carbon footprint", "ISO 14064-1"), ("Project carbon footprint", "ISO 14064-2"),
        ("Product carbon footprint", "ISO 14067"), ("Path to net zero", "ISO 14068-1"),
        ("Environmental Product Declarations", "EPD"), ("Life cycle assessment", "LCA"),
        ("Carbon Border Adjustment Mechanism", "CBAM"),
    ],
    sus_link="See sustainability services",
    acc_h="Accreditation and registrations",
    acc_p="A certificate is only as credible as the body behind it. These are ours, and you can check each one.",
    acc_rows=[
        ("Egyptian Accreditation Council (EGAC)", "Accredited certification body for management systems. EGAC is a member of the International Accreditation Forum (IAF).", "CAB 12203"),
        ("Egyptian Organization for Standardization (EOS)", "Registered for ISO 9001, ISO 14001 and ISO 45001.", "CB120/01, CB120/02, CB120/09"),
        ("Exemplar Global", "Lead Auditor courses delivered through an approved international training partner.", ""),
    ],
    acc_num="Registration", acc_link="See accreditation details and scope",
    verify_h="Check that a QME certificate is valid",
    verify_p="Anyone can confirm a certificate we issued, its scope and its current status.",
    verify_btn="Verify a certificate",
    faq_h="Common questions",
    faqs=[
        ("What is the difference between certification and accreditation?", "Certification is what your organization receives after a successful audit. Accreditation is what a certification body like QME holds, granted by a national authority such as EGAC, to show it audits competently and impartially."),
        ("How long is an ISO certificate valid?", "Three years, as long as the yearly surveillance audits are passed. A recertification audit before expiry starts the next cycle."),
        ("Can QME help us build the system and then certify it?", "No. To stay impartial, a certification body does not consult for the organizations it certifies. We can train your team, and we audit the system you build."),
        ("What do you need to prepare a quote?", "Your activities, the standard or standards you want, the number of sites and the number of employees. Use the form below or call us."),
    ],
    contact_h="Request a quote or ask a question",
    contact_p="Tell us about your organization and we will reply with a proposal. You can also use this form to send a complaint or an appeal.",
    f_name="Your name", f_company="Company", f_email="Email", f_phone="Phone",
    f_subject="Subject", f_opts=["Inquiry or quote", "Complaint", "Appeal"],
    f_std="Standard or service you are interested in", f_msg="Message", f_send="Send message",
    f_note="Sending opens your email app with the message ready to send to qme@qme-eg.com.",
    c_addr_l="Address", c_addr="5 Street 2, Maadi, Cairo, Egypt", c_mob_l="Mobile", c_tel_l="Tel / fax", c_mail_l="Email",
    foot_tag="Quality means efficiency.",
    foot_docs="Public documents",
    docs=[("Quality policy", "/quality-policy/"), ("Confidentiality and impartiality", "/confid_impartiality-policy/"),
          ("Complaints and appeals", "/complains-appeals/"), ("Terms of use of logo", "/use-of-logo/"),
          ("Certification process", "/qme-pd-06-certification-process/"), ("Security policy", "/qme-pd-09_security-policy/"),
          ("Company brochure", "/brochure-qme-pd-05/")],
    foot_co="Company", co=[("About us", "/about-us/"), ("News", "/news/"), ("Contact", "/contact-us/")],
    rights="QME, Quality Middle East. All rights reserved.",
)

AR = dict(EN,
    lang="ar", dir="rtl", path="/ar/", alt_path="/", alt_label="English", alt_lang="en",
    font_href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap",
    font_stack="'IBM Plex Sans Arabic', 'Segoe UI', Tahoma, Arial, sans-serif",
    title="QME | شهادات الأيزو وتدريب كبير المراجعين وخدمات الاستدامة في مصر",
    desc="كيو إم إي (Quality Middle East) جهة منح شهادات معتمدة من المجلس الوطني للاعتماد (إيجاك) في القاهرة. أيزو 9001 و14001 و45001 و27001 و22000 وغيرها، مع تدريب كبير المراجعين وخدمات البصمة الكربونية.",
    skip="انتقل إلى المحتوى", menu="القائمة",
    nav_cert="الشهادات", nav_train="التدريب", nav_sus="الاستدامة", nav_acc="الاعتماد",
    nav_verify="تحقق من شهادة", nav_contact="اتصل بنا", cta_quote="اطلب عرض سعر",
    h1="شهادات الأيزو وتدريب المراجعين وخدمات الاستدامة في مصر",
    lead="تقوم QME (Quality Middle East) بمراجعة نظم الإدارة ومنح شهاداتها للمؤسسات داخل مصر وخارجها. نحن معتمدون من المجلس الوطني للاعتماد (إيجاك)، عضو المنتدى الدولي للاعتماد.",
    hero_fact="رقم التسجيل لدى إيجاك CAB 12203",
    reg_title="المواصفات التي نمنح شهاداتها", reg_hint="اختر ما تريد إدارته",
    cats=[("all", "كل المواصفات"), ("quality", "الجودة"), ("env", "البيئة والطاقة"), ("safety", "السلامة والصحة المهنية"),
          ("food", "الغذاء"), ("it", "تقنية المعلومات والذكاء الاصطناعي"), ("gov", "الحوكمة والاستمرارية"), ("assets", "الأصول والمرافق")],
    reg_note="لست متأكدًا من المواصفة المناسبة؟ أخبرنا بمجال عملك وسنرشدك إلى الأنسب.",
    reg_note_link="اسألنا",
    proc_h="كيف تتم عملية منح الشهادة",
    proc_p="الخطوات الست نفسها تنطبق على كل المواصفات. الشهادة سارية لمدة ثلاث سنوات وتُجدَّد صلاحيتها بمراجعات سنوية.",
    steps=[
        ("الطلب وعرض السعر", "أرسل لنا أنشطتك ومواقعك وعدد العاملين، ونرد عليك بعرض يتضمن مدة المراجعة."),
        ("مراجعة المرحلة الأولى", "نراجع النظام الموثق ونتأكد من جاهزيتك للمراجعة الكاملة."),
        ("مراجعة المرحلة الثانية", "يتحقق مراجعونا في الموقع من أن النظام مطبق وفعّال."),
        ("قرار منح الشهادة", "يُراجَع تقرير المراجعة بشكل مستقل قبل إصدار الشهادة."),
        ("مراجعات المتابعة", "مراجعة سنوية تؤكد استمرار تطبيق النظام وتحسينه."),
        ("إعادة منح الشهادة", "مراجعة كاملة قبل انتهاء دورة الثلاث سنوات لتجديد شهادتك."),
    ],
    proc_doc="اقرأ وثيقة عملية منح الشهادات كاملة",
    train_h="تدريب للمراجعين وفرق العمل",
    train_p="دورات في نظم الإدارة والمهارات الشخصية والموضوعات الفنية، يقدمها مراجعون يعملون بهذه المواصفات يوميًا.",
    train_items=[
        ("دورات كبير المراجعين", "تُقدَّم من خلال شريك دولي معتمد من Exemplar Global، لمواصفات أيزو 9001 و14001 و45001 و27001 و22000 وغيرها.", "/lead-auditor-training/", "دورات كبير المراجعين"),
        ("دورات المراجع الداخلي والانتقال للإصدارات الجديدة", "جهّز فريقك لمراجعة نظامكم والانتقال إلى الإصدارات الجديدة من المواصفات.", "/list-of-courses/", "قائمة الدورات"),
        ("دورات مصممة لشركتك", "ندرس احتياجاتك ونصمم برنامجًا يناسبها. اطّلع على المواعيد المخططة.", "/training-plan/", "خطة التدريب"),
    ],
    sus_h="خدمات الاستدامة والكربون",
    sus_p="قِس أثرك البيئي وأعدّ تقاريره وخفّضه، مع دعم للمصدّرين الملزمين بقواعد الكربون الأوروبية.",
    sus_items=[
        ("البصمة الكربونية للمؤسسة", "ISO 14064-1"), ("البصمة الكربونية للمشروعات", "ISO 14064-2"),
        ("البصمة الكربونية للمنتج", "ISO 14067"), ("الطريق إلى الحياد الكربوني", "ISO 14068-1"),
        ("الإعلانات البيئية للمنتجات", "EPD"), ("تقييم دورة الحياة", "LCA"),
        ("آلية تعديل حدود الكربون", "CBAM"),
    ],
    sus_link="خدمات الاستدامة",
    acc_h="الاعتماد والتسجيلات",
    acc_p="قيمة الشهادة من مصداقية الجهة التي تصدرها. هذه اعتماداتنا، ويمكنك التحقق من كل منها.",
    acc_rows=[
        ("المجلس الوطني للاعتماد (إيجاك)", "جهة منح شهادات معتمدة لنظم الإدارة. إيجاك عضو في المنتدى الدولي للاعتماد (IAF).", "CAB 12203"),
        ("الهيئة المصرية العامة للمواصفات والجودة (EOS)", "مسجلون لمواصفات أيزو 9001 وأيزو 14001 وأيزو 45001.", "CB120/01, CB120/02, CB120/09"),
        ("Exemplar Global", "دورات كبير المراجعين تُقدَّم من خلال شريك تدريب دولي معتمد.", ""),
    ],
    acc_num="رقم التسجيل", acc_link="تفاصيل الاعتماد ومجاله",
    verify_h="تحقق من صلاحية شهادة صادرة عن QME",
    verify_p="يمكن لأي شخص التأكد من شهادة أصدرناها ومن مجالها وحالتها الحالية.",
    verify_btn="تحقق من شهادة",
    faq_h="أسئلة شائعة",
    faqs=[
        ("ما الفرق بين الشهادة والاعتماد؟", "الشهادة هي ما تحصل عليه مؤسستك بعد اجتياز المراجعة. أما الاعتماد فهو ما تحصل عليه جهة منح الشهادات مثل QME من جهة وطنية مثل إيجاك، لإثبات أنها تراجع بكفاءة وحياد."),
        ("ما مدة صلاحية شهادة الأيزو؟", "ثلاث سنوات، بشرط اجتياز مراجعات المتابعة السنوية. وتبدأ الدورة التالية بمراجعة إعادة منح الشهادة قبل انتهاء الصلاحية."),
        ("هل يمكن أن تساعدنا QME في بناء النظام ثم تمنحنا الشهادة؟", "لا. حفاظًا على الحياد، لا تقدم جهة منح الشهادات استشارات للمؤسسات التي تمنحها الشهادة. يمكننا تدريب فريقك، ثم نراجع النظام الذي تبنونه."),
        ("ما المعلومات المطلوبة لإعداد عرض السعر؟", "أنشطتك، والمواصفة أو المواصفات المطلوبة، وعدد المواقع وعدد العاملين. استخدم النموذج أدناه أو اتصل بنا."),
    ],
    contact_h="اطلب عرض سعر أو اطرح سؤالًا",
    contact_p="أخبرنا عن مؤسستك وسنرد عليك بعرض. يمكنك أيضًا استخدام هذا النموذج لتقديم شكوى أو تظلم.",
    f_name="الاسم", f_company="الشركة", f_email="البريد الإلكتروني", f_phone="الهاتف",
    f_subject="الموضوع", f_opts=["استفسار أو عرض سعر", "شكوى", "تظلم"],
    f_std="المواصفة أو الخدمة المطلوبة", f_msg="الرسالة", f_send="إرسال الرسالة",
    f_note="عند الإرسال يفتح تطبيق البريد لديك والرسالة جاهزة للإرسال إلى qme@qme-eg.com.",
    c_addr_l="العنوان", c_addr="5 شارع 2، المعادي، القاهرة، مصر", c_mob_l="المحمول", c_tel_l="تليفون / فاكس", c_mail_l="البريد الإلكتروني",
    foot_tag="الجودة تعني الكفاءة.",
    foot_docs="وثائق عامة",
    docs=[("سياسة الجودة", "/quality-policy/"), ("السرية والحياد", "/confid_impartiality-policy/"),
          ("الشكاوى والتظلمات", "/complains-appeals/"), ("شروط استخدام الشعار", "/use-of-logo/"),
          ("عملية منح الشهادات", "/qme-pd-06-certification-process/"), ("سياسة أمن المعلومات", "/qme-pd-09_security-policy/"),
          ("كتيّب الشركة", "/brochure-qme-pd-05/")],
    foot_co="الشركة", co=[("من نحن", "/about-us/"), ("الأخبار", "/news/"), ("اتصل بنا", "/contact-us/")],
    rights="QME, Quality Middle East. جميع الحقوق محفوظة.",
)

CSS = """
:root{--ink:#0D2B3E;--ink2:#17425C;--seal:#1B7F5F;--stamp:#E5A823;--paper:#FAFBF9;--mist:#E6EEEA;--text:#2E3D47;--line:#CBD8D2}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:var(--font);color:var(--text);background:var(--paper);font-size:17px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:var(--seal);text-underline-offset:3px}
a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,summary:focus-visible{outline:3px solid var(--stamp);outline-offset:2px}
h1,h2,h3{color:var(--ink);line-height:1.15;margin:0 0 .5em;font-weight:700;letter-spacing:-.01em}
[dir=rtl] h1,[dir=rtl] h2,[dir=rtl] h3{letter-spacing:0;line-height:1.35}
h1{font-size:clamp(2.1rem,4.6vw,3.5rem);font-weight:800}
h2{font-size:clamp(1.6rem,3vw,2.3rem)}
h3{font-size:1.15rem}
p{margin:0 0 1em;max-width:62ch}
.wrap{max-width:1180px;margin-inline:auto;padding-inline:24px}
.skip{position:absolute;inset-inline-start:-999px;top:0;background:var(--ink);color:#fff;padding:10px 16px;z-index:9}
.skip:focus{inset-inline-start:8px;top:8px}
.btn{display:inline-block;background:var(--seal);color:#fff;text-decoration:none;font-weight:600;padding:13px 22px;border-radius:4px;border:2px solid var(--seal);font:inherit;font-weight:600;cursor:pointer}
.btn:hover{background:#156a4f;border-color:#156a4f}
.btn.ghost{background:transparent;color:var(--ink);border-color:var(--ink)}
.btn.ghost:hover{background:var(--ink);color:#fff}
.btn.light{background:var(--stamp);border-color:var(--stamp);color:var(--ink)}

/* header */
.top{position:sticky;top:0;z-index:5;background:rgba(250,251,249,.96);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;gap:20px;min-height:68px}
.brand{display:flex;align-items:center;text-decoration:none;color:var(--ink);font-weight:800;font-size:1.5rem;letter-spacing:.02em}
.brand img{height:44px;width:auto;display:block}
.nav{display:flex;gap:22px;margin-inline-start:auto;align-items:center}
.nav a{color:var(--ink);text-decoration:none;font-size:.95rem;font-weight:500}
.nav a:hover{color:var(--seal)}
.nav .lang{border:1px solid var(--line);padding:4px 10px;border-radius:4px}
.nav .btn{color:#fff;padding:9px 16px}
.burger{display:none;margin-inline-start:auto;background:none;border:1px solid var(--line);border-radius:4px;padding:8px 12px;font:inherit;color:var(--ink)}

/* hero */
.hero{padding:64px 0 0}
.hero .wrap{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:56px;align-items:start}
.hero .lead{font-size:1.15rem}
.cta{display:flex;flex-wrap:wrap;gap:12px;margin:28px 0 22px}
.fact{display:inline-flex;align-items:center;gap:10px;font-weight:600;color:var(--ink);font-size:.95rem}
.fact::before{content:"";width:14px;height:14px;border-radius:50%;background:var(--stamp);box-shadow:0 0 0 4px rgba(229,168,35,.25)}

/* standards register: the signature element */
.register{background:var(--ink);color:#DCE7EC;border-radius:6px 6px 0 0;padding:28px 28px 8px;margin-bottom:-1px}
.register h2{color:#fff;font-size:1.3rem;margin-bottom:4px}
.register .hint{font-size:.9rem;color:#9FB6C2;margin-bottom:14px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:14px}
.chips button{font:inherit;font-size:.85rem;background:transparent;color:#DCE7EC;border:1px solid #3B6079;border-radius:99px;padding:5px 12px;cursor:pointer}
.chips button[aria-pressed=true]{background:var(--stamp);border-color:var(--stamp);color:var(--ink);font-weight:600}
.reg-list{list-style:none;margin:0;padding:0;border-top:1px solid #2A5069}
.reg-list li{border-bottom:1px solid #2A5069}
.reg-list li[hidden]{display:none}
.reg-list a{display:grid;grid-template-columns:8.6em 1fr;gap:16px;align-items:baseline;padding:9px 4px;color:#fff;text-decoration:none}
.reg-list a:hover{background:var(--ink2)}
.reg-list .num{font-weight:700;font-variant-numeric:tabular-nums;color:var(--stamp);white-space:nowrap;direction:ltr;text-align:start;font-size:.95rem}
[dir=rtl] .reg-list .num{text-align:end}
.reg-list .nm{font-size:.98rem}
.reg-note{font-size:.9rem;color:#9FB6C2;padding:14px 0}
.reg-note a{color:#fff}

section{padding:84px 0}
.band{background:var(--mist)}
.dark{background:var(--ink);color:#DCE7EC}
.dark h2{color:#fff}

/* process */
.steps{list-style:none;counter-reset:s;margin:36px 0 24px;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:2px solid var(--ink)}
.steps li{counter-increment:s;padding:22px 24px 26px 0;border-bottom:1px solid var(--line);padding-inline:0 24px}
.steps li::before{content:counter(s);display:block;font-size:2.4rem;font-weight:800;color:var(--seal);line-height:1;margin-bottom:10px;font-variant-numeric:tabular-nums}
.steps p{font-size:.97rem;margin:0}

/* two-column services */
.split{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:56px}
.rows{border-top:2px solid var(--ink)}
.rows>div{padding:20px 0;border-bottom:1px solid var(--line)}
.rows p{margin:0 0 6px;font-size:.97rem}
.sus{list-style:none;margin:0;padding:0;border-top:2px solid var(--ink);columns:2;column-gap:40px}
.sus li{break-inside:avoid;padding:12px 0;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;gap:12px;align-items:baseline}
.sus .code{font-size:.85rem;font-weight:600;color:var(--seal);white-space:nowrap;direction:ltr}

/* accreditation */
.acc{width:100%;border-collapse:collapse;margin:28px 0 20px}
.acc th,.acc td{text-align:start;vertical-align:top;padding:18px 16px 18px 0;padding-inline:0 16px;border-bottom:1px solid #2A5069}
.acc tr:first-child th,.acc tr:first-child td{border-top:2px solid var(--stamp)}
.acc th{color:#fff;font-weight:700;width:32%}
.acc .reg{color:var(--stamp);font-weight:700;white-space:nowrap;direction:ltr;text-align:start}
.dark a{color:#fff}
.verify{margin-top:44px;padding:28px;border:1px solid #3B6079;border-radius:6px;display:flex;flex-wrap:wrap;gap:20px;align-items:center;justify-content:space-between}
.verify h3{color:#fff;font-size:1.3rem;margin-bottom:4px}
.verify p{margin:0}

/* faq */
details{border-bottom:1px solid var(--line);padding:16px 0}
details:first-of-type{border-top:2px solid var(--ink)}
summary{cursor:pointer;font-weight:600;color:var(--ink);font-size:1.05rem}
details p{margin:10px 0 0}

/* contact */
form{display:grid;grid-template-columns:1fr 1fr;gap:14px 16px}
form .full{grid-column:1/-1}
label{display:block;font-size:.9rem;font-weight:600;color:var(--ink);margin-bottom:4px}
input,select,textarea{width:100%;font:inherit;padding:11px 12px;border:1px solid #9FB1A9;border-radius:4px;background:#fff;color:var(--text)}
textarea{min-height:120px;resize:vertical}
.fnote{font-size:.85rem;color:#5A6B75;margin:0}
.cinfo{margin:24px 0 0;padding:0}
.cinfo div{padding:12px 0;border-bottom:1px solid var(--line)}
.cinfo dt{font-size:.85rem;font-weight:600;color:#5A6B75}
.cinfo dd{margin:0;font-weight:600;color:var(--ink)}
.cinfo a{color:var(--ink)}
.ltr{direction:ltr;unicode-bidi:isolate;display:inline-block}

footer{background:var(--ink);color:#B9CBD4;padding:56px 0 28px;font-size:.93rem}
footer .wrap{display:grid;grid-template-columns:1.2fr 2fr 1fr;gap:40px}
footer h3{color:#fff;font-size:1rem}
footer ul{list-style:none;margin:0;padding:0}
footer .cols2{columns:2}
footer li{padding:3px 0}
footer a{color:#DCE7EC;text-decoration:none}
footer a:hover{text-decoration:underline}
.fbrand{color:#fff;font-weight:800;font-size:1.5rem}
.legal{grid-column:1/-1;border-top:1px solid #2A5069;padding-top:18px;font-size:.85rem}

@media (max-width:940px){
 .hero .wrap,.split,footer .wrap{grid-template-columns:1fr;gap:36px}
 .steps{grid-template-columns:1fr 1fr}
 .burger{display:block}
 .nav{display:none;position:absolute;top:68px;inset-inline:0;background:var(--paper);border-bottom:1px solid var(--line);flex-direction:column;align-items:flex-start;padding:16px 24px;gap:14px;margin:0}
 .nav.open{display:flex}
 section{padding:60px 0}
 .hero{padding-top:40px}
}
@media (max-width:600px){
 body{font-size:16px}
 .steps{grid-template-columns:1fr}
 .sus{columns:1}
 form{grid-template-columns:1fr}
 .acc,.acc tbody,.acc tr,.acc th,.acc td{display:block;width:auto}
 .acc th{border:0;padding-bottom:4px}
 .acc tr:first-child td{border-top:0}
 .acc td{border:0;padding-top:0;padding-bottom:6px}
 .acc tr{border-bottom:1px solid #2A5069;padding-bottom:10px}
 .register{padding:22px 18px 4px;border-radius:0;margin-inline:-24px}
 footer .cols2{columns:1}
}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
"""

JS = """
(function(){
  var b=document.querySelector('.burger'),n=document.getElementById('nav');
  b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});
  n.addEventListener('click',function(e){if(e.target.tagName==='A'){n.classList.remove('open');b.setAttribute('aria-expanded','false')}});
  var chips=document.querySelectorAll('.chips button'),items=document.querySelectorAll('.reg-list li');
  chips.forEach(function(c){c.addEventListener('click',function(){
    chips.forEach(function(x){x.setAttribute('aria-pressed',x===c)});
    var k=c.dataset.cat;items.forEach(function(li){li.hidden=!(k==='all'||li.dataset.cat===k)});
  })});
  var f=document.getElementById('quote');
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var d=new FormData(f),L=function(k){return f.querySelector('[name="'+k+'"]').closest('div').querySelector('label').textContent};
    var body=['name','company','email','phone','standard'].map(function(k){return L(k)+': '+(d.get(k)||'')}).join('\\n')+'\\n\\n'+(d.get('message')||'');
    location.href='mailto:qme@qme-eg.com?subject='+encodeURIComponent(d.get('subject')+' - '+(d.get('company')||d.get('name')))+'&body='+encodeURIComponent(body);
  });
})();
"""

def e(s): return html.escape(s, quote=True)

def render(t):
    ar = t["lang"] == "ar"
    url = SITE + t["path"]
    ld = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "name": "QME", "alternateName": "Quality Middle East", "url": SITE + "/",
        "logo": SITE + "/wp-content/uploads/2022/03/logo.png",
        "description": t["desc"], "telephone": "+201009190780", "email": "qme@qme-eg.com",
        "address": {"@type": "PostalAddress", "streetAddress": "5 Street 2", "addressLocality": "Maadi",
                    "addressRegion": "Cairo", "addressCountry": "EG"},
        "areaServed": "EG",
        "sameAs": ["https://web.facebook.com/qme.eg", "https://eg.linkedin.com/in/qmeeg"],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": t["reg_title"], "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": f"{n} {(a if ar else en)}", "url": SITE + p}}
            for n, en, a, c, p in STANDARDS]},
    }
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faqs"]]}

    chips = "".join(f'<button type="button" data-cat="{k}" aria-pressed="{"true" if k=="all" else "false"}">{e(l)}</button>' for k, l in t["cats"])
    reg = "".join(f'<li data-cat="{c}"><a href="{p}"><span class="num">{n}</span><span class="nm">{e(a if ar else en)}</span></a></li>' for n, en, a, c, p in STANDARDS)
    steps = "".join(f"<li><h3>{e(h)}</h3><p>{e(p)}</p></li>" for h, p in t["steps"])
    train = "".join(f'<div><h3>{e(h)}</h3><p>{e(p)}</p><a href="{u}">{e(l)}</a></div>' for h, p, u, l in t["train_items"])
    sus = "".join(f'<li><span>{e(n)}</span><span class="code">{c}</span></li>' for n, c in t["sus_items"])
    acc = "".join(f'<tr><th scope="row">{e(n)}</th><td>{e(d)}</td><td class="reg">{e(r)}</td></tr>' for n, d, r in t["acc_rows"])
    faqs = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in t["faqs"])
    opts = "".join(f"<option>{e(o)}</option>" for o in t["f_opts"])
    docs = "".join(f'<li><a href="{u}">{e(l)}</a></li>' for l, u in t["docs"])
    co = "".join(f'<li><a href="{u}">{e(l)}</a></li>' for l, u in t["co"])

    return f"""<!DOCTYPE html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{SITE}/">
<link rel="alternate" hreflang="ar" href="{SITE}/ar/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="QME">
<meta property="og:title" content="{e(t['title'])}">
<meta property="og:description" content="{e(t['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/wp-content/uploads/2022/03/logo.png">
<meta property="og:locale" content="{'ar_EG' if ar else 'en_US'}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="/wp-content/uploads/2022/04/cropped-icon-270x270.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{t['font_href']}">
<style>:root{{--font:{t['font_stack']}}}{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">{e(t['skip'])}</a>
<header class="top"><div class="wrap">
  <a class="brand" href="{t['path']}" aria-label="QME"><img src="/wp-content/uploads/2022/03/logo.png" alt="QME, Quality Middle East" width="150" height="72" onerror="this.replaceWith(document.createTextNode('QME'))"></a>
  <button class="burger" type="button" aria-expanded="false" aria-controls="nav">{e(t['menu'])}</button>
  <nav class="nav" id="nav" aria-label="{e(t['menu'])}">
    <a href="#certification">{e(t['nav_cert'])}</a>
    <a href="#training">{e(t['nav_train'])}</a>
    <a href="#sustainability">{e(t['nav_sus'])}</a>
    <a href="#accreditation">{e(t['nav_acc'])}</a>
    <a href="/certificate-search/">{e(t['nav_verify'])}</a>
    <a class="lang" href="{t['alt_path']}" lang="{t['alt_lang']}" hreflang="{t['alt_lang']}">{t['alt_label']}</a>
    <a class="btn" href="#contact">{e(t['cta_quote'])}</a>
  </nav>
</div></header>

<main id="main">
<div class="hero"><div class="wrap">
  <div>
    <h1>{e(t['h1'])}</h1>
    <p class="lead">{e(t['lead'])}</p>
    <div class="cta"><a class="btn" href="#contact">{e(t['cta_quote'])}</a><a class="btn ghost" href="/certificate-search/">{e(t['nav_verify'])}</a></div>
    <a class="fact" href="#accreditation">{e(t['hero_fact'])}</a>
  </div>
  <div class="register" id="certification">
    <h2>{e(t['reg_title'])}</h2>
    <p class="hint">{e(t['reg_hint'])}</p>
    <div class="chips" role="group" aria-label="{e(t['reg_hint'])}">{chips}</div>
    <ul class="reg-list">{reg}</ul>
    <p class="reg-note">{e(t['reg_note'])} <a href="#contact">{e(t['reg_note_link'])}</a></p>
  </div>
</div></div>

<section class="band" id="process"><div class="wrap">
  <h2>{e(t['proc_h'])}</h2>
  <p>{e(t['proc_p'])}</p>
  <ol class="steps">{steps}</ol>
  <a href="/qme-pd-06-certification-process/">{e(t['proc_doc'])}</a>
</div></section>

<section id="training"><div class="wrap split">
  <div><h2>{e(t['train_h'])}</h2><p>{e(t['train_p'])}</p></div>
  <div class="rows">{train}</div>
</div></section>

<section class="band" id="sustainability"><div class="wrap split">
  <div><h2>{e(t['sus_h'])}</h2><p>{e(t['sus_p'])}</p><a href="/sustainability/">{e(t['sus_link'])}</a></div>
  <ul class="sus">{sus}</ul>
</div></section>

<section class="dark" id="accreditation"><div class="wrap">
  <h2>{e(t['acc_h'])}</h2>
  <p>{e(t['acc_p'])}</p>
  <table class="acc"><tbody>{acc}</tbody></table>
  <a href="/accreditation-registrations/">{e(t['acc_link'])}</a>
  <div class="verify"><div><h3>{e(t['verify_h'])}</h3><p>{e(t['verify_p'])}</p></div><a class="btn light" href="/certificate-search/">{e(t['verify_btn'])}</a></div>
</div></section>

<section id="faq"><div class="wrap split">
  <h2>{e(t['faq_h'])}</h2>
  <div>{faqs}</div>
</div></section>

<section class="band" id="contact"><div class="wrap split">
  <div>
    <h2>{e(t['contact_h'])}</h2>
    <p>{e(t['contact_p'])}</p>
    <dl class="cinfo">
      <div><dt>{e(t['c_addr_l'])}</dt><dd>{e(t['c_addr'])}</dd></div>
      <div><dt>{e(t['c_mob_l'])}</dt><dd><a class="ltr" href="tel:+201009190780">010 0919 0780</a></dd></div>
      <div><dt>{e(t['c_tel_l'])}</dt><dd><a class="ltr" href="tel:+20227508044">+20 2 2750 8044</a></dd></div>
      <div><dt>{e(t['c_mail_l'])}</dt><dd><a class="ltr" href="mailto:qme@qme-eg.com">qme@qme-eg.com</a></dd></div>
    </dl>
  </div>
  <form id="quote" novalidate-off>
    <div><label for="f-name">{e(t['f_name'])}</label><input id="f-name" name="name" required autocomplete="name"></div>
    <div><label for="f-company">{e(t['f_company'])}</label><input id="f-company" name="company" autocomplete="organization"></div>
    <div><label for="f-email">{e(t['f_email'])}</label><input id="f-email" name="email" type="email" required autocomplete="email" dir="ltr"></div>
    <div><label for="f-phone">{e(t['f_phone'])}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" dir="ltr"></div>
    <div><label for="f-subject">{e(t['f_subject'])}</label><select id="f-subject" name="subject">{opts}</select></div>
    <div><label for="f-std">{e(t['f_std'])}</label><input id="f-std" name="standard"></div>
    <div class="full"><label for="f-msg">{e(t['f_msg'])}</label><textarea id="f-msg" name="message"></textarea></div>
    <div class="full"><button class="btn" type="submit">{e(t['f_send'])}</button></div>
    <p class="fnote full">{e(t['f_note'])}</p>
  </form>
</div></section>
</main>

<footer><div class="wrap">
  <div><div class="fbrand">QME</div><p>Quality Middle East<br>{e(t['foot_tag'])}</p>
    <p><a href="https://web.facebook.com/qme.eg" rel="noopener">Facebook</a> &nbsp; <a href="https://eg.linkedin.com/in/qmeeg" rel="noopener">LinkedIn</a></p></div>
  <div><h3>{e(t['foot_docs'])}</h3><ul class="cols2">{docs}</ul></div>
  <div><h3>{e(t['foot_co'])}</h3><ul>{co}</ul></div>
  <p class="legal">&copy; <span id="y">2026</span> {e(t['rights'])}</p>
</div></footer>
<script>{JS}</script>
</body>
</html>
""".replace(" novalidate-off", "")

os.makedirs(os.path.join(OUT, "ar"), exist_ok=True)
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(render(EN))
open(os.path.join(OUT, "ar", "index.html"), "w", encoding="utf-8").write(render(AR))
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /wp-admin/\nAllow: /wp-admin/admin-ajax.php\n\nSitemap: {SITE}/sitemap.xml\n")
urls = ["/", "/ar/", "/about-us/", "/services/certification/", "/training/", "/lead-auditor-training/", "/list-of-courses/",
        "/training-plan/", "/sustainability/", "/accreditation-registrations/", "/certificate-search/", "/news/", "/contact-us/"] + [s[4] for s in STANDARDS]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
     "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
print("built", OUT)
