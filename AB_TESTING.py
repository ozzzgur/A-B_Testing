#####################################################
# AB Testi ile BiddingYöntemlerinin Dönüşümünün Karşılaştırılması
#####################################################

#####################################################
# İş Problemi
#####################################################

# Facebook kısa süre önce mevcut "maximumbidding" adı verilen teklif verme türüne alternatif
# olarak yeni bir teklif türü olan "average bidding"’i tanıttı. Müşterilerimizden biri olan bombabomba.com,
# bu yeni özelliği test etmeye karar verdi veaveragebidding'in maximumbidding'den daha fazla dönüşüm
# getirip getirmediğini anlamak için bir A/B testi yapmak istiyor.A/B testi 1 aydır devam ediyor ve
# bombabomba.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor.Bombabomba.com için
# nihai başarı ölçütü Purchase'dır. Bu nedenle, istatistiksel testler için Purchasemetriğine odaklanılmalıdır.




#####################################################
# Veri Seti Hikayesi
#####################################################

# Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları
# reklam sayıları gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır.Kontrol ve Test
# grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleriab_testing.xlsxexcel’ininayrı sayfalarında yer
# almaktadır. Kontrol grubuna Maximum Bidding, test grubuna AverageBiddinguygulanmıştır.

# impression: Reklam görüntüleme sayısı
# Click: Görüntülenen reklama tıklama sayısı
# Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı
# Earning: Satın alınan ürünler sonrası elde edilen kazanç



#####################################################
# Proje Görevleri
#####################################################

######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################

# 1. Hipotezleri Kur
# 2. Varsayım Kontrolü
#   - 1. Normallik Varsayımı (shapiro)
#   - 2. Varyans Homojenliği (levene)
# 3. Hipotezin Uygulanması
#   - 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi
#   - 2. Varsayımlar sağlanmıyorsa mannwhitneyu testi
# 4. p-value değerine göre sonuçları yorumla
# Not:
# - Normallik sağlanmıyorsa direkt 2 numara. Varyans homojenliği sağlanmıyorsa 1 numaraya arguman girilir.
# - Normallik incelemesi öncesi aykırı değer incelemesi ve düzeltmesi yapmak faydalı olabilir.




#####################################################
# Görev 1:  Veriyi Hazırlama ve Analiz Etme
#####################################################

# Adım 1:  ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz. Kontrol ve test grubu verilerini ayrı değişkenlere atayınız.
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# !pip install statsmodels
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


df_cont = pd.read_excel("python_for_data_science/pythonProject/odevler/measurement_problems/ABTesti/ab_testing.xlsx",sheet_name="Control Group")
df_test = pd.read_excel("python_for_data_science/pythonProject/odevler/measurement_problems/ABTesti/ab_testing.xlsx",sheet_name="Test Group")

df_cont = df_cont.add_prefix("cont_")
df_test = df_test.add_prefix("test_")


# Adım 2: Kontrol ve test grubu verilerini analiz ediniz.
df_cont.describe().T
df_test.describe().T


# Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.


df = pd.concat([df_cont,df_test],axis=1)

#####################################################
# Görev 2:  A/B Testinin Hipotezinin Tanımlanması
#####################################################

# Adım 1: Hipotezi tanımlayınız.
# H0: M1 = M2  (Maxiumum Bidding ile Average Bidding arasında fark yoktur.)
# H1: M1 != M2 (kontrol grubu ile test grubu arasında fark vardır.

# Adım 2: Kontrol ve test grubu için purchase(kazanç) ortalamalarını analiz ediniz

df["cont_Purchase"].mean()
df["test_Purchase"].mean()

#####################################################
# GÖREV 3: Hipotez Testinin Gerçekleştirilmesi
#####################################################

######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################


# Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapınız.Bunlar Normallik Varsayımı ve Varyans Homojenliğidir.

# Kontrol ve test grubunun normallik varsayımına uyup uymadığını Purchase değişkeni üzerinden ayrı ayrı test ediniz

# Normallik Varsayımı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: .........sağlanmamaktadır.

# pvalue < 0.05 ise H0 red.
# pvalue < 0.05 değil ise H0 kabul.

test_stat,pvalue = shapiro(df["cont_Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Pvalue 0.58, 0.05'ten büyük olduğu için H0 kabul.

test_stat,pvalue = shapiro(df["test_Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Pvalue 0.15, 0.05'ten büyük olduğu için H0 kabul.

#Normallik varsayımına uygun.

# Varyans Homojenliği

# H0 : Varyans homojendir.
# H1 : Varyans homojen değildir.

test_stat,pvalue = levene(df["cont_Purchase"],df["test_Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


# P_value 0.10, 0.05'ten büyük olduğu için H0 kabul.


# Adım 2: Normallik Varsayımı ve Varyans Homojenliği sonuçlarına göre uygun testi seçiniz


test_stat,pvalue = ttest_ind(df["cont_Purchase"],df["test_Purchase"],equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))



# Adım 3: Test sonucunda elde edilen p_value değerini göz önünde bulundurarak kontrol ve test grubu satın alma
# ortalamaları arasında istatistiki olarak anlamlı bir fark olup olmadığını yorumlayınız.

# pvalue 0.349 , 0.05'ten büyük olduğu için H0 kabul edilir.



##############################################################
# GÖREV 4 : Sonuçların Analizi
##############################################################

# Adım 1: Hangi testi kullandınız, sebeplerini belirtiniz.

#Test grubu ve kontrol grubu normallik ve varyansları homojem olduğu için parametrik t
#testi kullandık.


# Adım 2: Elde ettiğiniz test sonuçlarına göre müşteriye tavsiyede bulununuz.
# Yapılan inceleme sonucunda test grubu ve kontrol grubu arasıda anlamlı bir ilişki bulunamadı.
