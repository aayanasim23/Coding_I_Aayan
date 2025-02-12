Aayan = (2, 3, 4)
Andrew = (3, 2, 3)
Jonas =  (2, 4, 5)
Idara = (5, 5, 5)

Aayan_score = Aayan[0] + Aayan[1] + Aayan[2]
print("Aayan's score is", Aayan_score)

Andrew_score = Andrew[0] + Andrew[1] + Andrew[2]
print("Andrew's score is", Andrew_score)

Jonas_score = Jonas[0] + Jonas[1] + Jonas[2]
print("Jonas's score is", Jonas_score)

Idara_score = Idara[0] + Idara[1] + Idara[2]
print("Idara's score is", Idara_score)


MrZipTotal = Aayan[0] + Andrew[0] + Jonas[0] + Idara[0]
print("Mr. Zip's total score is", MrZipTotal)

MsUnoTotal = Aayan[1] + Andrew[1] + Jonas[1] + Idara[1]
print("Ms. Uno's total score is", MsUnoTotal)

MrsDuoTotal = Aayan[2] + Andrew[2] + Jonas[2] + Idara[2]
print("Mrs. Duo's total score is", MrsDuoTotal)


print("The winner was Idara with:", max(Aayan_score, Andrew_score, Jonas_score, Idara_score)) #Used AI to help enhance this line with the (max) function.
print("The judge who gave the most points was Mrs. Duo who gave:", max(MrZipTotal, MsUnoTotal, MrsDuoTotal)) #Used AI to help enhance this line with the (max) function.