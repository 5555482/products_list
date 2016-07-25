import sqlite3

def init():
    conn = sqlite3.connect('db.sqlite3')
    print "Opened database successfully";

    conn.execute('''CREATE TABLE PRODUCT
           (ID INTEGER PRIMARY KEY AUTOINCREMENT,
           NAME           TEXT     NOT NULL,
           DESCRIPTION   TEXT     NOT NULL,
           PRICE         REAL);''')
    print "Table created successfully";

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('CIUK Total Confidence 14 Company Any Combination Internship Package (with Free CIUK Summer Internship Programme)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 4999.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('Breakinginto-iBank UK Internship Career Coaching Programme (10 Company Package with 1st Round Interview Guarantee* and No Win No Fee*)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 3999.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('City Law Firm Application Form Professional Review Packages (4 Companies))', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 399.990 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('Application Form Review/Amendment Services', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 129.99 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('Breakinginto-Big10 UK Internship Career Coaching Programme (10 Company Package with 1st Round Interview Guarantee* and No Win No Fee*)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 3999.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('Breakinginto-Big4 + Breakinginto-iBank (Combined) HongKong Full Time Career Coaching Programme (14 Company Package with Offer Guarantee* and No Win No Fee*)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 12699.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('Breakinginto-Big4 + Breakinginto-iBank (Combined) UK Full Time Career Coaching Programme (10 Company Package with 1st Round Interview Guarantee* and No Win No Fee*))', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 3999.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('Breakinginto-Big4 + Breakinginto-iBank + FMCG Leaders of Tomorrow(Combined) UK Internship Career Coaching Programme (14 Company Package with 1st Round Interview Guarantee* and No Win No Fee*)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 4299.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('Breakinginto-Big4 + Breakinginto-iBank UK Internship Career Coaching Programme (10 Company Package with 1st Round Interview Guarantee* and No Win No Fee*)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 3999.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('Breakinginto-Big6 + Breakinginto-iBank Combined UK Full Time Career Coaching Programme (16 Company Package with Offer Guarantee* and No Win No Fee*)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 18699.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('Breakinginto-Big4 China Full Time Career Coaching Programme (4 Company Package with 1st Round Interview Guarantee* and No Win No Fee*)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 1999.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('Breakinginto-Big6 UK Full Time Career Coaching Programme (6 Company Package with Three Assessment Centres Guarantee* and No Win No Fee*)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 8999.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('Breakinginto-Big6 UK Full Time Career Coaching Programme (6 Company Package with Two Assessment Centres Guarantee* and No Win No Fee*)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 6899.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('Breakinginto-Big6 UK Summer Internship Coaching Programme (6 Company Package with Summer Internship Offer Guarantee* and No Win No Fee*)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 13299.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('Case Study + Presentation', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 499.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('China Returnee Career Coaching Full Time Programme (4 Company Package)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 2999.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('City Law Firm Application Form Professional Review Packages (4 Companies)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 399.99 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('City Law Firm Application Form Professional Review Packages (8 Companies)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 699.99 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('City Lawyer Head Start Programme + Breakinginto-Big4 UK Full Time Career Coaching Programme (14 Company Package with 1st Round Interview Guarantee* and No Win No Fee*)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 3999.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('City Lawyer Head Start UK Full Time Career Coaching Programme (10 Company Package with 1st Round Interview Guarantee* and No Win No Fee*)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 3499.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('CIUK Express Full Time Career Coaching Programme', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 499.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('CIUK Introductory Full Time Career Coaching Programme', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 1649.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('CIUK Introductory Internship Career Coaching Programme', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 1499.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('CIUK Summer Internship Programme 2016 (With Accommodation)', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 3999.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('CIUK Unlimited CV and Cover Letter Review Service', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 99.00 )");

    conn.execute("INSERT INTO PRODUCT (NAME,DESCRIPTION,PRICE) \
          VALUES ('CIUK Work Experience Programme', 'Nullam vel sem. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Fusce pharetra convallis urna. Phasellus magna. Nunc nonummy metus. Vivamus laoreet. Sed lectus. Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Etiam iaculis nunc ac metus. Praesent nonummy mi in odio.', 2499.00 )");

    conn.commit()
    print "Records created successfully";

    conn.close()
