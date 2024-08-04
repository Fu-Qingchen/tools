import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import PercentFormatter

# 读取配置
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
main_dir = os.path.dirname(script_dir)
conf_path = os.path.join(main_dir, 'conf\\finance_manager.json')
with open(conf_path, 'r', encoding='utf-8') as file:
    conf_data = json.load(file)
df_finance = pd.read_excel(conf_data['finance_data'])
df_wh_house = pd.read_excel(os.path.join(main_dir, 'data\\武汉房地产研究.xlsx'))

# 图表绘制
plt.rcParams['font.family'] = ['Product Sans','SimHei']

## 资产趋势
plt.figure(figsize=(16/2, 6/2))
plt.plot(df_finance['日期'], df_finance['总资产'], color='red', linestyle='--', linewidth=2, label='总资产')
plt.plot(df_finance['日期'], df_finance['长期投资'] + df_finance['短期投资'] + df_finance['灵活取用'] + df_finance['借贷金额'], color='red', linewidth=2, label='总资金')
plt.fill_between(df_finance['日期'], 0, df_finance['长期投资'], color='#595e98', alpha=0.6, edgecolor='none', label='长期')
plt.fill_between(df_finance['日期'], df_finance['长期投资'], df_finance['长期投资'] + df_finance['短期投资'], color='#66b5cc', alpha=0.6, edgecolor='none', label='稳健')
plt.fill_between(df_finance['日期'], df_finance['长期投资'] + df_finance['短期投资'], df_finance['长期投资'] + df_finance['短期投资'] + df_finance['灵活取用'], color='#cb8967', alpha=0.6, edgecolor='none', label='活钱')
plt.legend(loc='upper center', ncol=5)
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.grid(True, which='major', color='grey', linewidth=0.8, alpha=0.5)
plt.xlim(pd.Timestamp('2021-01-01'),pd.Timestamp('2025-12-31'))
plt.ylim(0,600000)
img_total_path = os.path.join(conf_data['finance_out'], './assets/total.jpg')
img_total_path_pri = os.path.join(conf_data['finance_pri_out'], './assets/total.jpg')
plt.gca().yaxis.set_visible(True)
plt.savefig(img_total_path_pri, dpi=300)
plt.gca().yaxis.set_visible(False)
plt.savefig(img_total_path, dpi=300)

## 资产结构
plt.figure(figsize=(16/2, 6/2))
totals = df_finance['长期投资'] + df_finance['短期投资'] + df_finance['灵活取用']
long_perc = df_finance['长期投资']/totals
short_perc = df_finance['短期投资']/totals
cash_perc = df_finance['灵活取用']/totals
safe = df_finance['近一年消费']/2/totals + -df_finance['借贷金额']/totals
plt.stackplot(df_finance['日期'], cash_perc, short_perc, long_perc, labels=['活钱', '稳健', '长钱'], colors=['#cb8967', '#66b5cc', '#595e98'], alpha=[0.5, 0.5, 0.5])
plt.plot(df_finance['日期'], safe, color='red', linewidth=2, label='安全线')
plt.legend(loc='upper center', ncol=5)
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=1))
plt.grid(True, which='major', color='grey', linewidth=0.8, alpha=0.5)
plt.xlim(pd.Timestamp('2021-01-01'),pd.Timestamp('2025-12-31'))
plt.ylim(0,1)
img_struct_path = os.path.join(conf_data['finance_out'], './assets/struct.jpg')
img_struct_path_pri = os.path.join(conf_data['finance_pri_out'], './assets/struct.jpg')
plt.gca().yaxis.set_visible(True)
plt.savefig(img_struct_path_pri, dpi=300)
plt.gca().yaxis.set_visible(False)
plt.savefig(img_struct_path, dpi=300)

## 收入支出
plt.figure(figsize=(16/2, 6/2))
plt.plot(df_finance['日期'], -df_finance['近一年消费'], color='green', linewidth=2, label='近一年消费')
plt.plot(df_finance['日期'], df_finance['近一年存款'], color='red', linewidth=2, label='近一年存款')
plt.plot(df_finance['日期'], df_finance['近一年储蓄'], color='red', linestyle='--', linewidth=2, label='近一年储蓄')
plt.legend(loc='upper center', ncol=5)
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.grid(True, which='major', color='grey', linewidth=0.8, alpha=0.5)
plt.xlim(pd.Timestamp('2021-01-01'),pd.Timestamp('2025-12-31'))
plt.ylim(-200000,400000)
img_change_path = os.path.join(conf_data['finance_out'], './assets/change.jpg')
img_change_path_pri = os.path.join(conf_data['finance_pri_out'], './assets/change.jpg')
plt.gca().yaxis.set_visible(True)
plt.savefig(img_change_path_pri, dpi=300)
plt.gca().yaxis.set_visible(False)
plt.savefig(img_change_path, dpi=300)

## 房价指数
plt.figure(figsize=(16/2, 4))
plt.plot(df_wh_house['月份'], df_wh_house['二手房价格指数'], color='green', linewidth=2, label='二手房价格指数')
plt.plot(df_wh_house['月份'], df_wh_house['新房价格指数'], color='red', linewidth=2, label='新房价格指数')
plt.legend(loc='upper center', ncol=5)
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=1))
plt.grid(True, which='major', color='grey', linewidth=0.8, alpha=0.5)
plt.xlim(pd.Timestamp('2011-01-01'),pd.Timestamp('2025-12-31'))
plt.ylim(0.8, 2.2)
img_wh_house_path = os.path.join(conf_data['wuhan_out'], './assets/wh_house.jpg')
plt.gca().yaxis.set_visible(True)
plt.savefig(img_wh_house_path, dpi=300)

## 参考月供
plt.figure(figsize=(16/2, 4))
plt.plot(df_wh_house['月份'], df_wh_house['二手房30年月供'], linestyle='--', color='green', linewidth=2, label='二手房30年月供')
plt.plot(df_wh_house['月份'], df_wh_house['二手房20年月供'], color='green', linewidth=2, label='二手房20年月供')
plt.plot(df_wh_house['月份'], df_wh_house['新房30年月供'], linestyle='--', color='red', linewidth=2, label='新房30年月供')
plt.plot(df_wh_house['月份'], df_wh_house['新房20年月供'], color='red', linewidth=2, label='新房20年月供')
plt.legend()
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.grid(True, which='major', color='grey', linewidth=0.8, alpha=0.5)
plt.xlim(pd.Timestamp('2022-01-01'),pd.Timestamp('2025-12-31'))
plt.ylim(0, 12000)
img_wh_house_path = os.path.join(conf_data['wuhan_out'], './assets/wh_monthly_payment.jpg')
plt.gca().yaxis.set_visible(True)
plt.savefig(img_wh_house_path, dpi=300)