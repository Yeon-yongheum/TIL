students = {
    'asd1': {
        '순번' : '01',
        '이름' : '김성훈'
    },
    'asd2': {
        '순번' : '02',
        '이름' : '김은정'
    }
}
students2 = [
    {
        '순번' : '01',
        '이름' : '김성훈',
        'qwe' : 'asd'
    },
    {
        '순번' : '02',
        '이름' : '김은정',
        'qwe' : 'asd'
    }
]

# with open('a.csv', 'w', encoding='utf-8') as f:
#     f.write('number,name\n')
#     for number, name in students.items():
#         f.write(f'{number}, {name}\n')
#     f.write('hi')
import csv
with open('c.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['순번', '이름'] #여기만 변경
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in students2: #맞는 딕셔너리 만든것 반복
        csv_writer.writerow(item)
