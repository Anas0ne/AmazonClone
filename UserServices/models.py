from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore


class Users(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)
    username= models.CharField(max_length=150, unique=True, blank=False, null=False)
    password= models.CharField(max_length=255, blank=False, null=False)
    email= models.EmailField(unique=True, blank=False, null=False)
    phone_number= models.CharField(max_length=15, blank=True, null=True)
    address= models.TextField(blank=True, null=True)
    city= models.CharField(max_length=50, blank=True, null=True)
    state= models.CharField(max_length=50, blank=True, null=True)
    pincode= models.CharField(max_length=10, blank=True, null=True)
    date_of_birth= models.DateField(blank=True, null=True)
    profile_pic=models.JSONField(blank=True, null=True)
    social_media_links= models.JSONField(blank=True, null=True)
    additional_info= models.JSONField(blank=True, null=True)
    department= models.CharField(max_length=50, blank=True, null=True, choices=[
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
        ('Sales', 'Sales'),
        ('Operations', 'Operations'),
        ('Customer Service', 'Customer Service'),
        ('Legal', 'Legal'),
        ('Research and Development', 'Research and Development'),
        ('Administration', 'Administration'),
        ('Logistics', 'Logistics'),
        ('Production', 'Production'),
        ('Quality Assurance', 'Quality Assurance'),
        ('Procurement', 'Procurement'),
        ('Business Development', 'Business Development'),
        ('Project Management', 'Project Management'),
        ('Data Analysis', 'Data Analysis'),
        ('Design', 'Design'),
        ('Content Creation', 'Content Creation'),
        ('Public Relations', 'Public Relations'),
        ('Compliance', 'Compliance'),
        ('Training and Development', 'Training and Development'),
        ('Security', 'Security'),
        ('Facilities Management', 'Facilities Management'),
        ('Health and Safety', 'Health and Safety'),
        ('Environmental', 'Environmental'),
        ('Supply Chain', 'Supply Chain'),
        ('Technical Support', 'Technical Support'),
        ('Customer Success', 'Customer Success'),
        ('Community Management', 'Community Management'),
        ('Social Media Management', 'Social Media Management'),
        ('E-commerce', 'E-commerce'),
        ('Product Management', 'Product Management'),
        ('Analytics', 'Analytics'),
        ('Business Intelligence', 'Business Intelligence'),
        ('Innovation', 'Innovation'),
        ('Corporate Strategy', 'Corporate Strategy'),
        ('Investor Relations', 'Investor Relations'),
        ('Risk Management', 'Risk Management'),
        ('Change Management', 'Change Management'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Event Management', 'Event Management'),
        ('Customer Experience', 'Customer Experience'),
        ('Brand Management', 'Brand Management'),
        ('Content Marketing', 'Content Marketing'),
        ('Affiliate Marketing', 'Affiliate Marketing'),
        ('Email Marketing', 'Email Marketing'),
        ('Search Engine Optimization', 'Search Engine Optimization'),
        ('Pay-Per-Click Advertising', 'Pay-Per-Click Advertising'),
        ('Social Media Advertising', 'Social Media Advertising'),
        ('Influencer Marketing', 'Influencer Marketing'),
        ('Mobile Marketing', 'Mobile Marketing'),
        ('Video Marketing', 'Video Marketing'),
        ('Web Development', 'Web Development'),
        ('App Development', 'App Development'),
        ('Game Development', 'Game Development'),
        ('Cloud Computing', 'Cloud Computing'),
        ('Cybersecurity', 'Cybersecurity'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('Machine Learning', 'Machine Learning'),
        ('Blockchain', 'Blockchain'),
        ('Internet of Things', 'Internet of Things'),
        ('Augmented Reality', 'Augmented Reality'),
        ('Virtual Reality', 'Virtual Reality'),
        ('Big Data', 'Big Data'),
        ('Data Science', 'Data Science'),
        ('DevOps', 'DevOps'),
        ('Software Development', 'Software Development'),
        ('Network Administration', 'Network Administration'),
        ('Database Administration', 'Database Administration'),
        ('System Administration', 'System Administration'),
        ('Technical Writing', 'Technical Writing'),
        ('User Experience Design', 'User Experience Design'),
        ('Graphic Design', 'Graphic Design'),
        ('Video Production', 'Video Production'),
        ('Photography', 'Photography'),
        ('Audio Production', 'Audio Production'),
        ('Copywriting', 'Copywriting'),
        ('Editing', 'Editing')])
    designation= models.CharField(max_length=50, blank=True, null=True, choices=[
        ('Software Engineer', 'Software Engineer'),
        ('CEO', 'Chief Executive Officer'),
        ('CTO', 'Chief Technology Officer'),
        ('CFO', 'Chief Financial Officer'),
        ('COO', 'Chief Operating Officer'),
        ('CMO', 'Chief Marketing Officer'),
        ('HR Manager', 'Human Resources Manager'),
        ('IT Manager', 'Information Technology Manager'),
        ('Finance Manager', 'Finance Manager'),
        ('Marketing Manager', 'Marketing Manager'),
        ('Sales Manager', 'Sales Manager'),
        ('Operations Manager', 'Operations Manager'),
        ('Customer Service Representative', 'Customer Service Representative'),
        ('Legal Counsel', 'Legal Counsel'),
        ('Research Scientist', 'Research Scientist'),
        ('Data Analyst', 'Data Analyst'),
        ('Project Manager', 'Project Manager'),
        ('Business Analyst', 'Business Analyst'),
        ('Graphic Designer', 'Graphic Designer'),
        ('Content Writer', 'Content Writer'),
        ('Social Media Specialist', 'Social Media Specialist'),
        ('Web Developer', 'Web Developer'),
        ('App Developer', 'App Developer'),
        ('Network Administrator', 'Network Administrator'),
        ('Database Administrator', 'Database Administrator'),
        ('System Administrator', 'System Administrator')])
    timezone= models.CharField(max_length=50, blank=True, null=True, choices=[
        ('UTC', 'Coordinated Universal Time'),
        ('EST', 'Eastern Standard Time'),
        ('CST', 'Central Standard Time'),
        ('MST', 'Mountain Standard Time'),
        ('PST', 'Pacific Standard Time'),
        ('GMT', 'Greenwich Mean Time'),
        ('CET', 'Central European Time'),
        ('EET', 'Eastern European Time'),
        ('IST', 'Indian Standard Time'),
        ('JST', 'Japan Standard Time'),
        ('AEST', 'Australian Eastern Standard Time'),
        ('NZST', 'New Zealand Standard Time'),
        ('AST', 'Atlantic Standard Time'),
        ('HST', 'Hawaii-Aleutian Standard Time'),
        ('AKST', 'Alaska Standard Time'),
        ('ART', 'Argentina Time'),
        ('BRT', 'Brasilia Time'),
        ('CST', 'China Standard Time'),
        ('KST', 'Korea Standard Time'),
        ('SGT', 'Singapore Time'),
        ('WAT', 'West Africa Time'),
        ('CAT', 'Central Africa Time'),
        ('EAT', 'East Africa Time'),
        ('MSK', 'Moscow Standard Time'),
        ('PKT', 'Pakistan Standard Time'),
        ('WIB', 'Western Indonesian Time'),
        ('WIT', 'Eastern Indonesian Time'),
        ('MYT', 'Malaysia Time'),
        ('ICT', 'Indochina Time'),
        ('CST', 'Cuba Standard Time'),
        ('VET', 'Venezuela Time'),
        ('ART', 'Arabian Standard Time'),
        ('AST', 'Arabian Standard Time'),
        ('GST', 'Gulf Standard Time'),
        ('IRST', 'Iran Standard Time'),
        ('AFT', 'Afghanistan Time'),
        ('HKT', 'Hong Kong Time'),
        ('ULAT', 'Ulaanbaatar Time')])
    last_login= models.DateTimeField(blank=True, null=True)
    last_activity= models.DateTimeField(blank=True, null=True)
    last_ip= models.GenericIPAddressField(blank=True, null=True)
    last_device= models.CharField(max_length=100, blank=True, null=True)
    currency= models.CharField(max_length=10, blank=True, null=True, choices=[
        ('USD', 'United States Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound Sterling'),
        ('JPY', 'Japanese Yen'),
        ('AUD', 'Australian Dollar'),
        ('CAD', 'Canadian Dollar'),
        ('CHF', 'Swiss Franc'),
        ('CNY', 'Chinese Yuan Renminbi'),
        ('INR', 'Indian Rupee'),
        ('RUB', 'Russian Ruble'),
        ('BRL', 'Brazilian Real'),
        ('ZAR', 'South African Rand'),
        ('NZD', 'New Zealand Dollar'),
        ('KRW', 'South Korean Won'),
        ('MXN', 'Mexican Peso'),
        ('SGD', 'Singapore Dollar'),
        ('HKD', 'Hong Kong Dollar'),
        ('SEK', 'Swedish Krona'),
        ('NOK', 'Norwegian Krone'),
        ('DKK', 'Danish Krone'),
        ('PLN', 'Polish Zloty'),
        ('TRY', 'Turkish Lira'),
        ('AED', 'United Arab Emirates Dirham'),
        ('SAR', 'Saudi Riyal'),
        ('THB', 'Thai Baht'),
        ('IDR', 'Indonesian Rupiah'),
        ('MYR', 'Malaysian Ringgit'),
        ('PHP', 'Philippine Peso'),
        ('VND', 'Vietnamese Dong'),
        ('EGP', 'Egyptian Pound'),
        ('PKR', 'Pakistani Rupee'),
        ('BDT', 'Bangladeshi Taka'),
        ('ARS', 'Argentine Peso'),
        ('CLP', 'Chilean Peso'),
        ('COP', 'Colombian Peso'),
        ('PEN', 'Peruvian Sol'),
        ('UYU', 'Uruguayan Peso'),
        ('CRC', 'Costa Rican Colón'),
        ('DOP', 'Dominican Peso'),
        ('GTQ', 'Guatemalan Quetzal'),
        ('HNL', 'Honduran Lempira'),
        ('NIO', 'Nicaraguan Córdoba'),
        ('SVC', 'Salvadoran Colón'),
        ('BHD', 'Bahraini Dinar'),
        ('KWD', 'Kuwaiti Dinar'),
        ('OMR', 'Omani Rial'),
        ('QAR', 'Qatari Riyal'),
        ('JOD', 'Jordanian Dinar'),
        ('LBP', 'Lebanese Pound'),
        ('MAD', 'Moroccan Dirham'),
        ('TND', 'Tunisian Dinar'),
        ('LYD', 'Libyan Dinar'),
        ('YER', 'Yemeni Rial'),
        ('DJF', 'Djiboutian Franc'),
        ('SOS', 'Somali Shilling')])
    domain_user_id= models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    language= models.CharField(max_length=20, blank=True, null=True, choices=[
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('zh', 'Chinese'),
        ('ja', 'Japanese'),
        ('hi', 'Hindi'),
        ('ar', 'Arabic'),
        ('pt', 'Portuguese'),
        ('ru', 'Russian'),
        ('it', 'Italian'),
        ('ko', 'Korean'),
        ('nl', 'Dutch'),
        ('sv', 'Swedish'),
        ('no', 'Norwegian'),
        ('fi', 'Finnish'),
        ('da', 'Danish'),
        ('pl', 'Polish'),
    ])
    account_status= models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
        ('deleted', 'Deleted'),
        ('Blocked', 'Blocked')])
    role= models.CharField(max_length=20, choices=[
        ('admin', 'Admin'),
        ('customer', 'Customer'),
        ('user', 'User'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    ])
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    country= models.CharField(max_length=50, blank=True, null=True, choices=[
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('IN', 'India'),
        ('UK', 'United Kingdom'),
        ('AU', 'Australia'),
        ('DE', 'Germany'),
        ('FR', 'France'),
        ('JP', 'Japan'),
        ('CN', 'China'),
        ('BR', 'Brazil'),
        ('ZA', 'South Africa'),
        ('RU', 'Russia'),
        ('IT', 'Italy'),
        ('ES', 'Spain'),
        ('MX', 'Mexico'),
        ('KR', 'South Korea'),
        ('NL', 'Netherlands'),
        ('SE', 'Sweden'),
        ('NO', 'Norway'),
        ('FI', 'Finland'),
        ('DK', 'Denmark'),
        ('PL', 'Poland'),
        ('CH', 'Switzerland'),
        ('BE', 'Belgium'),
        ('AT', 'Austria'),
        ('IE', 'Ireland'),  
        ('PT', 'Portugal'),
        ('GR', 'Greece'),
        ('TR', 'Turkey'),
        ('PH', 'Pakistan'),
        ('ID', 'Indonesia'),
        ('MY', 'Malaysia'),
        ('TH', 'Thailand'),
        ('VN', 'Vietnam'),
        ('SG', 'Singapore'),
        ('AE', 'United Arab Emirates'),
        ('SA', 'Saudi Arabia'),
        ('EG', 'Egypt'),
        ('KE', 'Kenya'),
        ('NG', 'Nigeria'),
        ('GH', 'Ghana'),
        ('TZ', 'Tanzania'),
        ('UG', 'Uganda'),
        ('ZM', 'Zambia'),
        ('ZW', 'Zimbabwe'),
        ('MA', 'Morocco'),
        ('AL', 'Algeria'),
        ('TN', 'Tunisia'),
        ('LY', 'Libya'),
        ('SD', 'Sudan'),
        ('CM', 'Cameroon'),
        ('CI', 'Côte dIvoire'),
        ('SN', 'Senegal'),
        ('MZ', 'Mozambique'),
        ('AO', 'Angola'),
        ('CD', 'Democratic Republic of the Congo'),
        ('CG', 'Republic of the Congo'),
        ('BJ', 'Benin'),
        ('BF', 'Burkina Faso'),
        ('ML', 'Mali'),
        ('NE', 'Niger'),
        ('TG', 'Togo'),
        ('GW', 'Guinea-Bissau'),
        ('GN', 'Guinea'),
        ('SL', 'Sierra Leone'),
        ('LR', 'Liberia'),
        ('GH', 'Ghana'),
        ('ET', 'Ethiopia'),
        ('SO', 'Somalia'),
        ('DJ', 'Djibouti'),
        ('ER', 'Eritrea'),
        ])
    
class UserShippingAddress(models.Model):
        id = models.AutoField(primary_key=True)
        user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='shipping_addresses')
        address_line_1 = models.CharField(max_length=255)
        address_line_2 = models.CharField(max_length=255, blank=True, null=True)
        city = models.CharField(max_length=100)
        state = models.CharField(max_length=100)
        country= models.CharField(max_length=50, blank=True, null=True, choices=[
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('IN', 'India'),
        ('UK', 'United Kingdom'),
        ('AU', 'Australia'),
        ('DE', 'Germany'),
        ('FR', 'France'),
        ('JP', 'Japan'),
        ('CN', 'China'),
        ('BR', 'Brazil'),
        ('ZA', 'South Africa'),
        ('RU', 'Russia'),
        ('IT', 'Italy'),
        ('ES', 'Spain'),
        ('MX', 'Mexico'),
        ('KR', 'South Korea'),
        ('NL', 'Netherlands'),
        ('SE', 'Sweden'),
        ('NO', 'Norway'),
        ('FI', 'Finland'),
        ('DK', 'Denmark'),
        ('PL', 'Poland'),
        ('CH', 'Switzerland'),
        ('BE', 'Belgium'),
        ('AT', 'Austria'),
        ('IE', 'Ireland'),  
        ('PT', 'Portugal'),
        ('GR', 'Greece'),
        ('TR', 'Turkey'),
        ('PH', 'Pakistan'),
        ('ID', 'Indonesia'),
        ('MY', 'Malaysia'),
        ('TH', 'Thailand'),
        ('VN', 'Vietnam'),
        ('SG', 'Singapore'),
        ('AE', 'United Arab Emirates'),
        ('SA', 'Saudi Arabia'),
        ('EG', 'Egypt'),
        ('KE', 'Kenya'),
        ('NG', 'Nigeria'),
        ('GH', 'Ghana'),
        ('TZ', 'Tanzania'),
        ('UG', 'Uganda'),
        ('ZM', 'Zambia'),
        ('ZW', 'Zimbabwe'),
        ('MA', 'Morocco'),
        ('AL', 'Algeria'),
        ('TN', 'Tunisia'),
        ('LY', 'Libya'),
        ('SD', 'Sudan'),
        ('CM', 'Cameroon'),
        ('CI', 'Côte d’Ivoire'),
        ('SN', 'Senegal'),
        ('MZ', 'Mozambique'),
        ('AO', 'Angola'),
        ('CD', 'Democratic Republic of the Congo'),
        ('CG', 'Republic of the Congo'),
        ('BJ', 'Benin'),
        ('BF', 'Burkina Faso'),
        ('ML', 'Mali'),
        ('NE', 'Niger'),
        ('TG', 'Togo'),
        ('GW', 'Guinea-Bissau'),
        ('GN', 'Guinea'),
        ('SL', 'Sierra Leone'),
        ('LR', 'Liberia'),
        ('GH', 'Ghana'),
        ('ET', 'Ethiopia'),
        ('SO', 'Somalia'),
        ('DJ', 'Djibouti'),
        ('ER', 'Eritrea'),
        ])
        address_type = models.CharField(max_length=50, choices=[
            ('home', 'Home'),
            ('work', 'Work'),
            ('other', 'Other')
        ], default='home')
        domain_name = models.CharField(max_length=100, blank=True, null=True)
        plan_type = models.CharField(max_length=50, blank=True, null=True, choices=[
            ('free', 'Free'),
            ('basic', 'Basic'),
            ('premium', 'Premium'),
            ('enterprise', 'Enterprise')
        ])
        postal_code = models.CharField(max_length=20)
        phone_number = models.CharField(max_length=20, blank=True, null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

class Modules(models.Model):
      id = models.AutoField(primary_key=True)
      module_name = models.CharField(max_length=100, unique=True)
      module_description = models.TextField(blank=True, null=True)
      module_version = models.CharField(max_length=20, blank=True, null=True)
      module_author = models.CharField(max_length=100, blank=True, null=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      module_icon = models.TextField()
      display_order = models.IntegerField(default=0)
      is_menu = models.BooleanField(default=False)
      module_url = models.TextField()
      parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

class UserPermissions(models.Model):
      id = models.AutoField(primary_key=True)
      user = models.ForeignKey(Users, on_delete=models.CASCADE)
      module = models.ForeignKey(Modules, on_delete=models.CASCADE)
      can_view = models.BooleanField(default=False)
      can_add = models.BooleanField(default=False)
      can_edit = models.BooleanField(default=False)
      can_delete = models.BooleanField(default=False)
      domain_user_id = models.CharField(max_length=100, blank=True, null=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

class UserActivityLog(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50, choices=[
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('view', 'View'),
        ('add', 'Add'),
        ('edit', 'Edit'),
        ('delete', 'Delete')
    ])
    activity_description = models.TextField(blank=True, null=True)
    activity_timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    device_info = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
      