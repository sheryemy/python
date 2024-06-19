import time
print("--------------------------------------------------")
#Welcome the user
print("Selamat Datang ke Permainan Kuiz Sejarah Malaysia!")
time.sleep(1)
print("--------------------------------------------------")

#Chances
chances=1
print("Anda perlu memilih", chances,"jawapan yang tepat.\nAnda akan dapat 1 score jika jawapan anda tepat.\n")
time.sleep(2)

#score
score=0

#SOALAN 1
print("==================================================")
question_1=print("1) SIAPAKAH BAPA KEMERDEKAAN MALAYSIA?\n(A) Tun Mahadhir Mohamad\n(B) Tun Hussein Onn\n(C) Tunku Abdul Rahman\n(D) Sudirman Arshad\n\n")
answer_1= "c"

for i in range(chances):
    answer = input("Jawapan: ")
    if (answer.lower() == answer_1):
        print("TEPAT.BAGUS!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH", answer_1, "\n\n")

time.sleep(2)

#SOALAN 2
print("==================================================")
question_2 = print("2)Perdana Menteri dilantik oleh:\n(A) Sultan\n(B) Raja\n(C) YB\n(D) Yang Dipertuan Agong\n\n")  
answer_2 = "d"

for i in range(chances):
    answer = input("Jawapan: ")
    if (answer.lower() == answer_2):
        print("TEPAT.BAGUS!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN SALAH!\n ")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH", answer_2, "\n\n")

time.sleep(2)

#SOALAN 3
print("==================================================")
question_3 =print("3)  BILAKAH TARIKH TANAH MELAYU MERDEKA?\n(A) 31 Julai 1957\n(B) 31 Ogos 1957\n(C) 30 Ogos 1957\n(D) 31 Januari 1957\n\n")
answer_3= "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("TEPAT.BAGUS!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH", answer_3, "\n\n")

time.sleep(2)

#SOALAN 4
print("==================================================")
question_4 =print("4)  BERAPAKAH WARNA BENDERA MALAYSIA?\n(A) 4\n(B) 3\n(C) 5\n(D) 2\n\n")
answer_4= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("TEPAT.BAGUS!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH",answer_4, "\n\n")

time.sleep(2)

#question 5
print("==================================================")
question_5 =print("5)  APAKAH NAMA BUNGA KEBANGSAAN MALAYSIA?\n(A) Melur\n(B) Raya\n(C) Mawar\n(D) Kemboja\n\n")
answer_5= "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("TEPAT.BAGUS!\n")
        score = score + 1
        break
    else:
        print("JAWAPAN SALAH!\n")
        time.sleep(0.5)
        print("JAWAPAN YANG BETUL IALAH", answer_5, "\n\n")

time.sleep(2)

#print the score
print("==================================================")
while score >=2:
    print("TAHNIAH! Jumlah Score anda ialah", score)
    break

while score <2:
    print("Sila Cuba Lagi! Jumlah Score anda ialah",score)
    break

#Goobye message
print("Terima kasih kerana bermain permainan ini!")
