#coding utf-8

def main():
	dMan2Cost = {"stw":0, "cxf":0, "gjq":0, "mxp":130, "lsx":170,}
	iSum = 0
	for k, v in dMan2Cost.items():
		iSum += v
	fAvg = iSum*1.0/len(dMan2Cost)
	lWhoCanGet = []
	lWhoNeedPay = []
	for k, v in dMan2Cost.items():
		if v > fAvg:
			lWhoCanGet.append([k,v])
		elif v < fAvg:
			lWhoNeedPay.append([k,v])
	lWhoNeedPay.sort(key=lambda x: x[1])
	lWhoCanGet.sort(key=lambda x: x[1], reverse=True)
	print("avg", fAvg)
	sBill = ""
	for x in lWhoCanGet:
		sNameGet = x[0]
		fPaied = x[1]
		fCanGet = fPaied - fAvg
		for idx in range(len(lWhoNeedPay)):
			y = lWhoNeedPay[idx]
			sNamePay = y[0]
			fNeedPay = fAvg - y[1]
			if fNeedPay == 0:
				continue
			if fNeedPay <= fCanGet:
				oneBill = "[%s]pay[%s] %f\n" % (sNamePay, sNameGet, fNeedPay)
				sBill += oneBill
				lWhoNeedPay[idx][1] += fNeedPay
				fCanGet -= fNeedPay
			elif fNeedPay > fCanGet:
				oneBill = "[%s]pay[%s] %f\n" % (sNamePay, sNameGet, fCanGet)
				sBill += oneBill
				lWhoNeedPay[idx][1] += fCanGet
				break

	print(sBill)

if __name__ == '__main__':
	main()