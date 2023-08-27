def findDecision(obj): #obj[0]: PassengerId, obj[1]: Pclass, obj[2]: Name, obj[3]: Sex, obj[4]: Age, obj[5]: SibSp, obj[6]: Parch, obj[7]: Ticket, obj[8]: Fare, obj[9]: Cabin, obj[10]: Embarked
	# {"feature": "Cabin", "instances": 891, "metric_value": 0.9607, "depth": 1}
	if obj[9] == 'G6':
		# {"feature": "Ticket", "instances": 4, "metric_value": 1.0, "depth": 2}
		if obj[7] == '347054':
			return 'NO'
		elif obj[7] == 'PP 9549':
			return 'YES'
		else: return 'YES'
	elif obj[9] == 'C23 C25 C27':
		# {"feature": "Sex", "instances": 4, "metric_value": 1.0, "depth": 2}
		if obj[3] == 'male':
			return 'NO'
		elif obj[3] == 'female':
			return 'YES'
		else: return 'YES'
	elif obj[9] == 'B96 B98':
		return 'YES'
	elif obj[9] == 'F33':
		return 'YES'
	elif obj[9] == 'E101':
		return 'YES'
	elif obj[9] == 'C22 C26':
		# {"feature": "Sex", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[3] == 'female':
			return 'NO'
		elif obj[3] == 'male':
			return 'YES'
		else: return 'YES'
	elif obj[9] == 'D':
		# {"feature": "PassengerId", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[0]>293:
			return 'YES'
		elif obj[0]<=293:
			return 'NO'
		else: return 'NO'
	elif obj[9] == 'F2':
		# {"feature": "PassengerId", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[0]>149:
			return 'YES'
		elif obj[0]<=149:
			return 'NO'
		else: return 'NO'
	elif obj[9] == 'D35':
		return 'YES'
	elif obj[9] == 'C65':
		# {"feature": "PassengerId", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0]<=308:
			return 'YES'
		elif obj[0]>308:
			return 'NO'
		else: return 'NO'
	elif obj[9] == 'D17':
		return 'YES'
	elif obj[9] == 'C124':
		return 'NO'
	elif obj[9] == 'B5':
		return 'YES'
	elif obj[9] == 'E33':
		return 'YES'
	elif obj[9] == 'C92':
		return 'YES'
	elif obj[9] == 'B28':
		return 'YES'
	elif obj[9] == 'B22':
		# {"feature": "PassengerId", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0]<=541:
			return 'YES'
		elif obj[0]>541:
			return 'NO'
		else: return 'NO'
	elif obj[9] == 'B57 B59 B63 B66':
		return 'YES'
	elif obj[9] == 'B18':
		return 'YES'
	elif obj[9] == 'D36':
		return 'YES'
	elif obj[9] == 'F G73':
		return 'NO'
	elif obj[9] == 'B77':
		return 'YES'
	elif obj[9] == 'D33':
		return 'YES'
	elif obj[9] == 'D26':
		return 'NO'
	elif obj[9] == 'C52':
		return 'YES'
	elif obj[9] == 'D20':
		return 'YES'
	elif obj[9] == 'C126':
		return 'YES'
	elif obj[9] == 'E25':
		return 'YES'
	elif obj[9] == 'E24':
		return 'YES'
	elif obj[9] == 'E121':
		return 'YES'
	elif obj[9] == 'C83':
		# {"feature": "PassengerId", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0]>63:
			return 'YES'
		elif obj[0]<=63:
			return 'NO'
		else: return 'NO'
	elif obj[9] == 'B58 B60':
		# {"feature": "PassengerId", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0]<=119:
			return 'NO'
		elif obj[0]>119:
			return 'YES'
		else: return 'YES'
	elif obj[9] == 'C123':
		# {"feature": "PassengerId", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0]<=4:
			return 'YES'
		elif obj[0]>4:
			return 'NO'
		else: return 'NO'
	elif obj[9] == 'B49':
		return 'YES'
	elif obj[9] == 'B51 B53 B55':
		# {"feature": "PassengerId", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0]>680:
			return 'NO'
		elif obj[0]<=680:
			return 'YES'
		else: return 'YES'
	elif obj[9] == 'C2':
		# {"feature": "PassengerId", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0]>152:
			return 'NO'
		elif obj[0]<=152:
			return 'YES'
		else: return 'YES'
	elif obj[9] == 'B35':
		return 'YES'
	elif obj[9] == 'E67':
		# {"feature": "PassengerId", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0]>263:
			return 'YES'
		elif obj[0]<=263:
			return 'NO'
		else: return 'NO'
	elif obj[9] == 'B20':
		return 'YES'
	elif obj[9] == 'E8':
		return 'YES'
	elif obj[9] == 'E44':
		# {"feature": "PassengerId", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0]>435:
			return 'YES'
		elif obj[0]<=435:
			return 'NO'
		else: return 'NO'
	elif obj[9] == 'F4':
		return 'YES'
	elif obj[9] == 'C93':
		return 'YES'
	elif obj[9] == 'C68':
		# {"feature": "PassengerId", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0]<=582:
			return 'YES'
		elif obj[0]>582:
			return 'NO'
		else: return 'NO'
	elif obj[9] == 'C125':
		return 'YES'
	elif obj[9] == 'C78':
		# {"feature": "PassengerId", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0]>246:
			return 'YES'
		elif obj[0]<=246:
			return 'NO'
		else: return 'NO'
	elif obj[9] == 'A7':
		return 'NO'
	elif obj[9] == 'E34':
		return 'YES'
	elif obj[9] == 'D21':
		return 'YES'
	elif obj[9] == 'D50':
		return 'NO'
	elif obj[9] == 'B50':
		return 'YES'
	elif obj[9] == 'D47':
		return 'YES'
	elif obj[9] == 'B69':
		return 'YES'
	elif obj[9] == 'C91':
		return 'NO'
	elif obj[9] == 'D37':
		return 'YES'
	elif obj[9] == 'E17':
		return 'YES'
	elif obj[9] == 'A32':
		return 'NO'
	elif obj[9] == 'E68':
		return 'YES'
	elif obj[9] == 'C70':
		return 'YES'
	elif obj[9] == 'A20':
		return 'YES'
	elif obj[9] == 'F38':
		return 'NO'
	elif obj[9] == 'C111':
		return 'NO'
	elif obj[9] == 'C128':
		return 'NO'
	elif obj[9] == 'D30':
		return 'NO'
	elif obj[9] == 'F E69':
		return 'YES'
	elif obj[9] == 'D7':
		return 'YES'
	elif obj[9] == 'E63':
		return 'NO'
	elif obj[9] == 'C104':
		return 'YES'
	elif obj[9] == 'B42':
		return 'YES'
	elif obj[9] == 'B101':
		return 'YES'
	elif obj[9] == 'C62 C64':
		return 'YES'
	elif obj[9] == 'A31':
		return 'YES'
	elif obj[9] == 'B78':
		return 'YES'
	elif obj[9] == 'F G63':
		return 'NO'
	elif obj[9] == 'B37':
		return 'NO'
	elif obj[9] == 'E46':
		return 'NO'
	elif obj[9] == 'C85':
		return 'YES'
	elif obj[9] == 'C99':
		return 'YES'
	elif obj[9] == 'B4':
		return 'YES'
	elif obj[9] == 'C103':
		return 'YES'
	elif obj[9] == 'A10':
		return 'NO'
	elif obj[9] == 'D49':
		return 'YES'
	elif obj[9] == 'C82':
		return 'NO'
	elif obj[9] == 'E12':
		return 'YES'
	elif obj[9] == 'D9':
		return 'YES'
	elif obj[9] == 'C101':
		return 'YES'
	elif obj[9] == 'C110':
		return 'NO'
	elif obj[9] == 'A26':
		return 'YES'
	elif obj[9] == 'C32':
		return 'YES'
	elif obj[9] == 'A34':
		return 'YES'
	elif obj[9] == 'C49':
		return 'NO'
	elif obj[9] == 'B38':
		return 'NO'
	elif obj[9] == 'C86':
		return 'NO'
	elif obj[9] == 'A23':
		return 'YES'
	elif obj[9] == 'T':
		return 'NO'
	elif obj[9] == 'E58':
		return 'NO'
	elif obj[9] == 'B86':
		return 'NO'
	elif obj[9] == 'C50':
		return 'YES'
	elif obj[9] == 'A19':
		return 'NO'
	elif obj[9] == 'C45':
		return 'YES'
	elif obj[9] == 'C148':
		return 'YES'
	elif obj[9] == 'D46':
		return 'NO'
	elif obj[9] == 'B3':
		return 'YES'
	elif obj[9] == 'B79':
		return 'YES'
	elif obj[9] == 'C90':
		return 'YES'
	elif obj[9] == 'D15':
		return 'YES'
	elif obj[9] == 'B73':
		return 'YES'
	elif obj[9] == 'A24':
		return 'NO'
	elif obj[9] == 'E38':
		return 'NO'
	elif obj[9] == 'B82 B84':
		return 'NO'
	elif obj[9] == 'A36':
		return 'NO'
	elif obj[9] == 'D10 D12':
		return 'YES'
	elif obj[9] == 'C95':
		return 'NO'
	elif obj[9] == 'E10':
		return 'YES'
	elif obj[9] == 'D11':
		return 'YES'
	elif obj[9] == 'B71':
		return 'NO'
	elif obj[9] == 'D6':
		return 'NO'
	elif obj[9] == 'E40':
		return 'YES'
	elif obj[9] == 'C54':
		return 'YES'
	elif obj[9] == 'A16':
		return 'YES'
	elif obj[9] == 'D45':
		return 'YES'
	elif obj[9] == 'B94':
		return 'NO'
	elif obj[9] == 'B39':
		return 'YES'
	elif obj[9] == 'E31':
		return 'NO'
	elif obj[9] == 'B41':
		return 'YES'
	elif obj[9] == 'E77':
		return 'NO'
	elif obj[9] == 'B80':
		return 'YES'
	elif obj[9] == 'B102':
		return 'NO'
	elif obj[9] == 'C87':
		return 'NO'
	elif obj[9] == 'C118':
		return 'NO'
	elif obj[9] == 'E50':
		return 'YES'
	elif obj[9] == 'C7':
		return 'YES'
	elif obj[9] == 'D48':
		return 'NO'
	elif obj[9] == 'C47':
		return 'YES'
	elif obj[9] == 'D56':
		return 'YES'
	elif obj[9] == 'D19':
		return 'YES'
	elif obj[9] == 'A6':
		return 'YES'
	elif obj[9] == 'B30':
		return 'NO'
	elif obj[9] == 'C106':
		return 'YES'
	elif obj[9] == 'D28':
		return 'YES'
	elif obj[9] == 'B19':
		return 'NO'
	elif obj[9] == 'E36':
		return 'YES'
	elif obj[9] == 'E49':
		return 'YES'
	elif obj[9] == 'C30':
		return 'NO'
	elif obj[9] == 'A5':
		return 'NO'
	elif obj[9] == 'A14':
		return 'NO'
	elif obj[9] == 'C46':
		return 'NO'
	else: return 'NO'
