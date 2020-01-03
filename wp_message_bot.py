import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

seçim=input("\n[1] Zaman ayarlı mesaj at"
            "\n[2] Direk Mesaj at\n"
            "Seçiminiz : ")

if seçim=="1":

    if time.localtime().tm_min<10:
        print("\nsaat : "+str(time.localtime().tm_hour)+".0"+str(time.localtime().tm_min))

    else:
        print("\nsaat : "+str(time.localtime().tm_hour)+"."+str(time.localtime().tm_min))


    #whatsapp web açılıyor
    browser = webdriver.Chrome()
    browser.get("https://web.whatsapp.com")


    #kullanıcı tarafından zaman ve kişi bilgisi ayarlanıyor

    isim = input("\nmesaj atmak istediğiniz kişinin veya grubun ismini giriniz : ")

    print("\nmesaj atmak istediğiniz zamanı giriniz :\n")

    istenilen_saat=int(input("saat : "))
    istenilen_dakika=int(input("dakika : "))
    mesaj=input("mesajınız : ")

    sayı=int(input("bu mesajı kaç kere göndermek istiyorsunuz : "))

    input("QR kodu okuttuktan sonra herhangi bir şeye basınız")

    if istenilen_dakika<10:
        print("\nşu saatte mesaj atılacaktır -> "+str(istenilen_saat)+".0"+str(istenilen_dakika))

    else:
        print("\nşu saatte mesaj atılacaktır -> "+str(istenilen_saat)+"."+str(istenilen_dakika))



    #bekleniyor
    while True:
        if time.localtime().tm_hour==istenilen_saat and time.localtime().tm_min==istenilen_dakika:
            if time.localtime().tm_min<10:
                print("\nsaat : "+str(time.localtime().tm_hour)+".0"+str(time.localtime().tm_min))

            else:
                print("\nsaat : "+str(time.localtime().tm_hour)+"."+str(time.localtime().tm_min))
            time.sleep(1)
            print("\nmesaj : "+mesaj)
            print("\nmesaj "+str(sayı)+" kere gönderiliyor")

            #sohbete giriliyor
            select_person = browser.find_element_by_xpath("//span[@title = '{}']".format(isim))
            select_person.click()
            messagebox = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

            for i in range (sayı):
                #mesaj gönderiliyor
                messagebox.send_keys(mesaj)
                messagebox.send_keys(Keys.ENTER)

            print("\nmesaj gönderme işlemi tamamlandı")
            break

elif seçim=="2":

    #whatsapp web açılıyor
    browser = webdriver.Chrome()
    browser.get("https://web.whatsapp.com")


    #kullanıcı tarafından bilgi ayarlanıyor

    isim = input("\nmesaj atmak istediğiniz kişinin veya grubun ismini giriniz : ")

    mesaj=input("mesajınız : ")

    sayı=int(input("bu mesajı kaç kere göndermek istiyorsunuz : "))

    input("QR kodu okuttuktan sonra herhangi bir şeye basınız")


    print("\nmesaj : "+mesaj)
    print("\nmesaj "+str(sayı)+" kere gönderiliyor")

    #sohbete giriliyor
    select_person = browser.find_element_by_xpath("//span[@title = '{}']".format(isim))
    select_person.click()
    messagebox = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

    for i in range (sayı):
        #mesaj gönderiliyor
        messagebox.send_keys(mesaj)
        messagebox.send_keys(Keys.ENTER)

    print("\nmesaj gönderme işlemi tamamlandı")
