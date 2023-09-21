import matplotlib.pyplot as plt

# đọc dữ liệu từ file
with open('Data', 'r') as f:
    data = f.readlines()

# tạo dictionary
temp_dict = {}
for line in data:
    year, max_temp, min_temp, avg_temp = line.strip().split('\t')
    temp_dict[year] = [float(max_temp), float(min_temp), float(avg_temp)]

# tạo list các năm và nhiệt độ tương ứng
years = list(temp_dict.keys())
max_temps = [temp_dict[year][0] for year in years]
min_temps = [temp_dict[year][1] for year in years]
avg_temps = [temp_dict[year][2] for year in years]

# vẽ biểu đồ
plt.plot(years, max_temps, label='Nhiệt độ cao nhất')
plt.plot(years, min_temps, label='Nhiệt độ thấp nhất')
plt.plot(years, avg_temps, label='Nhiệt độ trung bình')
plt.xlabel('Năm')
plt.ylabel('Nhiệt độ (°C)')
plt.legend()
plt.show()
