from pprint import pprint

school = {
    'teacher' : {
        'physics' : [
            {'name': 'phy01', 'email': 'phy0@gmail.com', 'address': 'mumbai', 'phone': 345667},
            {'name': 'phy02', 'email': 'phy2@gmail.com', 'address': 'Pune', 'phone': 3456654357},
            {'name': 'phy03', 'email': 'phy3@gmail.com', 'address': 'Bang', 'phone': 88345667},
            {'name': 'phy04', 'email': 'phy4@gmail.com', 'address': 'Hyder', 'phone': 99345667}
        ],
        'math' : [
            {'name': 'math01', 'email': 'math0@gmail.com', 'address': 'mumbai', 'phone': 5345667},
            {'name': 'math02', 'email': 'math2@gmail.com', 'address': 'Pune', 'phone': 35456654357},
            {'name': 'math03', 'email': 'math3@gmail.com', 'address': 'Bang', 'phone': 848345667},
            {'name': 'math04', 'email': 'math4@gmail.com', 'address': 'Hyder', 'phone': 299345667}
        ],
        'chemestry' : [],
        'lab assistant' : [],
        'science' : []
    },
    'student' : {
        '10th' : [
            {'name': 'stu10_1', 'email': 'stu10_1@gmail.com', 'phone': 45667 },
            {'name': 'stu10_2', 'email': 'stu10_2@gmail.com', 'phone': 456675454 }
        ],
        '11th' : [
            {'name': 'stu11_1', 'email': 'stu11_1@gmail.com', 'phone': 4775667 },
            {'name': 'stu11_2', 'email': 'stu11_2@gmail.com', 'phone': 45776675454 }
        ],
        '12th' : [
            {'name': 'stu12_1', 'email': 'stu12_1@gmail.com', 'phone': 45552667 },
            {'name': 'stu12_2', 'email': 'stu12_2@gmail.com', 'phone': 4562675454 }
        ]
    },
    'other_staff' : {
        'account' : [],
        'security' : [],
        'swiper' : []

    }
}

pprint(school)

#Output:

"""
{'Development': [{'email': 'emailid', 'mobile': 54646454, 'name': 'name1'},
                 {'email': 'dev_emaiid1@gmail.com',
                  'mobile': 54646455,
                  'name': 'dev_name1'},
                 {'email': 'dev_emaiid2@gmail.com',
                  'mobile': 54646456,
                  'name': 'dev_name2'},
                 {'email': 'dev_emaiid3@gmail.com',
                  'mobile': 54646457,
                  'name': 'dev_name3'},
                 {'email': 'dev_emaiid4@gmail.com',
                  'mobile': 54646458,
                  'name': 'dev_name4'}],
 'HR': [{'email': 'emailid', 'mobile': 54646454, 'name': 'name1'},
        {'email': 'hr_emaiid1@gmail.com',
         'mobile': 54646455,
         'name': 'hr_name1'},
        {'email': 'hr_emaiid2@gmail.com',
         'mobile': 54646456,
         'name': 'hr_name2'},
        {'email': 'hr_emaiid3@gmail.com',
         'mobile': 54646457,
         'name': 'hr_name3'},
        {'email': 'hr_emaiid4@gmail.com',
         'mobile': 54646458,
         'name': 'hr_name4'}],
 'Support': [{'email': 'emailid', 'mobile': 54646454, 'name': 'name1'},
             {'email': 'sp_emaiid1@gmail.com',
              'mobile': 54646455,
              'name': 'sp_name1'},
             {'email': 'sp_emaiid2@gmail.com',
              'mobile': 54646456,
              'name': 'sp_name2'},
             {'email': 'sp_emaiid3@gmail.com',
              'mobile': 54646457,
              'name': 'sp_name3'},
             {'email': 'sp_emaiid4@gmail.com',
              'mobile': 54646458,
              'name': 'sp_name4'}],
 'Testing': [{'email': 'emailid', 'mobile': 54646454, 'name': 'name1'},
             {'email': 'test_emaiid1@gmail.com',
              'mobile': 54646455,
              'name': 'test_name1'},
             {'email': 'test_emaiid2@gmail.com',
              'mobile': 54646456,
              'name': 'test_name2'},
             {'email': 'test_emaiid3@gmail.com',
              'mobile': 54646457,
              'name': 'test_name3'},
             {'email': 'test_emaiid4@gmail.com',
              'mobile': 54646458,
              'name': 'test_name4'}]}






"""