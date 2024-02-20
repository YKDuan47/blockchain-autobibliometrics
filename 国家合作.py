# # 导入csv和locationtagger模块
# import csv
# import locationtagger

# # 打开输入文件
# with open("title_year_author_instation.csv", "r", encoding="utf-8") as input_file:
#     # 创建一个csv.reader对象
#     reader = csv.reader(input_file)
#     # 读取第一行，获取列名
#     header = next(reader)
#     # 找到地址列的索引
#     address_index = header.index("RP")
#     # 打开输出文件
#     with open("国家提取.csv", "w") as output_file:
#         # 创建一个csv.writer对象
#         writer = csv.writer(output_file)
#         # 写入列名，添加一个新的列名"Country"
#         writer.writerow(header + ["Country"])
#         # 遍历输入文件的每一行
#         for row in reader:
#             # 获取地址列的值
#             address = row[address_index]
#             # 使用locationtagger库提取国家
#             country = locationtagger.find_locations(text=address).countries
#             # 如果提取到了国家，就将所有国家的名称用逗号分隔
#             if country:
#                 country = ",".join([c for c in country])
#             # 否则，就用空字符串代替
#             else:
#                 country = ""
#             # 写入输出文件的一行，添加一个新的值"Country"
#             writer.writerow(row + [country])

# 导入locationtagger库
import locationtagger
import pandas as pd

# 读取csv文件中的地址列
addresses = pd.read_csv("topScientist.csv", skip_blank_lines=True)["C1"]

# 创建一个空的列表，用来存放国家名称
countries = []

# 遍历每个地址，用locationtagger.find_locations()方法获取位置信息
for address in addresses:
    # 如果地址不为空，就把它转换成字符串
    i = 0
    if address:
        address = str(address)
    # 用locationtagger.find_locations()方法获取位置信息，返回一个LocationTagger对象
    location = locationtagger.find_locations(text=address)
    # 如果LocationTagger对象不为空，且有国家属性，就把国家名称添加到列表中
    if location and location.countries:
        # 创建一个空的字符串，用来存放国家名称
        country_names = ""
        # 遍历location.countries列表中的每个元素
        for country in location.countries:
            # 如果是一个字符串对象，就直接添加到字符串中，用逗号隔开
            if isinstance(country, str):
                country_names += country + ","
            # 如果是一个Location对象，就用.name属性添加到字符串中，用逗号隔开
            else:
                country_names += country.name + ","
        # 去掉最后一个逗号
        country_names = country_names[:-1]
        # 把字符串添加到列表中
        countries.append(country_names)
    # 否则，就添加一个空值
    else:
        countries.append(None)
    if i % 500 == 1:
        print(i/13000,'%')
    i+=1

# 把国家列表保存到一个新的csv文件中
pd.DataFrame(countries, columns=["Country"]).to_csv("new_file1.csv", index=False, line_terminator="\n")