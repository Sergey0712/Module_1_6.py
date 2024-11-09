kolichestvo_vypolnennyh_zadach = 12
kolichestvo_zatrachennyh_chasov = 1.5
nazvanie_kursa = 'Python'
vremya_na_odno_zadanie = (kolichestvo_zatrachennyh_chasov / kolichestvo_vypolnennyh_zadach)
print('Курс:', nazvanie_kursa + ',', 'всего задач:', str(kolichestvo_vypolnennyh_zadach) + ',', 'затрачено часов:',
      str(kolichestvo_zatrachennyh_chasov) + ',', 'среднее время выполнения', vremya_na_odno_zadanie, 'часа.')