import CoolProp.CoolProp as cp

m_dot = 0.03 #kg/s <-- given
T1 = -20 + 273.15 # K <--given
T3 = 40 +273.15 # K <--given

h1 = cp.PropsSI('H', 'T', T1, 'Q', 1, 'R717')
print(f"Enthalpy of refrigerant after evaporator: {round(float(h1/1000),3)} kJ/kg")

s1 = cp.PropsSI('S', 'T', T1, 'Q', 1, 'R717')
s2 = s1
p_g = cp.PropsSI('P', 'T', T3, 'Q', 1, 'R717')

T2 = cp.PropsSI('T', 'P', p_g,  'S', s2,  'R717')
h2 = cp.PropsSI('H', 'T', T2, 'P', p_g, 'R717')
print("Enthalpy of refrigerant after compressor = ",h2/1000)
print("Temperature of refrigerant after compressor = ",T2)

h3 = cp.PropsSI('H', 'T', T3, 'Q', 0, 'R717')
h4 = h3

wc = h2 - h1
ql = h1 - h4

print(f"Work done by compressor: {round(float(wc/1000),3)} kJ/kg")
print(f"The refrigeration effect is: {round(float(ql/1000),3)} kJ/kg")

COP = (ql/wc)
print(f"The Coefficient of Performance is: {round(float(COP),3)} ")

