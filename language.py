languageselection = "Turkish" # Change this to the language you want to use. Options: Turkish, English, Arabic, Spanish


def MainTranslate():
    if languageselection == "Turkish":
        pinging = "Ping atılıyor..."
        invalidoperation = "Geçersiz işlem. Lütfen geçerli bir işlem seçin"
        sendpackets = "Gönderilen Paket Sayısı: "
        receivedpackets = "Alınan Paket Sayısı: "
        lowestping = "En Düşük Ping: "
        highestping = "En Yüksek Ping: "
        averageping = "Ortalama Ping: "
        packetloss = "Paket Kaybı: "
        pingjitter = "Ping Jitter Değeri: "
        pressanykeyexit = "Çıkmak için herhangi bir tuşa basın"
        request = "Ping"
        return pinging, invalidoperation, sendpackets, receivedpackets, lowestping, highestping, averageping, packetloss, pingjitter, pressanykeyexit,request
    elif languageselection == "English":
        pinging = "Pinging..."
        invalidoperation = "Invalid operation. Please select a valid operation."
        sendpackets = "Packets Sent: "
        receivedpackets = "Packets Received: "
        lowestping = "Lowest Ping: "
        highestping = "Highest Ping: "
        averageping = "Average Ping: "
        packetloss = "Packet Loss: "
        pressanykeyexit = "Press any key to exit"
        request = "Ping"
        return pinging, invalidoperation, sendpackets, receivedpackets, lowestping, highestping, averageping, packetloss,pressanykeyexit,request
    elif languageselection == "Arabic":
        pinging = "جاري العملية..."
        invalidoperation = "عمل غير صالح. يرجى تحديد عملية صالحة."
        sendpackets = "الحزم المرسلة: "
        receivedpackets = "الحزم المستلمة: "
        lowestping = "أقل بينغ: "
        highestping = "أعلى بينغ: "
        averageping = "متوسط بينغ: "
        packetloss = "فقدان الحزم: "
        request = "بينغ"
        return pinging, invalidoperation, sendpackets, receivedpackets, lowestping, highestping, averageping, packetloss,request
    elif languageselection == "Spanish":
        pinging = "Haciendo ping..."
        invalidoperation = "Operación no válida. Por favor seleccione una operación válida."
        sendpackets = "Paquetes enviados: "
        receivedpackets = "Paquetes recibidos: "
        lowestping = "Ping más bajo: "
        highestping = "Ping más alto: "
        averageping = "Ping promedio: "
        packetloss = "Pérdida de paquetes: "
        request = "Ping"
        return pinging, invalidoperation, sendpackets, receivedpackets, lowestping, highestping, averageping, packetloss,request
    elif languageselection == "German":
        pinging = "Ping wird ausgeführt ..."
        invalidoperation = "Ungültiger Betrieb. Bitte wählen Sie einen gültigen Betrieb aus."
        sendpackets = "Gesendete Pakete: "
        receivedpackets = "Empfangene Pakete: "
        lowestping = "Niedrigster Ping: "
        highestping = "Höchster Ping: "
        averageping = "Durchschnittlicher Ping: "
        packetloss = "Paketverlust: "
        request = "Ping"
        return pinging, invalidoperation, sendpackets, receivedpackets, lowestping, highestping, averageping, packetloss,request
    elif languageselection == "Russian":
        pinging = "Выполняется пинг..."
        invalidoperation = "Недопустимая операция. Пожалуйста, выберите допустимую операцию."
        sendpackets = "Отправленные пакеты: "
        receivedpackets = "Полученные пакеты: "
        lowestping = "Самый низкий пинг: "
        highestping = "Самый высокий пинг: "
        averageping = "Средний пинг: "
        packetloss = "Потеря пакетов: "
        pressanykeyexit = "Нажмите любую клавишу для выхода"
        request = "Пинг"
        return pinging, invalidoperation, sendpackets, receivedpackets, lowestping, highestping, averageping, packetloss,pressanykeyexit,request
    

def FunctionsTranslate():
    if languageselection == "Turkish":
        turkishtestserver = "Türk Test Sunucuları"
        globaltestserver = "Global Test Sunucuları"
        gametestserver = "Oyun Sunucuları"
        dnstestserver = "DNS Sunucuları"
        customtestserver = "Özel Sunucu"
        invalidcategory = "HATA : Geçersiz kategori numarası. Lütfen geçerli bir kategori numarası girin."
        return turkishtestserver, globaltestserver, gametestserver, dnstestserver, customtestserver, invalidcategory
    elif languageselection == "English":
        turkishtestserver = "Turkish Test Servers"
        globaltestserver = "Global Test Servers"
        gametestserver = "Game Servers"
        dnstestserver = "DNS Servers"
        customtestserver = "Custom Server"
        invalidcategory = "ERROR: Invalid category number. Please enter a valid category number."
        return turkishtestserver, globaltestserver, gametestserver, dnstestserver, customtestserver, invalidcategory