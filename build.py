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


# ---------- design v2: modern and colorful, brand colors from the QME logo ----------
EN.update(
    font_href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap",
    font_stack="'Plus Jakarta Sans', system-ui, -apple-system, 'Segoe UI', Arial, sans-serif",
    brand_name="Quality Middle East", brand_tag="Certification and training",
    hero_badge="Accredited by EGAC",
    svc=[("Certification", "Audits and certificates for 15 ISO management system standards.", "#certification", "See the standards"),
         ("Training", "Lead Auditor, internal auditor and tailored courses for your team.", "#training", "See the courses"),
         ("Sustainability", "Carbon footprint, EPD, life cycle assessment and CBAM support.", "#sustainability", "See the services")],
    ill_title="Management System Certificate", ill_ok="Audit passed",
    h1a="ISO Certification, Auditor Training and Sustainability Services", h1b="in Egypt",
    cert_p="Pick what your organization needs to manage and see the standards that fit.",
)
AR.update(
    font_href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&display=swap",
    font_stack="'Cairo', 'Segoe UI', Tahoma, Arial, sans-serif",
    brand_name="Quality Middle East", brand_tag="منح الشهادات والتدريب",
    hero_badge="معتمدون من إيجاك",
    svc=[("الشهادات", "مراجعات وشهادات لـ 15 مواصفة أيزو لنظم الإدارة.", "#certification", "المواصفات"),
         ("التدريب", "دورات كبير المراجعين والمراجع الداخلي ودورات مصممة لفريقك.", "#training", "الدورات"),
         ("الاستدامة", "البصمة الكربونية والإعلانات البيئية وتقييم دورة الحياة ودعم CBAM.", "#sustainability", "الخدمات")],
    ill_title="شهادة نظام إدارة", ill_ok="تم اجتياز المراجعة",
    h1a="شهادات الأيزو وتدريب المراجعين وخدمات الاستدامة", h1b="في مصر",
    cert_p="اختر ما تحتاج مؤسستك إلى إدارته لتظهر لك المواصفات المناسبة.",
)

ICONS = {
    "ISO 9001": '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.8 2.8L16 9.5"/>',
    "ISO 14001": '<path d="M5 19c0-8 5-13 14-14 0 9-5 14-12 14"/><path d="M5 19c2-4 5-7 9-9"/>',
    "ISO 45001": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M12 8v8M8 12h8"/>',
    "ISO 50001": '<path d="M13 2L5 14h6l-1 8 8-12h-6z"/>',
    "ISO 22000": '<path d="M6 3v8M9 3v8M6 7h3M7.5 11v10"/><path d="M17 3c-2 2-2 6 0 8v10"/>',
    "ISO 13485": '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M12 8v8M8 12h8"/>',
    "ISO 21001": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11.5V16c3 2.5 9 2.5 12 0v-4.5"/>',
    "ISO/IEC 27001": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 018 0v3"/>',
    "ISO/IEC 20000-1": '<rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><path d="M7 7.5h.01M7 16.5h.01"/>',
    "ISO/IEC 42001": '<rect x="7" y="7" width="10" height="10" rx="2"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/>',
    "ISO 37001": '<path d="M12 4v16M6 20h12M5 8h14"/><path d="M5 8l-3 6a3 3 0 006 0zM19 8l-3 6a3 3 0 006 0z"/>',
    "ISO 37301": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9zM9 13l2 2 4-4"/>',
    "ISO 22301": '<path d="M20 12a8 8 0 01-14 5M4 12a8 8 0 0114-5"/><path d="M18 3v4h-4M6 21v-4h4"/>',
    "ISO 55001": '<path d="M3 8l9-5 9 5v8l-9 5-9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/>',
    "ISO 41001": '<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M10 21v-4h4v4"/>',
}
ICONS.update({
    "plane": '<path d="M21 3L3 10.5l7 2.5 2.5 7z"/><path d="M10 13l5-5"/>',
    "shieldcheck": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>',
    "doc": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8h6M9 12h6M9 16h3"/>',
})
def ico(k, cls="ico"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[k]}</svg>'

CSS = """
:root{--blue:#1B4F9C;--blue-d:#0F2F66;--blue-l:#2F7DE1;--red:#D8232A;--green:#2A9D4B;--sky:#EEF5FD;--text:#33415A;--head:#0F2A55;--line:#D9E4F2;--card:#fff}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:100px}
body{margin:0;font-family:var(--font);color:var(--text);background:#fff;font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}
a{color:var(--blue);text-underline-offset:3px}
a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,summary:focus-visible{outline:3px solid #F5B301;outline-offset:2px}
h1,h2,h3{color:var(--head);line-height:1.2;margin:0 0 .5em;font-weight:700}
[dir=rtl] h1,[dir=rtl] h2,[dir=rtl] h3{line-height:1.45}
h1{font-size:clamp(2rem,3.9vw,3.1rem);font-weight:800}
h2{font-size:clamp(1.6rem,2.8vw,2.2rem)}
h3{font-size:1.15rem}
p{margin:0 0 1em;max-width:64ch}
.wrap{max-width:1240px;margin-inline:auto;padding-inline:24px}
.center{text-align:center}.center p{margin-inline:auto}
.skip{position:absolute;inset-inline-start:-999px;top:0;background:var(--blue-d);color:#fff;padding:10px 16px;z-index:9}
.skip:focus{inset-inline-start:8px;top:8px}
.btn{display:inline-block;background:var(--red);color:#fff;text-decoration:none;font:inherit;font-weight:700;padding:13px 26px;border-radius:999px;border:2px solid var(--red);cursor:pointer;box-shadow:0 8px 20px rgba(216,35,42,.25)}
.btn:hover{background:#b91c22;border-color:#b91c22}
.btn.white{background:#fff;color:var(--blue-d);border-color:#fff;box-shadow:none}
.btn.white:hover{background:var(--sky)}
.btn.line{background:transparent;color:#fff;border-color:rgba(255,255,255,.7);box-shadow:none}
.btn.line:hover{background:rgba(255,255,255,.14)}
.ico{width:26px;height:26px;flex:none}

/* header */
.top{position:sticky;top:0;z-index:5;background:#fff;box-shadow:0 2px 14px rgba(15,47,102,.08)}
.top .wrap{display:flex;align-items:center;gap:18px;min-height:92px}
.brand{display:flex;align-items:center;gap:14px;text-decoration:none;color:var(--blue)}
.brand img{height:68px;width:auto;display:block}
.brand .mark{font-size:2.4rem;font-weight:800;letter-spacing:.02em}
.brand .bt{display:flex;flex-direction:column;line-height:1.2;border-inline-start:2px solid var(--line);padding-inline-start:14px}
.brand .bn{font-size:1.3rem;font-weight:800;color:var(--blue-d)}
.brand .bg{font-size:.9rem;font-weight:600;color:var(--green)}
.nav{display:flex;gap:20px;margin-inline-start:auto;align-items:center}
.nav a{color:var(--head);text-decoration:none;font-size:.95rem;font-weight:600}
.nav a:hover{color:var(--blue-l)}
.nav .lang{border:1.5px solid var(--line);padding:5px 12px;border-radius:999px}
.nav .btn{color:#fff;padding:10px 20px}
.burger{display:none;margin-inline-start:auto;background:var(--sky);border:0;border-radius:10px;padding:10px 14px;font:inherit;font-weight:600;color:var(--blue-d)}

/* hero */
.hero{position:relative;overflow:hidden;color:#fff;background:linear-gradient(125deg,#0F2F66 0%,#1B4F9C 45%,#2F7DE1 100%);padding:72px 0 150px}
[dir=rtl] .hero{background:linear-gradient(235deg,#0F2F66 0%,#1B4F9C 45%,#2F7DE1 100%)}
.hero::before,.hero::after{content:"";position:absolute;border-radius:50%;background:rgba(255,255,255,.07)}
.hero::before{width:520px;height:520px;inset-inline-end:-140px;top:-180px}
.hero::after{width:300px;height:300px;inset-inline-start:-90px;bottom:-120px}
.hero .wrap{position:relative;z-index:1;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:48px;align-items:center}
.hero h1{color:#fff}
.hero .lead{font-size:1.13rem;color:#DCE9FB}
.badge{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.3);border-radius:999px;padding:6px 16px;font-size:.9rem;font-weight:600;margin-bottom:20px;color:#fff;text-decoration:none}
.badge i{width:10px;height:10px;border-radius:50%;background:#5EE08A;box-shadow:0 0 0 4px rgba(94,224,138,.25)}
.cta{display:flex;flex-wrap:wrap;gap:12px;margin:28px 0 18px}
.fact{color:#DCE9FB;font-weight:600;font-size:.95rem}
.ill{position:relative;min-height:340px}
.cert{position:absolute;inset-inline-start:8%;top:14px;width:74%;background:#fff;border-radius:18px;padding:26px 26px 30px;box-shadow:0 30px 60px rgba(6,22,56,.45);transform:rotate(-3deg);color:var(--head)}
[dir=rtl] .cert{transform:rotate(3deg)}
.cert .bar{height:10px;border-radius:99px;background:linear-gradient(90deg,var(--blue),var(--red) 55%,var(--green));margin-bottom:18px}
.cert b{display:block;font-size:1.05rem;margin-bottom:14px}
.cert .ln{height:9px;border-radius:99px;background:#E3ECF7;margin-bottom:10px}
.cert .ln.s{width:60%}
.seal{position:absolute;inset-inline-end:22px;bottom:-26px;width:84px;height:84px;border-radius:50%;background:var(--green);display:flex;align-items:center;justify-content:center;color:#fff;border:6px solid #fff;box-shadow:0 10px 22px rgba(42,157,75,.4)}
.seal .ico{width:40px;height:40px}
.ok{display:inline-flex;align-items:center;gap:6px;margin-top:8px;font-size:.88rem;font-weight:700;color:var(--green)}
.ok .ico{width:18px;height:18px}
.chip{position:absolute;display:flex;align-items:center;gap:8px;background:#fff;color:var(--blue-d);font-weight:700;font-size:.9rem;padding:9px 14px;border-radius:14px;box-shadow:0 14px 30px rgba(6,22,56,.35)}
.chip .ico{width:20px;height:20px}
.chip.c1{inset-inline-end:0;top:0;color:var(--blue)}
.chip.c2{inset-inline-end:2%;top:150px;color:var(--green)}
.chip.c3{inset-inline-start:0;bottom:6px;color:var(--red)}

/* service cards overlapping hero */
.svc{position:relative;z-index:2;margin-top:-96px;padding:0}
.svc .wrap{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.sc{background:var(--card);border-radius:20px;padding:28px;box-shadow:0 18px 44px rgba(15,47,102,.14);display:flex;flex-direction:column;gap:8px;border-top:5px solid var(--blue)}
.sc:nth-child(2){border-top-color:var(--red)}.sc:nth-child(3){border-top-color:var(--green)}
.sc .ib{width:56px;height:56px;border-radius:16px;background:var(--sky);color:var(--blue);display:flex;align-items:center;justify-content:center;margin-bottom:6px}
.sc:nth-child(2) .ib{background:#FDECEC;color:var(--red)}.sc:nth-child(3) .ib{background:#E9F7ED;color:var(--green)}
.sc h3{font-size:1.3rem;margin:0}
.sc p{margin:0;font-size:.98rem}
.sc a{font-weight:700;text-decoration:none;margin-top:6px}

section{padding:88px 0}
.tint{background:var(--sky)}

/* standards */
.chips{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin:26px 0 30px}
.chips button{font:inherit;font-size:.92rem;font-weight:600;background:#fff;color:var(--head);border:1.5px solid var(--line);border-radius:999px;padding:8px 18px;cursor:pointer}
.chips button:hover{border-color:var(--blue-l)}
.chips button[aria-pressed=true]{background:var(--blue);border-color:var(--blue);color:#fff}
.reg-list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:18px}
.reg-list li[hidden]{display:none}
.reg-list a{display:flex;gap:14px;align-items:center;height:100%;background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;text-decoration:none;color:var(--head);transition:transform .15s,box-shadow .15s,border-color .15s}
.reg-list a:hover{transform:translateY(-3px);box-shadow:0 14px 30px rgba(15,47,102,.14);border-color:var(--blue-l)}
.reg-list .ib{width:50px;height:50px;border-radius:14px;flex:none;display:flex;align-items:center;justify-content:center;background:var(--sky);color:var(--blue)}
.reg-list li[data-cat=env] .ib,.reg-list li[data-cat=food] .ib{background:#E9F7ED;color:var(--green)}
.reg-list li[data-cat=safety] .ib,.reg-list li[data-cat=gov] .ib{background:#FDECEC;color:var(--red)}
.reg-list .num{display:block;font-weight:800;color:var(--blue);direction:ltr;font-size:1.02rem}
[dir=rtl] .reg-list .num{text-align:right}
.reg-list .nm{font-size:.93rem;line-height:1.35;display:block;color:var(--text)}
.reg-note{text-align:center;margin:28px auto 0}

/* process */
.steps{list-style:none;counter-reset:s;margin:40px 0 28px;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.steps li{counter-increment:s;background:#fff;border-radius:18px;padding:26px;border:1px solid var(--line);position:relative}
.steps li::before{content:counter(s);display:flex;align-items:center;justify-content:center;width:46px;height:46px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--blue-l));color:#fff;font-size:1.2rem;font-weight:800;margin-bottom:14px}
.steps p{font-size:.97rem;margin:0}

/* training and sustainability */
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:36px}
.tc{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px;display:flex;flex-direction:column;gap:8px;text-align:start}
.tc .ib{width:50px;height:50px;border-radius:14px;background:#FDECEC;color:var(--red);display:flex;align-items:center;justify-content:center}
.tc p{margin:0;font-size:.97rem;flex:1}
.tc a{font-weight:700;text-decoration:none}
.green{background:linear-gradient(135deg,#1E7D3A,#2A9D4B);color:#EAF8EE}
.green h2{color:#fff}
.green .wrap{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:48px;align-items:center}
.green a{color:#fff;font-weight:700}
.sus{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.sus li{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.28);border-radius:14px;padding:14px 16px;display:flex;flex-direction:column;gap:2px;color:#fff;font-weight:600}
.sus .code{font-size:.82rem;font-weight:700;color:#C9F2D5;direction:ltr}
[dir=rtl] .sus .code{text-align:right}

/* accreditation */
.accs{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin:36px 0 22px}
.ac{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px;text-align:start}
.ac p{font-size:.97rem;margin:0 0 12px}
.ac .reg{display:inline-block;background:var(--sky);color:var(--blue);font-weight:800;border-radius:10px;padding:6px 12px;direction:ltr;font-size:.95rem}
.ac small{display:block;font-size:.8rem;font-weight:600;color:#6B7A93;margin-bottom:4px}
.verify{margin-top:44px;padding:34px;border-radius:22px;background:linear-gradient(125deg,#0F2F66,#2F7DE1);color:#DCE9FB;display:flex;flex-wrap:wrap;gap:20px;align-items:center;justify-content:space-between;text-align:start}
.verify h3{color:#fff;font-size:1.4rem;margin-bottom:4px}
.verify p{margin:0}

/* faq */
.faq{max-width:860px;margin:30px auto 0}
details{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px 20px;margin-bottom:12px}
summary{cursor:pointer;font-weight:700;color:var(--head);font-size:1.03rem}
details p{margin:10px 0 0}

/* contact */
.contact .wrap{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:48px}
form{display:grid;grid-template-columns:1fr 1fr;gap:14px 16px;background:#fff;border-radius:22px;padding:30px;box-shadow:0 18px 44px rgba(15,47,102,.12)}
form .full{grid-column:1/-1}
label{display:block;font-size:.9rem;font-weight:700;color:var(--head);margin-bottom:4px}
input,select,textarea{width:100%;font:inherit;padding:11px 14px;border:1.5px solid var(--line);border-radius:12px;background:#fff;color:var(--text)}
textarea{min-height:120px;resize:vertical}
.fnote{font-size:.85rem;color:#6B7A93;margin:0}
.cinfo{margin:24px 0 0;padding:0;display:grid;gap:12px}
.cinfo div{background:#fff;border-radius:14px;padding:14px 18px;border:1px solid var(--line)}
.cinfo dt{font-size:.82rem;font-weight:700;color:#6B7A93}
.cinfo dd{margin:0;font-weight:700;color:var(--head)}
.cinfo a{color:var(--head);text-decoration:none}
.ltr{direction:ltr;unicode-bidi:isolate;display:inline-block}

footer{background:var(--blue-d);color:#B9CBE8;padding:60px 0 28px;font-size:.93rem}
footer .wrap{display:grid;grid-template-columns:1.3fr 2fr 1fr;gap:40px}
footer h3{color:#fff;font-size:1rem}
footer ul{list-style:none;margin:0;padding:0}
footer .cols2{columns:2}
footer li{padding:3px 0}
footer a{color:#DCE9FB;text-decoration:none}
footer a:hover{text-decoration:underline}
.fbrand{color:#fff;font-weight:800;font-size:1.7rem;line-height:1.2}
.fbrand span{display:block;font-size:1rem;font-weight:600;color:#B9CBE8}
.legal{grid-column:1/-1;border-top:1px solid rgba(255,255,255,.16);padding-top:18px;font-size:.85rem;max-width:none}

@media (max-width:1120px){
 .burger{display:block}
 .nav{display:none;position:absolute;top:92px;inset-inline:0;background:#fff;box-shadow:0 14px 24px rgba(15,47,102,.12);flex-direction:column;align-items:flex-start;padding:18px 24px;gap:14px;margin:0}
 .nav.open{display:flex}
}
@media (max-width:900px){
 .hero .wrap,.green .wrap,.contact .wrap,footer .wrap{grid-template-columns:1fr;gap:36px}
 .svc .wrap,.grid3,.accs,.steps{grid-template-columns:1fr}
 .ill{min-height:300px;max-width:440px}
 section{padding:64px 0}
 .hero{padding:48px 0 140px}
}
@media (max-width:600px){
 body{font-size:16px}
 .top .wrap{min-height:78px}.nav{top:78px}
 .brand img{height:54px}.brand .mark{font-size:2rem}
 .brand .bn{font-size:1.05rem}.brand .bg{font-size:.8rem}
 .sus{grid-template-columns:1fr}
 form{grid-template-columns:1fr;padding:22px}
 footer .cols2{columns:1}
}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.reg-list a{transition:none}}
"""

CSS += """
/* v3: light hero, per client mockup */
body{background:#fff}
h1{font-size:clamp(1.7rem,3vw,2.5rem);line-height:1.22}
.wrap{max-width:1320px}
.top{box-shadow:0 2px 18px rgba(15,47,102,.10)}
.top .wrap{min-height:116px;max-width:1480px}
.brand img{height:86px}.brand .mark{font-size:3rem}
.brand .bn{font-size:1.5rem}.brand .bg{font-size:1rem}
.nav .lang{display:inline-flex;align-items:center;gap:6px}
.nav .lang .ico{width:18px;height:18px;color:var(--blue)}
.btn{display:inline-flex;align-items:center;gap:10px;background:linear-gradient(135deg,#3DB24F,#1E8A3A);border:0;padding:15px 28px;box-shadow:0 10px 22px rgba(42,157,75,.32)}
.btn:hover{background:linear-gradient(135deg,#34A046,#187A32)}
.btn .ico{width:20px;height:20px}
.btn.navy,.nav .btn.navy{background:linear-gradient(135deg,#1B4F9C,#0F2F66);box-shadow:0 10px 22px rgba(15,47,102,.28);padding:13px 24px}
.btn.out{background:#fff;color:var(--blue);border:2px solid var(--blue);padding:13px 26px;box-shadow:none}
.btn.out:hover{background:var(--sky)}
.btn.white{background:#fff;color:var(--blue-d);border:0;box-shadow:none}
.arrow::after{content:"\\2192";font-weight:700;margin-inline-start:2px}
[dir=rtl] .arrow::after{content:"\\2190"}
.hero{color:var(--text);background:linear-gradient(180deg,#F1F7FF 0%,#fff 100%);padding:56px 0 140px}
[dir=rtl] .hero{background:linear-gradient(180deg,#F1F7FF 0%,#fff 100%)}
.hero::before,.hero::after{display:none}
.hero .wrap{grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr);gap:32px}
.hero h1{color:var(--blue-d)}
.hero h1 .eg{color:var(--green);display:inline-block;border-bottom:4px solid #7AD15A;border-radius:0 0 40px 4px;padding-bottom:2px}
.hero .lead{color:var(--text);font-size:1.08rem}
.fact{color:var(--head);border-inline-start:4px solid var(--green);padding-inline-start:12px;font-size:.95rem}
.fact a{color:inherit;text-decoration:none}
.ill{min-height:440px}
.sky{position:absolute;inset:-56px -40px -60px 0;width:calc(100% + 40px);height:calc(100% + 116px);border-radius:0 0 0 80px}
[dir=rtl] .sky{transform:scaleX(-1)}
.cert{inset-inline-start:6%;top:46px;width:50%;transform:rotate(-5deg);border-radius:6px;padding:26px 24px 20px;border:1px solid #E8D9A8;outline:5px solid #fff;box-shadow:0 26px 50px rgba(15,47,102,.28)}
[dir=rtl] .cert{transform:rotate(5deg)}
.cert b{font-size:1.25rem;line-height:1.25;margin-bottom:16px;max-width:75%}
.cert .ln{height:8px;background:#E6EDF6}
.sig{width:90px;height:30px;display:block;margin-top:14px}
.gold{position:absolute;inset-inline-end:-18px;top:34px;width:64px;height:64px;border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFE9A6,#E3A812 60%,#B97E00);border:3px solid #fff;box-shadow:0 8px 16px rgba(185,126,0,.4);display:flex;align-items:center;justify-content:center}
.gold i{width:30px;height:30px;border-radius:50%;border:2px solid rgba(255,255,255,.85)}
.gold::after{content:"";position:absolute;top:56px;left:20px;width:24px;height:34px;background:linear-gradient(#2F7DE1,#1B4F9C);clip-path:polygon(0 0,100% 0,100% 100%,50% 76%,0 100%);z-index:-1}
.shield{position:absolute;inset-inline-start:40%;top:210px;width:150px;filter:drop-shadow(0 16px 22px rgba(21,87,192,.4))}
.isos{position:absolute;inset-inline-end:0;top:36px;display:flex;flex-direction:column;gap:14px;width:35%}
.iso{display:flex;align-items:center;gap:12px;background:#fff;border-radius:16px;padding:12px 14px;box-shadow:0 12px 26px rgba(15,47,102,.18)}
.iso .ib{width:44px;height:44px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;background:var(--sky);color:var(--blue)}
.iso:nth-child(2) .ib{background:#E9F7ED;color:var(--green)}
.iso b{white-space:nowrap;display:block;color:var(--blue-d);font-size:.98rem;direction:ltr}
[dir=rtl] .iso b{text-align:right}
.iso small{display:block;font-size:.78rem;line-height:1.3;color:var(--text)}
/* service cards */
.sc{flex-direction:row;gap:18px;align-items:flex-start;border-top:0;position:relative;overflow:hidden;padding:28px 26px 32px}
.sc::after{content:"";position:absolute;bottom:0;inset-inline-start:0;width:46%;height:7px;border-radius:0 8px 0 0;background:linear-gradient(90deg,#1B4F9C,#4FA3FF)}
[dir=rtl] .sc::after{border-radius:8px 0 0 0}
.sc:nth-child(2)::after{background:linear-gradient(90deg,#1E8A3A,#7AD15A)}
.sc:nth-child(3)::after{background:linear-gradient(90deg,#5B34B8,#A987F2)}
.sc .ib{width:66px;height:66px;border-radius:50%;flex:none;margin:0;background:linear-gradient(135deg,#DCEBFB,#B9D6F8);color:var(--blue)}
.sc:nth-child(2) .ib{background:linear-gradient(135deg,#DDF4E2,#B5E6BF);color:#1E8A3A}
.sc:nth-child(3) .ib{background:linear-gradient(135deg,#EBE3FB,#D2C1F6);color:#5B34B8}
.sc .ib .ico{width:32px;height:32px}
.sc .no{position:absolute;top:14px;inset-inline-end:20px;font-size:2rem;font-weight:800;color:#DCE7F5;line-height:1}
.sc h3{font-size:1.35rem;margin-bottom:6px}
.sc p{margin-bottom:8px}
.sc a{display:inline-block}
/* section headings */
.center h2::before{content:"";display:block;width:60px;height:5px;border-radius:99px;background:linear-gradient(90deg,#7AD15A,#2A9D4B);margin:0 auto 14px}
/* standards cards */
.reg-list .ib{border-radius:50%}
.reg-list a::after{content:"\\203A";margin-inline-start:auto;font-size:1.5rem;font-weight:700;color:var(--blue);line-height:1}
[dir=rtl] .reg-list a::after{content:"\\2039"}
.reg-list li[data-cat=food] .ib{background:#FFF0DE;color:#E9821A}
.reg-list li[data-cat=gov] .ib{background:#EFE9FB;color:#5B34B8}
.reg-list li[data-cat=assets] .ib{background:#E2F5F4;color:#12867F}
.tc .ib{border-radius:50%}
@media (max-width:1120px){.nav{top:116px}}
@media (max-width:900px){
 .hero .wrap{grid-template-columns:1fr}
 .hero{padding:40px 0 130px}
 .ill{min-height:400px;max-width:560px;margin-inline:auto;width:100%}
 .sky{inset:-20px -24px -40px -24px;width:calc(100% + 48px);height:calc(100% + 60px);border-radius:28px}
}
@media (max-width:600px){
 .top .wrap{min-height:92px}.nav{top:92px}
 .brand img{height:64px}.brand .mark{font-size:2.2rem}
 .brand .bn{font-size:1.1rem}.brand .bg{font-size:.82rem}
 .ill{min-height:360px}
 .cert{width:56%;top:30px;padding:18px 16px 14px}.cert b{font-size:1rem}
 .isos{width:40%;gap:10px;top:16px}.iso{padding:8px 10px;gap:8px}.iso .ib{width:34px;height:34px}.iso small{display:none}
 .shield{width:110px;top:190px;inset-inline-start:34%}
 .sc .no{font-size:1.6rem}
}

/* v4: client artwork as hero image */
.ill{min-height:0}
.heroimg{display:block;width:calc(100% + 70px);max-width:none;height:auto;margin-top:-56px;margin-inline-end:-70px;border-radius:0 0 0 70px;-webkit-mask-image:linear-gradient(to right,transparent,#000 16%);mask-image:linear-gradient(to right,transparent,#000 16%)}
[dir=rtl] .heroimg{border-radius:0 0 70px 0;-webkit-mask-image:linear-gradient(to left,transparent,#000 16%);mask-image:linear-gradient(to left,transparent,#000 16%)}
@media (max-width:900px){.ill{max-width:none}.heroimg,[dir=rtl] .heroimg{width:100%;margin:0;border-radius:22px;-webkit-mask-image:none;mask-image:none}}
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
    reg = "".join(f'<li data-cat="{c}"><a href="{p}"><span class="ib">{ico(n)}</span><span><span class="num">{n}</span><span class="nm">{e(a if ar else en)}</span></span></a></li>' for n, en, a, c, p in STANDARDS)
    svc_icons = ["doc", "ISO 21001", "ISO 14001"]
    svc = "".join(f'<div class="sc"><span class="no">0{i}</span><span class="ib">{ico(k)}</span><div><h3>{e(h)}</h3><p>{e(p)}</p><a class="arrow" href="{u}">{e(l)}</a></div></div>' for i, ((h, p, u, l), k) in enumerate(zip(t["svc"], svc_icons), 1))
    isos = "".join(f'<span class="iso"><span class="ib">{ico(n)}</span><span><b>{n}</b><small>{e(a if ar else en)}</small></span></span>' for n, en, a, c, p in STANDARDS[:3])
    steps = "".join(f"<li><h3>{e(h)}</h3><p>{e(p)}</p></li>" for h, p in t["steps"])
    tr_icons = ["ISO 21001", "ISO 37301", "ISO 55001"]
    train = "".join(f'<div class="tc"><span class="ib">{ico(k)}</span><h3>{e(h)}</h3><p>{e(p)}</p><a href="{u}">{e(l)}</a></div>' for (h, p, u, l), k in zip(t["train_items"], tr_icons))
    sus = "".join(f'<li><span>{e(n)}</span><span class="code">{c}</span></li>' for n, c in t["sus_items"])
    acc = "".join(f'<div class="ac"><h3>{e(n)}</h3><p>{e(d)}</p>' + (f'<small>{e(t["acc_num"])}</small><span class="reg">{e(r)}</span>' if r else "") + "</div>" for n, d, r in t["acc_rows"])
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
<meta name="theme-color" content="#1B4F9C">
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
  <a class="brand" href="{t['path']}" aria-label="QME, Quality Middle East">
    <img src="/wp-content/uploads/2022/03/logo.png" alt="QME" width="142" height="68" onerror="var s=document.createElement('span');s.className='mark';s.textContent='QME';this.replaceWith(s)">
    <span class="bt"><span class="bn">{e(t['brand_name'])}</span><span class="bg">{e(t['brand_tag'])}</span></span>
  </a>
  <button class="burger" type="button" aria-expanded="false" aria-controls="nav">{e(t['menu'])}</button>
  <nav class="nav" id="nav" aria-label="{e(t['menu'])}">
    <a href="#certification">{e(t['nav_cert'])}</a>
    <a href="#training">{e(t['nav_train'])}</a>
    <a href="#sustainability">{e(t['nav_sus'])}</a>
    <a href="#accreditation">{e(t['nav_acc'])}</a>
    <a href="/certificate-search/">{e(t['nav_verify'])}</a>
    <a class="lang" href="{t['alt_path']}" lang="{t['alt_lang']}" hreflang="{t['alt_lang']}">{ico('globe')}{t['alt_label']}</a>
    <a class="btn navy arrow" href="#contact">{e(t['cta_quote'])}</a>
  </nav>
</div></header>

<main id="main">
<div class="hero"><div class="wrap">
  <div>
    <h1>{e(t['h1a'])} <span class="eg">{e(t['h1b'])}</span></h1>
    <p class="lead">{e(t['lead'])}</p>
    <div class="cta"><a class="btn arrow" href="#contact">{ico('plane')}{e(t['cta_quote'])}</a><a class="btn out" href="/certificate-search/">{ico('shieldcheck')}{e(t['nav_verify'])}</a></div>
    <p class="fact"><a href="#accreditation">{e(t['hero_fact'])}</a></p>
  </div>
  <div class="ill" aria-hidden="true"><img class="heroimg" src="/img/hero.jpg" alt="" width="810" height="734"></div>
</div></div>

<div class="svc"><div class="wrap">{svc}</div></div>

<section id="certification"><div class="wrap center">
  <h2>{e(t['reg_title'])}</h2>
  <p>{e(t['cert_p'])}</p>
  <div class="chips" role="group" aria-label="{e(t['reg_hint'])}">{chips}</div>
  <ul class="reg-list" style="text-align:start">{reg}</ul>
  <p class="reg-note">{e(t['reg_note'])} <a href="#contact">{e(t['reg_note_link'])}</a></p>
</div></section>

<section class="tint" id="process"><div class="wrap center">
  <h2>{e(t['proc_h'])}</h2>
  <p>{e(t['proc_p'])}</p>
  <ol class="steps" style="text-align:start">{steps}</ol>
  <a href="/qme-pd-06-certification-process/">{e(t['proc_doc'])}</a>
</div></section>

<section id="training"><div class="wrap center">
  <h2>{e(t['train_h'])}</h2>
  <p>{e(t['train_p'])}</p>
  <div class="grid3">{train}</div>
</div></section>

<section class="green" id="sustainability"><div class="wrap">
  <div><h2>{e(t['sus_h'])}</h2><p>{e(t['sus_p'])}</p><a href="/sustainability/">{e(t['sus_link'])}</a></div>
  <ul class="sus">{sus}</ul>
</div></section>

<section id="accreditation"><div class="wrap center">
  <h2>{e(t['acc_h'])}</h2>
  <p>{e(t['acc_p'])}</p>
  <div class="accs">{acc}</div>
  <a href="/accreditation-registrations/">{e(t['acc_link'])}</a>
  <div class="verify"><div><h3>{e(t['verify_h'])}</h3><p>{e(t['verify_p'])}</p></div><a class="btn white" href="/certificate-search/">{e(t['verify_btn'])}</a></div>
</div></section>

<section class="tint" id="faq"><div class="wrap">
  <h2 class="center">{e(t['faq_h'])}</h2>
  <div class="faq">{faqs}</div>
</div></section>

<section class="contact" id="contact"><div class="wrap">
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
  <form id="quote">
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
  <div><div class="fbrand">QME<span>Quality Middle East</span></div><p>{e(t['foot_tag'])}</p>
    <p><a href="https://web.facebook.com/qme.eg" rel="noopener">Facebook</a> &nbsp; <a href="https://eg.linkedin.com/in/qmeeg" rel="noopener">LinkedIn</a></p></div>
  <div><h3>{e(t['foot_docs'])}</h3><ul class="cols2">{docs}</ul></div>
  <div><h3>{e(t['foot_co'])}</h3><ul>{co}</ul></div>
  <p class="legal">&copy; 2026 {e(t['rights'])}</p>
</div></footer>
<script>{JS}</script>
</body>
</html>
"""

import re
def preview(s, base="/QME-Website", live="https://qme-eg.com"):
    """Version for the GitHub Pages preview address. Never upload this one to qme-eg.com."""
    s = s.replace('href="/ar/"', f'href="{base}/ar/"').replace('href="/"', f'href="{base}/"')
    s = s.replace('src="/img/', f'src="{base}/img/')
    s = re.sub(r'(href|src)="/(?!/|' + base.strip("/") + ')', rf'\1="{live}/', s)
    return s.replace('<meta name="viewport"', '<meta name="robots" content="noindex">\n<meta name="viewport"')

ROOT = os.path.dirname(os.path.abspath(__file__))
for folder, fn in (("site", lambda s: s), ("preview", preview)):
    out = os.path.join(ROOT, folder)
    os.makedirs(os.path.join(out, "ar"), exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(fn(render(EN)))
    open(os.path.join(out, "ar", "index.html"), "w", encoding="utf-8").write(fn(render(AR)))
    if folder != "site" and os.path.isdir(os.path.join(ROOT, "site", "img")):
        import shutil; shutil.copytree(os.path.join(ROOT, "site", "img"), os.path.join(out, "img"), dirs_exist_ok=True)
urls = ["/", "/ar/", "/about-us/", "/services/certification/", "/training/", "/lead-auditor-training/", "/list-of-courses/",
        "/training-plan/", "/sustainability/", "/accreditation-registrations/", "/certificate-search/", "/news/", "/contact-us/"] + [s[4] for s in STANDARDS]
open(os.path.join(ROOT, "site", "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /wp-admin/\nAllow: /wp-admin/admin-ajax.php\n\nSitemap: {SITE}/sitemap.xml\n")
open(os.path.join(ROOT, "site", "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
print("built site/ (for qme-eg.com) and preview/ (for GitHub Pages)")
