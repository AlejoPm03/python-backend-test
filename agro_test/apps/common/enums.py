from enum import Enum

# Enum for the Brazilian states
class States(Enum):
	AC = "AC"
	AL = "AL"
	AP = "AP"
	AM = "AM"
	BA = "BA"
	CE = "CE"
	DF = "DF"
	ES = "ES"
	GO = "GO"
	MA = "MA"
	MT = "MT"
	MS = "MS"
	MG = "MG"
	PA = "PA"
	PB = "PB"
	PR = "PR"
	PE = "PE"
	PI = "PI"
	RJ = "RJ"
	RN = "RN"
	RS = "RS"
	RO = "RO"
	RR = "RR"
	SC = "SC"
	SP = "SP"
	SE = "SE"
	TO = "TO"

	@classmethod
	def choices(cls):
		return [(key.value, key.name) for key in cls]